import dns.resolver
import dns.reversename
import unittest

class DnsTest(unittest.TestCase):
    def _testResolve(self, nameserver, qname, rr, values):
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [ nameserver ]
        result = resolver.resolve(qname, rr)
        self.assertEqual(len(result), len(values))
        results = [r.to_text() for r in result]
        results.sort()
        for i in range(0, len(values)):
            self.assertEqual(results[i], values[i])

    def testDns(self):
        ip = '10.10.0.4'
        self._testResolve(ip, 'test.devel', 'NS', ['ns.test.devel.'])
        self._testResolve(ip, 'ns.test.devel', 'A', ['10.10.0.4'])
        self._testResolve(ip, 'test.devel', 'A', ['10.10.0.4'])
        self._testResolve(ip, 'foo.test.devel', 'DNAME', ['bar.test.devel.'])
        self._testResolve(ip, 'test1.foo.test.devel', 'CNAME', ['test1.bar.test.devel.'])
        self._testResolve(ip, 'test2.foo.test.devel', 'CNAME', ['test2.bar.test.devel.'])
        self._testResolve(ip, 'test1.foo.test.devel', 'A', ['10.10.0.6'])
        self._testResolve(ip, 'test2.foo.test.devel', 'A', ['10.10.0.7'])
        self._testResolve(ip, 'test1.bar.test.devel', 'A', ['10.10.0.6'])
        self._testResolve(ip, 'test2.bar.test.devel', 'A', ['10.10.0.7'])
        self._testResolve(ip, dns.reversename.from_address('10.10.0.6'), 'PTR', ['test1.bar.test.devel.'])
        self._testResolve(ip, dns.reversename.from_address('10.10.0.7'), 'PTR', ['test2.bar.test.devel.'])

if __name__ == '__main__':
    unittest.main()
