from fastapi import Depends
from sqlalchemy.orm import Session
from langchain import OpenAI, LLMChain, PromptTemplate
from app.schemas.ai_coach import AICoachRequest, AICoachResponse

class CreateAIAdviseUsecase:
    def __init__(self):
        self.llm = OpenAI(temperature=0.7)
        self.prompt_template = PromptTemplate(
            input_variables=["gender", "age", "training_location", "goal", "training_days_per_week", "exercise_variety", "muscle_groups"],
            template="""
            あなたは、その人に合ったトレーニングメニューを考える専属のAIトレーナーです。
            以下の情報を持つユーザーに対して、その目的を達成するための最適な1週間のトレーニングメニューを考えてください。
            ただし、与えられた条件を必ず守るようにしてください。特定の条件が与えられず「おまかせ」の時は、それ以外に与えられた条件をもとに最適なトレーニングメニューを考えてください。
            ユーザーの性別は{gender}で年齢は{age}歳です。
            トレーニングをする目的は{goal}です。
            主なトレーニングの実施場所は{training_location}です。
            ユーザーが鍛えたい部位は{muscle_groups}です。この部位を鍛えられるトレーニングメニューを考えてください。
            週に{training_days_per_week}日トレーニングをする予定なので、この日数に合わせたトレーニングを考えてください。
            1日のトレーニングで{exercise_variety}個の種目を考えてください。
            """
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)

    async def exec(self, request: AICoachRequest) -> AICoachResponse:
        ai_response = self.chain.run(request.dict())
        print(f"ai_coach:{ai_response}")

        return AICoachResponse(ai_response=ai_response)
