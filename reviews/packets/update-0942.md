<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0942.txt",
      "sha256": "badaf333b5fd0897e6bbcd9473461af4264cd8e6162d226e0eb48bc42af3f9da",
      "bytes": 13224
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "40811b7fa5bf89bb1d05e093e2083f2e71de707c4c9aa59fed29913c280c34c1",
      "bytes": 2347
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5300d99770ec82b6bd6ea63a4515ccef6274e613735776322842509d00745fd8",
      "bytes": 233016
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0976313167a3b6718bf5f5626c8d8c9f021758361ab31565a295a633a109ba6b",
      "bytes": 759
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "180ea6462056794e7a56c00771c003793326d13522d012799ae0a5d17059a0fd",
      "bytes": 699
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b3988aa0820e227c9c2afa7b0f8e0ffd007cea2f9c2be191fa2319b607e5736b",
      "bytes": 1449
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "63d195017ad7d03f1125897a3d2fed086c2b998053c2ee2201cf498fd2adbcd2",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "fca65a257bde11721db4f2084f3129d1b0bfc7d1f9e66e2bd30b690bb1d23034",
      "bytes": 973
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "f20d8d6b24d1da8fa986b8aeb30d3bf22e0a689a87067fb2d9f3d732a9e0387b",
      "bytes": 699
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1eadeed5c15d37b4d14c41a82667a271d46a57b86c0c7bdada76e3b595e6854f",
      "bytes": 267113
    }
  ],
  "estimated_tokens": 10774
}
-->

# Durable State Update — Chapter 942

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
1 and safe_through 942. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 942. Profile updates may replace only one
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
  "chapter": 942,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 942,
    "continuity_sources": [942],
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
    "The Emperor was poisoned with Blood Soul Gu; it has reached his marrow, and the Divine Physician says his vitality is at its limit and cannot guarantee he will survive another couple of months.",
    "Taekyung’s System quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; its reward and failure consequence are unknown.",
    "The Emperor prepared for his death by transferring loyal retainers and his power base to Zhu Bao.",
    "War against Dark Heaven has begun, and the imperial court is mobilizing troops and warships after Taekyung warned of a possible invasion of Shanxi before the Double Ninth Festival.",
    "The Emperor appoints Taekyung Marquis of Shangshan and Thousand Captain, entrusting him with a thousand Embroidered Uniform Guards to fight the foreign enemy.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "The Eastern Heaven Demon Lord’s hidden iron chest contains old bamboo slips, recent papers, and a small silk pouch of unknown significance.",
    "Taekyung’s System update reward is a durable pocket watch that appears broken and bears the faint inscription “A broken clock is right twice a day.”",
    "The Bow Saint says the Martial God chose her; she tested Taekyung in the banquet-hall battle to confirm he was the chosen one and assess his power and character.",
    "Jeok Cheongang considers Taekyung his one and only Disciple and is furious that the Bow Saint put him in danger."
  ],
  "continuity_sources": [
    941,
    940
  ],
  "open_questions": [
    "What is the Martial God’s identity, and what is the full nature of his connection to the chosen one and the Bow Saint?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "Who sent the Shanxi Annihilation Plan missive, and will Dark Heaven’s invasion proceed as described?",
    "What do the papers, bamboo slips, and silk pouch from the Eastern Heaven Demon Lord’s chest contain, and what is their significance?"
  ],
  "safe_through": 941,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 안휘     | **Anhui**              |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 모산파 | **Maoshan Sect** | Jiangsu sect known for sorcery, destroyed by the founding emperor. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 941
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 941
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 941
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 941
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 930
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 941
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

## Korean source

