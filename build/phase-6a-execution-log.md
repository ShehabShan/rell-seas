# Phase 6a execution log

Spec: build/phase-6a-dry-run.md + build/phase-5-blueprint.md.
Entries append as the run goes, so a cut-off session keeps a record.

2026-10-07T03:57:32Z RUN mode=preflight start
2026-10-07T03:57:32Z PREFLIGHT start
2026-10-07T03:57:32Z HARD STOP phase=preflight error=HTTP 403 path=/users/@me code=? message=?
2026-10-07T03:58:16Z RUN mode=preflight start
2026-10-07T03:58:16Z PREFLIGHT start
2026-10-07T03:58:16Z HARD STOP phase=preflight error=HTTP 403 path=/users/@me non-json-body len=17 head=error code: 1010

2026-10-07T03:58:52Z RUN mode=preflight start
2026-10-07T03:58:52Z PREFLIGHT start
2026-10-07T03:58:52Z PREFLIGHT bot_user=RELL Seas Setup Bot status=bot-identity
2026-10-07T03:58:53Z PREFLIGHT guild name=Md Shehab Shan's server members=2 features=COMMUNITY,NEWS status=guild-info
2026-10-07T03:58:54Z PRE-EXISTING channel type=4 name=Text channels id=1556633735384797195 status=pre-existing
2026-10-07T03:58:54Z HARD STOP phase=preflight error=unexpected pre-existing channel 'Text channels' (id=1556633735384797195); stopping rather than touching an unknown server state
2026-10-07T03:59:13Z RUN mode=preflight start
2026-10-07T03:59:13Z PREFLIGHT start
2026-10-07T03:59:14Z PREFLIGHT bot_user=RELL Seas Setup Bot status=bot-identity
2026-10-07T03:59:14Z PREFLIGHT guild name=Md Shehab Shan's server members=2 features=NEWS,COMMUNITY status=guild-info
2026-10-07T03:59:15Z PRE-EXISTING channel type=4 name=Text channels id=1556633735384797195 status=pre-existing
2026-10-07T03:59:15Z PRE-EXISTING channel type=4 name=Voice channels id=1556633735384797196 status=pre-existing
2026-10-07T03:59:15Z PRE-EXISTING channel type=0 name=general id=1556633735384797197 status=pre-existing
2026-10-07T03:59:15Z PRE-EXISTING channel type=2 name=General id=1556633735863210095 status=pre-existing
2026-10-07T03:59:15Z PRE-EXISTING channel type=0 name=rules id=1557230037869133876 status=pre-existing
2026-10-07T03:59:15Z PRE-EXISTING channel type=0 name=moderator-only id=1557230037869133879 status=pre-existing
2026-10-07T03:59:15Z HARD STOP phase=preflight error=unexpected pre-existing channel 'moderator-only' (id=1557230037869133879); stopping rather than touching an unknown server state
2026-10-07T03:59:33Z RUN mode=preflight start
2026-10-07T03:59:33Z PREFLIGHT start
2026-10-07T03:59:33Z PREFLIGHT bot_user=RELL Seas Setup Bot status=bot-identity
2026-10-07T03:59:34Z PREFLIGHT guild name=Md Shehab Shan's server members=2 features=COMMUNITY,NEWS status=guild-info
2026-10-07T03:59:35Z PRE-EXISTING channel type=4 name=Text channels id=1556633735384797195 status=pre-existing
2026-10-07T03:59:35Z PRE-EXISTING channel type=4 name=Voice channels id=1556633735384797196 status=pre-existing
2026-10-07T03:59:35Z PRE-EXISTING channel type=0 name=general id=1556633735384797197 status=pre-existing
2026-10-07T03:59:35Z PRE-EXISTING channel type=2 name=General id=1556633735863210095 status=pre-existing
2026-10-07T03:59:35Z PRE-EXISTING channel type=0 name=rules id=1557230037869133876 status=pre-existing
2026-10-07T03:59:35Z PRE-EXISTING channel type=0 name=moderator-only id=1557230037869133879 status=pre-existing
2026-10-07T03:59:35Z PRE-EXISTING role name=@everyone id=1556633734340542464 managed=False status=pre-existing
2026-10-07T03:59:35Z PRE-EXISTING role name=RELL Seas Setup Bot id=1556635704711315459 managed=True status=pre-existing
2026-10-07T03:59:35Z PREFLIGHT bot_role=RELL Seas Setup Bot id=1556635704711315459 position=1 administrator=yes status=clean
2026-10-07T03:59:35Z PREFLIGHT result=clean
2026-10-07T03:59:35Z RUN mode=preflight done; no writes performed
2026-10-07T03:59:35Z SECRET-HYGIENE token never appeared in any output or file (preflight)
2026-10-07T03:59:58Z RUN mode=execute start
2026-10-07T03:59:58Z PREFLIGHT start
2026-10-07T03:59:59Z PREFLIGHT bot_user=RELL Seas Setup Bot status=bot-identity
2026-10-07T03:59:59Z PREFLIGHT guild name=Md Shehab Shan's server members=2 features=NEWS,COMMUNITY status=guild-info
2026-10-07T04:00:01Z PRE-EXISTING channel type=4 name=Text channels id=1556633735384797195 status=pre-existing
2026-10-07T04:00:01Z PRE-EXISTING channel type=4 name=Voice channels id=1556633735384797196 status=pre-existing
2026-10-07T04:00:01Z PRE-EXISTING channel type=0 name=general id=1556633735384797197 status=pre-existing
2026-10-07T04:00:01Z PRE-EXISTING channel type=2 name=General id=1556633735863210095 status=pre-existing
2026-10-07T04:00:01Z PRE-EXISTING channel type=0 name=rules id=1557230037869133876 status=pre-existing
2026-10-07T04:00:01Z PRE-EXISTING channel type=0 name=moderator-only id=1557230037869133879 status=pre-existing
2026-10-07T04:00:01Z PRE-EXISTING role name=@everyone id=1556633734340542464 managed=False status=pre-existing
2026-10-07T04:00:01Z PRE-EXISTING role name=RELL Seas Setup Bot id=1556635704711315459 managed=True status=pre-existing
2026-10-07T04:00:01Z PREFLIGHT bot_role=RELL Seas Setup Bot id=1556635704711315459 position=1 administrator=yes status=clean
2026-10-07T04:00:01Z PREFLIGHT result=clean
2026-10-07T04:00:03Z ROLE name=Castaway id=1557241066741301283 color=9807270 permissions=0 status=created
2026-10-07T04:00:05Z ROLE name=Watchkeeper id=1557241075037380669 color=6139362 permissions=0 status=created
2026-10-07T04:00:07Z ROLE name=Solo Banner id=1557241082755162135 color=11188152 permissions=0 status=created
2026-10-07T04:00:10Z ROLE name=Beacon id=1557241090493386754 color=16101441 permissions=0 status=created
2026-10-07T04:00:12Z ROLE name=Elder id=1557241102602473532 color=11500229 permissions=0 status=created
2026-10-07T04:00:13Z ROLE name=Keeper id=1557241109883654214 color=15158332 permissions=0 status=created
2026-10-07T04:00:15Z ROLES order={'Solo Banner': 1, 'Castaway': 2, 'Watchkeeper': 3, 'Beacon': 4, 'Elder': 5, 'Keeper': 6} status=verified (Solo Banner flair parked lowest)
2026-10-07T04:00:18Z CATEGORY name=LIGHTHOUSE ENTRY id=1557241127948521553 status=created
2026-10-07T04:00:20Z CATEGORY name=WATCH DECK id=1557241135242543136 status=created
2026-10-07T04:00:21Z CATEGORY name=MILESTONE BOARD id=1557241143299670136 status=created
2026-10-07T04:00:23Z CATEGORY name=HEARTH id=1557241150266540153 status=created
2026-10-07T04:00:25Z CATEGORY name=OCEAN & HELP id=1557241157505785946 status=created
2026-10-07T04:00:27Z CATEGORY name=COMMUNITY CRAFT id=1557241165026164857 status=created
2026-10-07T04:00:30Z CATEGORY name=SAFETY id=1557241171707953173 status=created
2026-10-07T04:00:32Z CHANNEL name=read-first-rules id=1557241190087139348 parent=LIGHTHOUSE ENTRY slowmode=0 overwrites=readonly status=created
2026-10-07T04:00:34Z CHANNEL name=welcome-in-pt-fr-es id=1557241196701683712 parent=LIGHTHOUSE ENTRY slowmode=0 overwrites=readonly status=created
2026-10-07T04:00:36Z CHANNEL name=watch-deck id=1557241204419330089 parent=WATCH DECK slowmode=60 overwrites=open status=created
2026-10-07T04:00:38Z CHANNEL name=lantern-room id=1557241211905900604 parent=WATCH DECK slowmode=60 overwrites=open status=created
2026-10-07T04:00:40Z CHANNEL name=milestone-board id=1557241222073155624 parent=MILESTONE BOARD slowmode=0 overwrites=keeper status=created
2026-10-07T04:00:42Z CHANNEL name=receipts-and-rumors id=1557241229522112603 parent=MILESTONE BOARD slowmode=0 overwrites=open status=created
2026-10-07T04:00:44Z CHANNEL name=introductions id=1557241237470183454 parent=HEARTH slowmode=0 overwrites=open status=created
2026-10-07T04:00:46Z CHANNEL name=tenure-and-returns id=1557241244768272415 parent=HEARTH slowmode=0 overwrites=open status=created
2026-10-07T04:00:48Z CHANNEL name=finder id=1557241252016160832 parent=HEARTH slowmode=0 overwrites=open status=created
2026-10-07T04:00:50Z CHANNEL name=ocean-joy id=1557241260694179910 parent=OCEAN & HELP slowmode=0 overwrites=open status=created
2026-10-07T04:00:52Z CHANNEL name=help-desk id=1557241270940860457 parent=OCEAN & HELP slowmode=0 overwrites=open status=created
2026-10-07T04:00:54Z CHANNEL name=patient-craft id=1557241277979037758 parent=COMMUNITY CRAFT slowmode=0 overwrites=open status=created
2026-10-07T04:00:55Z CHANNEL name=creator-mirror id=1557241285604016248 parent=COMMUNITY CRAFT slowmode=0 overwrites=open status=created
2026-10-07T04:00:58Z CHANNEL name=scam-watch-and-report id=1557241295351586836 parent=SAFETY slowmode=0 overwrites=scamwatch status=created
2026-10-07T04:00:59Z CHANNEL name=mod-action-log id=1557241302599344222 parent=SAFETY slowmode=0 overwrites=private status=created
2026-10-07T04:01:00Z CHANNEL mod-action-log privacy double-check passed status=verified
2026-10-07T04:01:04Z PIN channel=read-first-rules message_id=1557241314418884611 status=created (disclaimer only)
2026-10-07T04:01:06Z AUTOMOD name=Long Watch - slurs and profanity id=1557241330399322203 actions=block+alert status=created
2026-10-07T04:01:08Z AUTOMOD name=Long Watch - spam shield id=1557241337059737622 actions=block+alert status=created
2026-10-07T04:01:09Z AUTOMOD name=Long Watch - mention flood id=1557241344726929498 actions=block+alert status=created
2026-10-07T04:01:11Z AUTOMOD name=Long Watch - scam bait id=1557241351563771954 actions=block+alert status=created
2026-10-07T04:01:13Z AUTOMOD name=Long Watch - unsourced claims flag id=1557241358669058159 actions=alert status=created
2026-10-07T04:01:15Z VERIFY level=Medium status=set+verified
2026-10-07T04:01:17Z COMMUNITY rules_channel status=soft-fail (rules channel pointer verify mismatch); defaults kept
2026-10-07T04:01:19Z COMMUNITY updates_channel status=soft-fail (updates channel pointer verify mismatch); defaults kept
2026-10-07T04:01:19Z ONBOARDING attempt=1 current enabled=False prompts=0 status=read
2026-10-07T04:01:21Z ONBOARDING attempt=1 status=failed (HTTP 400 path=/guilds/1556633734340542464/onboarding code=50035 message=Invalid Form Body); retrying once
2026-10-07T04:01:21Z ONBOARDING attempt=2 current enabled=False prompts=0 status=read
2026-10-07T04:01:22Z ONBOARDING status=soft-fail (onboarding needs manual setup in the dashboard; HTTP 400 path=/guilds/1556633734340542464/onboarding code=50035 message=Invalid Form Body)
2026-10-07T04:01:22Z ONBOARDING final=manual
2026-10-07T04:01:24Z FINAL channels=28 roles=8 automod=5 missing=none status=verified
2026-10-07T04:01:24Z API-IMPOSSIBLE/TODO full 6-rules/report-path/parity/partner text (not worded in blueprint; owner to-do)
2026-10-07T04:01:24Z API-IMPOSSIBLE/TODO PT/FR/ES blurb translation (needs human check; owner to-do)
2026-10-07T04:01:24Z API-IMPOSSIBLE/TODO milestone-board Day-1 seeds (need freshness re-check; not authorized this session)
2026-10-07T04:01:24Z API-IMPOSSIBLE/TODO helper-bot welcome-DM/reaction-role (Phase 6b scope)
2026-10-07T04:01:24Z API-IMPOSSIBLE/TODO scam lookalike-domain + slur-variant keyword extension (blocklist refresh; owner to-do)
2026-10-07T04:01:24Z RUN mode=execute done status=complete
2026-10-07T04:01:24Z SECRET-HYGIENE token never appeared in any output or file
