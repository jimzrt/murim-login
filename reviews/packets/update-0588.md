<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0588.txt",
      "sha256": "1a569e5554286270b8a0b69a4004bf715e90594b12cff2d93df046c352f67cb1",
      "bytes": 14015
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d0998d80a1f72562f29de8a175bc5695136ffc7ffa00bd450c3513faf1d06059",
      "bytes": 3014
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0f51b716b8d0b41af207d943d3e716e0f344920d94828232d9611c236e5b7065",
      "bytes": 183791
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "d2241033910a787a8c00c9556b0bb4b6345df233bef31e1895080dbaebb2a09b",
      "bytes": 1030
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "7e06807c438e3847883a1fedb157c50209643f1014908d01fceb7d18b4f07956",
      "bytes": 667
    },
    {
      "path": "characters/Hwa-jong.md",
      "sha256": "078ee7263319caab45c8e5e6e1c71070732173c8c4e80aceed527d727af85fde",
      "bytes": 646
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "d953d566f20f44281cb0cf999926d2fe0e15f0a67f6ee006315dbf367f205f8e",
      "bytes": 2317
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "096a84b9a0134da387b747bfe27c7b813ed1c6793efbf5727c3f2f289b782f57",
      "bytes": 622
    },
    {
      "path": "characters/Kim Hwajong.md",
      "sha256": "4d3074f5bb0c07dd32b64455b6960d4462c06e7fdfc971cb1c72a0aac51343bd",
      "bytes": 694
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "03c508039e959d670aacf33f65a2e1ca64a8c08c8f20ecb5399c5623c471aeb8",
      "bytes": 181236
    }
  ],
  "estimated_tokens": 11254
}
-->

# Durable State Update — Chapter 588

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 588. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 588. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 588,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 588,
    "continuity_sources": [588],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Kim Hwajong died after sacrificing himself to restrain Behemoth, and Choi Minwoo remains unconscious after being transported from the battlefield.",
    "Behemoth's Turbid Abyss is a Supreme Peak Magic Gem that absorbed another source of mana and requires purification before use.",
    "Jin Taekyung identifies Go Jun as the culprit behind the Monster Wave and deaths, and Go Jun now believes Jin caused the failure of his Pyeongchang plan.",
    "Jin Taekyung has withdrawn from the Peace Guild and is heading to Ares Guild; Skeleton King remains to protect the Guild and its people.",
    "Cheon Taemin collapsed more than twenty years ago and remains unconscious; his location is unknown, with Area A only suspected.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition and purged those who knew the truth.",
    "Busan's Kraken is dead, but more than one thousand Mermen remain across Haeundae and Gwangalli.",
    "Go Jun seized Song Cheonwoo's children, used an S-grade Magic Gem to cause the Busan Monster Wave, and targeted Choi Minwoo.",
    "Song Cheonwoo was killed by an unidentified monster after falling into an abyss; the object in his pocket released darkness that became light.",
    "Jin Taekyung killed Behemoth with One Annihilation and lost Exhaustion and Internal Energy Depletion through the resulting level-up.",
    "Go Jun intends to kill Jin Taekyung within one year and is relying on Ares's political, prosecutorial, corporate, and media influence plus Lee Jungryong's corruption ledger to protect him.",
    "Go Se-won now openly opposes Go Jun's crimes and cover-up orders, intends to resign if he survives, and has left the office as emergency sirens sound at shaking Ares headquarters."
  ],
  "continuity_sources": [
    587,
    586
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is the unidentified being involved in Go Jun's plan, and is it connected to the monster that killed Song Cheonwoo?",
    "What was the object Song Cheonwoo kept in his pocket, and what did its release of darkness and light accomplish?",
    "What is the old necklace Go Jun wears, and why does it matter to his plan?"
  ],
  "safe_through": 587,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥, Stone King for 스톤 킹, Skeleton King for 스켈레톤 킹, Behemoth for 베히모스, and Behemos for 베헤모스.",
    "Use Area A for A구역 and Mount Balwang for 발왕산.",
    "Use Hero's Soul for 영웅의 혼, Hyung for 형님, S-grade Magic Gem for S급 마정석, Hell Fire for 헬 파이어, and Hellfire Mage for 겁화의 마법사.",
    "Use final rally for 회광반조 and Young Master for 도련님.",
    "Use Internal Energy Depletion for 공력 소진 and Teleport for 텔레포트."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 김화종    | **Kim Hwajong**   |
