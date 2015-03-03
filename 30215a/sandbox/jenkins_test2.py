class JenkinsIntegrationTest(BaseTestCase):
    """
    This test should ensure a full cycle of tasks completes successfully within
    the jenkins builder space.
    """
    @mock.patch('changes.config.redis.lock', mock.MagicMock())
    @eager_tasks
    @responses.activate
    def test_full(self):
        responses.add(
            responses.POST, 'http://jenkins.example.com/job/server/build/api/json/',
            body='',
            status=201)
        responses.add(
            responses.GET, 'http://jenkins.example.com/queue/api/xml/?xpath=%2Fqueue%2Fitem%5Baction%2Fparameter%2Fname%3D%22CHANGES_BID%22+and+action%2Fparameter%2Fvalue%3D%2281d1596fd4d642f4a6bdf86c45e014e8%22%5D%2Fid',
            body=self.load_fixture('fixtures/GET/queue_item_by_job_id.xml'),
            match_querystring=True)
        responses.add(
            responses.GET, 'http://jenkins.example.com/queue/item/13/api/json/',
            body=self.load_fixture('fixtures/GET/queue_details_building.json'))
        responses.add(
            responses.GET, 'http://jenkins.example.com/job/server/2/api/json/',
            body=self.load_fixture('fixtures/GET/job_details_with_test_report.json'))
        responses.add(
            responses.GET, 'http://jenkins.example.com/job/server/2/testReport/api/json/',
            body=self.load_fixture('fixtures/GET/job_test_report.json'))
        responses.add(
            responses.GET, 'http://jenkins.example.com/job/server/2/logText/progressiveHtml/?start=0',
            match_querystring=True,
            adding_headers={'X-Text-Size': '7'},
            body='Foo bar')
        responses.add(
            responses.GET, 'http://jenkins.example.com/computer/server-ubuntu-10.04%20(ami-746cf244)%20(i-836023b7)/config.xml',
            body=self.load_fixture('fixtures/GET/node_config.xml'))