<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0908.txt",
      "sha256": "74e6a0ac13caf63a27389e64263e5a3ab6770d9da36f298a201b7731a3b79408",
      "bytes": 14169
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7019518626f9d2f642ff285ca034521b8ce6b4e7b939e9891c250cf11e80a163",
      "bytes": 975
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "15b7559bed5551ab89a765328d3f0a3fb2d8b907d46fb1c26625499fb4cab311",
      "bytes": 230936
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "0df3c63e99d2d53be7f2c2570dd8afa6006de5031b4a6fa1b6b6f1d32cecfb21",
      "bytes": 739
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "bd93f71b315a40a3d4c5fd66edcdc14f02fc03677aafb8e37aa760f420054bbe",
      "bytes": 759
    },
    {
      "path": "characters/Hwangso.md",
      "sha256": "67b8233e9b6e5638f13ae548b9275eeeda6f5523ee93757f87afa8eacb2fe1ee",
      "bytes": 698
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "8f0860f478f1b37fc9bf403f6b6ac26e5206a8579cf9b3a48d5e5f6abc23457c",
      "bytes": 628
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "b58ce8a2d62d01bff659de8384070b0c85b11492210814cbb40fbcc2058badfc",
      "bytes": 699
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "5e708d2eba419917f47a5853f32cd182adf8306f1bf38f1296b4a5f2cd7ba411",
      "bytes": 1002
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c336a9b74793e3bf73bdc6e4d5a7447e62c84594f5d5258f730ffe7383f34d3d",
      "bytes": 262942
    }
  ],
  "estimated_tokens": 10390
}
-->

# Durable State Update — Chapter 908

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 908. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 908. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 908,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 908,
    "continuity_sources": [908],
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
    "Taekyung killed Ma Sanbao and remains in the banquet-hall battle, exhausted and badly injured.",
    "Jeok Cheongang is fighting Cang Gong, the Eastern Heaven Demon Lord.",
    "Jeong Hogun and the Embroidered Uniform Guard have intervened on the Emperor’s side and protected Taekyung.",
    "So Gyo’s identity and allegiance remain unknown.",
    "The Emperor and Cang Gong have not revealed all their forces.",
    "Hyuk Mujin and the Fire Dragon Pavilion members have arrived, followed by numerous black figures."
  ],
  "continuity_sources": [
    907
  ],
  "open_questions": [
    "Who is So Gyo, and where does her allegiance lie?",
    "What is the nature of Cang Gong’s power and his relationship to the Lord of Heaven?",
    "What forces are the Emperor and Cang Gong still withholding?",
    "Who are the black figures following Hyuk Mujin’s group?"
  ],
  "safe_through": 907,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 신법     | **movement technique**                           |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 황소 | **Hwangso** | First-generation disciple of the Gongdao Sect and a reluctant search-party member. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 이형환위 | **Shifting Form and Position** | Supreme Peak movement or evasion technique used by Jeok Cheongang. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 허공답보 | **Stepping on Empty Air** | Technique that allows Jongni Chu to move through empty air as if climbing invisible stairs. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 답보 | **stagnation** | Taekyung's current lack of progress in martial arts. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 마삼보 | 정호군 | East Depot de facto leader to Embroidered Uniform Guard Thousand Captain | Commander Jeong | courteous and controlled | Ma Sanbao addresses him as 정 천호 while asserting procedural limits and drawing him into a conversation. |
| 정호군 | 마삼보 | Embroidered Uniform Guard Thousand Captain to East Depot official | Eunuch Ma | formal and guarded | Jeong Hogun addresses him as 마 태감 and shows wariness despite his restrained replies. |

## Listed compact profiles

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 907
- **Aliases:** None
- **Role:** Cang Gong is a formidable martial artist who has taken the bestowed title Eastern Heaven Demon Lord and intends to take Jin Taekyung to the Lord of Heaven for recruitment.
- **Personality:** Calculating and self-assured, he admires Taekyung's ability while believing the Lord of Heaven's power will make him submit.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He serves the Lord of Heaven, recalls a former master and fellow disciples as family, and is Ma Sanbao's master; he regards Jin Taekyung as a potential recruit.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 907
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hwangso.md

