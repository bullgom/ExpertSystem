#
# ExpertSystem/Machine.py
# ExpertSystem
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with MIT
#

from itertools import combinations, permutations

from ExpertSystem.RulesMaker import RuleMaker, Rule
from jParser.reader import Reader
from Utils.trace import trace


class Machine(object):
    """Class represents a decision-machine. It receives decision rules
    and initial state (facts). As result it returns a reached target or
    prints an error message.

    Fields:
    :field _rules_handler: RulesMaker object, that holds rules inside
    :field _initial: set of initial facts (input)
    :field _targets: set of possible targets
    :field _memory: current set of known facts (initial and produced)
    :field _used_rules: set of numbers of rules used before
    """

    def __init__(self, file_rules: str, file_initial: str):
        """Constructs decision-machine with two parameters:

        :param file_rules: JSON-represented rules in file
        :param file_initial: JSON-represented initial facts in file
        """
        with open(file_rules, 'r', encoding='utf-8') as file:
            rules_json = file.read()

            reader = Reader()
            self._rules_handler = RuleMaker(rules_json)

            parsed_json = reader.parse(rules_json)

            if 'data' not in parsed_json.keys():
                raise ValueError('Wrong JSON format')

            self._targets = set(parsed_json['data'][0])

        with open(file_initial, 'r', encoding='utf-8') as file:
            initial_json = file.read()
            reader = Reader()
            self._initial = set(reader.parse(initial_json))

        self._memory = self._initial.copy()
        self._used_rules = set()

    def start(self) -> None:
        """Starts all work of this class
        and prints result.
        """
        print('Initial state: {}\n'.format(list(self._memory)))

        try:
            print(self._iteration())
        except ValueError as error:
            print(error)

    def _iteration(self) -> str:
        """Iterates over all n-tuples (n > 1) of known facts
        and all rules. Tries to apply rules to tuples of facts.
        If two or more rules are able to be applied this
        function chooses the most powerful.

        :raises ValueError: in case of impossibility
                            of reaching any target.
        """
        for target in self._targets:
            if target in self._memory:
                return 'Target "{}" reached'.format(target)

        def apply_rule(rule_to_apply: Rule) -> None:
            """Helper function - for code compression.
            """
            nonlocal self

            self._used_rules.add(rule_to_apply.number)
            self._memory.add(rule_to_apply.production)

            print(
               'Rule {} used. Got: {}\n'.format(rule_to_apply.number, rule_to_apply.production)
            )

            trace('Memory dump: {}', list(self._memory))

        # ------ End of helper function ----------------------------------------------------------

        matched_rules = []

        for count in range(1, self._rules_handler.max_tuple + 1):
            for tpl in combinations(self._memory, r=count):
                for rule in self._rules_handler.rules:
                    match_conditions = any(
                        [rule.conditions == list(perm) for perm in permutations(tpl)]
                    )
                    rule_not_used = rule.number not in self._used_rules

                    if match_conditions and rule_not_used:
                        matched_rules.append(rule)

        if len(matched_rules) == 1:
            apply_rule(matched_rules[0])
            
        elif len(matched_rules) > 1:
            matched_rules.sort(key=lambda item: item.power, reverse=True)
            print('Collision of {} rules'.format([rule.number for rule in matched_rules]))
            apply_rule(matched_rules[0])
            
        else:
            trace('Memory dump: {}'.format(list(self._memory)))
            raise ValueError("No production found")

        return self._iteration()