| 삼류     | **Third Rate**    |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 화종 | **Hwa-jong** | Butler Kim's personal name. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 광안 | **Guang'an** | Sichuan location where the party boards Mu Song's ship. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 부산 | **Busan** | City where the Haeundae Gate crisis occurs. |
| 광안대교 | **Gwangan Bridge** | Busan suspension bridge central to Taekyung's childhood memory and the current disaster. |
| 크라켄 | **Kraken** | Sea monster leading the Monster Wave; newly identified in this chapter. |
| 평창 | **Pyeongchang** | Location in Gangwon Province where the Gate is situated. |
| 베히모스 | **Behemoth** | Mythical monster emerging from the Pyeongchang Gate. |
| 종로 | **Jongno** | Destination named by Taekyung. |
| 발왕산 | **Mount Balwang** | Mountain near Pyeongchang and the site of the Monster Wave broadcast. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 아이들 | 청년 | children_to_stranger | beggar bastard | childlike-insulting | The children repeat their mother's insulting description of Taekyung's beggar-like appearance. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |
| 팀장 | 중년인 | Hunter_team_leader_to_stranger | Boss | casual and polite | The Team Leader mistakes disguised Song for an ordinary raid customer and warns him not to proceed. |
| 길드원 | 진태경 | Peace Guild member to allied S-rank Hunter | Hunter Jin Taekyung | formal-polite and hesitant | A Guild member addresses Taekyung as 진태경 헌터님 while asking whether Choi should be awakened. |

## Listed compact profiles

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 587
- **Aliases:** Team Leader Seok
- **Role:** Go Jun is Ares Guild's Vice Guild Master, Lee Jungryong's disciple and former Head of Security, and the de facto successor to Lee's Ares legacy who passed the S-rank Hunter qualification assessment with a very high score but lacks Lee's legitimacy.
- **Personality:** Disciplined and controlled under ordinary pressure, fiercely loyal to Lee Jungryong, but consumed by humiliation and rage when Ares Guild's authority is challenged.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of Lee Jungryong, Go Jun inherited Lee's Ares Guild legacy after his death, regards Jin Taekyung and Choi Minwoo as enemies seeking to take it away, has seized Song Cheonwoo's children as leverage, and used an S-grade Magic Gem to trigger the Busan Monster Wave while targeting Choi.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 574
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hwa-jong.md

# Hwa-jong (화종)

- **Safe through:** Chapter 587
- **Aliases:** Butler Kim
- **Role:** Hwa-jong was Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Loyal, vigilant, and uncompromising toward perceived threats to Choi Minwoo.
- **Voice:** Formal and deferential toward Choi Minwoo, cold and openly hostile toward Song Cheonwoo.
- **Relationships:** Hwa-jong serves Choi Minwoo and was formerly close to Song Cheonwoo, but their relationship ended over loyalty and ambition.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 587
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and has just withdrawn from the Peace Guild after identifying Go Jun as the Monster Wave culprit.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 587
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Kim Hwajong.md

# Kim Hwajong (김화종)

- **Safe through:** Chapter 587
- **Aliases:** Butler Kim
- **Role:** Kim Hwajong was a Level 80 mage known as Butler Kim and Choi Minwoo's loyal butler and personal escort who sacrificed his life to restrain Behemoth and died after Jin Taekyung killed it.
- **Personality:** Gentle and composed as Butler Kim, but retains a fiery temperament and a habit of swearing.
- **Voice:** Gentle and measured
- **Relationships:** Kim Hwajong formerly instructed Im Chunsoo, who remains terrified of and obedient to him, and serves Choi Minwoo as butler and personal escort, having become Choi's only family.

## Korean source

