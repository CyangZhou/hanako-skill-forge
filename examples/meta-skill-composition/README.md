# Meta-Skill Composition Example

This example shows how a higher-level meta-skill can organize lower-level skill capabilities into a maintainable workflow.

## Composition idea

A useful meta-skill usually needs at least:

1. an entry file
2. a route or intake rule
3. one or more execution branches
4. a maintenance path
5. a review or validation path

## Example shape

```text
meta-skill/
  SKILL.md
  modules/
    route/
    build/
    maintenance/
    review/
```

## What this demonstrates

- route first, then execution
- clear module responsibilities
- explicit maintenance and validation exits
- documentation as the main source of truth

## What this does not demonstrate

- production runtime guarantees
- host-native integration guarantees
- universal compatibility with all agent platforms

Those depend on the target runtime and host environment.
