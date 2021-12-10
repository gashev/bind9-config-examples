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
        for ip in ['10.6.0.4', '10.6.0.5']:
            self._testResolve(ip, 'test.devel', 'NS', ['ns1.test.devel.', 'ns2.test.devel.'])
            self._testResolve(ip, 'ns1.test.devel', 'A', ['10.6.0.4'])
            self._testResolve(ip, 'ns2.test.devel', 'A', ['10.6.0.5'])
            self._testResolve(ip, 'test.devel', 'A', ['10.6.0.4'])
            self._testResolve(ip, 'www.test.devel', 'CNAME', ['test.devel.'])
            self._testResolve(ip, 'www.test.devel', 'A', ['10.6.0.4'])
            self._testResolve(ip, dns.reversename.from_address('10.6.0.4'), 'PTR', ['ns1.test.devel.'])
            self._testResolve(ip, dns.reversename.from_address('10.6.0.5'), 'PTR', ['ns2.test.devel.'])

if __name__ == '__main__':
    unittest.main()
