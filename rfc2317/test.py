import dns.resolver
import dns.reversename
import unittest

class DnsTest(unittest.TestCase):
    ip = '10.7.0.2'

    def _testResolve(self, nameserver, qname, rr, values):
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [ nameserver ]
        result = resolver.resolve(qname, rr)
        self.assertEqual(len(result), len(values))
        results = [r.to_text() for r in result]
        results.sort()
        for i in range(0, len(values)):
            self.assertEqual(results[i], values[i])

    def testDomain(self):
        self._testResolve(self.ip, 'domain', 'NS', ['ns.domain.'])
        self._testResolve(self.ip, 'ns.domain', 'A', ['10.7.0.2'])

    def testADomain(self):
        self._testResolve(self.ip, 'a.domain', 'NS', ['ns.a.domain.'])
        self._testResolve(self.ip, 'ns.a.domain', 'A', ['10.7.1.1'])

        self._testResolve(self.ip, 'host1.a.domain', 'A', ['10.7.1.1'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.1'), 'PTR', ['host1.a.domain.'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.1'), 'CNAME', ['1.1-126.1.7.10.in-addr.arpa.'])

        self._testResolve(self.ip, 'host2.a.domain', 'A', ['10.7.1.2'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.2'), 'PTR', ['host2.a.domain.'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.2'), 'CNAME', ['2.1-126.1.7.10.in-addr.arpa.'])

        self._testResolve(self.ip, 'host3.a.domain', 'A', ['10.7.1.3'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.3'), 'PTR', ['host3.a.domain.'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.3'), 'CNAME', ['3.1-126.1.7.10.in-addr.arpa.'])

    def testBDomain(self):
        self._testResolve(self.ip, 'b.domain', 'NS', ['ns.b.domain.'])
        self._testResolve(self.ip, 'ns.b.domain', 'A', ['10.7.1.129'])

        self._testResolve(self.ip, 'host1.b.domain', 'A', ['10.7.1.129'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.129'), 'PTR', ['host1.b.domain.'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.129'), 'CNAME', ['129.129-190.1.7.10.in-addr.arpa.'])

        self._testResolve(self.ip, 'host2.b.domain', 'A', ['10.7.1.130'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.130'), 'PTR', ['host2.b.domain.'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.130'), 'CNAME', ['130.129-190.1.7.10.in-addr.arpa.'])

        self._testResolve(self.ip, 'host3.b.domain', 'A', ['10.7.1.131'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.131'), 'PTR', ['host3.b.domain.'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.131'), 'CNAME', ['131.129-190.1.7.10.in-addr.arpa.'])

    def testCDomain(self):
        self._testResolve(self.ip, 'c.domain', 'NS', ['ns.c.domain.'])
        self._testResolve(self.ip, 'ns.c.domain', 'A', ['10.7.1.193'])

        self._testResolve(self.ip, 'host1.c.domain', 'A', ['10.7.1.193'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.193'), 'PTR', ['host1.c.domain.'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.193'), 'CNAME', ['193.193-254.1.7.10.in-addr.arpa.'])

        self._testResolve(self.ip, 'host2.c.domain', 'A', ['10.7.1.194'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.194'), 'PTR', ['host2.c.domain.'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.194'), 'CNAME', ['194.193-254.1.7.10.in-addr.arpa.'])

        self._testResolve(self.ip, 'host3.c.domain', 'A', ['10.7.1.195'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.195'), 'PTR', ['host3.c.domain.'])
        self._testResolve(self.ip, dns.reversename.from_address('10.7.1.195'), 'CNAME', ['195.193-254.1.7.10.in-addr.arpa.'])


if __name__ == '__main__':
    unittest.main()
