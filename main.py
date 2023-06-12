import asyncio
import logging
import os

import graphene
from graphql import graphql


class User(graphene.ObjectType):
    id = graphene.ID()
    fib = graphene.Int()
    name = graphene.String()

    thing_one = graphene.String()
    thing_two = graphene.String()
    thing_three = graphene.String()
    thing_four = graphene.String()
    thing_five = graphene.String()
    thing_six = graphene.String()
    thing_seven = graphene.String()
    thing_eight = graphene.String()
    thing_nine = graphene.String()
    thing_ten = graphene.String()
    thing_eleven = graphene.String()
    thing_twelve = graphene.String()
    thing_thirteen = graphene.String()
    thing_fourteen = graphene.String()
    thing_fifteen = graphene.String()
    thing_sixteen = graphene.String()
    thing_seventeen = graphene.String()
    thing_eighteen = graphene.String()
    thing_nineteen = graphene.String()
    thing_twenty = graphene.String()

    @staticmethod
    def _resolve_thing(index):
        return f"thing {index}"

    @staticmethod
    def resolve_thing_one(parent, info):
        return User._resolve_thing(1)

    @staticmethod
    def resolve_thing_two(parent, info):
        return User._resolve_thing(2)

    @staticmethod
    def resolve_thing_three(parent, info):
        return User._resolve_thing(3)

    @staticmethod
    def resolve_thing_four(parent, info):
        return User._resolve_thing(4)

    @staticmethod
    def resolve_thing_five(parent, info):
        return User._resolve_thing(5)

    @staticmethod
    def resolve_thing_six(parent, info):
        return User._resolve_thing(6)

    @staticmethod
    def resolve_thing_seven(parent, info):
        return User._resolve_thing(7)

    @staticmethod
    def resolve_thing_eight(parent, info):
        return User._resolve_thing(8)

    @staticmethod
    def resolve_thing_nine(parent, info):
        return User._resolve_thing(9)

    @staticmethod
    def resolve_thing_ten(parent, info):
        return User._resolve_thing(10)

    @staticmethod
    def resolve_thing_eleven(parent, info):
        return User._resolve_thing(11)

    @staticmethod
    def resolve_thing_twelve(parent, info):
        return User._resolve_thing(12)

    @staticmethod
    def resolve_thing_thirteen(parent, info):
        return User._resolve_thing(13)

    @staticmethod
    def resolve_thing_fourteen(parent, info):
        return User._resolve_thing(14)

    @staticmethod
    def resolve_thing_fifteen(parent, info):
        return User._resolve_thing(15)

    @staticmethod
    def resolve_thing_sixteen(parent, info):
        return User._resolve_thing(16)

    @staticmethod
    def resolve_thing_seventeen(parent, info):
        return User._resolve_thing(17)

    @staticmethod
    def resolve_thing_eighteen(parent, info):
        return User._resolve_thing(18)

    @staticmethod
    def resolve_thing_nineteen(parent, info):
        return User._resolve_thing(19)

    @staticmethod
    def resolve_thing_twenty(parent, info):
        return User._resolve_thing(20)


class Query(graphene.ObjectType):
    users = graphene.List(User)

    @staticmethod
    def resolve_users(root, info):
        return [
            {
                "id": "john",
                "name": "John",
            } for x in range(0, 100)
        ]


Schema = graphene.Schema(query=Query)


QUERY_TEXT = """
{
    users {
        thingOne
        thingTwo
        thingThree
        thingFour
        thingFive
        thingSix
        thingSeven
        thingEight
        thingNine
        thingTen
        thingEleven
        thingTwelve
        thingThirteen
        thingFourteen
        thingFifteen
        thingSixteen
        thingSeventeen
        thingEighteen
        thingNineteen
        thingTwenty
    }
}
"""


async def query():
    thing = await graphql(
        Schema.graphql_schema,
        source=QUERY_TEXT,
    )
    return thing.data


if __name__ == "__main__":
    if os.getenv("NEW_RELIC_LICENSE_KEY"):
        import newrelic.agent
        newrelic.agent.initialize("./newrelic.ini")

    # Run many repetitions to try to amortize startup costs
    repetitions_str = os.getenv("REPETITIONS", "100")
    repetitions = int(repetitions_str)
    for index in range(1, repetitions):
        result = asyncio.run(query())
        assert result is not None