```text
＃588화



그날, 대한민국의 공기는 심란했다.

부산과 평창에서 잇따라 발생한 몬스터 웨이브는 성공적으로 진압되었으나 적지 않은 사상자를 냈다.

여느 때와 다름없는 하루를 보내고 있던 사람들은 충격적인 소식을 접하고 불안에 떨었다.

“과장님, 뉴스 보셨어요?”

“봤지. 봤으니까 작업도 내팽개치고 여기 나와 있지.”

“저도 일이 손에 안 잡혀요. 이러다가 정말 집이나 회사 근처에서 몬스터 웨이브…….”

“야, 말이 씨가 된다. 그만하고 담배나 한 대 피우자.”

갑갑한 회사를 빠져나와 카페로 향한 직장인들, 이제 막 수업을 끝마치고 하교 중인 학생들, 무슨 일이 벌어지는지도 모른 채 더 놀고 싶다며 매달리는 아이들과 혹시나 하는 마음에 자식들을 잡아끄는 부모들까지.

심란한 오후였고, 사람들의 마음은 혼란스러웠다. 걱정과 불안이 서린 눈동자들은 긴급 속보가 흘러나오는 스마트폰에 고정되어 있었다.

- 지금 시청자 여러분들께서는 무너진 광안대교를 보고 계십니다. 인근 앞바다에는 이번 부산 몬스터 웨이브의 원인이자, 네임드 몬스터인 크라켄의 사체가…….

- 현재까지 집계된 사상자는 4천여 명에 육박합니다. 구출 및 수색 작업은 계속해서 이루어지고 있으며, 지금까지 확인된 사상자 명단은 [몬스터 재난] 어플을 통하여 확인하실 수…….

- 저는 지금 강원도 평창 발왕산에 나와 있습니다. 네임드 몬스터 베히모스의 죽음으로 몬스터 웨이브가 종결되었지만, 인근 콘도와 스키장을 찾은 7천여 명의 시민들은 아직 불안에 떨고 있습니다.

- 평창 몬스터 웨이브로 발생한 사상자는 371명으로, 최종집계된 45명의 사망자 중에는 평화 길드장 김화종 씨가 포함되어 큰 충격을…….

하나같이 끔찍하고, 충격적인 소식이었다. 공중파, 케이블, 인터넷 뉴스 기사까지. 벌집을 쑤신 것처럼 온 사방이 소란스러웠다.

거리의 사람들은 처참하게 붕괴된 광안대교를 보고 마른침을 삼켰고, 핏물에 잠긴 도시의 모습에 할 말을 잃었다.

재앙. 그것은 한 단어로밖에 표현할 수 없는 광경이었다.

그러나 언론의 조명은 비단 피해 상황만을 비추지 않았다.

아니, 오히려 몬스터 웨이브에 관해 이야기하려면 결코 빠질 수 없는 이름이 있었다.

- 대격변 이후 국내에서 전례를 찾아볼 수 없는 초유의 사태입니다. 두 시간 간격으로 발생한 두 번의 몬스터 웨이브는 큰 피해를 낳았지만, 완벽한 초동조치로 빠르게 혼란을 잠재울 수 있었습니다. 그리고 놀랍게도 이 두 번의 몬스터 웨이브 진압 과정에는 한 사람이 있었습니다.

- 혜성처럼 등장한 젊은 영웅이자, 오늘 하루에만 두 마리의 네임드 몬스터를 처치한 S급 헌터 진태경 씨의 행방이 묘연한 상황입니다. 이에 관하여 평화 길드 측은 아직 공식 입장을 내놓지 않고 있…….

혼란을 잠재우고 홀연히 사라진 영웅. 그 키워드에 모두의 관심이 쏠리는 것은 당연했다.

진태경의 행방이 묘연하다는 정부 발표가 나오자, 채 몇 분이 지나기도 전에 각종 미디어에서는 그에 관련된 여러 가지 추측을 쏟아 내고 있었다.

사망, 실종, 혹은 전투의 여파로 인한 의식불명 상태에 빠졌다는 말까지.

루머와 뜬소문을 다루는 것으로 유명한 삼류 언론사가 대부분이었으나, 사람들 역시 같은 의문을 품었다.

‘정말 무슨 일이라도 생긴 건가?’

사라질 이유가 없는 사람이 자취를 감췄다. 한마디의 말도 없이, 모습도 보여 주지 않을 채.

지원 병력이 도착했을 때 젊은 영웅은 이미 사라진 후였고 평화 길드는 공식 입장을 내놓지 않고 있었다.

이 소식이 국내를 휩쓸고, 해외까지 전해지자 의문은 눈덩이처럼 불어났다.

그리고…… 그렇게 구르고, 또 구르며 거대해진 눈덩이는 종로의 빌딩 숲에서 멈췄다.

저벅.

그가 언제, 어떻게 모습을 드러냈는지는 아무도 몰랐다.

하지만 저마다의 사정으로 빽빽한 빌딩 숲을 바쁘게 오가던 사람들은 깨달았다.

지금 들고 있는 스마트폰 화면을 가득 채운 프로필 사진 속 인물이, 자신들의 눈앞에 나타났음을.

툭. 투두둑.

붉었고, 푸르렀다.

인간과 몬스터의 핏물을 뒤집어쓴 그가 걸음을 옮길 때마다 붉고 푸른 핏물이 인도 위를 적셨다.

190센티에 달하는 큰 키와 완벽한 균형을 이룬 몸이 핏물을 밟으며 천천히 나아갔다.

“……진태경?”

누군가의 넋 나간 목소리가 순간 내려앉은 정적을 깨트렸다.

하지만 사람들은 마침내 모습을 드러낸 젊은 영웅을 향해 환호하고, 가까이 다가서고, 스마트폰을 꺼내 언론에 제보하며 사진을 찍는 대신 입을 다문 채 발걸음을 멈췄다.

그건 어쩌면, 피에 젖은 머리카락 사이로 보이는 그의 눈동자가 깊게 가라앉아 있었기 때문일지도 몰랐다.

저벅. 저벅.

그의 한 걸음 한걸음에 짙은 피로가 배어 나와서였을 수도.

후우.

터진 입술 사이로 하얗게 뿜어지는 숨결에 누군가를 잃은 슬픔이 느껴져서였을 수도 있었다.

하지만 한 가지는 확실했다. 인근 거리를 가득 메운 모두가 본능적으로 알아차렸다.

지금의 그를 막아서는 안 된다는 것을.

슥. 스윽.

수백에 달하는 인파가 좌우로 갈라졌다.

신화 속에 등장하는 선지자의 지팡이 대신, 새하얀 창을 든 청년은 한 사람만을 위해 만들어진 인(人)의 파도를 가로질렀다.

멍한 눈빛으로 그의 뒷모습을 좇던 이들이 그를 따라 걸음을 옮겼다.

이유는 이 자리의 누구도 알 수 없었으나, 모두가 무언가에 홀린 듯 움직였다. 그렇게 수백에 수백이 더해지고, 천에 천이 더해졌다.

어느덧 수천으로 불어난 인파(人波)는 최면에 걸린 것처럼 걷고, 또 걸었다.

한 사람의 걸음으로 시작되어 영원히 멈출 것 같지 않던 이 대규모 행진이 멈춘 것은, 마찬가지로 한 사람의 걸음이 멈추었기 때문이었다.

저벅.

마지막 한 걸음.

청년은 문득 고개를 들어 하늘을 바라보았다.

오후 다섯 시. 유난히 춥고, 지치고, 슬펐던 1월의 하루가 불그스름한 빛과 함께 서서히 저물고 있었다.

하지만 한 사람에게만큼은 아니었다.

‘이제 시작이지.’

서쪽으로부터 뻗어 나온 노을빛에 까마득한 높이의 초고층 빌딩이 번쩍였다.

그중에서도 최상층에 걸린 거대한 글자가 그의 눈동자에 비쳤다.



ARES GUILD



무너지지 않는 철옹성이자 화려한 왕궁.

이 안에 도대체 얼마나 많은 숫자의 헌터가 있을까. 왕좌에 앉아 있는 그놈을 마주하기 위해서는 몇 명의 적들을 쓰러트려야 할까.

‘수백? 수천?’

상관없었다. 수백이든. 수천이든.

청년, 진태경은 붉게 물든 하늘 아래에서 중얼거렸다.

“거, 조지기 딱 좋은 날씨다.”

화륵. 노을을 닮은 화염이 그의 팔을 휘감고 솟구친다. 홀린 듯이 그 광경을 바라보던 군중들이 숨을 삼키며 물러난 그 순간.

“나 왔다. 이 씨벌놈아.”

후우우우웅, 꽈앙!

미증유(未曾有)의 힘이, 초고층 빌딩을 뒤흔들었다.



* * *



구구구구궁!

사방을 뒤흔드는 거대한 진동. 일대가 지진이라도 난 것처럼 흔들렸다.

바닥을 빈틈없이 메운 대리석 위로 거미줄 같은 금이 번지고, 로비를 장식한 화려하고 값진 미술품들이 금 간 대리석 위로 소나기처럼 떨어져 내렸다.

쩌저적, 콰창!

그것이 내가 로비로 진입하자마자 본 광경이었다.

방금 깨진 건 웬 남자를 표현한 석고상이었는데…… 이름이 뭐였는지 도통 생각이 나지 않아 가까이에 있는 사람에게 물어볼 수밖에 없었다.

“방금 깨진 게 뭐였지? 미술 교과서에서 봤던 건데. 로댕의 생각 난 사람이었나?”

“……아. 아아.”

아레스 길드원. 그중에서도 보안팀으로 보이는 젊은 남자가 얼어붙은 표정으로 말을 더듬는다.

그 모습이 퍽 안타까워 보여서, 나는 질문을 바꿨다.

“그럼 오늘 일어난 몬스터 웨이브에 대한 개인적인 생각은?”

“예, 예?”

“운 좋네. 아무것도 모르는 말단이라서.”

그리고 그것이, 이 남자의 목숨을 살렸다.

쉭!

은밀한 파공성과 함께 내가 쏘아 보낸 지풍(指風)이 남자의 혈도를 짚었다.

동시에 뻣뻣하게 굳으며 쓰러지는 그의 신형 너머로, 한 줄기의 빛살이 쇄도했다.

쐐애애액! 쾅!

귓가를 스친 화살이 출입문이 박살낸다. A급 헌터로 보이는 중년인이 굳은 얼굴로 나를 향해 시위를 팽팽하게 당겼다.

아니, 나를 향해 겨누어진 무기는 그뿐만이 아니었다.

스스스슥!

수십 명의 보안팀. 그리고 로비를 가득 메운 수백의 헌터가 긴장된 얼굴로 나를 주시했다. 그들의 손에는 제각각 불꽃과 얼음이, 창과 검 따위의 날붙이나 활이 들려 있었다.

보안팀장으로 짐작되는 중년 헌터가 딱딱한 목소리로 입을 열었다.

“물러서십시오, 진태경 씨.”

물러서라니. 참지 못하고 헛웃음을 흘린 내가 대답했다.

“그건 좀 곤란한데.”

“이러시는 이유가 뭡니까.”

“이유는 많지. 하지만 당장 그 이유를 말한다고 여러분들이 믿어 줄지는 모르겠네.”

“진태경 씨. 당신……!”

나는 공허한 눈빛으로 로비를 가득 메운 사람들을 바라보았다.

이들 중 누굴 죽이고, 누굴 살려야 할까. 이 중 누가 오늘 일어난 일들과 직접적인 연관이 있을까.

숨을 쉬는 것처럼 일어나는 살심(殺心)을 억누르는 것만으로도 안간힘을 써야 했다.

‘잊지 말자. 나는 괴물이 아니다.’

오늘 이 자리에서 모두를 죽이면 괴물이 되겠지만, 끝까지 사람으로 남고 싶었다.

적어도 죄 없는 이들이 자신들의 상관이 벌인 일에 애꿎은 죽임을 당하지 않기를 바랐다.

그게 김화종을, 모두를 위한 길이라고 생각했다.

“다들, 쉽게 갑시다.”

나는 수백 쌍의 시선을 직시하며, 한 마디를 내뱉었다.

“석고준 불러.”

“……!”

“……!”

보이지 않는 울림이 로비 내부와 수백의 헌터들을 휩쓴다.

찌르르 울리는 공기 속, 나는 천천히 말을 이었다.

“지금 당장.”

보안팀장이 딱딱하게 굳은 얼굴로 대답했다.

“그건 힘들 것 같군요.”

“어째서?”

“지시를 받았습니다. 무슨 수를 써서라도 진태경 씨를 막으라는 지시를.”

“그렇군.”

“어떤 용무로 찾아왔는지는 모르나 지금이라도 돌아가십시오. 이 빌딩 안에, 아레스 길드의 길드 하우스 안에 도대체 몇 명의 헌터가 있을거라고 생각하십니까?”

“로비에만 이 정도니까, 다 합치면 천 명은 우습겠지.”

“장담하는데, 지금 돌아가지 않으면 늦어도 오 분 안에 이 빌딩 안의 모두가 진태경 씨를 노릴 겁니다.”

나는 담담하게 대꾸했다.

“장담하는데, 지금 당장 무기 내려놓고 도망가지 않으면 늦어도 오 분 안에 전부 사람 구실 못 하게 될 줄 알아라.”

“……!”

“그러니까 눈앞에서 사라져. 애꿎은 사람 병신 만들기 싫으니까.”

후우우우웅!

난데없이 들이닥친 바람이 로비를 휩쓸었다.

내 전신으로부터 흘러나온 강대한 기파(氣波)에 짓눌린 보안팀장이 이를 악물었다.

끝까지 예의를 지키려던 어투는 상상을 아득히 뛰어넘는 압박감에 저 멀리 날아가 버린 후다.

“도대체…… 왜 이렇게까지 하는 거지?”

“헌터라서.”

“뭐?”

“석고준, 그 새끼는 괴물이야. 헌터가 몬스터 잡는 데 이유는 없지.”

석고준이 자신이 한 일을 동네방네 소문냈을 리가 없으니, 이들 중 대다수는 내가 무슨 말을 하는지 쉽게 이해하지 못할 것이다.

하지만 한 가지는 확실히 깨달았을 것이다.

내 앞을 막아선다면, 결코 끝이 좋지 않으리라는 것을.

복잡한 표정으로 나를 바라보던 보안팀장이 중얼거렸다.

“씨발. 용코로 걸렸네.”

“솔직해서 좋네. 그래서 대답은?”

이건 한 사람에게만 던진 질문이 아니다.

보안팀장의, 사방에서 나를 둘러싼 이백여 쌍의 눈동자에 갈등의 빛이 어렸다.

저마다의 무기를 쥔 손이 파르르 떨린 찰나였다.

- 코드 레드. 코드 레드. 대상은 아레스 길드원 전원. 목표는…….

곳곳에 설치된 대형 스피커 너머로, 누군가의 목소리가 초고층 빌딩 내부를 쩌렁쩌렁하게 울렸다.

- 진태경.

“……!”

“……!”

주위의 공기가 잘게 떨렸다.

그리고 다음 순간, 나는 보았다. 크게 뜨인 수백 쌍의 눈동자에서 갈등이 사라지고, 그들의 손에서 터져 나온 무수한 빛줄기가 거대한 섬광이 되어 온 사방을 물들이는 것을.

콰아아아아아!

붉고, 푸르고, 희다.

나는 그 거대한 섬광을 향해, 눈부시도록 새하얀 창날을 휘둘렀다.

쏴아아아악!
```

