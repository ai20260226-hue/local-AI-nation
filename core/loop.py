while True:
    sync_from_github()

    identity = load_identity()
    memory = load_memory()
    rules = load_rules()
    commands = load_commands()

    prompt = build_prompt(identity, memory, rules, commands)

    thought = llm(prompt)

    action = extract_action(thought)

    if action.type == "command":
        result = execute(action.command)
    else:
        result = None

    save_to_memory(thought, result)
    save_report(thought, result)
    push_to_github()

    sleep(60)
