<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1119.txt",
      "sha256": "14d1571b8c6bd007e9362923dcc4979722c13b61ae60257b5d86ec07d6ffd26e",
      "bytes": 17040
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ff0c8e87dc3c91bc8c451c19f350bd64bbc8d29e08fd5217b646573e2d3f27ce",
      "bytes": 1445
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "66b724f4d846741f2cbbc7e843d83ef54cdbfc708dd1f9b56308f753f4d5a999",
      "bytes": 244911
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7217008b93cd30f25419bcac5817a1010f8231e38a41ae8d7607f340d67f32ef",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "bb7781c95d951ac4d60cabd5a548705531e491c67ecbdc3be909509cb557d370",
      "bytes": 1371
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "d4f95cec0e6cda002f5118c6ed3e12604d150163fa7bc8a7090162560f91928d",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8252682f9deed1781e22920f77a320961649dd0a0e7a08a3bfce4485cbca1e87",
      "bytes": 623
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "375129cd76f613be20b05e63b0663f6657ca42be0be0c49e0d2609016cdc8593",
      "bytes": 974
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "ae4ba6b41c7c737d2042080dd5df08541758ba587c6ef9541f5bfc3747e5891a",
      "bytes": 850
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "d3d364fe23754ded500068531cc909767e5f6d8a02edb916cd732f0716ee9ed3",
      "bytes": 774
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "50e40137a2654a732b9061240991cb7c1cefc240664a413416f4f397170daad6",
      "bytes": 980
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "93f5660c6fd343c478a6feff68681376c8c9b920890235d1d128e1186036b85c",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d55475543ec1fb1c82a8c660ed8fc6b6c7536abad3e5c84ebccc42321005d0fd",
      "bytes": 289267
    }
  ],
  "estimated_tokens": 14118
}
-->