```text
＃942화



환자를 두고 왔습니다.

신의의 입술 사이로 흘러나온 그 대답에, 황제의 눈동자가 잘게 흔들렸다.

‘설마.’

불현듯 숨이 막혔다.

그도 모르는 사이에 두 주먹이 불끈 쥐어졌다.

완전히 비워 냈다고 생각했던 마음속에서 희망의 불씨가 피어오른다.

침실이 아닌 전장에서 죽고자 다짐했던 자신의 각오가 흔들리는 것을, 황제는 느낄 수 있었다.

‘아니, 그럴 리 없다.’

그러나 황제는 내심 고개를 내저을 수밖에 없었다.

한 인간을 벼랑 끝으로 내모는 것은 위기지만, 끝내 나락으로 떨어트리는 것은 희망이니까.

그렇기에 황제는 지금 이 순간에도 잔잔하게 웃으며 자신을 바라보는 신의를 애써 외면했다.

“……병영에 합류할 생각이라면 구태여 말리지 않겠네. 머지않아 수많은 사상자가 발생할 테니, 그대의 의술이 크게 빛을 보겠지.”

“폐하.”

뭐라 말을 이으려는 신의를 남겨 둔 채, 황제는 조용히 돌아섰다.

촌각이 아쉬운 것은 태원진가를 지키기 위해 떠난 진태경 뿐만이 아니다.

이제는 정말로 얼마 남지 않은 삶.

길어야 몇 달에 불과한 그 짧은 시간 동안, 황제는 자신이 할 수 있는 모든 것을 끝낼 생각이었다.

보다 더 나은 미래를 위해.

그가 떠난 후에도 이승에 남아 있을 소중한 이들을 위해.

‘그것이 짐의 유일한 사명이다.’

황제가 잠시 흔들린 각오를 다잡은 바로 그 순간이었다.

그의 등 뒤에서 나직한 목소리가 들려온 것은.

“압니다. 폐하의 그 마음.”

저벅.

거침없이 나아가던 황제의 발걸음이 못 박힌 듯 멈춰 섰다.

그런 그의 귓가로 신의의 음성이 계속해서 전해졌다.

“찰나의 희망이 두려우시겠지요. 헛된 희망만큼 고통스러운 것은 없으니.”

잠시 침묵하던 황제는 천천히 돌아섰다. 그리고 여전히 빙그레 웃고 있는 신의와 마주했다.

“잘 아는군.”

“원치 않게도, 그리 되었습니다.”

“그럴 수밖에 없었겠지. 그대는 한 사람의 의원으로서 생사의 기로(岐路)에 선 이들을 수도 없이 만났을 테니.”

“단지 그뿐만은 아닙니다.”

“하면?”

문득, 신의의 입가에 맺혀 있던 미소가 흐릿해졌다.

“아주 오래전, 어느 젊은 목수가 있었습니다.”

“목수라. 그자 또한 죽을병에 걸려 자네를 찾았었나?”

“정확히는, 역병에 걸린 처자식을 살리기 위해서였지요.”

“……처자식이라.”

“열이 펄펄 끓는 안사람과 두 아이를 지게에 짊어지고 꼬박 사흘 밤을 새워 가며 산을 올랐다고 하더군요. 인근 화전민촌에 머무르고 있다는 용한 의원을 찾아가기 위해서.”

황제는 땀에 흠뻑 젖은 채 산을 오르는 목수의 모습을 떠올리며 뇌까렸다.

“고되었겠군. 아주 많이.”

“폐하의 말씀처럼, 분명 그랬을 겁니다.”

“하나 그 목수는 피로조차 제대로 느끼지 못했을 걸세. 처자식을 살릴 수 있으리라는 희망이 있었으니.”

신의가 고개를 끄덕였다.

“예, 맞습니다. 끝끝내 목적지에 다다른 후에야 지게를 내려놓고 쓰러졌지요. 그리고 하루하고도 반나절을 앓았습니다.”

“하여, 그대는 목수의 처자식을 치료해 주었나?”

“불행하게도, 그럴 수 없었습니다.”

작게 탄식하는 황제를 향해, 신의는 씁쓸하게 덧붙였다.

“제가 마침내 의식을 되찾았을 때는, 모든 것이 늦어 있었으니 말입니다.”

“……!”

“그렇기에 잘 압니다. 희망이 얼마나 잔인한 것인지. 그 아래 낭떠러지에는 어떠한 절망이 기다리고 있는지.”

황제는 침묵했다.

그리고 눈앞의 늙은 의원을, 오래전 역병으로 처자식을 잃고 새로운 길을 택한 젊은 목수를 한참을 응시하다 불현듯 입술을 뗐다.

“그렇다면, 그렇다면 진정으로…….”

숨기지 못한 격동이 담긴 떨리는 목소리로, 처음부터 묻고 싶었던 그 한 마디를 쥐어 짜냈다.

“짐을 치료할 방도를 찾았단 말인가.”

가라앉아 있던 눈동자에 빛이 깃들고, 목소리에는 희망이 묻어 나온다.

신의는 그런 황제를 향해 길게 읍하며 대답했다.

“그렇습니다. 하늘의. 아니, 진 공자의 도움으로 하나뿐인 생로(生路)를 찾을 수 있었습니다.”

“……!”

진태경.

생각지도 못한 그 이름에 황제는 자신도 모르게 눈을 감았다.

그리고 눈앞에 드리워진 어둠 속에서 진태경의 얼굴을 떠올리며, 들리지 않을 감사의 인사를 건넸다.

‘잊지 않았군. 짐과의 약속을.’

진태경을 떠나보내면서도 원망하지 않았다.

약속에 관하여 일언반구 없이 멀어져 가는 그의 뒷모습을 바라보며, 그저 지금껏 황실을 위해 해 준 일들에 감사할 뿐이었다.

그것이 이 나라의 군주로서, 아우를 둔 형으로서, 더불어 한 인간으로서의 도리라고 생각했으니까.

그러나 진태경은 끝끝내 황제에게 했던 약속을 지켰다.

천하에서 가장 뛰어난 의원에게, 그 어느 때보다도 환하게 빛나는 희망을 건네어 돌려보냈다.

‘이 빚을 갚으려면, 더 무엇을 해 주어야 하나.’

상관없다.

진태경이 원하는 것이 무엇이든, 기꺼이 응할 수 있었으니까.

실소와 함께 눈을 뜬 황제는 천천히 입을 열었다.

“말해 보게. 짐이 살기 위해 무엇을 해야 하는지.”

그리고 그 순간, 신의의 입가에 걸려 있던 미소가 왠지 모르게 어색해지는 것을 보았다.

“왜 그러나?”

“그러니까. 음, 그것이…….”

“망설일 필요 없네. 그대의 말이라면 한 치의 의심도 없이 믿고 따를 테니.”

“송구하오나, 아무리 그렇다 하셔도 약간의 오해가 있을 수 있기에…….”

황제는 자꾸만 머뭇거리는 신의의 모습에 충분히 짐작 가는 바가 있었다.

늘 있는 일이다.

그는 천하의 주인인 황제였고, 황실의 어의(御醫)들은 황제의 건강에 조금이라도 이상이 생긴다면 죽음까지 각오해야 할 정도였으니까.

이러한 후환(後患)은 천하제일의 의원이라고 한들 우려하지 않을 수 없는 부분이었다.

“대관절 무엇을 걱정하는지는 모르나, 그대가 생각하는 그 어떤 불상사도 결코 일어나지 않을 걸세. 짐의 이름으로……. 아니, 선황들의 무덤에 걸고 맹세하지.”

더할 나위 없이 부드러운 어조로 다독이는 황제의 모습에, 줄곧 소리 없이 입술만 달싹거리던 신의가 조심스럽게 입을 열었다.

“지금 하신 말씀, 한 치의 거짓도 없는 진심이십니까?”

“물론일세. 지금부터 짐은 천자이기 이전에 그대의 치료가 필요한 병자이니, 어떤 것이라도 믿고 따르지.”

“좋습니다. 폐하께서 이렇게까지 말씀하시니, 저 역시 솔직하게 말씀드리겠습니다.”

그리고 다음 순간, 황제는 깨달았다.

왜 신의가 이토록 망설였던 것인지.

더불어 그가 앞서 말했던 ‘약간의 오해’가 얼마나 축소된 표현이었는지.

“사실, 폐하를 살릴 방도는 없습니다.”

“……?”

“치료를 위해서는 일단 한 번 죽으셔야 됩니다. 그것부터가 시작……. 폐하?”

황제는 눈을 깜빡였다. 어느새 자신의 손에 들린 보검이 보였다.

“아니, 이게 갑자기 왜.”

“폐하, 폐하?”

“미안하네, 신의. 하지만 이건 짐의 의지로 뽑은 것이 아닐세. 검이 스스로 움직이고 있어.”

“폐하아!”

지나가는 역적도 안 믿을 소리와 함께 검을 들고 다가오는 황제를 보며, 신의는 새된 비명을 내질렀다.

동시에 만일을 대비하여 미리 꺼내 두었던, 몇 시진 전 진태경이 건네주었던 ‘그것’을 황제를 향해 내밀었다.

아니, 정확히는 내던졌다.

탁.

황제가 본능적으로 손을 뻗어 날아드는 물건을 잡아챈 그 순간.

촤르르륵!

‘그것’을 고정하고 있던 끈이 풀리며 낡다 못해 반쯤 삭아 버린 죽간(竹簡)이 펼쳐졌다.

“……이건.”

찰나의 의문.

그러나 흐릿하게나마 남아 있는 글자를 확인한 황제의 눈동자가, 이내 크게 부풀어 올랐다.

모산파(茅山波).

백환강시공(白幻僵尸功).

그것은, 더는 이 세상에 없는 누군가가 소중히 간직하고 있던 사문의 옛 뿌리였다.



* * *



두두두두두!

거센 말발굽 소리가 어둠 너머로 울려 퍼진다.

한혈마(汗血馬)의 피를 이어받았다는 준마는 그 명성답게 단 한 순간도 발을 멈추지 않았고, 나를 포함한 모두는 고삐를 늦추지 않았다.

“저 언덕을 넘어가면 덕청현(德淸縣)이에요!”

불현듯, 세차게 스쳐 지나가는 바람 사이로 주화란의 외침이 울려 퍼졌다.

불과 한 시진.

황도를 떠난 지 고작 한 시진 만에 두 번째 현(縣)에 도달했다는 희소식이었지만, 나는 조금도 웃지 못했다.

‘아직이다. 지금 이 속도라면, 정오까지 달려도 안휘성에 닿을 수 있을지 장담하지 못해.’

턱없이 부족하다.

속도도, 시간도.

약 반 시진 정도를 앞서 황도를 빠져나간 황실의 전서응과 전령들조차도 전투가 벌어지기 전에 도착할 수 있을지 장담하지 못하는 상황.

한시라도 빨리 움직여야 한다.

“정호군!”

공력이 실어 터트린 부름에, 투구를 깊게 눌러쓴 정호군이 말을 몰며 앞서 나왔다.

“말해라.”

“산서성까지 예상되는 시간은, 얼마나 남았지?”

쉴 새 없이 내달리는 말안장 위에서 잠시 뭔가를 생각하던 정호군이 짧게 대답했다.

“최소 열흘. 길면 보름.”

자그마치 닷새 차이.

게다가 보름이라는 저 수치도 결코 느긋하게 잡은 것이 아니라는 사실을, 나는 충분히 짐작하고 있었다.

“더 자세히.”

“중간중간 역관(驛官)이 준비된 현에서 제때 말을 갈아타고, 최소한의 휴식을 취한다는 가정하에 보름이다.”

“제기랄. 그럼 열흘은?”

“그건 최소한의 직선거리로만 이동했을 경우다. 험준한 산맥이나 강을 넘어야 할 테니 때에 따라 말은 버려야 할 테고…….”

문득 말꼬리를 흐린 정호군은 말과 한 몸이 되어 맹렬하게 내달리는 일천의 금의위와, 그 뒤를 따르는 화룡각 대원들을 힐끗 바라보며 덧붙였다.

“휴식은 꿈도 꿀 수 없겠지.”

평소처럼 무뚝뚝한 표정과 말투였지만, 그 안에 담긴 우려는 충분히 전해졌다.

아니, 나 역시 모를 수 없었다.

‘산서성에 도착한다고 해서, 모든 것이 끝나는 게 아니니까.’

암천이 산서성을 침공하는 시기는 정확하지 않다.

하늘의 도움으로 전투가 벌어지기 이전에 도착하여 충분한 휴식을 취할 수 있다면야 다행이지만, 그 반대의 상황이 될 가능성도 차고 넘쳤다.

‘이미 암천이 산서성을 점령했거나, 혹은 전투가 막 시작된 시점에 도착한다면…….’

뒷말은 필요 없다.

나는 아까부터 줄곧 입안에 맴돌던 욕설을 씹어 뱉었다.

“이런 제기랄.”

서걱!

길가에 드리워진 나뭇가지를 잘라 낸 정호군이 입 안에 들어간 잎사귀를 뱉으며 대꾸했다.

“심정은 충분히 공감하지만, 단지 그 말을 하기 위해 부른 건 아닐 텐데.”

듣는 것만으로도 정나미가 뚝 떨어지는 냉정한 말투에, 나는 뜨겁게 달아올랐던 머릿속이 차갑게 식는 것을 느꼈다.

“개 같네. 빌어먹을.”

“좋아. 신세 한탄은 다 했나?”

“정 없는 새끼.”

“…….”

“공감도 더럽게 못 해 주는 놈. 그러니까 친구 하나 없지.”

“……아니, 그건 신세 한탄이 아닌 것 같은데.”

“전혀. 단순한 신세 한탄이었어.”

내 단호한 대답에 정호군이 굳게 입을 다물었다.

투구 사이로 보이는 눈빛이 살짝 슬퍼 보이는 건, 단순한 기분 탓이 분명하다.

‘그나저나 이렇게 된다면.’

정호군의 반응을 깔끔하게 무시한 나는, 얼마 지나지 않아 빠른 결단을 내렸다.

“덕청현을 지나는 즉시 분산한다. 병력이 너무 많아.”

“병력을 나누겠다는 건…….”

“너희 전부. 그리고 세 명.”

“뭐?”

반문하는 정호군에게, 나는 저 멀리 앞서가는 두 인영을 가리켰다.

“먼저 도착하는 건, 셋으로도 충분해.”

혹시 들어 봤는지 모르겠다.

좌화왕 우궁성이라고.
```

