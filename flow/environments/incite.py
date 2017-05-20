# Copyright (c) 2017 The Regents of the University of Michigan
# All rights reserved.
# This software is licensed under the BSD 3-Clause License.
"""Environments for XSEDE super computers."""
from ..environment import DefaultTorqueEnvironment


class TitanEnvironment(DefaultTorqueEnvironment):
    hostname_pattern = 'titan'
    cores_per_node = 1

    @classmethod
    def mpi_cmd(cls, cmd, np):
        return "aprun -n {np} -N 1 -b {cmd}".format(cmd=cmd, np=np)

    @classmethod
    def script(cls, _id, **kwargs):
        js = super(TitanEnvironment, cls).script(_id=_id, **kwargs)
        js.writeline('#PBS -A {}'.format(cls.get_config_value('account')))
        return js


class EosEnvironment(DefaultTorqueEnvironment):
    hostname_pattern = 'eos'
    cores_per_node = 32

    @classmethod
    def mpi_cmd(cls, cmd, np):
        return "aprun -n {np} -b {cmd}".format(cmd=cmd, np=np)

    @classmethod
    def script(cls, _id, **kwargs):
        js = super(EosEnvironment, cls).script(_id=_id, **kwargs)
        js.writeline('#PBS -A {}'.format(cls.get_config_value('account')))
        return js


__all__ = ['TitanEnvironment', 'EosEnvironment']
