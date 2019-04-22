# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Environment(object):
    def __init__(self, parent=None):
        self.bindings = {}
        self.parent = parent

    def __getitem__(self, key):
        return self.bindings[key] if key in self.bindings else self.parent[key]

    def __setitem__(self, key, value):
        self.bindings[key] = value


class Solution(object):
    def evaluate(self, expression):
        return self.eval(self.parse(expression), Environment())

    def eval(self, ast, env):
        if isinstance(ast, basestring):
            return env[ast]
        elif isinstance(ast, int):
            return ast
        elif ast[0] == 'add':
            return self.eval(ast[1], env) + self.eval(ast[2], env)
        elif ast[0] == 'mult':
            return self.eval(ast[1], env) * self.eval(ast[2], env)
        elif ast[0] == 'let':
            new_env = Environment(parent=env)
            for var, exp in zip(*[iter(ast[1:-1])] * 2):
                new_env[var] = self.eval(exp, new_env)
            return self.eval(ast[-1], new_env)

    def parse(self, expression):
        return self.to_ast(self.to_tokens(expression))

    def to_ast(self, tokens):
        token = tokens.pop(0)
        if token == '(':
            result = []
            while tokens[0] != ')':
                result.append(self.to_ast(tokens))
            tokens.pop(0)
            return result
        elif token.lstrip('-').isdigit():
            return int(token)
        return token

    def to_tokens(self, expression):
        return expression.replace('(', ' ( ').replace(')', ' ) ').split()


if __name__ == '__main__':
    solution = Solution()

    assert 3 == solution.evaluate('(add 1 2)')
    assert 15 == solution.evaluate('(mult 3 (add 2 3))')
    assert 10 == solution.evaluate('(let x 2 (mult x 5))')
    assert 14 == solution.evaluate('(let x 2 (mult x (let x 3 y 4 (add x y))))')
    assert 2 == solution.evaluate('(let x 3 x 2 x)')
    assert 5 == solution.evaluate('(let x 1 y 2 x (add x y) (add x y))')
    assert 6 == solution.evaluate('(let x 2 (add (let x 3 (let x 4 x)) x))')
    assert 4 == solution.evaluate('(let a1 3 b2 (add a1 1) b2)')
    assert -12 == solution.evaluate('(let x 7 -12)')
