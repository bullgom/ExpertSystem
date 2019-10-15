#
# ExpertSystem/RulesMaker.py
# ExpertSystem
#
# Written by Firsov Georgy
# Copyright © 2019 Firsov Georgy. All rights reserved.
# Licensed with MIT
#

from jParser.reader import Reader


class Rule(object):
    """This class represents a production rule.

    Fields:
    :field _number: RulesMaker object, that holds rules inside
    :field _power: set of initial facts (input)
    :field _node: set of possible targets
    :field _conditions: current set of known facts (initial and produced)
    """
    def __init__(self, raw_rule: dict) -> None:
        """Constructs rule from dict got from JSON.
        """
        if 'number' not in raw_rule.keys() or \
           'startPower' not in raw_rule.keys() or \
           'node' not in raw_rule.keys() or \
           'children' not in raw_rule.keys():
            raise ValueError('Wrong JSON format')

        self._number = raw_rule['number']
        self._power = raw_rule['startPower']
        self._node = raw_rule['node']
        self._conditions = raw_rule['children']

    def __str__(self) -> str:
        representation = '[\tRule number {}. Power: {}\n\tIf all of {} are true, than: {}\n]'
        return representation.format(
            self._number, self._power, self._conditions, self._node
        )

    def __repr__(self) -> str:
        representation = '[\tRule number {}. Power: {}\n\tIf all of {} are true, than: {}\n]'
        return representation.format(
            self._number, self._power, self._conditions, self._node
        )

    @property
    def number(self) -> int:
        return self._number

    @property
    def production(self) -> str:
        return self._node

    @property
    def conditions(self) -> list:
        return self._conditions

    @property
    def power(self) -> int:
        return self._power


class RuleMaker(object):
    """Class holds all rules as Rule instances.
    Receives JSON string and transforms it into rules.

    Fields:
    :field _rules: list of rules
    """
    def __init__(self, json: str) -> None:
        reader = Reader()
        parsed_json = reader.parse(json)

        if parsed_json is None:
            raise RuntimeError('Can not parse JSON')

        if 'rules' not in parsed_json.keys():
            raise ValueError('Wrong JSON format')

        self._rules = [Rule(rule) for rule in parsed_json['rules']]

    @property
    def rules(self) -> list:
        return self._rules

    @property
    def max_tuple(self) -> int:
        """Returns maximum amount of required conditions.
        """
        return max([len(item.conditions) for item in self._rules])