## Final English reading copy

```markdown
# Chapter 588

That day, the air in Korea was heavy with unease.

The Monster Waves that had erupted one after another in Busan and Pyeongchang had been successfully contained, but not without a substantial number of casualties.

People who had been going about an ordinary day were confronted with shocking news and began trembling with anxiety.

“Manager, did you see the news?”

“I did. That’s why I abandoned my work and came out here.”

“I can’t focus on anything either. What if there’s really a Monster Wave near our homes or workplaces…?”

“Hey, don’t say things like that. You’ll make them come true. Come on, let’s have a cigarette.”

Office workers escaping their suffocating workplaces and heading for cafés. Students who had just finished class and were on their way home. Children clinging to their parents and begging to keep playing, unaware of what was happening, and parents dragging their children away just in case.

It was an uneasy afternoon, and people’s hearts were in turmoil. Eyes filled with worry and fear remained fixed on smartphones broadcasting emergency news alerts.

> — You are now looking at the collapsed Gwangan Bridge. In the nearby waters lies the corpse of the Named Monster Kraken, the cause of the Busan Monster Wave…

> — The number of casualties tallied so far is approaching four thousand. Rescue and search operations are still underway, and the list of confirmed casualties can be viewed through the *Monster Disaster* app…

> — I am currently at Mount Balwang in Pyeongchang, Gangwon Province. The Monster Wave has ended with the death of the Named Monster Behemoth, but more than seven thousand citizens who had visited nearby condominiums and ski resorts remain terrified.

> — The Pyeongchang Monster Wave resulted in 371 casualties. Of the forty-five confirmed dead, the Guild Master of the Peace Guild, Mr. Kim Hwajong, is included, causing tremendous shock…

Every report was horrible and shocking. Public broadcasts, cable channels, online news articles—everywhere was in an uproar, as though someone had stirred up a hornet’s nest.

People in the streets swallowed dryly as they looked at the ruin of Gwangan Bridge and were left speechless by the sight of a city drowned in blood.

It was a disaster. There was no other word for it.

But the media’s attention was not focused solely on the damage.

No, there was one name that could never be left out when discussing the Monster Waves.

> — This is an unprecedented event, unlike anything Korea has experienced since the Great Cataclysm. Two Monster Waves occurred two hours apart and caused tremendous damage, but a flawless initial response brought the chaos under control quickly. And, amazingly, one person was present during the suppression of both Monster Waves.

> — The whereabouts of S-rank Hunter Jin Taekyung, a young hero who appeared like a comet and killed two Named Monsters in a single day, remain unknown. The Peace Guild has yet to issue an official statement regarding the matter…

A hero who had calmed the chaos and then vanished without a trace. Naturally, everyone’s attention focused on that one fact.

As soon as the government announced that Jin Taekyung’s whereabouts were unknown, various media outlets began pouring out speculation before even a few minutes had passed.

Some claimed he was dead or missing. Others said he had fallen unconscious from the aftereffects of the battle.

Most of them were Third Rate media companies famous for dealing in rumors and wild gossip, but ordinary people were wondering the same thing.

*Did something really happen to him?*

A man who had no reason to disappear had vanished without a trace. Without saying a word. Without showing himself to anyone.

The young hero had already disappeared by the time the support forces arrived, and the Peace Guild had issued no official statement.

As the news swept across Korea and reached other countries, the questions grew like a snowball.

And then…

That snowball rolled and rolled, growing larger and larger, until it came to a stop amid the skyscrapers of Jongno.

Step.

No one knew when or how he had appeared.

But the people hurrying through the densely packed forest of buildings for their own reasons realized something.

The person in the profile photo filling the smartphone screens in their hands had appeared right before their eyes.

Drip. Drip-drip.

He was red, and he was blue.

Every time he moved, red and blue blood soaked into the sidewalk beneath him. He was covered in the blood of humans and monsters.

His nearly six-foot-four frame moved slowly forward, his perfectly balanced body stepping through the blood.

“…Jin Taekyung?”

Someone’s dazed voice broke the silence that had suddenly settled over the street.

But instead of cheering at the young hero who had finally appeared, approaching him, taking out their smartphones to photograph him, or reporting his presence to the media, the people fell silent and stopped where they stood.

Perhaps it was because his eyes, visible between his blood-soaked hair, had sunk into unfathomable depths.

Step. Step.

Perhaps it was because profound exhaustion seeped from every one of his footsteps.

Huff.

Perhaps it was because the white breath escaping between his split lips carried the sorrow of someone who had lost another person.

But one thing was certain.

Everyone filling the surrounding streets instinctively understood.

They must not stand in his way.

Swish. Swoosh.

Hundreds of people parted to either side.

Instead of the staff of a prophet from myth, the young man carried a pure-white spear as he crossed a human wave made for a single person.

Those who had followed his back with dazed eyes began walking after him.

No one there knew why, but everyone moved as though under a spell. Hundreds became hundreds more, and thousands became thousands more.

Before long, the crowd had grown into the thousands. Like people under hypnosis, they walked and kept walking.

The massive procession, which had begun with one man’s footsteps and seemed as though it would never stop, came to a halt for the same reason: one man’s footsteps stopped.

Step.

The final step.

The young man suddenly raised his head and looked at the sky.

It was five in the afternoon. A particularly cold, exhausting, and sorrowful day in January was slowly drawing to a close beneath a reddish glow.

But not for one person.

*It’s beginning now.*

The sunset stretching from the west flashed across the towering skyscrapers.

Among them, the enormous letters mounted on the top floor reflected in his eyes.

**ARES GUILD**

An impregnable fortress that could not be brought down, and a magnificent royal palace.

How many Hunters were inside this place? How many enemies would he have to defeat to face the bastard sitting on the throne?

*Hundreds? Thousands?*

It didn’t matter. Hundreds or thousands.

Beneath the red sky, the young man, Jin Taekyung, muttered,

“Well, this is perfect weather for fucking someone up.”

Whoosh!

Flames resembling the sunset coiled around his arm and surged upward. The crowd, gazing at the sight as if entranced, swallowed hard and retreated.

At that moment—

“I’m here, you fucking bastard.”

Whoooooosh—BOOM!

An unprecedented force shook the skyscraper.

* * *

Rumble-rumble-rumble!

A massive vibration shook everything in every direction. The entire area trembled as though an earthquake had struck.

Spiderweb cracks spread across the marble covering the floor without a gap, and the splendid, valuable works of art decorating the lobby fell like a sudden shower onto the cracked marble.

Crack! Crash!

That was the sight I saw the instant I entered the lobby.

The thing that had just shattered was a plaster statue depicting some man, but I couldn’t remember its name at all, so I had no choice but to ask someone nearby.

“What was that statue that just broke? I saw it in an art textbook. Was it Rodin’s *The Man Who Had a Thought*?”

“…Ah. Ahh.”

A young Ares Guild member who appeared to belong to the Security Team stammered with a frozen expression.

He looked so pitiful that I changed my question.

“Then what are your personal thoughts on today’s Monster Wave?”

“P-Pardon?”

“You’re lucky. You’re just a low-ranking grunt who doesn’t know anything.”

And that was what saved the man’s life.

Whoosh!

With a stealthy whistle through the air, the Finger Qi I fired struck the man’s acupoints.

At the same time, a streak of light came rushing forward over his rigid body as he collapsed.

Screeeeech! Boom!

The arrow that grazed my ear smashed into the entrance door. A middle-aged man who appeared to be an A-rank Hunter stood there with a hardened expression, his bowstring drawn taut as he aimed at me.

No, that was not the only weapon pointed at me.

Swish, swish, swish!

Dozens of Security Team members. Hundreds of Hunters filling the lobby. They watched me with tense expressions.

Their hands held flames and ice, spears and swords and other bladed weapons, or bows.

A middle-aged Hunter presumed to be the Security Team Leader spoke in a rigid voice.

“Step back, Mr. Jin.”

Step back?

Unable to hold back a hollow laugh, I answered,

“That’s going to be difficult.”

“Why are you doing this?”

“There are a lot of reasons. But I’m not sure you’ll believe me even if I tell you right now.”

“Mr. Jin Taekyung. You…!”

I looked at the people filling the lobby with hollow eyes.

*Who should I kill, and who should I spare? Which of them is directly connected to what happened today?*

Suppressing the murderous intent that arose as naturally as breathing took all the strength I had.

*Don’t forget. I’m not a monster.*

If I killed everyone here today, I would become a monster. But I wanted to remain a human being until the end.

At the very least, I wanted to ensure that innocent people were not killed for something their superior had done.

I thought that was the path that was best for Kim Hwajong—and for everyone.

“Let’s make this easy for everyone.”

I looked straight into hundreds of pairs of eyes and said one thing.

“Bring Go Jun.”

“……!”

“……!”

An invisible resonance swept through the lobby and the hundreds of Hunters.

Within the air vibrating with a sharp ringing, I continued slowly.

“Right now.”

The Security Team Leader answered with a stiff expression.

“I don’t think that will be possible.”

“Why not?”

“I received orders. I was ordered to stop Mr. Jin Taekyung by any means necessary.”

“I see.”

“I don’t know what business brought you here, but you should turn around and leave while you still can. How many Hunters do you think there are in this building—in Ares Guild House?”

“There are already this many in the lobby, so there must easily be a thousand in total.”

“I guarantee that if you don’t leave now, every person in this building will be targeting you within five minutes at the latest.”

I answered calmly.

“And I guarantee that if you don’t put down your weapons and run right now, within five minutes, every last one of you will be physically incapable of functioning normally.”

“……!”

“So disappear from my sight. I don’t want to cripple people who have nothing to do with this.”

Whoooooosh!

A sudden gust of wind swept through the lobby.

Crushed beneath the powerful wave of qi flowing from my entire body, the Security Team Leader clenched his teeth.

The polite tone he had tried to maintain until the end had flown far away beneath pressure that surpassed anything he could have imagined.

“Why… Why are you going this far?”

“Because I’m a Hunter.”

“What?”

“Go Jun, that bastard, is a monster. Hunters don’t need a reason to kill monsters.”

Go Jun obviously wouldn’t have broadcast what he had done far and wide, so most of these people would not easily understand what I was talking about.

But they would have realized one thing for certain.

If they stood in my way, things would not end well for them.

The Security Team Leader looked at me with a complicated expression and muttered,

“Fuck. We’re seriously screwed.”

“I like your honesty. So, what’s your answer?”

That question was not directed at him alone.

A conflicted light appeared in the eyes of the Security Team Leader and the roughly two hundred people surrounding me from every direction.

Their hands trembled around their weapons.

Then—

> — Code Red. Code Red. All Ares Guild members are to respond. The target is…

A voice rang thunderously throughout the skyscraper from the large speakers installed in various places.

> — Jin Taekyung.

“……!”

“……!”

The air around us trembled.

And in the next moment, I saw it.

The conflict vanished from hundreds of wide-open eyes, and countless streaks of light burst from their hands, becoming a gigantic flash that flooded every direction.

Kuwaaaaaaah!

Red, blue, and white.

I swung the dazzlingly white blade of my spear toward the enormous flash.

Whoooooosh!
```
