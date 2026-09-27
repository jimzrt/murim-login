<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1070.txt",
      "sha256": "6152ef03d5327f4868c6b6f7dba5e8567d4e938183294b21757375b3dc265f59",
      "bytes": 12297
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "685cb18eede2136a247e0acf61cd71ce9e7ba94b9bf563b551f97dbd84f0d6df",
      "bytes": 1414
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5be93eb6bd068e9f3140c82d613f582e8e72d687cb3b90fa54d2c393096f3e5c",
      "bytes": 242356
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "747020984959e7108b5deee7f0d065b57d8ad94823dc06b27c86cd0674336f65",
      "bytes": 760
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "997b3dba76203e5a8859c9f8a82408327f6bf034c713f5e50f6ae3d34b8baff6",
      "bytes": 839
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "fa3699e3146b4147940549d30c2122de56f73df2c4da99455f186ef777cf1480",
      "bytes": 1502
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "7d424ae7a32bdc9fd53271cf373486d4a1261c023fbfe4635ff66d53e90476c2",
      "bytes": 700
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0259aca58b614d4464af2d4cf05e533bf32470e8476e9295bc8469f420e73abb",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0582c27e93439b0b8b2af15db2c05c74222687a70d65249256c7a0722261150b",
      "bytes": 623
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "2208bab2a1db79c0db16e45b5d6a8cad5bed43460eccf76cf1e4c751e61b233e",
      "bytes": 700
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7df8b2357d0faa08e63a571debd66c331206f8c9af0b11d116826f4c7dad2ad4",
      "bytes": 284375
    }
  ],
  "estimated_tokens": 10780
}
-->

# Durable State Update — Chapter 1070

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
1 and safe_through 1070. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1070. Profile updates may replace only one
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
  "chapter": 1070,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1070,
    "continuity_sources": [1070],
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
    "Jin’s allied force is retreating toward Qinghai Lake while repeatedly pursued by tireless undead; reaching the lake is estimated to take two days at full effort.",
    "A rumble stronger than any previous pursuer’s has begun in the distance as Jin’s group retreats.",
    "Jeong Hogun agreed to Jin’s order to remove the Embroidered Uniform Guard’s armor, but Jin told him to keep his helmet on when the new rumble began.",
    "Ma Sanbao serves the Blood Lord and was covertly watching Jin’s force; Great Sir first detected the surveillance in Ningxia.",
    "The East Depot’s network had shared its view with Dark Heaven through the Eastern Heaven Demon Lord.",
    "The Grand Mage suspects Hyeoncheon and the Kongtong survivors went to Great Sir."
  ],
  "continuity_sources": [
    1068,
    1069
  ],
  "open_questions": [
    "Who is Great Sir, and what is his connection to Hyeoncheon and the surviving Kongtong Disciples?",
    "Did Jin’s sword strike kill or otherwise affect the watching crow?",
    "Are Dark Heaven’s forces broadly composed of reanimated corpses, and has Ma Sanbao spread the Corpse Art to others?",
    "What caused the new rumble, and what is approaching the retreating group?",
    "What is the Lord of Heaven seeking through Jin, and when will he appear?"
  ],
  "safe_through": 1069,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 궁성     | **Bow Saint**                 | —              |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 사파     | **unorthodox faction**                           |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 지능               | **Intelligence**               |
| 몬스터     | **monster**           |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천라지망 | **net over heaven and earth** | Jeok Cheongang's figurative threat to pursue a culprit everywhere. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화룡일미 | **Fire Dragon's Single Tail** | A form of the Fire Dragon Divine Spear. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 반고 | **Pangu** | Primordial giant from Chinese creation mythology. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 정호군 | 진태경 | imperial officer responding to the Marquis of Shangshan | Marquis of Shangshan | formal and deferential | Accepts the command with a formal acknowledgment of Taekyung’s title. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1068
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 1068
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1069
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 1069
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1068
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1068
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 1069
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

