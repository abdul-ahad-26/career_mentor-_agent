from agents import Runner
from my_agent.career_agent import career_agent
from my_config.gemini_config import run_config

# import asyncio # for Runner.run
import chainlit as cl



# set_tracing_disabled(True)

# runConfig
# some use it

# Runner

# res = Runner.run_sync(
#     starting_agent=agent,
#     input="What is 2 + 2"
# )

# print(res.final_output)


# Asyncronous code
# async def main():
#     res = await Runner.run(
#         starting_agent=agent,
#         input="What is 2 + 2"
#     )

#     print(res.final_output)

# asyncio.run(main())

# async def chat_loop():

    # history = []
    # print("🎓 Career Mentor Agent")
    # print("I help users explore career options based on their strengths and interests")
    # print("Type 'exit' to quit.")

    # # seed a friendly opener
    # history.append({
    #     "role": "assistant",
    #     "content": "Tell me about your skills, passions, or favorite subjects"
    # })
    # print(f"\nAssistant: {history[-1]['content']}")

    # while True:
    #     user_input = input("\nYou: ").strip()
    #     if user_input.lower() in ("exit", "quit"):
    #         print("👋 Bye!")
    #         break

    #     history.append({"role": "user", "content": user_input})

    #     # Run the orchestrated agent on the whole history
    #     result = await Runner.run(
    #         career_agent,   # entry/orchestrator agent
    #         history,
    #         # run_config=run_config
            
    #     )

    #     # Show the response
    #     print(f"\nAssistant: {result.final_output}")

    #     # Keep the conversation stateful
    #     history = result.to_input_list()

# if __name__ == "__main__":
#     asyncio.run(chat_loop())

# Chainlit code
@cl.on_chat_start
async def start():
    cl.user_session.set("history",[])
    await cl.Message("""🎓 Career Mentor Agent
                    Welcome! I'm here to help you explore career options based on your strengths and interests.
                    What are your skills, passions, or favorite subjects?
                     """).send()
    

@cl.on_message
async def handle(msg: cl.Message):
    history = cl.user_session.get("history",[])
    history.append({
        "role": "user",
        "content":msg.content
    })

    thinking = cl.Message("💡Thinking...")
    await thinking.send()

    try:
        result = await Runner.run(
            career_agent,   
            history,
            run_config=run_config
            )
        
        output = result.final_output
        
        thinking.content = output
        await thinking.update()

        history = result.to_input_list()
        cl.user_session.set("history",history)
    except Exception as e:
        thinking.content = f"❌ Error: {e}"
        await thinking.update()









        
