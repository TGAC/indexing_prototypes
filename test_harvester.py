# indexing python file created 05/06/2017 by fshaw

import unittest
from harvester import figshare_search_general, figshare_get_article

output_file = 'curl_output.json'

'''
        with open(output_file, 'w+') as f:
            f.write(resp.content.decode('utf-8'))
            '''


class TestHarvester(unittest.TestCase):

    def test_harvester(self):
        resp = figshare_search_general('homo sapiens')
        #print_to_file(resp.content.decode('utf-8'))
        self.assertEqual(resp.status_code, 200, resp.content)

    def test_get_article(self):
        t = '3943347'
        resp = figshare_get_article(t)
        print_to_file(resp.content.decode('utf-8'))
        self.assertEqual(resp.status_code, 200, resp.content)


if __name__ == '__main__':
    unittest.main()

def print_to_file(data):
    with open(output_file, 'w+') as f:
        f.write(data)