## Korean source

```text
1070화




감각이란 곧 정보를 의미한다.

인간은 자신에게 주어진 오감(五感)을 통해 보고, 듣고, 맡고, 맛보고, 느낌으로써 주위에서 벌어지는 상황을 알 수 있다.

바로 지금처럼.

‘이건.’

그 감각은 초대받지 않는 사람처럼 불현듯 찾아왔고, 나는 호흡마저 삼키며 어딘가를 응시했다.

고작 십여 장 밖의 사물도 제대로 분간하기 어려운 어둠 너머를.

그러나 무공의 향상은 감각의 발달을 의미하고, 체내에 축적된 수 갑자의 공력은 그 발달된 감각을 한계 이상으로 끌어올리기에 차고 넘친다.

“아직 벗지 마라.”

“……!”

단 한 마디로도 충분했다.

일순간 크게 부풀어 오른 정호군의 눈동자가 대답을 대신했으니.

그리고 나와 거의 동시에, 아니 분명 그보다 미세하게 앞서 이변을 알아차렸을 궁성과 적천강이 차례대로 입을 열었다.

“삼백여 장 밖. 먼지구름.”

“지금껏 상대했던 놈들과는 다르군. 다들 각오하거라.”

궁성이 보고 들은 것을 말했다면, 적천강은 자신의 짐작을 입에 담았다.

나 역시도 느끼고 있던 불길한 짐작을.

드득, 드드득.

지면을 통해 점점 가까워지는 진동.

하지만 지금까지와는 뭔가 다르다.

세 번에 걸쳐 맞닥트린 추격대와 달리, 이번의 울림은 비교할 수 없을 만큼 크고 깊었다.

‘뭐지?’

머릿속 의문과 함께 더욱더 감각을 극대화시키자, 비로소 새로운 단서를 얻을 수 있었다.

쿵. 쿠궁.

쉼 없이 이어지는 잔 떨림 사이에 드문드문 스며 있는 울림.

아니.

‘굉음.’

그 사실을 깨달은 순간, 서늘한 한기가 등골을 타고 흘러내렸다.

이건, 저 굉음은 한낱 인간이 낼 수 있는 종류의 것이 아니다.

이 세상에 존재해서는 안 되는, 그러나 결국 현실로 나타나고야 말았던 저주받은 괴물들의 전유물이다.

쿠우우웅!

성큼 가까워진 울림이 땅을 뒤흔들고, 야트막한 언덕 위로 또 다른 어둠과 악취가 덧씌워진다.

그리고…….

- 그. 아. 아. 아.

도저히 인간이라 부를 수 없는 무언가가, 느릿하면서도 음산한 포효와 함께 언덕 위로 고개를 내밀었다.

아니, 몬스터(Monster)가.



* * *



그 저주받은 괴물을 두 눈으로 목격한 순간, 삼천여 명의 사람들은 동시에 얼어붙었다.

강철보다 단단한 충성심으로 무장한 금의위도.

사파 무림에서 활동하며 산전수전을 겪어 왔던 흑룡마문의 무인들도.

긴 세월 도가(道家)에 몸담아 정순하게 심신을 갈고닦은 종남과 공동의 제자들도.

무공의 고하도, 강호의 경륜도 지금 이 순간만큼은 무의미했다.

그들을 강타한 거대한 충격에는 무공의 고하도, 나이와 경험에 의한 경륜도 소용없었다.

그럴 수밖에 없었고, 그것이 당연했다.

‘도대체…… 저게 뭐지?’

언덕 위로 모습을 드러낸 괴물을 확인한 순간, 모두가 동시에 같은 생각을 떠올렸다.

거대했고, 그저 거대했다.

그 압도적인 광경 앞에서 척(尺)이라는 단위는 이미 머릿속에서 지워졌다.

비단 그들이 아닌 천하의 누구라도 마찬가지였을 것이다.

물경 이 장에 달하는 높은 키와 아름드리나무 같은 몸통을 지닌 저 괴물을 보았다면.

- 그. 아. 아. 아.

거대한 구멍이, 아니 괴물의 입이 열리자 바람이 불었다.

그리고 포효라고 부르기에는 너무나도 느린, 그래서 더욱 소름 끼치게 느껴지는 괴성과 함께 쏟아진 바람에는 끔찍한 악취 이상의 것이 담겨 있었다.

공포.

그것은 공포였다.

인간이 느낄 수 있는 가장 어두운 감정인 동시에, 어느 괴물들에게 있어서는 탄생과 함께 부여된 권능.

공포 이외에는 설명할 길이 없기에, 다른 세상의 이들이 그 의미 그대로 피어(Fear)라 부르는 그 힘.

우우우웅.

사람들은 느낄 수 있었다.

파르르 떨리는 공기와 어느덧 흐릿해져만 가는 시야를.

그리고 지면에서 떨어지지 않는 자신들의 두 다리를.

“워, 원시천존이시여…….”

어느 도사의 입술 사이로 흘러나온 외마디 신음이 모두의 심정을 대변하고 있었다.

괴력난신(怪力亂神)?

불가해(不可解)?

아니다. 틀렸다. 부족하다.

도대체 어떤 표현과 단어로 지금 이 상황을, 저 괴물을 온전히 설명할 수 있을 것인가.

어찌하여 그들이 따르는 신이, 정녕 저토록 저주받은 존재를 이 땅에 허락했단 말인가.

불과 며칠 전, 대설산의 광활한 설원을 새카맣게 뒤덮었던 그 무수한 암천의 교도들조차 이 정도의 공포를 심어 주지는 못했다.

금의위들이 똑똑히 기억하고 있는, 동천마군의 방울 소리를 따라 황실의 대연회장을 피로 물들였던 강시들 역시 마찬가지였다.

최소한 그들은 인간의 형태를 하고 있었으니까.

더는 인간이라 부를 수 없는 상태가 되었을지언정, 본래의 형태는 조금이나마 간직하고 있었으니까.

하지만…….

‘말도 안 돼.’

‘있을 수 없다. 결코 있을 수 없는 일이야.’

‘꿈. 그래. 꿈이 분명해.’

제자리에 얼어붙은 사람들은 아득하게 물든 시선으로, 마침내 언덕 위에 우뚝 선 괴물을 바라보았다.

감히 추측할 수조차 없는 까마득한 과거.

한 자루의 도끼를 휘둘러 세상을 열었다는 태곳적의 거인, 반고(盤古)가 실재한다면 저런 모습일까 싶었다.

물론 구설로만 전해져 내려오는 반고의 장엄한 신화와 달리, 저 괴물은 누군가의 악몽에서 끄집어낸 것과 다름없는 모습을 하고 있었지만.

쿠웅. 구구구궁!

단 한 걸음.

그러나 결코 ‘고작’이라고 표현할 수 없는 괴물의 무거운 발걸음에, 야트막한 언덕이 단숨에 허물어지는 광경을 본 이들은 끝없는 공포에 사로잡혔다.

지금껏 듣도 보도 못한 것에 대한 막연한 두려움.

그저 바라보는 것만으로도 숨이 멎을 것 같은 그들의 감정이 보이지 않는 손이 되어 심장을 힘주어 터트리는 듯했다.

바로 다음 순간, 어디선가 터져 나온 눈부신 섬광이 아니었다면 분명 그러했을 것이다.

화아아악!

일순간, 캄캄했던 어둠이 갈라졌다.

어둡지만 밝고, 밝지만 어두운 검푸른 기운을 따라 공간이 일그러졌다.

빛도, 어둠도 아닌 무언가.

그것의 정체는 다름 아닌 화염이었다.

어둠과 빛 모두를 간직한, 그리고 모든 것을 불태우고 정화시킬 수 있을 만큼 강대한 겁화(劫火).

그리고 공간을 일그러트리며 나아가는 그 화염의 끝자락에는, 이제 막 언덕을 넘어 걸음을 내디딘 거대한 괴물이 있었다.

- 그. 아. 아!

사방을 떨어 울리는 포효.

그와 동시에 통나무만큼이나 두꺼운 팔이 압축된 공기를 터트리며 화염을 향해 휘둘려졌다.

아니.

정확히는 화염이 깃든 창과 한 몸이 되어 쏘아지고 있는, 작고 초라한 한 인간을 향해.

후우우웅!

끔찍하리만치 거센 파공성.

그러나 엄청난 거력(巨力)이 실린 주먹이 다가오고 있음에도, 보이지 않은 허공의 계단을 밟으며 괴물을 향해 쇄도하는 진태경의 눈빛은 조금도 흔들리지 않았다.

나아가는 발걸음도, 그에 따라 쏘아지는 신형도.

그리고.

군청색의 화염이 깃든, 은백색의 창날도.

스륵.

돌연 부드럽게 움직이는 창날을 따라 일렁이는 화염.

그 안에 담긴 강대한 열기를 따라 공간이 일그러지는 광경은, 마치 한 마리의 화룡이 움직이는 것과 닮아 있었다.

머나먼 과거, 열화문의 옛 사조가 고심 끝에 창안한 창술의 어느 초식명 그대로.

‘화룡일미(火龍一尾).’

그렇게 허공을 유영하던 화룡의 꼬리가, 괴물의 주먹과 마주친 그 순간.

서걱!

지상의 모두는 볼 수 있었다.

소름이 끼칠 만큼 예리한 절삭음과 함께, 주인의 몸뚱어리에서 분리된 거대한 살덩어리를.

그리고 그것은 괴물 역시 마찬가지였다.

- 그. 어?

괴물은 의문이 담긴 눈빛으로 자신의 거대한 주먹을, 정확히는 주먹이 있던 자리를 바라보았다.

이제서야 핏물이 몽글몽글 맺히기 시작한 그 예리한 단면을.

푸화아악!

폭발하듯 터져 나오는 피분수. 뒤늦게 찾아온 고통과 아직 해결되지 못한 의문에 휩싸인 괴물은 형용할 수 없는 감정에 사로잡혀 몸부림쳤다.

지금 이 순간에도 오직 일점(一點)을 향해 나아가는, 눈부신 속도의 창날을 인지하지 못한 채.

푸욱.

괴물은 느꼈다.

눈앞이 새하얗게 물들만큼 뜨겁고, 한편으로는 몸서리칠 정도로 차가운 무언가를.

정확히 목줄기를 파고든 그것은 괴물이 막 토해 내려던 괴성을 틀어막은 채, 도무지 저항할 수 없는 불길을 쏟아 내고 있었다.

지금 이 순간 괴물의 시야를 가득 채운, 한 사람의 눈동자처럼.

“이건 트롤도, 오우거도 아니고…… 너, 도대체 뭐냐?”

낮게 가라앉은 목소리.

그러나 지능이 낮은 괴물로서는 그 말의 뜻을 이해할 수 없었고, 진태경은 혼란에 물든 괴물의 커다란 눈동자를 통해 그 사실을 받아들였다.

“그래, 그렇겠지. 딱 그 정도까지만 허락된 거겠지. 네게는.”

몬스터의 지능은 곧 힘과 비례하는 법.

작게 중얼거린 진태경은 깊게 가라앉은 눈빛으로 괴물을 바라보았다.

창날에 가로막혀 어떠한 소리도 내지 못한 채, 서서히 꺼져 가는 눈동자로 눈앞의 인간을 응시하는 그것의 모습에 저절로 이가 악물렸다.

“도대체 누가, 어떻게 널 탄생시킨 거지?”

그건 대답을 듣기 위한 질문이 아니었다.

진태경이 스스로에게 던지는 질문이자, 거인의 어깨너머로 모습을 드러낸 또 다른 적들을 향한 물음이었다.

쿠웅! 구구구궁!

짙은 어둠을 망토처럼 두른 채 파도처럼 밀려오는 크고 작은 그림자들.

잘게 떨렸던 대지는 이제 지진이라도 난 것처럼 거세게 뒤흔들리고 있었고, 이는 비단 한 방향에서만 벌어지는 일이 아니었다.

드드득.

수십여 장 앞까지 다가온 적들이 일으키는 거대한 굉음의 틈바구니에 숨어 전해지는 미세한 울림들.

어느덧 저 멀리, 사방에서 겹겹이 전해지는 그 크고 작은 진동을 느낀 진태경은 자신도 모르게 뇌까렸다.

“……천라지망(天羅地網).”

틀림없다.

어느샌가 그들은 포위되었다. 그것도 아주 치밀하게.

그리고 이것이 지능이 낮은 몬스터들 따위가 갖출 수 있는 포위망이 아니라는 사실을, 진태경은 누구보다 잘 알고 있었다.

짤랑. 짤랑.

바람을 타고 곳곳에서 전해지는 희미한 방울 소리를 들으며, 진태경은 깊게 박힌 창날을 비틀었다.

콰득, 푸화악!

단말마도 없이 숨이 끊어진 괴물의 신형이 허물어지고, 고약한 악취를 풍기는 핏물이 터져 나와 옷깃을 적셨다.

하지만 진태경은 조금도 신경 쓰지 않았다.

오늘 밤이 지나도록, 어쩌면 앞으로 며칠이 지나더라도 수도 없이 놈들의 피를 뒤집어써야 할 테니까.

그래야만 이 끔찍하리만치 촘촘한 그물망을 찢고 동쪽으로 갈 수 있을 테니까.

“다들 봤지? 이 새끼들 좆도 아닌 거.”

진태경은 모두를 향해 말했다.

동서남북.

그 어디에도 피할 곳은 없다. 남은 길은 오직 맞서는 것뿐이다.

“가자.”

낮게 가라앉은 그 한 마디와 함께, 삼천여 개의 병장기가 적들을 향해 겨누어졌다.
```