## Final English reading copy

```markdown
# Chapter 942

“I left a patient behind.”

At the Divine Physician’s answer, the Emperor’s eyes trembled.

*Could it be…?*

Suddenly, he found it hard to breathe.

Without even realizing it, his fists clenched.

A spark of hope kindled in a heart he’d thought he’d emptied completely.

The Emperor could feel his resolve wavering—the resolve to die on a battlefield, not in his bedchamber.

*No. It can’t be.*

But deep down, the Emperor could only shake his head.

A crisis could drive a person to the edge of a cliff. But it was hope that finally sent them plunging into the abyss.

And so, even now, the Emperor forced himself to look away from the Divine Physician, who gazed back at him with a gentle smile.

“If you intend to join the military camp, I won’t stop you. Before long, there will be countless casualties, and your medical skills will be put to good use.”

“Your Majesty.”

Leaving the Divine Physician with more to say, the Emperor quietly turned away.

Jin Taekyung wasn’t the only one whose every moment mattered—the one who had left to protect the Jin Family of Taiyuan.

The Emperor’s life was truly drawing to a close.

In the brief time he had left—just a few months at most—he meant to finish everything he could.

For a better future.

For the precious people who would remain in this world after he was gone.

*That is my sole duty.*

It was at that very moment, as the Emperor steeled his resolve again, that a quiet voice sounded behind him.

“I understand, Your Majesty. I understand how you feel.”

Thud.

The Emperor’s brisk stride came to an abrupt halt.

The Divine Physician’s voice continued in his ear.

“A fleeting hope must frighten you. Nothing is more painful than a false hope.”

After a brief silence, the Emperor slowly turned around. The Divine Physician was still facing him with a gentle smile.

“You understand well.”

“Through no choice of my own, I came to.”

“You must have. As a physician, you must have met countless people standing at the crossroads between life and death.”

“That’s not the only reason.”

“Then what is?”

For an instant, the Divine Physician’s smile faded.

“A very long time ago, there was a young carpenter.”

“A carpenter? Did he come to you because he had a fatal illness, too?”

“More precisely, he came to save his wife and children from an epidemic.”

“……His wife and children.”

“They say he carried his wife, burning with fever, and his two children on a wooden frame, and climbed the mountain for three days and nights without sleep. He was trying to find a renowned physician who was staying in a nearby settlement of slash-and-burn farmers.”

The Emperor pictured the carpenter, drenched in sweat as he climbed the mountain, and muttered,

“That must have been hard. Very hard.”

“As you say, it surely was.”

“But that carpenter probably couldn’t even feel his exhaustion. He had hope that he could save his family.”

The Divine Physician nodded.

“Yes. That’s right. He didn’t set down his load and collapse until he’d finally reached his destination. Then he lay sick for a full day and a half.”

“So, did you treat the carpenter’s family?”

“Unfortunately, I couldn’t.”

The Divine Physician added bitterly, facing the Emperor, who let out a small sigh.

“By the time I finally regained consciousness, it was too late for everything.”

“……!”

“That’s why I understand so well how cruel hope can be. And what despair waits at the bottom of that cliff.”

The Emperor fell silent.

He gazed at the old physician before him—and at the young carpenter who had lost his family to the epidemic so long ago and chosen a new path. After a long while, he suddenly spoke.

“Then, does that mean you really have…?”

His voice trembled with an agitation he could not hide. He forced out the one question he’d wanted to ask from the very beginning.

“Have you found a way to treat Us?”

A light appeared in his once-subdued eyes, and hope crept into his voice.

The Divine Physician bowed deeply before the Emperor and answered.

“Yes. With the help of Heaven—or rather, Young Master Jin—I was able to find the one and only path to survival.”

“……!”

Jin Taekyung.

At the unexpected name, the Emperor closed his eyes without meaning to.

In the darkness before him, he pictured Jin Taekyung’s face and offered a silent word of thanks.

*You didn’t forget. You kept your promise to Us.*

Even as Jin Taekyung left, the Emperor had never resented him.

He’d watched Jin Taekyung walk away without a word about the promise between them, and could only be grateful for everything he had done for the imperial house.

He’d believed that was his duty—as ruler of this nation, as an older brother, and as a human being.

But Jin Taekyung had kept his promise to the Emperor after all.

He had given the finest physician beneath Heaven a hope that shone brighter than ever and sent him back.

*What more must I do for him to repay this debt?*

It didn’t matter.

Whatever Jin Taekyung wanted, the Emperor would gladly give it to him.

With a quiet chuckle, the Emperor opened his eyes and slowly spoke.

“Tell Us. What must We do to live?”

And in that instant, the Divine Physician’s smile seemed to turn strangely awkward.

“What is it?”

“Well, it’s… that is…”

“There’s no need to hesitate. We’ll believe and follow your instructions without the slightest doubt.”

“I’m sorry, but even so, there may be a slight misunderstanding…”

The Emperor could well imagine what was making the Divine Physician hesitate.

It happened all the time.

He was the Emperor, ruler of all beneath Heaven. If anything at all went wrong with the Emperor’s health, the imperial physicians might have to prepare for death themselves.

Even the finest physician beneath Heaven couldn’t help worrying about what might come after.

“Whatever you’re worried about, I assure you that nothing unfortunate will happen. We swear by Our name… No, We swear on the tombs of the late Emperors.”

At the Emperor’s gentle reassurance, the Divine Physician—who had been silently moving his lips for some time—carefully spoke up.

“Are those words truly sincere? Without the slightest falsehood?”

“Of course. From this moment on, We are a patient in need of your treatment before We are the Son of Heaven. We’ll trust you and follow your instructions, whatever they may be.”

“Very well. Since Your Majesty has gone so far, I’ll speak frankly, too.”

And in the next instant, the Emperor understood.

Why the Divine Physician had been hesitating so much.

And just how understated the words *a slight misunderstanding* had been.

“The truth is, there’s no way to save Your Majesty.”

“……?”

“To treat you, you’ll have to die once first. That’s where it begins—Your Majesty?”

The Emperor blinked. Somehow, a treasured sword had appeared in his hand.

“Wait, why is this—”

“Your Majesty? Your Majesty!”

“I’m sorry, Divine Physician. But I didn’t draw this of my own will. The sword’s moving by itself.”

“Your Majesty!”

Watching the Emperor approach with his sword, uttering words that even a passing traitor wouldn’t believe, the Divine Physician let out a shrill scream.

At the same time, he thrust out the thing he’d taken out earlier, just in case—the thing Jin Taekyung had handed him a few hours ago.

Or, more accurately, he hurled it at the Emperor.

Clack.

The Emperor reflexively reached out and caught the flying object.

*Rattle!*

The cord holding it in place came undone, and a bamboo slip unfurled—so old it had half rotted away.

“……What is this?”

For an instant, the Emperor was puzzled.

But as soon as he made out the faint characters that remained, his eyes widened.

Maoshan Sect.

White Illusion Jiangshi Art.

It was the ancient root of a sect belonging to someone who no longer existed in this world, and who had treasured it dearly.

* * *

*Dududududu!*

The thunder of galloping hooves rang out in the darkness.

The fine horses, said to have descended from Ferghana horses, lived up to their reputation. Not one of them stopped for even a moment, and none of us—including me—slackened our reins.

“Deokcheong County is just beyond that hill!”

Ju Hwaran’s shout suddenly cut through the wind rushing past us.

It was good news: we’d reached our second county just one shichen after leaving the imperial capital. But I couldn’t bring myself to smile.

*Not yet. At this speed, I can’t even be sure we’ll reach Anhui Province by noon.*

It wasn’t nearly enough.

Not the speed. Not the time.

Even the imperial messenger eagles and couriers who had left the capital about half a shichen ahead of us might not arrive before the fighting began.

We had to move as fast as possible.

“Commander Jeong!”

At my call, infused with internal energy, Jeong Hogun—his helmet pulled low over his brow—rode up beside me.

“Speak.”

“How long do you estimate until we reach Shanxi Province?”

Jeong Hogun thought for a moment in the saddle as his horse raced onward, then gave a short answer.

“At least ten days. As many as fifteen.”

A difference of no less than five days.

And I could tell well enough that fifteen days wasn’t some leisurely estimate, either.

“Be more specific.”

“Fifteen days, assuming we change horses promptly at counties with prepared relay stations and take only the bare minimum of rest.”

“Damn it. And ten days?”

“That would mean traveling only the shortest possible straight-line route. We’ll have to cross rugged mountains and rivers, so depending on the conditions, we may have to abandon our horses…”

Jeong Hogun’s voice trailed off. He glanced at the thousand Embroidered Uniform Guards charging forward as one with their horses, then at the Fire Dragon Pavilion members following behind them, and continued,

“And we can forget about rest.”

His expression and tone were as impassive as ever, but his concern came through clearly.

No, I couldn’t miss it, either.

*Reaching Shanxi Province won’t mean everything’s over.*

We didn’t know exactly when Dark Heaven would invade Shanxi Province.

If Heaven was on our side and we arrived before the fighting began, with enough time to rest, that would be fortunate. But there was every chance the opposite would happen.

*If Dark Heaven has already taken Shanxi, or we arrive just as the battle begins…*

There was no need to finish the thought.

I spat out the curse that had been circling in my mouth for a while.

“Goddamn it.”

*Shhk!*

Jeong Hogun cut through a branch hanging over the road, spat out a leaf that had flown into his mouth, and replied,

“I understand how you feel, but I doubt you called me over just to say that.”

His tone was so cold it made me dislike him on the spot. I felt my overheated thoughts cool down.

“Shit. This sucks.”

“Good. Are you done feeling sorry for yourself?”

“You cold bastard.”

“……”

“You can’t even show a little sympathy. No wonder you don’t have a single friend.”

“……No, I don’t think that counts as feeling sorry for yourself.”

“Of course it does. That was just me feeling sorry for myself.”

At my firm reply, Jeong Hogun pressed his lips together.

The eyes visible through his helmet looked a little sad. That had to be my imagination.

*Anyway, in that case…*

Ignoring Jeong Hogun’s reaction, I made a quick decision.

“We’ll split up as soon as we pass through Deokcheong County. We have too many people.”

“You mean we should split the troops…”

“All of you. And three others.”

“What?”

At Jeong Hogun’s question, I pointed toward two figures racing ahead in the distance.

“Three of us will be enough to get there first.”

Not sure if you’ve heard the saying:

The Fire King on the left, the Bow Saint on the right.
```
