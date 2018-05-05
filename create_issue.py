import aiohttp
import asyncio
from gidgethub.aiohttp import GitHubAPI
import os


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "syin", oauth_token=os.getenv("GH_AUTH"))

        issue = await gh.post(
            '/repos/syin/gitbot/issues',
            data={
                'title': 'test',
                'body': 'test',
            })

        issue_id = issue["number"]
        comment = await gh.post(
            '/repos/syin/gitbot/issues/{id}/comments'.format(id=issue_id),
            data={
                'body': 'test comment',
            })

        close_issue = await gh.patch(
            '/repos/syin/gitbot/issues/{id}'.format(id=issue_id),
            data={'state': 'closed'},
        )

        reaction = await gh.post(
            '/repos/syin/gitbot/issues/{id}/reactions'.format(id=issue_id),
            accept="application/vnd.github.squirrel-girl-preview+json",
            data={'content': 'hooray'},
        )


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