# Hwangso (황소)

- **Safe through:** Chapter 882
- **Aliases:** None
- **Role:** First-generation disciple of the Gongdao Sect in Sichuan, deployed with roughly thirty second- and third-generation disciples to search for the surviving Third Fiend.
- **Personality:** Privileged, impatient, pleasure-seeking, inattentive, and dismissive of the danger surrounding the mission.
- **Voice:** Complaining and casual, with irreverent sarcasm toward his Senior Brother and the search.
- **Relationships:** His Senior Brother supervises him, and his prosperous merchant father forced him into the Murim to establish family connections.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 907
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 907
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 907
- **Aliases:** None
- **Role:** Ma Sanbao was the East Depot’s Brush-Holding Eunuch and a Supreme Peak martial artist who secretly led a restoration effort for Prince Shangshan and served as disciple of the Eastern Heaven Demon Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, led the restoration effort for Prince Shangshan, and recruited Jin Taekyung and Jeok Cheongang as allies; Jin killed him during the banquet-hall battle after Ma revealed his allegiance to his master, the Eastern Heaven Demon Lord.

## Korean source

```text
＃908화



아주 잠깐, 모든 사고 회로가 정지했다.

‘뭐야, 이게.’

나는 멍하니 입을 벌린 채 저 멀리 보이는 광경을 응시했다.

혼비백산한 얼굴로 뛰어오는 화룡각 대원들.

그리고 그 뒤를 맹렬히 쫓아 달려오는 일단의 무리.

두두두두!

지축이 울린다. 머리부터 발끝까지 흑의(黑衣)를 걸친 그들의 머릿수는 당장 보이는 머릿수만으로도 일천을 훌쩍 넘어갔고, 가까워질수록 또렷하게 느껴지는 섬뜩한 기세는 한 가지를 의미했다.

‘적!’

판단과 동시에 머릿속에서 켜진 붉은 경고등.

‘빌어먹을.’

도대체 어떻게 된 사정인지는 모른다, 하지만 지금부터 해야 할 일은 명백하다.

나는 정체를 알 수 없는 흑의인들의 등장으로 순간 소강상태에 빠진 전장에 외쳤다.

정확히는 금의위들에게.

“넋 놓고 있지 말고 무기 들어!”

물론 금의위들이 내가 명령을 내렸다고 해서 고분고분 따를 거라고는 생각하지 않았지만, 지금 내 옆에는 금의위 천호씩이나 되는 높으신 분이 있다.

“집결! 즉각 집결하라!”

전장을 일깨우는 정호군의 고함을 들으며, 나는 공력을 실어 땅을 박찼다.

꽈앙!

염화일로(炎火一路).

발끝에서 터져 나온 불꽃이 공기를 태운다.

폭발로 말미암은 충격을 등에 업고 한 걸음, 또다시 한 걸음을 내뻗자 이십여 장의 거리가 사라지고 석벽 위 그림자들이 가까워졌다.

금위군(禁衛軍).

금의위와 더불어 황도를 수호하는 대국의 정예이자, 황제를 배반하고 창공이라는 거죽을 뒤집어쓴 채 살아왔던 동천마군(東天魔君)의 그늘로 숨어든 역적들.

높게 솟은 석벽 뒤에서 숨어 쉴 새 없이 화살을 쏘아 대던 그들의 활시위는, 어느덧 흑의인들과 함께 자신들의 등 뒤에서 나타난 화룡각 대원들을 향해 겨누어져 있었다.

적어도 내가 들이닥치기 전까지는.

“장군, 명령을!”

하급 장교로 보이는 누군가의 다급한 부름에, 화려한 갑주를 걸친 중년인이 망설임 없이 손에 쥔 지휘봉을 휘둘렀다.

삽시간에 수십여 장의 거리를 지우며 다가오는 나를 향해서.

“발시(發矢)!”

짧은 갈등 끝에 명령이 떨어진 그 순간.

투투퉁! 솨아아악!

물경 일천에 달하는 궁수들이 몸을 돌려 팽팽하게 당겨져 있던 활시위를 놓았다.

무수한 은빛 화살촉이 공력을 머금은 채 하늘을 뒤덮으며 나를 향해 떨어져 내렸다.

완벽에 가까운 일제 사격, 그리고 초절정 고수라 해도 결코 무시하지 못할 위력까지.

하지만…….

‘상대를 맞추지 못한다면, 아무런 의미도 없지.’

꽈앙!

다시 한번 발끝에서 폭발시킨 염화일로의 화염과 함께, 나는 포탄처럼 쏘아졌다.

급격한 가속. 그리고 회피.

푸푸푸푸푹!

듣는 것만으로도 섬뜩해지는 맹렬한 파공성이 등 뒤에서 울려 퍼진다.

굳이 돌아보지는 않았지만, 조금 전까지 내가 서 있던 그 자리가 수많은 화살로 빼곡히 뒤덮였을 거라는 사실쯤은 소리만 듣고도 알 수 있었다.

대국을 대표하는 정예 중 하나인 금위군이 고작 이 정도에서 공격을 멈추지 않으리라는 것도.

“이게 무슨……!”

“동요하지 마라! 발시!”

예상을 뛰어넘는 내 속도에 당황했던 것도 잠시뿐. 철저하게 훈련받은 휘하의 금위군들은 물 흐르듯 자연스럽게, 동시에 쾌속한 속도로 새로운 화살을 시위에 걸어 쏘아 보냈다.

솨아아악!

한 번.

푸푸푸푹!

또다시 한번.

“쏴라! 쏘란 말이다!”

“순차 사격 개시!”

투투퉁!

그리고 두 차례에 나누어 쏟아진 네 번째 화살 비마저 아슬아슬하게 피해 냈을 때.

쾅!

나는 땅을 박차며 허공으로 솟구쳤고, 다섯 번째이자 마지막이 될 화살을 시위에 걸고 있던 금위군들의 비명 같은 외침이 터져 나왔다.

“노, 놈이. 놈이 옵니다!”

“발시! 발시하라!”

그야말로 찰나였다.

도합 네 번의 발사가 퍼부어지기까지 걸린 시간도, 내가 그 빽빽한 화살 비를 뚫고 석벽 위로 도달한 것 역시도.

그리고 순간 느려진 그 세상 속에서, 가장 기민하게 명령을 따라 움직인 일부 금위군이 나를 향해 쏘아 보낸 화살이 공간을 갈랐다.

아주 천천히. 나아가는 화살촉을 타고 흐르는 바람 소리마저 똑똑히 들을 수 있을 만큼.

솨악.

공력을 머금은 채 어둠 속에서 번뜩이는 수십여 발의 화살을 향해, 나는 손을 뻗었다.

동시에 가라앉은 심장 소리를, 옥당혈(玉堂血)이라 불리는 가슴의 정중앙에서 나만이 느낄 수 있는 파동을 일깨웠다.

‘멈춰라.’

그 순간.

화아아악!

보이지 않는 기운이, 공력(功力)과는 궤를 달리하는 미지의 힘이 내 의지에 따라 사방으로 뻗어 나갔다.

바람을 지우고, 공기를 멈추고, 그 안에서 느릿하게 움직이던 수십여 개의 화살을 붙잡았다.

우우웅.

대기가 몸을 떨었다. 느려졌던 시간이 원래의 속도를 되찾는다.

하지만 허공을 밟은 채 우뚝 서 있는 나를 올려다보는 무수한 눈동자들의 주인들은, 금위군은 경악에 물든 얼굴로 얼어붙어 있을 뿐이었다.

“이, 이런 미친…….”

누군가의 입술 사이로 신음처럼 흘러나온 한마디가 무거운 침묵을 깨트린다.

금방이라도 튀어나올 듯이 부릅떠진 그들의 눈동자에는, 마치 보이지 않은 손에 붙잡힌 듯이 허공에 멈춰 있는 수십여 발의 화살과 그 중심에 있는 내 모습이 고스란히 비치고 있었다.

“괴, 괴물.”

“도대체…… 도대체 어떻게.”

경악과 두려움. 불가해(不可解)에 가까운 존재를 목격한 자들만이 가질 수 있는 의문.

마지막으로, 아직 포기하지 않은 몇몇 이들의 발악까지.

“무엇들 하느냐! 어서 놈을 쏴라!”

“하, 하지만.”

“금위군 전원! 장군의 명을 따라 저 극악무도한……!”

목에 핏대를 세우며 휘하 병력을 향해 고함을 내지르는 일부 장교들을 향해, 나는 벼락처럼 손을 뻗었다.

아니, 정확히는 중단전(中丹田)의 기운으로 붙잡고 있던 화살을 흩뿌렸다.

쐐액 푸푸푹!

“커, 커헉.”

“크아아악!”

세찬 파공성에 뒤이어 울려 퍼지는 비명.

금위군이라는 이름에 걸맞는 명성답게 그들 역시 한 사람 한 사람이 제법 뛰어난 수준에 오른 고수들이었지만, 내가 조종하듯 쏘아 보낸 화살을 피할 수는 없었다.

한 사람을 제외한다면.

카카캉!

번뜩이는 검광(劍光)과 함께 비산하듯 튕겨 나가는 화살들.

금위군 중 누구보다 화려한 갑주만큼이나 빛나는 강기로 사방에서 들이닥친 공격을 단숨에 베어 낸 중년인의 모습에, 나는 문득 머릿속을 스친 생각을 입 밖으로 흘려보냈다.

“황도십이궁(黃道十二宮)?”

황도십이궁.

황실을 대표하는 열두 명의 초절정 고수를 통틀어 지칭하는 이명.



‘혹시 황도십이궁(黃道十二宮)이라고 들어봤나?’

‘알죠. 별자리 명칭 아닙니까?’

‘황도를 대표하는 열두 명의 초절정 고수를 뜻하는 말이기도 하지. 바로 그 황도십이궁에 속한 이들 중 절반이 아군이고.’



그건 마삼보에게서 직접 들었던 정보 중 하나였고, 무거운 눈빛으로 나를 바라보던 중년인은 자신의 대도(大刀)를 힘있게 말아 쥐었다.

“나를 알고 있나?”

“잘 알지.”

고개를 끄덕인 내가 말을 이었다.

“황제 통수 치고 암천이랑 붙어먹은 천하의 역적 새끼. 나와 내 사람들을 고슴도치로 만들고 싶었던 새끼. 그리고 잠시 후면 곧 뒈질 새끼.”

“……!”

“내 생각에는 이 정도면 충분한 것 같은데, 혹시 부연 설명이 더 필요하면 직접 씨부려 봐.”

“……아니. 충분하다. 한 가지만 빼고.”

형형하게 빛나는 안광과 함께, 중년인이 나직이 덧붙였다.

“죽는 건 내가 아니야.”

그 순간.

쐐액!

중년인의 신형이 흐릿해졌다.

경지에 다다른 이들만이 펼칠 수 있는 극상승의 경신법, 이형환위(移形換位).

그가 석벽을 박차고 허공으로 솟구침과 동시에, 어지간한 장정보다도 길고 큰 대도가 섬광처럼 공간을 뛰어넘어 나를 향해 쇄도했다.

초인이라 칭하기에 한 치의 부족함도 없는 속도와 힘.

그리고 도신을 빈틈없이 휘감고 있는 강기에서 뿜어져 나오는 무시무시한 기운까지.

‘강하다.’

나는 한눈에 알아볼 수 있었다.

저 이름 모를 중년인이 어느 정도 수준의 강자인지. 또한 지금의 경지에 올라 금위군을 이끄는 수장이 되기까지 얼마나 고된 수련을 거쳤을지.

하지만 바로 그렇기에, 저자의 대도는 결코 내 몸에 닿지 못한다.

어느 산맥의 정경을 한눈에 파악할 수 있다는 것은, 그보다 높은 위치에서 굽어보고 있다는 반증이었으니.

쏴아악!

단 한 걸음. 그것으로 족했다.

공간을 일그러트리며 들이닥친 대도는 텅 빈 허공을 평지처럼 밟으며 움직인 내 속도를 따라잡지 못했고, 줄기줄기 뿜어진 강기만이 아슬아슬하게 몸을 스쳤다.

치직.

불에 덴 듯한 통증.

이미 넝마가 된 의복 사이로 드러나 있던 살갗이 강대한 압력을 이기지 못하고 갈라진다. 터져 나가며 핏방울을 흩뿌린다.

내 것이 아닌, 또 다른 누군가의 핏물과 함께 뒤섞이며.

그륵, 컥.

가래 끓는 소리와 함께 중년인의 몸뚱어리가 파르르 떨렸다. 황소처럼 두꺼운 목에는 조금 전만 하더라도 찾아볼 수 없던 무언가가 삐죽 솟아 있었다.

어둠 속에서 차갑게 번뜩이는 무언가가.

“크륵. 이, 이건.”

간신히 허공답보(虛空踏步)를 유지하는 와중에도 믿을 수 없다는 듯이 화살촉을 더듬는 그를, 나는 담담하게 바라보았다.

“뜻하지 않은 선물을 너무 많이 받았더니 마음이 불편하더라고. 하나는 돌려줄 테니까 가져가.”

“허, 허공섭물(虛空攝物)?”

“비슷하긴 한데, 달라.”

툭.

나는 손가락으로 비틀거리는 그의 가슴 정중앙을 짚으며 말을 이었다.

“하지만 훨씬 더 어렵고, 확실한 거지.”

“……중단전. 중단전이로군.”

쿨럭.

한 움큼의 핏물을 토해 낸 중년인이 파르르 떨리는 눈빛으로 나를 바라보았다.

그리고 마지막 힘을 다해 아직 놓지 않은 대도를 힘겹게 들어 올렸다.

꺼져 가는 목소리와 함께.

“나, 나는 황도십이궁의 금우궁(金牛宮)이자, 금위군 친군지휘사사(直衛親軍指揮使司)이며, 그 누구보다 위대하고 전능하신 천주를 위해 신명을 다하는…….”

그리고 그 뒷말은, 영영 끝맺어지지 못했다.

스륵.

손아귀에서 미끄러진 대도가 먼저였을까.

아니면 눈앞에 짙게 드리워진 죽음과 함께 기울어진 몸뚱어리가 먼저였을까.

누가 먼저 지면에 처박혔는지는 모른다. 알고 싶지도 않다.

다만 주인과 병장기는 한 몸이 되어 추락했고, 나는 곧이어 지상에서 들려오는 둔탁한 소음을 들으며 석벽 위로 발을 내디뎠다.

정확히는 석상처럼 굳어 있는 금위군들의 한가운데로.

흐읍.

누군가가 헛숨을 삼킨다. 석벽 위를 가득 메운 그들에게서 무수한 감정의 소용돌이가 느껴졌다.

두려움과 분노, 경악. 마지막으로 어찌할 바를 모르는 혼란도.

그리고 저 혼란이 의미하는 바는, 단 하나일 것이다.

‘저들 모두가 암천의 끄나풀은 아니다.’

당장 이 전장에 있는 배신자들의 숫자만 물경 수천.

제아무리 동천마군이 창공이라는 이름으로 오랜 기간 황실에 있었다고는 하나, 이들 모두가 처음부터 암천의 개로 길러진 것은 아닌 것이 분명했다.

대국의 황실은 그리 호락호락하지 않으니까.

‘포섭. 강압. 혹은 거부할 수 없는 명령.’

아마도 암천은 그렇게 저들을 길들였을 테고, 놈들이 사용했던 당근과 채찍은 이제 내 손에 들어왔다.

“다른 것 몰라도 한 가지는 약속할 수 있다.”

불쑥 입을 연 나는 금위군 모두를 향해 말을 이었다.

“지금이라도 황실의 편에 선다면, 역적이 되는 것만은 어떻게 해서는 막아 주지.”

그리고 말이 끝남과 동시에, 손을 뻗었다.

살기를 띤 채 보이지 않는 사각에서 다가오던 금위군 장교를 향해.

쉭. 쿠웅.

한 줄기 파공성이 울려 퍼졌고, 하나의 시체가 늘어났다.

나는 지풍(指風)에 미간을 관통당한 채 쓰러진 시체를 가리키며 담담하게 덧붙였다.

“내 제안이 마음에 들지 않는 사람, 손?”

“……!”

“……!”

아무도 손을 들지 않았고, 나는 석벽 아래로 뛰어내렸다.

물론, 마지막으로 꼭 필요한 한 마디를 건네는 것도 잊지 않았다.

“아, 너희들이 봤을 때 진짜 이 새끼는 악질이다 싶은 놈은 지금 당장 쳐내라.”

“예, 예?”

“죽이라고, 너희가 직접.”

“……!”

그래.

지금부터 서로 죽여라.

나는 서로를 곁눈질하는 금위군들 을 뒤로 하고 달려나갔다.

정체불명의 흑의인들을 피해 도망쳐 오는 화룡각 대원들을 맞이하기 위해서.

그들을 구하기 위해서.

쐐애액!
```