# Durable State Update — Chapter 1119

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
1 and safe_through 1119. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1119. Profile updates may replace only one
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
  "chapter": 1119,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1119,
    "continuity_sources": [1119],
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
    "The West Gate has fallen, and the South Gate defenders were ordered to retreat to the Inner City.",
    "Cheongheoja remains at the East Gate with allies, including Kunlun Disciples.",
    "Hak Eui is alive; a disguised prisoner's corpse led others to believe he had been killed.",
    "Hak Su, formerly Cheongheoja’s Senior Disciple and a Dark Heaven spy known as Number Six, was killed at the East Gate as a Kunlun Sect traitor.",
    "The East Gate trap let two Black Ghosts and a thousand monsters enter before the gate began closing.",
    "The Green Forest Alliance, the Yangtze River Channel League, and Dark Heaven forces—estimated at thirty thousand—have arrived from the east; their horn is approaching the East Gate.",
    "A captured jiangshi sorcerer returned with bells from jiangshi sorcerers killed near Qinghai Lake; ringing multiple bells confuses the monsters but cannot control the Black Ghosts.",
    "Cheongheoja and Great Sir block the two Black Ghosts; the confused monsters rampage without distinguishing friend from foe."
  ],
  "continuity_sources": [
    1117,
    1118
  ],
  "open_questions": [
    "What happens when the approaching coalition reaches the East Gate?",
    "Can the defenders stop the two Black Ghosts?"
  ],
  "safe_through": 1118,
  "temporary_decisions": [
    "Render 육호 as “Number Six” for Hak Su’s Dark Heaven identifier."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 쾌풍검    | **Swift Wind Sword**          | Hyuk Mujin     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 태원     | **Taiyuan**            |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 철구 | **iron balls** | Training weights attached to Taekyung. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 육부 | **Six Ministries** | The central government ministries. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1117
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1118
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and Vice Captain of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1118
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1118
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1069
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1073
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Courteous and calculating, he chooses what he believes is right over expedience and accepts responsibility for his choices, even when they expose him to blame.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo is Sima Gong’s son and chosen heir, commands Taishan, and is Jin Taekyung’s friend; he deliberately let Namho suspect his father’s actions to protect their companions, was Ju Hwaran’s former fiancé, and is hostile toward Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1069
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1069
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1117
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1119화



콰아아앙!

굉음이 울려 퍼지고, 지면이 뒤흔들린다.

적아(敵我)를 가리지 않고 미쳐 날뛰기 시작한 일천의 괴물과 결사항전을 각오한 삼천의 수비군.

거기에 더해 섬광처럼 공간을 가로지르며 쉴 새 없이 뒤얽히는 네 명의 초절정 고수까지.

동문을 중심으로 펼쳐진 난전(亂戰)의 시작은 그 어느 때보다 혼란스러웠고, 또한 잔혹했다.

지금의 이 사태를 설계하고 완성시킨 장본인조차 온 힘을 다해 간신히 두려움을 억누를 만큼.

- 캬우우우우!

혁무진은 떨리는 눈빛으로 흉포한 괴성을 내지르며 들이닥치는 괴물들을 바라보았다.

무려 일장이 넘는 키와 아름드리나무처럼 두꺼운 팔다리.

게다가 인간의 한계를 훌쩍 뛰어넘은 괴력과 속도를 갖춘 놈들의 돌격은, 그 어떤 무엇으로도 막을 수 없는 거대한 파도처럼 느껴졌다.

‘도대체 어떻게, 조장님은 이런 놈들을 수도 없이 상대해 오신 거지?’

혁무진은 본능처럼 떠올렸다.

언제나 모두의 선두이자 중심에서 목숨 걸고 싸웠던 그, 진태경을.

그와 동시에, 다시 한번 깨달았다.

지금까지의 그 수많은 위기의 순간 속에서도 자신이 매번 살아남을 수 있었던 이유를.

그리고 진태경이 홀로 감당하고 있던 그 거대한 공백과 책임의 무게를.

‘이런 기분이었습니까.’

닿지 않을 물음과 함께, 혁무진은 거친 숨을 내뱉었다.

두려웠다.

지금이라도 당장 검을 내던지고 저 멀리 도망치고 싶을 정도로.

‘예전이었다면, 분명 그랬겠지.’

하지만 이제는 모든 것이 달라졌다.

어느 유서 깊은 포목점의 후계자는 태원진가의 무인이 되었고, 도망치기에는 이미 너무 먼 길을 와 버렸으니까.

재능도, 실력도 부족한 그를 기꺼이 길동무로 삼아 준 고마운 이들에게.

바로 그, 진태경에게 너무나도 많은 것을 보고 배웠으니까.

“절대, 물러서지 마라.”

파르르 떨리는 입술을 비집고 흘러나온 나직한 음성은, 주위의 아군이 아닌 혁무진 자신을 향한 다짐에 가까웠다.

또한 그것은, 이제는 과거의 기억으로만 남아 있는 망나니 삼공자가 언젠가 그에게 해 주었던 말이기도 했다.

“한 번 물러서는 순간…… 두 번 다시 앞으로 나아갈 수 없다.”

그렇기에, 혁무진은 물러서지 않았다.

가슴 깊은 곳에서 울컥 치밀어오르는 두려움을 억누르고, 흔들리는 검 끝을 다잡으며, 거대한 함성을 터트리며 온 힘을 다해 괴물들을 향해 쏘아졌다.

진태경이 그러했듯이 언제나 자신을 믿어 주었던, 또 다른 동료들이 그러하듯이.

쐐애애애액!

거세게 휘몰아치는 바람이, 그의 전신을 휘감았다.



* * *



한 번이라도 전란(戰亂)을 경험한 이들은 입을 모아 말한다.

전투란 광기(狂氣)의 다른 표현이며, 전쟁은 바로 그 광기의 집합체라고.

그저 눈앞의 적을 계속해서 쓰러트리고, 쉴 새 없이 날아드는 공격을 피하다 보면 어느샌가 자신이 알고 있던 모든 것을 잊게 된다고.

어릴 적 나이 지긋한 노인에게서 들었던 그 말을, 혁무진은 또렷하게 기억하고 있었다.

무림인이 되겠다고 다짐하는 그에게 노인이 건넸던 한 마디도.

‘희망은 눈부시지만, 현실은 잔인한 법이지.’

그래, 분명 그렇게 말했던 것 같다.

그리고 노인의 그 말들이 모두 옳았다는 사실을, 혁무진은 다시금 뼈저리게 깨달았다.

뻐억!

둔탁한 소음과 함께 전신을 뒤흔드는 강렬한 충격.

그에 대응할 시간 따위는 없었다.

아니, 설령 대응할 만한 시간이 있었다 하더라도 완전히 피할 수는 없었을 것이다.

그럴 기력 따위, 이미 바닥 나버린 지 오래였으니까.

콰드드득!

새하얗게 물든 시야 속에서 하늘과 땅이 몇 번이나 뒤집혔을까, 저 멀리 튕겨 나간 혁무진이 가장 처음 느낀 것은 전신을 휩쓰는 크고 작은 고통이었다.

쿨럭.

기침과 함께 튀어나온 핏물이 입가를 타고 흐른다.

욱신거리는 뼈마디와 뒤틀린 오장육부는 그의 몸이 결코 성치 않다는 진실을 알려주고 있었다.

‘빌어……먹을.’

혁무진은 이를 악물며 울컥 솟구치는 핏물을 삼켰다.

이제는 얼굴조차 기억도 나지 않는 노인이 했던 말처럼, 현실은 잔인했다.

적어도 그에게는 그랬다.

‘불과 일각 만에 이런 꼴이라니.’

좀처럼 힘이 들어가지 않는 몸뚱어리를 느끼며, 그는 힘없이 자조했다.

통제를 잃고 미쳐 날뛴다고 그 힘이 사라지지는 않는 법.

암천에 의해 탄생한 저 괴물들은 그 끔찍한 외관만큼이나 강했다.

지금 이 순간에도 손에 쥐고 있는 이 명검(名劍)이 아니었다면, 그 홀로 스무 마리나 되는 괴물들을 쓰러트리진 못했으리라 생각될 만큼.

‘따지고 보면, 나 같은 놈이 이 정도로 싸울 수 있었던 것도 전부 조장님 덕분이겠지.’

혁무진은 자신의 손에 들린 검을 바라보았다.

단단하기 그지없는 괴물들의 뼈와 살을 베어냈음에도 선명하게 남아 있는 예기(銳氣).

그의 검은 성라대연이 열리기 직전, 마침내 철구를 끊어 낸 진태경에게서 받은 쇠사슬로 만들어진 것이었다.

열화문이 사문의 죄인들을 속박하기 위해 만든, 바로 그 쇠사슬.

물론 그중에서도 일부만을 사용했으나, 만년한철이 무려 넉 냥이나 들어갔으니 그 강도와 예리함은 과히 명검이라 부르기에 손색이 없을 정도.

그 사실을 알고 있는 사람들은 종종 혁무진에게 과분한 검이라며 놀려 대고는 했지만, 매번 발끈하던 그 역시 마음속 깊은 곳에서는 알고 있었다.

일류의 경지에서 제자리걸음만 반복하는 자신이 이토록 귀한 검을 얻을 수 있었던 것은, 어디까지나 수하를 위한 진태경의 마음 덕분이었다는 사실을.

“하여간…… 말만 틱틱거리지 챙겨 줄 건 다 챙겨 주신다니까.”

실소 섞인 뇌까림과 함께, 혁무진은 비명을 내지르는 몸뚱이를 서서히 일으켜 세웠다.

그리고 남은 힘을 쥐어 짜내어, 가장 가까운 곳에 있는 적의 등 뒤를 향해 달려들었다.

서걱!

이미 한계에 다다른 육체의 피로 때문일까.

마지막 순간 검 끝이 흔들렸지만, 그럼에도 본래의 목표대로 적의 목을 베어 내기에는 조금의 부족함도 없었다.

더군다나 이번 상대는 그와 같은 피륙으로 이루어진 인간이었으니.

철퍽.

머리를 잃고 비틀거리던 육신이 피 웅덩이 위로 고꾸라졌지만, 죽음을 맞이한 광신도의 시신을 내려다보는 혁무진의 마음은 무겁게 가라앉아 있었다.

‘조금만, 아주 조금만 더 우리에게 여력이 있었더라면…….’

포로로 잡았던 강시술사를 이용한 전략은 분명 주효했다.

일천의 괴물 중 대다수가 혼란에 휩싸였고, 그 혼란을 틈타 돌격한 삼천의 수비군은 목숨을 도외시한 공격으로 적들을 몰아붙였으니까.

하지만 그들이 상대해야 할 적은 성 내부에만 있는 것이 아니었다.

동문의 수비군들이 괴물들과의 전투에 총력을 기울이는 사이, 갈고리와 사다리를 이용하여 성벽을 타 넘은 암천의 광신도들은 난입함과 동시에 수비군 향해 기울던 힘의 저울추를 단숨에 뒤집었다.

지금 이 순간조차도.

“……!”

“……!”

이제는 질릴 만큼 익숙한, 광기에 사무친 여덟 글자의 교언(敎言)이 먹먹하게 울려 퍼진다.

성벽 위에서 끊임없이 쏟아져 내려오는 광신도들과 이미 지칠 대로 지친 아군이. 그리고 어느새 하나둘씩 제정신을 차리기 시작하는 괴물들의 모습이 차례대로 혁무진의 눈동자에 비쳤다.

어느덧 수백여 장 앞까지 성큼 다가온 힘찬 나팔 소리와, 언제 그랬냐는 듯 웃음을 되찾은 누군가의 얼굴도 함께.

- 네놈들의 발악도 여기까지다.

들리지 않는다. 하지만 보였다.

저 멀리, 굳게 닫힌 성문 앞에서 벙긋거리는 흑의인의 입술이.

전투가 시작됨과 동시에 자신이 부리던 괴물들에 의해 죽음을 맞이한 동료와는 달리, 약간의 통제력을 발휘할 수 있었던 그는 아직도 수십 마리의 괴물을 방패 삼아 목숨을 부지하고 있었다.

잠깐의 위기를 지나, 이제 확실시된 것이나 다름없는 승리를 만끽하며.

‘그래, 정말 그럴지도 모르지. 하지만…….’

지금 이 자리에서 도망친다면, 어디에서 승리할 수 있단 말인가.

혁무진은 내심 중얼거리며 비틀거리는 발걸음을 옮겼다.

뒤가 아닌, 앞으로.

후우웅!

무뎌진 감각 속, 맹렬한 풍압이 불어닥친다.

족히 수백 근의 힘이 실린 괴물의 주먹이, 혁무진은 단숨에 짓이기고도 남을 일격이 그의 정수리로 떨어져 내렸다.

그리고.

서걱.

어디선가 휘둘려진 한 줄기의 예리한 검기(劍氣)가, 두꺼운 뼈와 살을 갈라 냈다.

“이미 늦었다. 죽고 싶지 않으면 물러서, 지금 당장!”

익숙한 얼굴과 음성.

하지만 그러한 송일섬의 만류에도 불구하고, 혁무진은 발걸음을 멈추지 않았다.

정확히는, 아무것도 듣지 못했다.

지금 이 순간 그의 귓가에는, 오직 한 사람의 목소리가 환청처럼 울려 퍼지고 있었으니까.

- 무진아.

진태경.

혁무진이 가장 닮고 싶은 사람이자, 결코 닮을 수 없다는 사실을 깨닫게 해 준 사람.

마치 그 음성의 주인이 눈앞에 있기라도 한 것처럼, 그는 핏물이 덕지덕지 말라붙은 입술을 달싹였다.

전투가 시작되기 전, 진태경과 나누었던 대화를 떠올리며.

“예. 말씀하십시오.”

쉬이익!

사각에서 울려 퍼진 파공성이 대답 대신 돌아왔지만, 혁무진의 죽음을 바라지 않는 것은 송일섬 한 사람뿐만이 아니었다.

푹!

혁무진의 측면에서 달려들던 광신도의 허리가 활처럼 휘었다.

힘없이 허물어지는 시체에 등에 박힌 검을 뽑아내는 주화란의 모습에, 혁무진을 막아서려던 십여 명의 적들이 방향을 바꾸어 달려들었다.

카가가가각!

끊임없이 울려 퍼지는 비명과 함성 사이로 섞여드는 강철읨 소음 속, 혁무진은 더욱 넓어진 길을 향해 홀린 듯이 걸었다.

주위의 모든 것을 뒤로한 채, 계속해서 귓가를 울리는 목소리를 들으며.

- 만약에, 그러니까 아주 만에 하나라도 일이 잘못된다면…….

달랐다.

그때의 진태경은, 분명 평소와는 달랐다.

한 줌의 웃음도, 장난기도 없이 이렇게 말했었다.

- 최소한, 내가 보는 앞에서 죽어라.

그리고 우뚝 굳어 버린 수하를 향해, 애써 억지웃음을 지어 보였다.

- 물론 그런 일이야 없겠지만, 그래야 내가 복수는 해 줄 거 아니냐. 안 그래?

처음이었다.

진태경이 저런 식의 말을 한 것은.

지금껏 함께 수많은 위기를 헤쳐 나오며, 그가 해 왔던 말은 두 종류밖에 없었다.

도망쳐라.

혹은, 반드시 살아남아라.

어떤 위험이 닥쳐오더라도 진태경은 늘 그랬다.

언제나 모두의 중심이자 선두였고, 목숨을 판돈으로 건 이 빌어먹을 도박판에서 주저 없이 앞장서 왔다.

수하를, 동료를, 스승을.

또는 아무런 일면식조차 없는 누군가를 지키기 위해서.

그랬기에 존경할 수밖에 없었고, 그렇기에 그가 원하는 대답을 내놓을 수밖에 없었다.

- 당연히 이번에도 우리가 이기겠지만, 예. 반드시 그러겠습니다.

아마도 그 순간부터였을 것이다.

혁무진이 홀로 조용히 마음 한구석에서 죽음이라는 단어를 매만지고 있었던 것은.

진정으로 죽기를 각오했던 것은.

하지만…….

‘죽더라도, 의미 없는 개죽음 따위를 당할 수는 없지.’

피딱지가 말라붙은 입꼬리를 억지로 말아 올리며, 혁무진은 굳게 말아쥔 검을 내리그었다.

서걱!

앞길을 가로막았던 두 명의 광신도가 약속이라도 한 듯이 동시에 쓰러진다.

너무나도 손쉽게. 한 편의 연극이라도 되는 것처럼.

그리고 이 예상치 못한 상황에 눈을 크게 뜬 채 멈춰선 광신도들을 향해, 거칠기 짝이 없는 도기(道氣)가 휘몰아쳤다.

콰드드득!

솟구치는 피 분수 아래, 광포한 기운과는 어울리지 않는 차가운 음성이 울려 퍼졌다.

“가라. 그게 네 선택이라면…… 길을 열어 주마.”

그것이 끝이었다.

사마표는 망설임 없이 적들의 사이를 파고들었고, 누군가의 단단한 손이 일순간 비틀거리는 혁무진의 어깨를 붙잡았다.

“혁무…….”

말꼬리를 흐리는 태산을 향해, 혁무진은 조용히 고개를 가로저었다.

무슨 말을 하고 싶은지 안다. 

어느덧 이십여 장 앞까지 가까워진 저 흑의인을, 강시술사를 해치워도 승패는 달라지지 않는다 말하고 싶은 거겠지.

하지만 진태경이라면 분명 이렇게 말했을 것이다.

설령 죽는다 하더라도, 이건 충분히 남는 장사라고.

“어……서.”

간신히 쥐어 짜낸 음성.

그런 혁무진의 모습을 말없이 응시하던 태산은 힘주어 그를 붙잡았다.

그리고, 짤막한 한 마디와 함께 온 힘을 다해 혁무진의 몸뚱어리를 저 멀리 날려 보냈다.

“나중에, 맛있는 거 먹으러 가자. 부각주.”

쐐애애액!

전신을 스치는 거센 바람을 느끼며, 혁무진은 마음속으로 대답했다.

반드시 그러겠노라고. 배가 터지도록 먹자고.

그리고 그와 동시에, 어느덧 허공을 가로질러 코앞까지 성큼 다가온 흑의인의 부릅뜬 눈동자를 보았다.

서걱!

마지막 힘이 실린 섬광이, 강시술사의 목을 스치듯 가로질렀다.



* * *



수천, 수만이 뒤얽힌 전투에서 어느 한 사람의 죽음은 아무것도 아닐지 모른다.

그러나 지금 이 순간 두둥실 떠오르는 단 하나의 목은, 동문을 둘러싼 난전에 큰 변화를 불러 일으키기에 충분했다.

투둑. 쩔그럭.

목이 떨어지고, 힘이 풀린 시체의 손아귀에 들려있던 요령도 떨어졌다.

그리고 동시에, 끔찍한 혼전 속에서 살아남아 날뛰던 삼백여 마리의 괴물들 역시 움직임을 멈췄다.

“……!”

“……!”

시간을 쪼개고 쪼갠, 찰나에 내려앉은 침묵.

누군가는 눈을 부릅떴고, 누군가는 희미하게 웃었으며.

이 모든 것을 만들어 낸, 또 다른 누군가는 등골을 타고 흐르는 전율을 느끼며 자신의 발치에 떨어진 목을 말없이 바라보고 있었다.

아니, 정확히는 강시술사의 목에 남아 있는 예리한 단면(斷面)을.

천하인들이 검기(劍氣)라 불리는 그것의 흔적을.

‘검 때문이…… 아니었어.’

단 한 순간이었다.

어쩌면, 이미 제정신이 아닌 상태에서 맞이한 환각일지도 모른다.

하지만 상관없었다.

마침내 스스로의 힘으로 해냈으니까.

스무 마리나 되는 괴물을 쓰러트릴 수 있었던 이유도, 분에 넘치는 동료들과 함께할 수 있었던 자격도 조금이나마 증명해 냈으니까.

그리고 혁무진의 입가에 힘없는 미소가 맺힌 그 순간.

콰아아앙!

하늘이 쪼개지는 듯한 굉음과 함께, 천지를 떨어 울리는 강대한 기파가 굳게 닫혀 있던 성문을 열어젖혔다.

우우우우웅.

부르르 떨리는 공기.

흐릿한 어둠 속, 태산과도 같은 기운으로 뒤덮은 그림자가 성문 앞에 홀로 우뚝 서 있던 혁무진을 향해 기울어졌다.

“이름이 무엇인가.”

그 순간, 혁무진은 깨달았다.

바로 이곳이, 그의 마지막이라는 것을.

전투가 시작되기 전, 진태경과 했던 약속은 지킬 수 없으리라는 것을.

“화룡각…… 아니, 쾌풍검(快風劍) 혁무진.”

혁무진은 대답했다.

그 어느 때보다도 평온하고, 담담하게.

그리고 나직한 한 마디와 함께, 가슴을 파고드는 거대한 힘을 느꼈다.

“기억해 두지.”

퍼엉!

혁무진의 시야가, 어둠 속으로 곤두박질쳤다.
```

## Final English reading copy

```markdown
# Chapter 1119

BOOOOM!

A deafening crash rang out, and the ground shook.

A thousand monsters rampaged without distinguishing friend from foe, while three thousand defenders prepared to fight to the death.

And on top of that, four Supreme Peak masters flashed across the battlefield, constantly clashing as they tangled together.

The battle raging around the East Gate was more chaotic and brutal than ever.

Even the man who had designed and set this whole situation in motion could barely suppress his fear, despite putting all his strength into it.

—Kyaaaaa!

Hyuk Mujin watched the monsters charge at him, roaring ferociously. His eyes trembled.

They stood over one jang tall, with limbs as thick as the trunks of great trees.

Their immense strength and speed, far beyond human limits, made their charge feel like an unstoppable tidal wave.

*How in the world has Captain faced countless monsters like these?*

The thought came to him instinctively.

Jin Taekyung—the man who had always fought at the head of the group, at its center, risking his life.

And at the same time, Mujin understood once more.

Why he had survived every one of the countless crises they’d faced until now.

The enormous gap Taekyung had been filling alone, and the weight of the responsibility he’d borne.

*So this is what it felt like.*

With a question that would never reach its recipient, Hyuk Mujin let out a ragged breath.

He was afraid.

So afraid that he wanted to throw down his sword and run as far away as he could, right now.

*If this had happened before, I definitely would have.*

But everything was different now.

The heir to a venerable textile shop had become a martial artist of the Jin Family of Taiyuan, and he had already come too far to run away.

He had seen and learned so much from the people who had gladly taken someone as untalented and unskilled as him along for the journey.

Especially from Jin Taekyung.

“Don’t you dare retreat.”

The quiet words slipped past his trembling lips. They were less a warning to his allies than a vow to himself.

They were also words the Third Young Master, the reckless son who now existed only in his memories, had once said to him.

“The moment you retreat once… you’ll never be able to move forward again.”

And so Hyuk Mujin didn’t retreat.

He suppressed the fear surging up from the depths of his chest, steadied his trembling sword tip, and charged at the monsters with all his might, roaring at the top of his lungs.

Like Jin Taekyung had, and like the other companions who had always believed in him.

SHWEEEE!

A fierce wind whirled around him, wrapping his entire body.

* * *

Anyone who has experienced war agrees on one thing.

Battle is another word for madness, and war is the sum of that madness.

If you keep knocking down the enemy in front of you and dodging attacks flying at you without pause, before you know it, you forget everything you once knew.

Hyuk Mujin remembered those words clearly. He’d heard them as a child from an elderly man.

He also remembered what the old man had told him when Mujin declared he would become a martial artist.

*Hope is dazzling, but reality is cruel.*

Yes. That was probably how he’d put it.

And Hyuk Mujin once more learned, down to his bones, that the old man had been right about all of it.

THUD!

A heavy thump, and a powerful shock that shook him from head to toe.

There was no time to react.

No—even if he’d had time, he wouldn’t have been able to dodge it completely.

He’d run out of strength long ago.

KRRRUNCH!

How many times had the sky and ground turned over in his vision, bleached white? The first thing Hyuk Mujin felt after he was flung a long way was pain, great and small, sweeping through his body.

Cough.

Blood came up with his cough and ran from the corner of his mouth.

His aching joints and twisted innards told him the truth: he was in terrible shape.

*Damn… it.*

Hyuk Mujin gritted his teeth and swallowed down the blood welling in his throat.

Just as the old man—whose face he could no longer remember—had said, reality was cruel.

At least, it was for him.

*I’m in this shape after only fifteen minutes.*

Feeling his body, which barely had the strength to move, he gave a feeble, self-mocking laugh.

Losing control and going mad didn’t make the monsters any less powerful.

The monsters born of Dark Heaven were every bit as strong as their horrifying appearance suggested.

Even now, he couldn’t imagine bringing down twenty of them alone without the famous sword in his hand.

*When you think about it, the fact that I managed to fight this well at all is thanks to Captain.*

Hyuk Mujin looked at the sword in his hand.

Its keen edge remained sharp and clear, even after cutting through the monsters’ bones and flesh, hard as they were.

The sword had been made from the iron chain Jin Taekyung gave him, after finally breaking the iron balls just before the Star-Array Grand Banquet.

The very chain the Fire Gate Clan had made to restrain criminals within the sect.

Only part of the chain had gone into the sword, of course, but the blade contained a full four nyang of Ten-Thousand-Year Cold Iron. Its strength and sharpness more than earned it the name of a famous sword.

People who knew that often teased Mujin, saying the sword was too good for him. Though he always bristled at the jabs, deep down he knew the truth.

He’d received such a precious sword only because Jin Taekyung cared for his subordinate—even though Mujin himself had been stuck in the First Rate realm, making no progress.

“Seriously… he talks all sharp, but he still makes sure we have everything we need.”

With a snort of amusement, Hyuk Mujin slowly forced his screaming body upright.

Then he squeezed out what strength he had left and charged at the back of the nearest enemy.

Slice!

Maybe it was the exhaustion of a body that had reached its limit.

His sword tip wavered at the last moment, but he still managed to cut his target’s neck without the slightest trouble.

Especially since this time, his opponent was made of flesh and blood, just like him.

SPLAT.

The headless body staggered and collapsed into a pool of blood, but Hyuk Mujin’s heart sank as he looked down at the dead fanatic.

*If only we’d had a little more strength—just a little more…*

The strategy involving the captured jiangshi sorcerer had worked.

Most of the thousand monsters had fallen into confusion, and the three thousand defenders had charged into the chaos, forcing the enemy back with attacks that disregarded their own lives.

But the enemies they had to face weren’t all inside the fortress.

While the East Gate defenders threw everything they had into fighting the monsters, Dark Heaven fanatics had climbed over the walls with hooks and ladders. The moment they broke in, they had instantly tipped the balance of power away from the defenders.

Even now—

“……!”

“……!”

The familiar eight-character sermon, steeped in madness, rang dully through the air.

Fanatics kept streaming down from the walls. His allies were already exhausted. And, one by one, the monsters were starting to come to their senses.

All of it passed before Hyuk Mujin’s eyes.

Along with the powerful blare of a horn, now only a few hundred jang away, and the face of someone who had regained their smile as if nothing had happened.

—Your struggle ends here.

He couldn’t hear the words. But he could see them.

Far away, in front of the tightly shut gate, the black-robed man’s lips were moving.

Unlike his companion, who had been killed by the monsters he’d commanded as soon as the battle began, this man had managed to exert a measure of control. He was still alive, using dozens of monsters as a shield.

He was savoring a victory that had seemed uncertain for a moment but now looked all but assured.

*Yeah, maybe it really is over. But…*

If he ran away now, where could he win?

Hyuk Mujin muttered to himself as he staggered forward.

Not backward, but ahead.

Whoooosh!

Through his dulled senses, he felt a fierce rush of air.

A monster’s fist, carrying the strength of hundreds of geun, came crashing down toward the top of his head. The blow could have crushed him in an instant.

And then—

Slice.

A sharp streak of Sword Energy, swung from somewhere, cut through thick bone and flesh.

“It’s too late. If you don’t want to die, get back! Right now!”

A familiar face and voice.

But even with Song Ilseom trying to stop him, Hyuk Mujin didn’t halt.

More precisely, he heard nothing at all.

At that moment, only one person’s voice echoed in his ears like a hallucination.

—Mujin.

Jin Taekyung.

The person Hyuk Mujin most wanted to be like—and the person who had made him realize he never could be.

As if the owner of that voice were right in front of him, he parted his lips, caked with dried blood.

Remembering the conversation he’d had with Jin Taekyung before the battle began, he said:

“Yes. Go ahead.”

SHWICK!

A burst of air from his blind spot came back as the answer. But Song Ilseom wasn’t the only one who didn’t want Hyuk Mujin to die.

THUNK!

The fanatic who had charged at Mujin from the side bent backward like a bow.

Ju Hwaran pulled the sword from the back of the body as it crumpled limply. The dozen or so enemies who had been rushing to stop Mujin changed course and charged at her instead.

KRRRANG!

Amid the screams and shouts that never let up, steel rang out. Hyuk Mujin walked as if entranced, toward the path that had opened wider before him.

Leaving everything around him behind, he listened to the voice that kept ringing in his ears.

—If, I mean, if something goes wrong—just in the very unlikely event…

He had been different.

Jin Taekyung had definitely been different then from how he usually was.

With not a trace of laughter or playfulness, he’d said:

—At least die where I can see you.

And then, facing his subordinate, who had gone rigid, he’d forced a strained smile.

—Of course, that won’t happen. But if it did, I’d be able to avenge you, wouldn’t I?

It was the first time.

The first time Jin Taekyung had ever said something like that.

Until then, through all the dangers they’d overcome together, he’d only ever said two things.

Run.

Or make sure you survive.

No matter what danger came their way, Jin Taekyung was always the same.

Always at the center and out in front. He had never hesitated to lead the way in this damn game of chance where they wagered their lives.

To protect a subordinate, a companion, a Master.

Or even someone he’d never met before.

That was why Mujin couldn’t help but respect him, and why he had no choice but to give him the answer he wanted.

—Of course we’ll win this time, too. But yes. If it comes to that, I promise I will.

Maybe that was when it started.

When Hyuk Mujin began quietly turning the word death over in one corner of his mind.

When he truly prepared himself to die.

But…

*Even if I die, I can’t just throw my life away for nothing.*

Forcing up the corner of his mouth, caked with dried blood, Hyuk Mujin swung the sword he gripped tightly.

Slice!

The two fanatics in his path fell at the same time, as if they’d planned it together.

So easily. As if it were all part of a play.

Then, at the fanatics who had stopped short, eyes wide at this unexpected turn, a fierce torrent of saber energy swept in.

KRRRUNCH!

Beneath a fountain of blood, a cold voice rang out, at odds with the wild energy.

“Go. If that’s your choice… I’ll clear the way.”

That was all.

Sama Pyo plunged into the ranks of the enemy without hesitation, and a hard hand caught Hyuk Mujin’s shoulder as he briefly stumbled.

“Hyuk Mu…”

Hyuk Mujin quietly shook his head at Taishan, who trailed off.

He knew what Taishan wanted to say.

He wanted to tell him that even if they killed the jiangshi sorcerer—the black-robed man now just twenty jang away—the outcome wouldn’t change.

But Jin Taekyung would have said this:

Even if you died, this was a deal well worth making.

“Hur…ry.”

The words took all the strength he had left.

Taishan watched Hyuk Mujin in silence, then gripped him tightly.

And with one short sentence, he used all his strength to send Mujin flying far away.

“Let’s go eat something good later, Vice Captain.”

SHWEEEE!

Feeling the fierce wind pass over his entire body, Hyuk Mujin answered in his heart.

*We will. We’ll eat until we burst.*

And as he flew through the air, he saw the black-robed man’s wide eyes suddenly right in front of him.

Slice!

A flash carrying the last of his strength swept across the jiangshi sorcerer’s neck.

* * *

In a battle where thousands, tens of thousands, clash, one person’s death might mean nothing.

But the single head now tumbling through the air was enough to bring about a great change in the battle around the East Gate.

Thud. Clatter.

The head fell, then the ritual bell slipped from the dead body’s hand.

At the same time, the roughly three hundred monsters that had survived the horrifying melee and continued rampaging stopped moving.

“……!”

“……!”

A silence settled over the instant, stretched thinner and thinner.

Some opened their eyes wide. Some smiled faintly.

And someone else, who had made all of this possible, felt a shiver run down his spine as he silently looked at the head at his feet.

Or, more precisely, at the sharp cut across the jiangshi sorcerer’s neck.

At the trace of what people under heaven called Sword Energy.

*It wasn’t the sword…*

It had lasted only an instant.

Maybe it had been a hallucination, born while he was already out of his mind.

But it didn’t matter.

At last, he had done it with his own strength.

He had proved, at least a little, why he’d been able to defeat twenty monsters, and why he deserved to stand alongside companions who were far more than he could ever hope to deserve.

And just as a feeble smile formed on Hyuk Mujin’s lips—

BOOOOM!

A tremendous blast, like the sky splitting apart, shook heaven and earth. An immense surge of qi flung open the tightly shut gate.

Wooooooong.

The air trembled.

Through the faint darkness, a shadow wreathed in an aura as immense as Mount Taishan leaned toward Hyuk Mujin, standing alone before the gate.

“What is your name?”

At that moment, Hyuk Mujin understood.

This was where his life ended.

He wouldn’t be able to keep the promise he’d made to Jin Taekyung before the battle began.

“Fire Dragon Pavilion’s… no. Swift Wind Sword Hyuk Mujin.”

Hyuk Mujin answered.

Calmer and more composed than ever.

And with a quiet reply, he felt an immense force pierce into his chest.

“I’ll remember it.”

POOM!

Hyuk Mujin’s vision plunged into darkness.
```
