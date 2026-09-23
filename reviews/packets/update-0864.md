<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0864.txt",
      "sha256": "d8b8b764e33eb7ea092d0d9be898779668860ad6c52dde3ff4bc557234c2a758",
      "bytes": 12862
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ebde6599174ada5ce3c371995bd49ad2d8bfaf8e4fd1048f92af6f0b1a9b94ac",
      "bytes": 1015
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4c101b31c65ea71d45efd4357ef39f4e35dc7c82b77dbe6d7cdd92374a1106dc",
      "bytes": 229215
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "bec693938f13604e2348aa80bf775f714d08e32555a7c1f5d3a3790bd6544fa6",
      "bytes": 647
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0e3326fca99d3f38c37310b5f5d18ae397800c8eca055a73d9629a7ff8e92bb4",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "2bcd816dc837fe6589743d6a3a1f3d62d24e3b622f57ff17d1baa3b6bd30d42f",
      "bytes": 791
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "9f62b220bc063907da21c59755051e64154f25a0d7635cdd09d004526653e9a5",
      "bytes": 1378
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "93fb55083982ad47bc5a31d1ce154234c106c31fcc193f3d7d825061e3ea8f40",
      "bytes": 634
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "bfd584b311b97cca66093ccedb184d2a09fb2817db07c2916033a9ad274187fe",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "615d8e2f62ab41bc790b46e360cb02b313068109d6e45489aa6642aa3f3950ee",
      "bytes": 622
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "946b4931267575906abd3a868776b864a18f91d073faa769e7e2e2fe48d11f1a",
      "bytes": 699
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "9a5ecad81ca1bd2323eace5db8aa00d908afedb179f9218b26329d8bc01a3716",
      "bytes": 876
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f292cd3ab98b8967e776f406c1177e41b8af8a031b04bb2abb8e4b84ca022ddd",
      "bytes": 255111
    }
  ],
  "estimated_tokens": 11208
}
-->