## Final English reading copy

```markdown
# Chapter 908

For a very brief moment, every thought in my head ground to a halt.

*What the hell is this?*

I stared, mouth hanging open, at the scene in the distance.

The Fire Dragon Pavilion members were running toward me, panic written all over their faces.

And a group was charging after them at full speed.

*Rumble, rumble, rumble!*

The ground shook. The figures were dressed in black from head to toe, and even the ones I could see right then numbered well over a thousand. The more clearly I felt their chilling aura as they drew closer, the more obvious one thing became.

*Enemies!*

A red warning light flashed in my mind at the same moment I reached that conclusion.

*Shit.*

I had no idea what was going on, but what I needed to do now was clear.

The battlefield had fallen into a momentary lull at the appearance of the unknown black-clad figures. I shouted into the quiet.

More precisely, I shouted at the Embroidered Uniform Guards.

“Quit standing there with your jaws hanging open and pick up your weapons!”

Of course, I didn’t expect the Embroidered Uniform Guards to obediently follow my orders just because I’d given them. But right beside me was a man of high standing—a Thousand Captain of the Embroidered Uniform Guard, no less.

“Rally! Rally immediately!”

As Jeong Hogun’s shout roused the battlefield, I channeled my internal energy and kicked off the ground.

*Boom!*

Flamefire Path.

Flames burst from my toes, scorching the air.

Riding the shock wave from the explosion, I took a step, then another. In an instant, the distance of twenty-odd *jang* vanished, and the shadows atop the stone wall drew near.

The Imperial Guards.

Along with the Embroidered Uniform Guard, they were one of the Great Nation’s elite forces, charged with protecting the imperial capital. They were also traitors who’d betrayed the Emperor and taken refuge in the shadow of the Eastern Heaven Demon Lord, who had lived behind the guise of Cang Gong.

The archers who’d hidden behind the towering stone wall and fired arrow after arrow had now turned their bows toward the Fire Dragon Pavilion members, who had appeared behind them alongside the black-clad figures.

At least, that was where they’d been aiming before I arrived.

“General, your orders!”

At the urgent call of someone who looked like a junior officer, a middle-aged man in ornate armor swung the baton in his hand without hesitation.

He swung it at me as I closed the dozens of *jang* between us in an instant.

“Loose!”

The order came after a brief moment of hesitation.

*Thwang-thwang-thwang! Fwoooosh!*

A full thousand archers turned and released their taut bowstrings.

Countless silver arrowheads, imbued with internal energy, blanketed the sky as they came raining down on me.

A near-perfect volley, with enough power that even a Supreme Peak master couldn’t afford to ignore it.

But…

*If they don’t hit their target, they’re useless.*

*Boom!*

With another burst of flame from my toes, I shot forward like a cannonball.

A sudden burst of speed. Then a swerve.

*Thup-thup-thup-thup!*

A fierce, chilling whistle of arrows rang out behind me.

I didn’t bother looking back, but I could tell from the sound alone that the spot where I’d stood a moment ago was now covered in arrows.

And I knew the Imperial Guards, one of the Great Nation’s elite forces, wouldn’t stop attacking after just that.

“What the—!”

“Don’t lose your nerve! Loose!”

Their surprise at my speed lasted only a moment. The Imperial Guards under the commander’s control had been trained thoroughly. They nocked new arrows and loosed them in a smooth, swift rhythm.

*Fwoooosh!*

Once.

*Thup-thup-thup!*

Then again.

“Fire! I said fire!”

“Begin staggered fire!”

*Thwang-thwang!*

And just as I narrowly evaded the fourth rain of arrows, shot in two successive waves—

*Bang!*

I kicked off the ground and shot into the air. The Imperial Guards were already nocking the fifth and final volley when their screams broke out.

“H-He’s coming!”

“Loose! Loose!”

It all happened in the blink of an eye.

The four volleys had been fired in barely any time at all. And I’d crossed that thick storm of arrows to reach the top of the stone wall just as quickly.

In the world that had slowed to a crawl, a few of the most alert Imperial Guards had reacted to the order and loosed their arrows at me. The arrows cut through space.

Very slowly. Slowly enough that I could hear the wind rushing along each advancing arrowhead.

*Whoosh.*

I reached out toward the dozens of arrows flashing in the darkness, each imbued with internal energy.

At the same time, I stirred my quiet heartbeat—the pulse I alone could sense at the very center of my chest, in the spot called the Jade Hall.

*Stop.*

At that instant—

*Whoooosh!*

An invisible force—an unknown power on a completely different plane from internal energy—spread out in every direction at my will.

It erased the wind, stilled the air, and caught the dozens of arrows moving sluggishly through it.

*Rrrrrumble.*

The air trembled. Time, which had slowed, returned to its normal pace.

But the Imperial Guards looking up at me, standing upright in midair, could only stare, their faces frozen in shock.

“Th-This is insane…”

The groan that slipped from someone’s lips broke the heavy silence.

In their wide eyes, bulging as if they might pop out, the dozens of arrows hanging in midair—as though caught by an invisible hand—and me at their center were reflected in full.

“A m-monster.”

“How… How is this possible?”

Shock and fear. Questions only those who’d witnessed something close to incomprehensible could ask.

And lastly, the desperate resistance of a few who still hadn’t given up.

“What are you waiting for? Shoot him!”

“B-But…”

“All Imperial Guards! Follow the General’s orders and take down that heinous—!”

I shot my hand out like a bolt of lightning toward the few officers screaming at their men.

Or, to be exact, I scattered the arrows I’d been holding with the power of my Middle Dantian.

*Whoosh! Thup-thup-thup!*

“G-Gah!”

“Gaaah!”

Screams rang out after the arrows’ fierce whistle.

True to their reputation as Imperial Guards, each of them was a master of no small skill. But they couldn’t dodge the arrows I sent flying as if I were controlling them.

Except for one man.

*Clang-clang!*

Arrows bounced away in a flash of swordlight.

The middle-aged man had cut down the attacks coming at him from all sides in a single sweep, his Force shining as brilliantly as the ornate armor that set him apart from every other Imperial Guard. A thought flashed through my mind, and I let it slip out.

“One of the Twelve Palaces of the Zodiac?”

The Twelve Palaces of the Zodiac.

The title collectively referring to the twelve Supreme Peak masters who represented the imperial court.

*“Have you ever heard of the Twelve Palaces of the Zodiac?”*

*“Sure. Aren’t they the names of constellations?”*

*“It’s also what they call the twelve Supreme Peak masters who represent the imperial capital. And half of them are on our side.”*

It was one of the things Ma Sanbao had told me himself. The middle-aged man looked at me with a grave expression and tightened his grip on his great saber.

“Do you know me?”

“I know you well.”

I nodded and went on.

“You’re the treacherous piece of shit who betrayed the Emperor and sided with Dark Heaven. The asshole who wanted to turn me and my people into pincushions. And the asshole who’s about to die.”

“……!”

“That seems like enough to me. If you need more explanation, spit it out.”

“……No. That’s enough. Except for one thing.”

With a sharp gleam in his eyes, the middle-aged man added quietly,

“I’m not the one who’s going to die.”

At that moment—

*Whoosh!*

The man’s figure blurred.

Shifting Form and Position, a supreme movement technique that only those who’d reached the highest realms could perform.

The moment he kicked off the stone wall and sprang into the air, his great saber—longer and larger than most men—crossed the space between us in a flash.

Speed and power that left nothing wanting in a superhuman.

And the terrifying aura pouring from the Force wrapped tightly around the blade.

*Strong.*

I could tell at a glance how powerful this nameless middle-aged man was. I could also tell how grueling the training must have been that brought him to this realm and made him the commander of the Imperial Guards.

But that was exactly why his great saber could never touch me.

To take in the scenery of an entire mountain range at a glance meant you were looking down at it from higher up.

*Whoooosh!*

A single step. That was all it took.

The great saber tore through distorted space, but it couldn’t match my speed as I moved through the air as if it were solid ground. Only the strands of Force it sent flying barely grazed me.

*Sizzle.*

Pain like a burn.

The powerful pressure split the skin showing through my already-tattered clothes. It burst open, scattering drops of my blood.

They mingled with someone else’s.

*Grrk. Cough.*

With a wet, phlegmy sound, the middle-aged man’s body quivered. Something that hadn’t been there moments ago jutted from his thick, bull-like neck.

Something glinting coldly in the darkness.

“Grrk. Wh-What is this?”

Even as he struggled to maintain Stepping on Empty Air, he fumbled at the arrowhead, unable to believe what had happened. I looked at him calmly.

“I’ve been getting so many unexpected gifts that I started feeling bad. I’ll return one of them. Take it.”

“Seizing an Object Through Empty Space?”

“Similar, but different.”

*Tap.*

I touched the center of his unsteady chest with my finger and continued.

“But it’s much harder—and a lot more certain.”

“……The Middle Dantian. It’s the Middle Dantian.”

*Cough.*

The middle-aged man spat out a mouthful of blood and looked at me with trembling eyes.

Then, with what little strength he had left, he struggled to raise the great saber he still clutched.

His voice fading, he said,

“I… I am the Golden Ox Palace of the Twelve Palaces of the Zodiac, the Chief Commander of the Imperial Guard, and one who gives his life to the great and almighty Lord of Heaven…”

The rest of his words would never be spoken.

*Slip.*

Was it the great saber sliding from his hand that happened first?

Or his body, tipping over as death loomed darkly before his eyes?

I didn’t know which hit the ground first. I didn’t care to know.

Master and weapon fell as one. Then, as the dull thud rose from the ground below, I stepped onto the stone wall.

More precisely, into the middle of the Imperial Guards, who stood frozen like statues.

*Hff.*

Someone sucked in a breath. A whirl of emotions rose from the countless men crowding the top of the wall.

Fear and anger, shock. And, last of all, confusion at not knowing what to do.

And that confusion could only mean one thing.

*Not all of them are Dark Heaven’s lackeys.*

There were thousands of traitors on this battlefield alone.

No matter how long the Eastern Heaven Demon Lord had served in the imperial court under the name Cang Gong, it was clear that not all these men had been raised as Dark Heaven’s dogs from the beginning.

The Great Nation’s imperial court wasn’t that easy to fool.

*Winning them over. Coercion. Or orders they couldn’t refuse.*

Dark Heaven had probably broken them in that way. And now the carrots and sticks they’d used were in my hands.

“There’s one thing I can promise you, at least.”

I spoke up abruptly, then addressed all the Imperial Guards.

“If you side with the imperial court now, I’ll make sure you don’t end up as traitors, one way or another.”

As soon as I finished speaking, I reached out.

Toward the Imperial Guard officer who was approaching unseen from a blind spot, his killing intent clear.

*Whoosh. Thud.*

A streak of air whistled by, and one more corpse hit the ground.

I pointed at the body lying there, a Finger Qi hole through its brow, and added calmly,

“Anyone here who doesn’t like my offer, raise your hand.”

“……!”

“……!”

No one raised a hand. I jumped down from the stone wall.

Of course, I didn’t forget one last thing I absolutely had to say.

“Oh, and if you see someone who’s a real bastard, cut him down right now.”

“E-Excuse me?”

“Kill him. Do it yourselves.”

“……!”

That’s right.

From here on out, kill each other.

I left the Imperial Guards glancing at one another and ran toward the Fire Dragon Pavilion members fleeing from the mysterious black-clad figures.

To meet them.

To save them.

*Whoooosh!*
```