## Final English reading copy

```markdown
# Chapter 1070

The senses were information.

Through their five senses—sight, hearing, smell, taste, and touch—people could learn what was happening around them.

Just like now.

*This is…*

The sensation came without warning, like an uninvited guest. I held my breath and stared into the darkness.

Beyond it, I could barely make out anything a hundred feet away.

But improving your martial arts meant sharpening your senses, and the several jiazi of internal energy stored within me were more than enough to push those sharpened senses past their limits.

“Don’t take it off yet.”

“……!”

One short sentence was all it took.

Jeong Hogun’s eyes widened in an instant, answering for him.

And nearly at the same time as me—or, no, just a hair before me—Bow Saint and Jeok Cheongang each spoke in turn.

“Dust cloud. About a thousand yards out.”

“They’re not like the ones we’ve faced so far. Everyone, prepare yourselves.”

Bow Saint told us what she’d seen and heard. Jeok Cheongang voiced his suspicions.

The same ominous suspicions I’d been having.

*Rumble. Rumble.*

The ground trembled, the vibration drawing closer by the moment.

But something was different this time.

The rumble was incomparably louder and deeper than the pursuing forces we’d clashed with three times already.

*What is it?*

I pushed my senses further, and at last picked up a new clue.

*Boom. Boom.*

Amid the constant, faint tremors came the occasional, heavier impact.

No.

*A thunderous boom.*

The moment I realized, a chill ran down my spine.

That sound—that tremendous boom—wasn’t something an ordinary human could make.

It belonged to cursed monsters that shouldn’t exist in this world, but had come into reality all the same.

*Rooooom!*

The rumble surged closer and shook the earth. Another darkness, carrying a stench with it, spread over the low hill.

And then—

“Grrrraaaah.”

Something that could hardly be called human slowly raised its head above the hill, letting out a low, ominous roar.

No. It was a monster.



* * *



The moment they saw the cursed monster with their own eyes, all three thousand people froze.

The Embroidered Uniform Guard, clad in loyalty harder than steel.

The martial artists of the Black Dragon Demon Gate, who’d endured every hardship the unorthodox martial world could throw at them.

The Disciples of the Zhongnan and Kongtong Sects, who’d spent long years cultivating their minds and bodies in the Daoist tradition.

In that moment, the level of their martial arts and their experience in the martial world meant nothing.

The enormous shock that hit them was beyond the reach of skill, age, or experience.

It couldn’t have been otherwise. It was only natural.

*What the hell… is that?*

The moment the monster came into view atop the hill, everyone had the same thought.

It was huge. Just huge.

Faced with that overwhelming sight, the very unit of measurement called a *foot* vanished from their minds.

Anyone in the world would have felt the same if they’d seen that monster, nearly twenty feet tall, with a torso as thick as a great tree.

“Grrrraaaah.”

A vast hole opened—or rather, the monster’s mouth—and wind blew from it.

Its cry was too slow to call a roar, and all the more chilling for it. The wind that poured out with that sound carried more than a horrible stench.

Fear.

It was fear.

The darkest emotion a human could feel—and, for some monsters, a power bestowed at birth.

There was no other word for it. So people from another world called that power exactly what it was: Fear.

*Hummmmmm.*

The people could feel it.

The air trembling around them. Their vision growing hazy.

And their legs, unable to move from the ground.

“P-Primordial Heavenly Venerable…”

The single groan that slipped from one Daoist’s lips spoke for them all.

Supernatural powers?

The inexplicable?

No. Wrong. Not enough.

What words could possibly describe this moment, this monster, in full?

Why had the god they followed allowed such a cursed being to walk this earth?

Only days ago, countless followers of Dark Heaven had blackened the vast snowy fields of Great Snow Mountain. Even they hadn’t filled the people with this much terror.

Nor had the jiangshi who, following the Eastern Heaven Demon Lord’s bell, had stained the imperial palace’s great banquet hall with blood—the ones the Embroidered Uniform Guard remembered all too well.

At least they’d still had human shapes.

No matter how far they’d fallen from being human, they’d retained some trace of what they once were.

But—

*This can’t be real.*

*It can’t be. This is impossible.*

*It’s a dream. Yes. It has to be.*

Frozen in place, the people stared with distant, clouded eyes at the monster standing atop the hill.

If Pangu, the primordial giant said to have opened the world with a single swing of his axe, had truly existed in some unimaginably distant past, perhaps he’d looked like that.

Of course, unlike Pangu’s majestic myth, passed down through rumor alone, this monster looked as though it had been dragged straight out of someone’s nightmare.

*Boom. Rumble!*

One step.

But no one who saw the low hill crumble in a single step could call it “just” a step. The monster’s heavy footfall trapped them in endless terror.

A vague fear of something they’d never seen or heard of before.

Just looking at it felt enough to stop their breath. Their fear seemed to become an invisible hand, squeezing their hearts until they burst.

That was what would have happened—if a dazzling flash hadn’t erupted from somewhere at that very moment.

*Whoosh!*

In an instant, the pitch-black darkness split apart.

Space warped along a deep blue flame, dark yet bright, bright yet dark.

Something that was neither light nor darkness.

It was fire.

Hellfire, holding both darkness and light, powerful enough to burn and purify everything.

At the very tip of that fire, warping space as it surged forward, stood the enormous monster that had just stepped over the hill.

“Grrrraah!”

Its roar shook the air in every direction.

At the same time, an arm as thick as a log swung toward the flame, bursting through the compressed air.

No.

It was swinging at the small, unimpressive human being who was flying toward it, fused with a spear wreathed in flame.

*Whoooosh!*

A horrifyingly violent rush of air.

But even as the monster’s fist, packed with tremendous force, bore down on him, Jin Taekyung’s gaze didn’t waver. He rushed toward the monster, stepping on invisible stairs in midair.

Neither did his advancing steps, his body hurtling forward with them, or the silver-white spearhead wreathed in navy-blue flame.

*Shhk.*

The spearhead moved with sudden, fluid grace, the flames rippling along its edge.

Space warped with the tremendous heat within them. The sight looked like a fire dragon in motion.

Just like the name of one of the forms of spearplay devised long ago, after painstaking thought, by an old ancestor of the Fire Gate Clan.

*Fire Dragon’s Single Tail.*

The fire dragon’s tail, gliding through the air, met the monster’s fist.

*Slice!*

Everyone on the ground heard the chillingly sharp cut.

They saw the enormous mass of flesh separate from its owner’s body.

And the monster saw it, too.

“Grr…?”

With a puzzled look, it stared at its huge fist—or, more precisely, the place where its fist had been.

Only now did blood begin to bead along the cleanly severed edge.

*Splaaash!*

Blood erupted in a fountain. Caught between the pain that arrived a moment late and a question it couldn’t answer, the monster writhed, overwhelmed by an emotion beyond description.

It didn’t notice the spearhead, moving at blinding speed toward a single point even now.

*Thud.*

The monster felt something so hot it turned its vision white—and, at the same time, so cold it made its body shudder.

The spearhead had driven straight into its throat. It cut off the roar the monster had been about to unleash and poured out a fire it couldn’t possibly resist.

Just like the eyes of the man filling its vision.

“This isn’t a Troll or an ogre… What the hell are you?”

His voice was low and steady.

But the monster’s intelligence was too low to understand him. Jin Taekyung read the truth in its large, bewildered eyes.

“Yeah. I figured. That’s as far as you’re allowed to go, isn’t it?”

A monster’s Intelligence was proportional to its strength.

Jin Taekyung murmured softly, looking at the monster with a deeply troubled gaze.

It couldn’t make a sound with the spearhead lodged in its throat. As its eyes slowly dimmed, it stared back at the human before it. Jin Taekyung’s jaw clenched.

“Who made you? And how?”

He wasn’t asking for an answer.

It was a question Jin Taekyung asked himself—and a question for the other enemies emerging over the giant’s shoulder.

*Boom! Rumble!*

Large and small shadows, cloaked in darkness, surged forward like a wave.

The ground, which had trembled faintly, now shook violently, as though an earthquake had begun. And it wasn’t happening in just one direction.

*Rumble.*

Amid the tremendous noise raised by the enemies, now a few hundred feet away, came faint vibrations nearly lost beneath it.

Feeling the large and small tremors, layered in from every direction in the distance, Jin Taekyung muttered without realizing it.

“…A net over heaven and earth.”

There was no doubt.

They’d been surrounded. And very carefully, too.

Jin Taekyung knew better than anyone that this wasn’t a net a pack of low-Intelligence monsters could form.

*Jingle. Jingle.*

Hearing the faint sound of bells carried by the wind from all around, Jin Taekyung twisted the spearhead embedded deep in the monster.

*Crack. Splaaash!*

The monster’s body crumpled, its life ending without so much as a dying cry. Foul-smelling blood burst out and soaked Jin Taekyung’s collar.

He didn’t care in the slightest.

He’d have to be drenched in their blood countless times before tonight was over—maybe even for days to come.

Only then could he tear through this horrifyingly tight net and make it east.

“You all saw that, right? These fuckers ain’t shit.”

Jin Taekyung spoke to everyone.

East, west, south, north.

There was nowhere to run. The only path left was to fight.

“Let’s go.”

With that low, steady command, three thousand weapons leveled toward the enemy.
```