# Durable State Update — Chapter 864

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
1 and safe_through 864. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 864. Profile updates may replace only one
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
  "chapter": 864,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 864,
    "continuity_sources": [864],
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
    "Prince Shangshan and his party are inside the imperial palace under Baek Yeon’s escort.",
    "The Emperor postponed Prince Shangshan’s audience until the next day without giving a reason.",
    "Baek Yeon has agreed that Shangshan’s guests must not be harmed, but how long that protection will hold is uncertain.",
    "Baek Yeon privately tested Taekyung’s strength with his aura.",
    "Hong Jin has unresolved history with former East Depot associates."
  ],
  "continuity_sources": [
    862,
    863
  ],
  "open_questions": [
    "Why did the Emperor postpone Prince Shangshan’s audience?",
    "What does the Emperor intend for Prince Shangshan?",
    "What happened between Hong Jin and the old eunuch, and why did Hong Jin leave the East Depot?"
  ],
  "safe_through": 863,
  "temporary_decisions": [
    "Render 동창 as “East Depot.”",
    "Render 금의위 as “Embroidered Uniform Guard” and 금위군 as “Imperial Guards.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 태원     | **Taiyuan**            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 주표 | 혁무진 | prince_to_subordinate_of_his_companion | Tenfold Man Hyuk Mujin | formal and playful | Zhu Bao takes Mujin’s boast literally and grants him the title. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |
| 주표 | 백연 | prince addressing an imperial military officer | Commander Baek Yeon | formal and authoritative | Addresses Baek Yeon by name and office while insisting that he answer. |
| 백연 | 주표 | imperial officer addressing a prince | Your Highness | formal and deferential | Uses 전하 when apologizing to and answering Prince Shangshan. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 863
- **Aliases:** None
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard and a military officer trusted by the Emperor.
- **Personality:** Politically assured and controlled, he asserts imperial authority while tactically conceding the prince’s authority and enforcing protocol with ruthless decisiveness.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; his relationship with Prince Shangshan is marked by conspicuous lack of deference.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 863
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 863
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, trusts Jin Taekyung to keep the prince safe, and has unresolved ties to former East Depot associates.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 863
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 863
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he presents loyalty to the Emperor's command as the foundation of his force's actions.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Commands the Embroidered Uniform Guard force confronting Jin Taekyung and serves the Emperor's command.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 862
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 862
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 863
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 863
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, and seeks candid counsel when making difficult decisions.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃864화



“수하의 죄는 곧 소신의 잘못. 부디 용서하소서. 전하.”

백연은 빙그레 웃으며 눈앞의 어린 왕을 바라보았다.

유난히도 또렷하게 빛나는 상산왕의 눈동자에는 수하의 피를 뒤집어쓴 자신의 모습이 담겨 있었다.

마치 먹잇감을 앞에 둔 맹수와 같은 모습이.

그리고 그에 대한 반응은 즉각적이었다.

“백연, 당신이 감히……!”

곧장 어린 주군의 앞을 가로막은 홍진이 끓어오르는 듯한 외침을 토해 냈지만 백연은 신경 쓰지 않았다.

아니, 정확히는 신경 쓰지 못했다.

어느 환관과는 비교도 할 수 없을 만큼 위험한 누군가가 그를 뚫어져라 바라보고 있었으니.

“이 양반 이거, 좋게좋게 넘어가나 싶더니 선 세게 넘으시네.”

청년이 툭 던진 한 마디에, 백연의 입가에 맺혀 있던 미소가 더욱 짙어졌다.

“무슨 문제라도 있나? 태원진가의 진태경.”

“문제, 있지. 그것도 큰 문제가. 이거 이래도 되는 거야?”

턱을 긁적인 진태경이 지면에 떨어진 목을 가리켰다.

소름 돋을 만큼 깔끔하게 잘려 나간 단면에서는 쉴 새 없이 핏물이 뿜어져 나오고 있었다.

“전하가 보고 계신 앞에서 살인을 저질러? 원래 금의위 지휘사쯤 되면 이렇게 막 나가도 되나?”

“물론.”

“뭐?”

“그래도 된다고 했네. 아무리 큰 권세를 누리는 고관대작(高官大爵)도, 그것이 설령 황족이라 해도 나와 금의위는 오직 한 분만을 섬기며 그분의 뜻에 따르니까.”

백연은 손을 들어 어둠에 잠긴 하늘을 가리키고, 이어 자신의 등 뒤로 끝없이 펼쳐진 거대한 건물들을 향해 두 팔을 펼쳤다.

“천자(天子). 하늘을 대신하여 이 천하를 다스리시는 황제 폐하를 제외한다면, 그 누가 감히 금의위를 사사로이 벌할 수 있겠나.”

“……!”

“내가, 아니 우리 금의위가 존재하는 이유는 오직 폐하를 위해서야. 만약 그분의 권위를 해하거나 맞서려는 자가 있다면…….”

입은 여전히 웃고 있으나, 눈은 아니다.

백연은 착 가라앉은 눈동자로 주위를 훑었다.

딱딱하게 굳은 얼굴을 한 동창의 환관들. 긴장하고 있는 홍진과 혁무진. 마지막으로 자신과 상산왕 사이를 가로막은 진태경의 모습을 눈에 담은 뒤 천천히 말을 이었다.

“그것이 누구라 해도, 죽음을 면치 못할 걸세.”

툭.

백연이 걷어찬 목이 데굴데굴 굴러 누군가의 발치에 닿았다. 피에 젖어 들어 가는 가죽신을 물끄러미 내려다보던 진태경이 입을 열었다.

“그래서, 지금부터 우리가 반역이라도 저질렀다고 우길 셈인가?”

“상산왕 전하께서 반역을? 허, 이 친구. 무서운 소릴 하는군.”

소리 내어 웃은 백연이 손사래를 쳤다.

“아니지, 아니야. 나는 다만 손수 처벌했을 뿐일세.”

“처벌이라.”

“감히 상산왕 전하가 보시는 앞에서 검을 뽑았으니 이는 죽어 마땅한 중죄. 앞서 들었던 누구의 말처럼 완전히 조져 놔야 하지 않겠나.”

“내 의견까지 반영해 주니 고맙긴 한데, 아무래도 그 과정에서 조져야 할 놈이 하나 더 생긴 것 같네.”

진태경이 따라 웃으며 말을 이었다.

“황족 앞에서 검 뽑은 놈은 뒈졌고, 피를 본 놈은 어떻게 되려나.”

“글쎄. 반역자가 될지도 모르는 자를 즉결 처분했으니, 그에 마땅한 치하와 상이 내려지겠지.”

“누구 마음대로?”

“자네는 모르겠지만, 금의위 내에서 벌어진 사건은 통상적으로 신속하게 마무리된다네. 결정권자가 두 명뿐이거든.”

진태경은 문득 헛웃음을 흘렸다.

여기까지만 들어도 대충 감이 잡힌다.

두 명의 결정권자 중 한 명은 금의위의 존재 이유나 다름없는 천자일 것이고, 또 다른 하나는…….

“금의위 지휘사?”

“정답. 생각보다 명석하군. 태원진가의 진태경.”

“빌어먹을.”

“다른 방법도 있으니 벌써부터 애석해하지 말게. 만약 나를 처벌하고 싶다면, 황제 폐하께 정식으로 상소문을 올리면 될 테니까. 대국의 모든 백성들은 그럴 권리가 있거든. 아, 물론.”

백연이 문득 생각났다는 듯이 말을 이었다.

“호패(號牌)조차 없는 강호의 무뢰배라면 곤란하지만.”

“……허.”

“또 다른 방법도 있긴 한데, 듣고 싶나?”

잠시 생각하던 진태경이 고개를 저었다.

“그건 아무래도 곤란하지.”

“어째서?”

“죽이고는 싶은데, 죽기는 싫거든.”

“전자는 허무맹랑한 헛소리에 가깝지만, 후자는 제법 그럴듯한 이유로군. 그리고 지금 그 대답이 자네 목숨을 살렸어.”

철컥, 철컥.

백연이 걸음을 옮길 때마다 거슬리는 마찰음이 울려 퍼졌다.

어둠 속에서도 빛나는 황금빛 갑옷을 걸친 채 진태경의 앞에 선 그는, 자신보다 머리 하나는 더 큰 청년을 올려다보다가 이내 그의 옆구리 사이로 보이는 어린 왕을 응시했다.

“상산왕 전하. 혹여 전하께서도 소신의 행동이 불손하다 생각하십니까?”

“…….”

“전하. 소신이 이리 여쭙고 있지 않습니까.”

파르르 떨리는 숨결이 전해진다. 그러나 어둠 속에서도 빛을 잃지 않은 것은 백연의 갑옷뿐만이 아니었다.

“그대는…… 실로 오만무례한 자로구나.”

상산왕 주표는 몸을 떨면서도 백연을 똑바로 응시하며 말을 이었다.

“하나, 짐은 그대를 탓하지 않겠다. 형님 폐하께 그대의 죄를 청하지도 않을 것이다.”

백연이 과장되게 허리를 굽혔다.

“참으로 감사한 이야기입니다만, 이유를 여쭈어도 되겠나이까?”

“그대는 형님 폐하의 신하이지, 짐의 신하가 아니니까.”

“……!”

“짐도, 그대도 결국 폐하의 신하다. 그러나 만약 그대가 짐의 신하였다면 오늘 이 자리에서 죽음을 면치 못했으리라. 군주(君主)란 불충한 신하를 용서해서는 안 되는 법이니까.”

그 대답을 듣는 순간, 백연의 얼굴 위로 뜻 모를 감정이 스쳤다.

하지만 그것은 아주 찰나에 불과했고, 곧 아무런 대답 없이 그대로 돌아선 그는 수하들을 향해 턱짓했다.

“긴 여정으로 피로하신 모양이다. 어서 안으로 모셔라.”

“충(忠)!”

“아, 정 천호는 잠시 남고.”

잠시 제자리에 멈춰 있던 금의위 무사들이 다시금 일행을 에워쌌다.

호위인지 포위인지 알 수 없는 그 움직임 속에서 백연은 나직한 전음(傳音)을 흘려보냈다.

― 이곳에 온 것을 후회하게 만들어 주지.

마치 흘러가듯 내성(內城)으로 향하는 황금빛 물결 속에서, 기다렸다는 듯 진태경의 답신이 날아들었다.

― 이미 내 인생이 후회다. 남 신경 쓰지 말고 좆이나 까 잡숴.

감히 그 누가 금의위 지휘사에게 이런 말을 할 수 있단 말인가.

매번 예상을 아득히 벗어나는 젊은 무뢰배의 대답에 헛웃음을 흘린 백연은, 동창의 환관들을 남겨 둔 채 걸음을 옮겼다.

그의 명령으로 남아 있던 정호군 역시 당연하다는 듯 그 뒤를 따르며 입을 열었다.

“따로 하명하실 일이 있으신지요.”

“그렇다. 하나 명을 듣기에 앞서 미리 스스로 생각하는 것 또한 금의위가 지녀야 할 덕목이다.”

“상산왕 전하와 그 일행들을 빈틈없이 감시하겠습니다.”

“원했던 대답과 비슷하지만, 다르다.”

“그렇다면…….”

“빈틈없이 감시하는 것처럼 보이게, 그러나 동시에 빈틈이 있도록 만들어라. 누군가는 반드시 그 틈을 비집고 접근할 수 있도록.”

“……!”

철컥. 철컥.

백연은 끝없이 위로 이어진 계단을 올랐다. 자그마치 수백, 수천 개나 되는 계단은 바로 천자의 권위를 상징한다.

그 어떤 고관대작이라 해도 등청(登廳)할 때마다 땀을 뻘뻘 흘리며 이 계단을 올라야 했다.

자신이 지닌 권세도, 금은보화도 내려놓은 채.

하늘과 맞닿아 있는 천자의 위엄을 상기하며.

“그들이 누굴 만나는지. 누가 그들을 찾아오는지. 그 모든 것을 감시하고 알아내야 할 것이다.”

그물로 물고기를 잡기 위해서는 우선 넓게 펼쳐야 한다.

촘촘하게 에워싼 채 낚아 올리는 것은 그다음이다.

물론 체구가 육중하거나, 날카로운 이빨을 지닌 무언가가 그물을 뜯을 가능성 역시 생각해야 했다.

“일전에 맡긴 ‘그 일’은 어찌 되었느냐?”

돌아오는 대답은 없었다. 묵묵히 고개를 떨군 정호군의 모습에 백연이 작게 혀를 찼다.

“영악한 놈들이로군.”

“뭐라 드릴 말씀이 없습니다. 최선을 다했습니다만…….”

“상관없다. 아직까지는. 하지만 두 번의 실수는 없어야 할 것이다.”

“이를 말씀입니까. 명령만 내려 주신다면 반드시 빈틈없이 이행하겠습니다.”

“빈틈없이? 그 어떤 명령이라도?”

“예.”

문득 걸음을 멈춘 백연이 돌아서서 정호군을 응시했다. 작게 달싹이는 입술 사이로 소리 없는 속삭임이 흘러나왔다.

― 만약, 네게 상산왕 전하를 시해하라는 명령을 내린다 하더라도 그리 하겠느냐?

“……!”

부릅뜬 두 눈동자와 흔들리는 동공. 그런 수하의 모습을 말없이 내려다보던 백연이 낄낄거리며 웃었다.

“그리 놀랄 것 없다. 단지 농일 뿐이니까.”

“농……이라 하셨습니까.”

“그래, 하지만 네 대답이 궁금한 것도 사실이다.”

언제 맺혔는지 모를 식은땀 한 방울이 정호군의 이마를 타고 흘렀다.

하지만 그의 침묵은 그리 길게 이어지지 않았다.

“목숨 바쳐 따르겠습니다. 그것이 황명(皇命)이라면.”

백연의 입가에 맺힌 웃음이 천천히 흩어졌다. 묘한 표정으로 수하를 응시하던 그가 다시 흐릿하게 미소 지었다.

“네 말이 옳다. 실로 금의위다운 대답이로군.”

“……송구합니다.”

“무엇이 송구하단 말이냐. 금의위란 본래 황명에 죽고 사는 이들. 오직 황제 폐하의 뜻에 따라 움직이는 것이 당연한 것을.”

백연은 문득 고개를 돌렸다.

저 멀리, 꼬리를 물고 늘어지는 횃불과 황금빛 갑옷들이 보였다.

비록 지금은 볼 수 없으나, 저 철통같은 호위 어딘가에 파묻혀 있을 용의 핏줄도.

‘상산왕 주표.’

어린 왕은 기억하지 못하겠지만, 늙은 무장은 똑똑히 기억한다.

천자의 하나뿐인 동생이자, 역사상 가장 잔혹했던 암투 속에서 목숨을 건진 유일한 직계 황족을.

장장 십여 년 만에 마주한 그 어린아이는 훌쩍 자라나 있었다. 몸도, 마음도.

“……그래서 더 위험해졌지.”

마치 속삭이듯 흘러나온 백연의 혼잣말에 정호군이 고개를 든 그때.

아무렇지 않다는 듯 손을 내저은 백연이 재차 입을 열었다.

어느새 웃음기 따위는 조금도 찾아볼 수 없는 냉엄한 얼굴로.

“한 가지만 기억하거라.”

“하명하십시오.”

“이 황궁에 한번 발을 디딘 이상, 그 누구도 빠져나가게 해서는 안 된다.”

정호군은 즉각 깨달았다.

저 말은 비단 상산왕 주표만을 뜻하는 것이 아니라는 것을.

금의위가 주시해야 할 이는 용의 핏줄뿐만 아니라, 감히 신룡(神龍)이라 칭해진 강호의 무뢰배 또한 있었으니.

‘열화신룡(烈火神龍) 진태경.’

용은 오직 천자만을 상징하는 신화 속 영물.

하지만 어린 왕은 다름아닌 천자가 기거하는 황궁에 허락받지 않은 신룡을 들였다.

대국의 법도를 무시하는 저 무뢰배를 자신의 호위로 삼고, 두둔하며 감싸 안았다.

그리고 이 선택이 불러올 결과는 그 누구도 확신할 수 없었다.

정호군은 물론이고, 이 상황을 예상하고 묵인한 백연조차도.

그들이 아는 열화신룡 진태경은 늘 그래 왔으니.

언제나 모두의 예상을 뒤엎고, 사방을 휩쓸 폭풍과 불길을 불러왔으니.

화르륵.

어둠 속, 어디선가 불어온 거센 바람에 횃불이 흔들리고 있었다.
```

## Final English reading copy

```markdown
# Chapter 864

“The crime of my subordinate is my own failing. Please forgive me, Your Highness.”

Baek Yeon smiled warmly as he looked at the young prince before him.

Prince Shangshan’s eyes shone with unusual clarity, reflecting the sight of Baek Yeon with his subordinate’s blood spattered across him.

He looked like a beast facing its prey.

And the response was immediate.

“Baek Yeon, how dare you—!”

Hong Jin sprang in front of his young lord and shouted, his voice boiling with fury, but Baek Yeon paid him no mind.

No—more precisely, he couldn’t afford to.

Someone far more dangerous than any eunuch was staring right at him.

“This guy. I thought we were going to settle this nicely, but you’ve really crossed the line.”

At the young man’s offhand remark, the smile on Baek Yeon’s lips deepened.

“Is there a problem, Jin Taekyung of the Jin Family of Taiyuan?”

“There is. A big one. Are you really allowed to do this?”

Jin Taekyung scratched his chin and pointed at the head lying on the ground.

Blood poured without pause from the cut, so clean it sent a shiver down his spine.

“You commit murder in front of His Highness? Is a Commander of the Embroidered Uniform Guard allowed to run wild like this?”

“Of course.”

“What?”

“I said I’m allowed. No matter how much power a high official wields—even if he’s a member of the imperial family—I and the Embroidered Uniform Guard serve only one person and obey his will.”

Baek Yeon raised one hand toward the darkened sky, then spread both arms toward the vast buildings stretching endlessly behind him.

“The Son of Heaven. Aside from His Majesty the Emperor, who rules this world on Heaven’s behalf, who would dare punish the Embroidered Uniform Guard on a private whim?”

“……!”

“The only reason I—or, rather, the Embroidered Uniform Guard—exists is to serve His Majesty. If anyone tries to challenge or undermine his authority…”

His mouth was still smiling, but his eyes weren’t.

Baek Yeon swept a cold, steady gaze over those around him.

The East Depot eunuchs, their faces stiff. Hong Jin and Hyuk Mujin, tense. And finally, Jin Taekyung, standing between him and Prince Shangshan. After taking them all in, he continued slowly.

“Whoever it is, they won’t escape death.”

Thud.

Baek Yeon kicked the head. It rolled and came to rest at someone’s feet. Jin Taekyung stared at the leather shoe soaking up the blood, then spoke.

“So, are you going to claim we’ve committed treason now?”

“Prince Shangshan committing treason? Ha! That’s a frightening thing to say, my friend.”

Baek Yeon laughed aloud and waved a hand.

“No, no. I merely punished him myself.”

“Punished him?”

“He dared draw his sword in front of His Highness Prince Shangshan. That’s a capital crime. Like someone said earlier, he deserved to be completely fucked up.”

“I appreciate you taking my opinion into account, but it looks like there’s one more person who needs to be fucked up.”

Jin Taekyung laughed along as he continued.

“The man who drew his sword in front of royalty is dead. What happens to the one who spilled his blood?”

“Since I summarily dealt with someone who might have been a traitor, I expect I’ll receive due praise and reward.”

“Who says?”

“You may not know this, but incidents within the Embroidered Uniform Guard are generally resolved quickly. There are only two people with the authority to decide.”

Jin Taekyung let out a dry laugh.

He already had a rough idea from that much.

One of the two decision-makers was the Son of Heaven, the very reason the Embroidered Uniform Guard existed. The other was…

“The Commander of the Embroidered Uniform Guard?”

“Correct. You’re sharper than I expected, Jin Taekyung of the Jin Family of Taiyuan.”

“Damn it.”

“There’s another way, so don’t look so crestfallen just yet. If you want me punished, you can submit a formal petition to His Majesty the Emperor. Every citizen of the Great Nation has that right. Ah, of course…”

Baek Yeon continued as if he’d just remembered something.

“That might be difficult for a martial-world ruffian without even an identity tag.”

“……Hah.”

“There is another way, though. Want to hear it?”

Jin Taekyung thought for a moment, then shook his head.

“That would be difficult.”

“Why?”

“I want to kill you, but I don’t want to die.”

“The former is little more than absurd nonsense, but the latter is a fairly reasonable explanation. And that answer just saved your life.”

Clank. Clank.

An unpleasant scrape rang out with every step Baek Yeon took.

Clad in golden armor that gleamed even in the dark, he stopped in front of Jin Taekyung. He looked up at the young man, who stood a head taller than him, then turned his gaze to the young prince visible beside him.

“Your Highness Prince Shangshan. Do you also believe my conduct was disrespectful?”

“……”

“Your Highness. I am asking you.”

His trembling breath was audible. Yet Baek Yeon’s armor wasn’t the only thing that still shone in the darkness.

“You are… truly arrogant and discourteous.”

Prince Shangshan Zhu Bao trembled, but kept his eyes fixed on Baek Yeon as he continued.

“However, I will not blame you. Nor will I ask My Imperial Elder Brother to punish you.”

Baek Yeon bent at the waist, theatrically.

“I am most grateful to hear that, but may I ask your reason?”

“You are My Imperial Elder Brother’s subject, not mine.”

“……!”

“Both you and I are ultimately His Majesty’s subjects. But if you were my subject, you would not escape death here today. A sovereign must not forgive a disloyal subject.”

At those words, an unreadable emotion passed over Baek Yeon’s face.

But it was gone in an instant. Without answering, he turned and gestured to his subordinates with his chin.

“His Highness appears weary from the long journey. Take him inside at once.”

“Loyalty!”

“Oh, and Thousand Captain Jeong, stay behind a moment.”

The Embroidered Uniform Guard soldiers, who’d paused where they stood, closed in around the party once more.

As the guards moved in a way that made it impossible to tell whether they were escorting the party or surrounding them, Baek Yeon sent a quiet Sound Transmission.

—You’ll regret coming here.

Jin Taekyung’s reply came flying back amid the golden tide flowing toward the Inner City, as though he’d been waiting for it.

—My whole life’s a regret already. Don’t worry about me. Go fuck yourself.

Who else could say something like that to the Commander of the Embroidered Uniform Guard?

Baek Yeon let out a dry laugh at the young ruffian’s reply, which went far beyond all expectations, and walked away, leaving the East Depot eunuchs behind.

Jeong Hogun, who’d stayed at Baek Yeon’s order, naturally followed after him and spoke.

“Is there something you wish to command me?”

“There is. But before you hear an order, thinking for yourself is also a virtue the Embroidered Uniform Guard must possess.”

“I will watch Prince Shangshan and his party without the slightest lapse.”

“That’s close to the answer I wanted, but not quite.”

“Then…”

“Make it look as though you’re watching them without a lapse, but leave gaps all the same. Make sure someone can slip through and approach them.”

“……!”

Clank. Clank.

Baek Yeon climbed the stairs that stretched upward without end. Hundreds, even thousands of them. They symbolized the Son of Heaven’s authority.

No matter how high an official’s rank, whenever they went to court, they had to climb those stairs, sweating profusely.

Leaving behind their power and their gold and silver treasures.

Reminded of the Son of Heaven’s majesty, which reached all the way to Heaven.

“You must watch and find out whom they meet. Who comes to see them. Everything.”

To catch fish in a net, you first had to spread it wide.

Only after that did you close it tightly and haul it in.

Of course, you also had to consider the possibility that something bulky or sharp-toothed might tear through it.

“How is ‘that matter’ I entrusted to you some time ago?”

There was no answer. Jeong Hogun lowered his head in silence, and Baek Yeon clicked his tongue softly.

“Cunning bastards.”

“I have nothing to say. I did my best, but…”

“It doesn’t matter. Not yet. But there must not be a second mistake.”

“Of course. Give me the order, and I will carry it out without fail.”

“Without fail? Whatever the order?”

“Yes.”

Baek Yeon suddenly stopped and turned to look at Jeong Hogun. A silent whisper slipped through his slightly parted lips.

—If I ordered you to assassinate His Highness Prince Shangshan, would you do it?

“……!”

Jeong Hogun’s eyes widened, his pupils wavering. Baek Yeon stared down at his subordinate without a word, then burst out laughing.

“No need to be so shocked. It was only a joke.”

“A joke… you said?”

“Yes. But I really am curious about your answer.”

A bead of cold sweat, he didn’t know when it had formed, ran down Jeong Hogun’s forehead.

But his silence didn’t last long.

“I will follow your orders with my life. If they are the Emperor’s command.”

The smile on Baek Yeon’s lips slowly faded. He studied his subordinate with a curious expression, then smiled faintly again.

“You’re right. That is a truly Embroidered Uniform Guard answer.”

“……I apologize.”

“What are you apologizing for? The Embroidered Uniform Guard lives and dies by the Emperor’s command. Naturally, we move only according to His Majesty’s will.”

Baek Yeon suddenly looked away.

Far in the distance, he could see a procession of torches and golden armor stretching out one after another.

And although he couldn’t see him now, somewhere within that ironclad escort was the bloodline of a dragon.

‘Prince Shangshan Zhu Bao.’

The young prince might not remember, but the old officer remembered clearly.

The Son of Heaven’s only younger brother, and the sole direct member of the imperial family to survive the most brutal power struggle in history.

The child he was seeing again after more than a decade had grown considerably—in body and in mind.

“……Which makes him all the more dangerous.”

Jeong Hogun lifted his head at Baek Yeon’s whispered words.

Baek Yeon waved a hand as if nothing had happened, then spoke again.

His face was stern now, without the slightest trace of a smile.

“Remember one thing.”

“Give me your command.”

“Once someone has set foot in this imperial palace, no one is to be allowed to leave.”

Jeong Hogun immediately understood.

Those words weren’t meant only for Prince Shangshan Zhu Bao.

The Embroidered Uniform Guard had to keep its eyes on more than just the bloodline of the dragon. There was also the martial-world ruffian who had dared to bear the title of Divine Dragon.

‘Blazing Flame Divine Dragon Jin Taekyung.’

The dragon was a mythical creature that symbolized only the Son of Heaven.

But the young prince had brought an uninvited Divine Dragon into the imperial palace where the Son of Heaven resided.

He’d made that ruffian, who ignored the laws of the Great Nation, his guard, defending and sheltering him.

No one could be certain what the result of that choice would be.

Not Jeong Hogun, nor even Baek Yeon, who had anticipated the situation and allowed it to happen.

The Blazing Flame Divine Dragon Jin Taekyung they knew had always been like that.

He always overturned everyone’s expectations, bringing storms and flames that swept in from every direction.

Fwoosh.

In the darkness, a fierce wind blew from somewhere, making the torches flicker.
```
