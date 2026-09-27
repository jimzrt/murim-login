<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1046.txt",
      "sha256": "23761af28aa9fc7b840928f3b472d8b90b5a8f251f5675057ae9947576e2107f",
      "bytes": 13206
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e6b1168a797dc1ef1cb2b9989b4abc24e941124a09c051c9e25c85da6f00db20",
      "bytes": 1758
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91edff1ea0e7f2d1bdf20f77998a86f250b89f1bc3f043cd106289bea1e118b4",
      "bytes": 240895
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "15843a22741176f223b3ab88e0be966ab68203b6d35d74edac1798b90168ad50",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "98da90daf8ba97501fc147166c1a65797f3674b05e0dab3fd3c884176a6c46de",
      "bytes": 1375
    },
    {
      "path": "characters/Hyuk Sopyung.md",
      "sha256": "483cd81383348d0d0b5a49c8c55620a26f3746b88906413dedc638bb3ad75e77",
      "bytes": 619
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "8bb8e21cd2f1697d6c3a1be82b6608a9cf7cb7aef0ca9a9dc22fce7b85616bc7",
      "bytes": 700
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ef0ca74abf548987839367dd1536d40bfb57e4fa752cd6cd690b556f6f80dbd6",
      "bytes": 1823
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f7db4a9160e2cadf5eeb9b1525508cf9064e29852d3a4a7d178fd1d42de2551b",
      "bytes": 623
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "80d9ca93c791a43ca138d8d562167e5a0333289252f85b95a0d0b788fb1b9f6b",
      "bytes": 974
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "40879f46fdafdebc2f72a0407fd3b74563827b35491eac5b0cce5c6f92031114",
      "bytes": 700
    },
    {
      "path": "characters/Ma Junggeol.md",
      "sha256": "6eea7e6cce272ab43cf870d4a4ce4137d1e4eed23d93f5f752eb62e89c3e2532",
      "bytes": 673
    },
    {
      "path": "characters/Namho.md",
      "sha256": "829595ef03db4b2d4fc66f516e422500213bfe28fc86c8cc18fcc813c191fd50",
      "bytes": 1092
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "3fa427e45966dae37dd6ab805cad0cf923cf94920a4d2793a88deff12ba10c13",
      "bytes": 774
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "b30fbfa00dc10f1cb6c9c1e517ee6403e400cac34768f0bfbb4af4c6f005c56f",
      "bytes": 980
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "0f3b58c55b1cc2dc100e6d9dc54ca219f88067af554f3b7c30f9b6dc9552f93c",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "24b2b369c1e3f38fc8df312c6634dbb257b3bba0ca19767c87202073bdab4513",
      "bytes": 280926
    }
  ],
  "estimated_tokens": 14366
}
-->

# Durable State Update — Chapter 1046

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
1 and safe_through 1046. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1046. Profile updates may replace only one
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
  "chapter": 1046,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1046,
    "continuity_sources": [1046],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "Fire Dragon Armor is severely damaged, stored in Inventory, and unavailable until its automatic repair completes in three days.",
    "The Bow Saint’s Force arrows shattered the Grand Mage’s Hell Fire sphere, causing thousands of casualties, overwhelmingly among Dark Heaven’s forces.",
    "Sima Gong intervened against the Blood-Sword Demon Lord to let Jeok Cheongang proceed; their fight’s outcome is unknown.",
    "Jeok Cheongang attempted to awaken his innate qi and struck the Hell Fire sphere with the Flame-Extinguishing Divine Fist; his condition after the blast is unknown.",
    "Jin Taekyung survived the blast; his condition beyond that is unknown.",
    "The Grand Mage survived the blast and recognized the Bow Saint as the archer who struck the sphere.",
    "Song Il and Hwangbo Eom faced the Hell Fire sphere; their fate remains unknown."
  ],
  "continuity_sources": [
    1044,
    1045
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who are the white-robed mages, and what is their purpose?",
    "How were the former Demonic Cult fiends made into Black Ghosts?",
    "What happened to Jeok Cheongang, Sima Gong, Jin Taekyung, Song Il, and Hwangbo Eom after the blast?"
  ],
  "safe_through": 1045,
  "temporary_decisions": [
    "Render 대마도사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.",
    "Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화.",
    "Render 쇄월검진 as Moon-Shattering Sword Formation."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 혁소평    | **Hyuk Sopyung**   |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 궁성     | **Bow Saint**                 | —              |
| 종남파    | **Zhongnan Sect**                |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 산서     | **Shanxi**             |
| 감숙     | **Gansu**              |
| 소저      | **Young Lady**                                                  |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마중걸 | **Ma Junggeol** |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 유엽도 | **willow-leaf saber** | Saber wielded by Song Ilseom. |
| 종남일룡 | **Zhongnan One Dragon** | Epithet of Hyuk Sopyung. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 추혼객 | **Soul-Chasing Guest** | Song Ilseom’s former epithet; he was known by it ten years earlier. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 절강 | **Zhejiang** | Region from which the boat travels east. |
| 대초자곤 | **two-section staff** | Weapon carried by Sama Pyo's giant subordinate. |
| 요녕 | **Liaoning** | Northeastern region from which the Murong Family arrives. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 천호 | **Thousand Captain** | Rank held by Jeong Hogun in the Embroidered Uniform Guard. |
| 황도 | **Imperial Capital** | The capital where the imperial court resides. |
| 백마칠종 | **Seven Masters of Baekma Bang** | Collective title for Ma Junggeol and his six associates. |

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
| 혁소평 | 진태경 | hostile_opponents | you; bastard | hostile and contemptuous | Hyuk insults Taekyung as a beggar and attacks him after Taekyung refuses to defer to his status. |
| 진태경 | 혁소평 | hostile_opponents | you; bastard | insulting and taunting | Taekyung mocks Hyuk’s appearance, cultivation, and failed attack while forcing him to agree to end the dispute. |
| 혁소평 | 주화란 | senior_Zhongnan_disciple_to_young_bureau_head | Young Lady Ju | formal-apologetic | Hyuk apologizes on Zhongnan's behalf; Ju Hwaran rejects the address and orders him to call her Young Bureau Head. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 정호군 | 태산 | guard officer questioning a performer | you | blunt and direct | He calls Taishan forward and asks whether he belongs to the circus troupe. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |
| 정호군 | 진태경 | imperial officer responding to the Marquis of Shangshan | Marquis of Shangshan | formal and deferential | Accepts the command with a formal acknowledgment of Taekyung’s title. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |
| 진태경 | 마중걸 | Murim Alliance member to visiting horse-caravan chief | Junggeol | casual | Initially addresses him familiarly, then apologizes and shifts to polite speech. |
| 마중걸 | 진태경 | visiting horse-caravan chief to young Murim Alliance member | young man | polite and deferential | Initially calls him a pretty little gigolo as an insult, then uses a respectful address. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1045
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1024
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Hyuk Sopyung.md

# Hyuk Sopyung (혁소평)

- **Safe through:** Chapter 1044
- **Aliases:** Zhongnan One Dragon
- **Role:** Peak master of the Zhongnan Sect known as the Zhongnan One Dragon and a senior disciple who can command the Taeeul Sword Unit in Hwangbo Eom's presence.
- **Personality:** Proud, volatile, entitled, and quick to anger, especially when drunk.
- **Voice:** Loud, confrontational, insulting, and imperious.
- **Relationships:** Baek Museong knows him from several prior encounters; Baek says their elders' connection has been passed down to them.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 1023
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1045
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1045
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1022
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 1023
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Junggeol.md

# Ma Junggeol (마중걸)

- **Safe through:** Chapter 1024
- **Aliases:** Chief of Baekma Bang
- **Role:** Ma Junggeol is the chief of Baekma Bang, a horse-caravan group founded by reformed Ningxia mounted-bandit leaders.
- **Personality:** Though timid by nature, he is earnest and protective of his sworn brothers, loyal to the benefactor who helped them reform, and willing to bear personal risk for their mission.
- **Voice:** Not established
- **Relationships:** He leads six sworn brothers who, with him, are known as the Seven Masters of Baekma Bang, and trusts the benefactor they call the Lord.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1023
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1044
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1022
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1044
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1046화



드넓은 전장에 뒤얽혀 죽고 죽이는 처절한 전투를 이어 가던 수만 명의 적과 아군 중, 그 누구도 처음에는 제대로 인지하지 못했다.

어느 순간 날아들어 거대한 불덩어리를 조각낸 새하얀 섬광을.

그리고 지금 이 순간에도 대설산의 산자락을 뒤덮으며 쏘아지는 강기의 화살들을.

쉬쉬슁!

하나, 둘, 셋. 그리고 열.

연달아 터져 나온 열 개의 빛줄기가 동시에 허공을 찢었다.

분명 미약한 시간의 격차가 있었음에도 불구하고, 나란히 늘어선 그 휘황한 섬광들은 자그마치 이백 장이 넘는 공간을 가로질러 전장을 덮쳤다.

정확히는, 허락되지 않은 방향으로 떨어져 내리고 있던 크고 작은 불덩어리들을.

꽈아아아앙!

겹겹이 울려 퍼지는 굉음과 함께, 그 충돌의 여파로 인해 뻗어 나온 열기가 지면을 스쳤다.

화륵, 치이이익!

옷깃이 까맣게 그을리고 머리카락이 녹아내린다.

그러나 이미 자신들을 향해 쏟아지는 화염의 구를 보며 죽음을 직감하고 있던 이들에게는, 이런 고통 따위는 아무것도 아니었다.

아니, 그보다도 훨씬 큰 놀라움과 충격이 고통을 잠시나마 잊게 했다.

“어, 어떻게…… 쿨럭.”

한 움큼이나 되는 핏물을 토해 낸 노도사, 태을무정검은 말을 잇지 못하고 눈가를 파르르 떨었다.

마지막 순간, 모든 것을 포기한 채 눈을 감기까지 했던 그로서는 자신이 아직도 이승에 남아 있다는 현실을 믿을 수 없었다.

그런 태을무정검의 곁에서, 눈앞까지 들이닥친 죽음을 직시하고 있던 누군가는 달랐지만.

“허, 허허.”

노호검객은 자신의 한쪽 팔이 새카맣게 타들어 갔다는 사실조차 잊은 채, 힘없는 실소를 흘렸다.

이대로 죽고 싶었다. 죽어 마땅했다.

그러나 살아남았다.

생각지도 못한 도움으로.

이제는 저 끔찍한 녹아내리고 없는 흰 머리카락이 검게 물들어 있던, 까마득한 젊은 시절에 보았던 그 파괴적이면서도 눈부신 섬광을 오늘 이 자리에서 다시 한번 보았다.

‘궁성(弓星). 진정 당신이오?’

기막힌 우연인가. 혹은 하늘의 도우심인가.

마음속에 울려 퍼지는 뇌까림과 함께, 노호검객은 남아 있는 힘을 쥐어 짜내어 신형을 일으켜 세웠다.

이것이 그저 단순한 행운인지, 하늘이 정한 운명인지는 모른다.

하지만 한 가지는 확실했다.

자신들이 아직 살아 있는 이유가 있다면, 그건 남아 있는 죗값을 치르기 위해서라는 것.

“……원시천존(元始天尊)이시여.”

가까스로 지면에 두 발을 딛고 선 노호검객은, 실로 오랜만에 원시천존을 입에 담으며 문득 하늘을 바라보았다.

스아아.

마치 그의 부름에 대답하듯, 하늘을 뒤덮은 새카만 먹구름 너머로 스치듯 비쳐 오는 빛.

그리고 그 빛 아래에는, 이미 떠난 줄로만 알았던 종남파의 제자들이 적들을 휩쓸고 있었다.

쐐애액, 서걱!

검이 번뜩이고 피가 흩뿌려진다.

오직 적들의 머리 위로만 쏟아지는 불덩어리 아래로, 처절하면서도 힘찬 함성이 울려 퍼진다.

“종남의 제자들이여! 절대 물러서지 마라!”

“으아아아아!”

콰아앙!

드드드득!

끝없이 솟구치는 불길과 뒤집히는 땅거죽.

그리고 숯덩이가 되어 가면서도 천주를 찬양하는 교언(敎言)을 읊으며 홀린 듯이 나아가는 암천의 군세.

하지만 이제 불과 오백여 명도 남지 않은 종남파 제자들의 발걸음은 단 한 시도 멈추지 않았다.

“우리의 도(道)는, 이곳에 있다!”

종남일룡 혁소평.

피를 토하는 듯한 그의 외침이 피로에 젖어 있던 모두의 정신을 깨웠다.

죽음을 각오하고 싸우는 그들의 모습과 연이어 쏟아지는 강기의 화살이, 짙은 패색을 띤 채 뒷걸음질 치던 감숙 연합군의 발목을 붙잡았다.

“제기랄! 쳐!”

“지금이다! 모조리 밀어붙여!”

“으아아! 이 시발새끼들아!”

사파, 정파, 흑도. 심지어는 관군까지.

전황만큼이나 혼잡하게 뒤섞여 있던 그들은 아직까지도 현재의 상황을 정확히 알 수 없었지만, 모두가 본능처럼 직감하고 있었다.

지금이 아니라면 두 번 다시 기회는 없다는 것을.

그리고 비명과도 같은 고함을 내지르며 다시 적을 향해 달려드는 그들의 선두에는, 처음부터 지금까지 단 순간도 물러선 적 없었던 일단의 무리가 있었다.

“우오오오오!”

후우웅!

듣는 것만으로도 등골이 서늘해지는 파공성.

흡사 맹수의 포효와도 같은 기합과 함께 휘둘려진 거대한 대초자곤(大哨子棍)이 앞을 막아선 적들을 휩쓸었다.

콰드드득!

사방으로 비산하는 핏물과 살점.

전장에서도 단연 눈에 띄는 거한의 어깨에 올라타 있던 자그마한 체구의 이민족 노인이 입에 들어간 살점을 내뱉으며 비명을 내질렀다.

“마! 옆에! 옆에 봐!”

그러나 이민족 노인, 남호의 외침을 태산이 이해하기도 전에 측면에서 들이닥친 일곱 명의 적들은 검기를 휘둘렀고.

쉬이잉, 서걱!

그보다 앞서 공간을 가로지른 세 자루의 병장기가 그들의 목과 가슴을 베어 갈랐다.

푸화아악!

터져 나오는 피분수 속, 추혼객(抽魂客) 송일섬은 자신의 유엽도를 적신 끈적한 핏물을 털어내며 입을 열었다.

“다들 괜찮소?”

입을 벌리고 있다가 한 움큼이나 되는 핏물을 삼켜 버린 남호가 대답했다.

“안 괜찮다. 속이 울렁거려.”

뻐억!

끔찍한 타격음과 함께 또 한 명의 적을 쓰러트린, 아니 반쯤 부숴 버린 태산이 평소와 달리 착 가라앉은 목소리로 말을 받았다.

“남호. 토하면 안 된다. 주군 찾기 전까지는.”

“이 씨부럴 놈 보게, 그게 늙은 나이에 고생하는 어르신한테 할 말이냐?”

“그러게 왜 왔나. 누가 칼 들고 협박했나?”

“……!”

남호가 말문이 막힌 그때, 춤을 추는 것처럼 유려한 몸놀림으로 적들을 베어 넘긴 주화란이 입을 열었다.

“저희도 괜찮아요. 다만 각주님이 걱정이에요.”

혁무진이 격전 도중 길게 베어 나간 옆구리를 움켜잡으며 중얼거렸다.

“저 다쳤는데…….”

“다들 멀쩡해요. 그러니까 머뭇거리지 말고 어서 각주님께 가요.”

“아니, 왜 물어보지도 않고…….”

“각주님. 위험. 급박.”

혁무진은 즉각 입을 닥쳤고, 엉겁결에 이 자리에 함께하게 된 백마칠종의 우두머리 마중걸은 슬픈 얼굴로 비수가 박힌 자신의 허벅지와 주화란을 번갈아 바라보았다.

“왜요, 하실 말씀 있으신가요?”

“소저, 그러니까. 그게.”

“없으시군요.”

“……그래, 그런 걸로 합시다.”

이제 눈까지 희번득거리는 주화란의 모습에 마중걸은 침울하게 고개를 떨구었다.

미쳤다.

이 연놈들은 미쳐도 단단히 미친 것이 틀림없다.

‘도대체 왜 내가 여기까지 온 거지?’

모른다.

눈을 몇 번 깜빡이자 함께 달려가고 있었고, 어어 하다 보니 최전선에서 싸우고 있었다.

초절정 고수가 아닌 마당에야 어디 멀쩡할 수 있나.

격전을 치르던 와중에 칼도 맞고, 비수도 박혔다.

하지만 계속해서 싸워야 한다.

아니, 싸우랜다.

‘이런 씨벌…….’

마중걸은 그 어느 때보다 이 자리에 없는 자신의 의형제들이 보고 싶었다.

헛소리만 해 대던 대인의 모습도 눈앞에 어른거렸다.

‘늦지 않게 모시고 온다더니. 이 염병할 놈들.’

마중걸은 차오르는 눈물을 삼키며 괜히 뒤를 돌아보았다.

살아생전 마지막으로 보는 것일지도 모르는 대설산은, 수만여 명의 불청객들이 빠져나간 지금에도 언제나 그렇듯 웅장하고도 눈부신 자태를 자랑하고 있었…….

“응?”

순간 마중걸은 자신의 눈을 의심했다.

그리고 그가 놀란 이유는, 대설산의 산자락을 타고 연이어 전장을 향해 퍼부어지는 빛줄기 때문이 아니었다.

말로만 듣던 궁성이 나타났다는 사실은, 이미 이 꺼림칙한 동행인들을 통해 알고 있었으니까.

하지만…….

‘저건 또 뭐지?’

지금 이 순간 마중걸의 눈동자에 미친 것은, 대설산을 타고 흘러내리는 황금빛 물결이었다.



* * *



녹지 않는 만년설(萬年雪)로 뒤덮인 대설산은 언제나 희었다.

봄에도, 여름에도, 가을과 겨울에도.

그것은 이미 천 년 전부터 그래 왔듯이, 천 년 후에도 변함없을 사실이었다.

하지만 바로 오늘, 지금 이 순간만큼은 예외였다.

솨아아악!

거칠게 휘몰아치는 바람.

대설산 산맥 어디선가 홀연히 나타나, 섬광이 되어 나아가는 신형들을 따라 지면에 쌓인 눈발이 흩날렸다.

가파른 산비탈을 평지처럼 질주하는 그들의 모습은, 마치 하나의 물결과도 같았다.

어떤 곳에서도 그 눈부신 광채를 잃지 않는, 황금빛 물결.

“금의위(錦衣衛)……!”

숨길 수 없는 격동이 담긴 누군가의 외침이 전장을 휩쓸었을 때, 황금빛 갑주를 걸친 일천의 금의위는 산비탈을 물결처럼 쓸어내리며 속도를 더해 가고 있었다.

오직 승리라는 두 글자는 끊임없이 되새기는 동시에.

귓가로 또렷하게 전해지는 지휘관의 목소리를 들으며.

“보이는가?”

금의위 천호(千戶), 정호군의 물음에 대답하는 목소리는 없었다.

다만, 가마솥에 담긴 물처럼 서서히 들끓어 오르는 기세가 있을 뿐.

“저곳에 우리의 적이 있다. 순리를 거스르고, 천하를 도탄에 빠트리려는 악적들이 있다.”

군웅할거의 시대가 저물고 새로운 왕조가 들어선 지 어언 일백여 년.

주씨 성을 쓰는 영웅은 황상에 올라 비로소 만백성의 어버이가 되었고, 그의 피를 이은 용의 후손들은 천자를 자처하며 자신들의 권위를 공고히 다졌다.

그리고 수많은 백성 중에서 무예와 충성심이 가장 뛰어난 이들만을 선별하여 황금빛 옷과 갑주를 입혔으니, 그것이 곧 금의위의 탄생이었다.

“황실을 어지럽히고, 더 나아가 지엄하신 황제 폐하께서 다스리시는 이 나라를 무너트리려 한 자들이다!”

조금씩 힘을 더해 가는 정호군의 음성을 따라, 깊게 눌러쓴 투구 아래로 일천 쌍의 안광이 빛났다.

황도가 위치한 절강성에서부터 산서까지.

뒤이어 요녕과 하북을 아우른 것으로도 모자라, 이제는 대륙의 절반을 가로질러 감숙까지 다다른 숨 가쁜 여정.

지치지 않았다면 거짓말이다.

제아무리 황실을 수호하는 대국의 최정예라 한들, 그들의 육신은 강철이 아니었으니까.

그러나 그들이 마음속에 품은 의지와 충성심은, 강철보다 단단하고 황금만큼이나 빛났다.



‘가거라. 그대들은 짐이 가진 가장 날카로운 검이자 방패인즉, 황실의 은인인 상산후(上山侯)를 지키고 그의 적들을 토벌하라.’



일천의 금의위들은 아직도 선명하게 기억하고 있었다.

아니, 죽는 그 순간까지 잊지 못할 것이다.

황도를 떠나기 전날 마주했던 천자의 모습을.

병색이 완연한 안색으로도 상산후 진태경을 입에 담으며 머금었던 그 미소와, 마지막 명령을.



‘명심하라. 그의 적은, 곧 짐의 적이다.’



천자의 위엄 어린 음성이 모두의 귓가에 맴돌던 그때, 정호군이 힘 있는 외침을 토해 냈다.

“그날의 황명(皇命)을, 모두 기억하는가!”

또 한 번 들려오는 지휘관의 물음에, 그들은 대답했다.

자신들만의 방식으로.

차차차창!

마침내 세상 밖으로 모습을 드러낸 무수한 병장기가 번뜩인다. 투구의 틈새 사이로 드러난 안광은 지금 이 순간에도 빠르게 가까워지는 적들을 향해 빛나고 있었다.

유형화된 기운이 어른거리는 일천 자루의 병장기.

숨 막히는 투기(鬪氣)를 뿜어내는 일천 쌍의 안광.

그리고 이 두 가지 모두를 지닌, 일천 명의 고수.

그 거대한 황금빛 물결이 산비탈을 뒤덮으며 전장을 향해 쏟아졌다.

아니, 파도가 되어 막아서는 모든 것을 휩쓸었다.

쉬이잉, 콰앙!

궁성이 쏘아 보낸 강기의 화살이 적들의 전열을 증발시킨 그 순간.

콰드드드득!

송곳처럼 그 사이를 파고든 일천의 금의위가, 전장의 흐름을 뒤바꾸었다.
```

## Final English reading copy

```markdown
# Chapter 1046

Among the tens of thousands of allies and enemies locked in a brutal battle across the vast battlefield, killing and dying, no one noticed at first.

Not the dazzling white flash that suddenly flew in and shattered the enormous ball of fire.

Nor the Force arrows still raining down over the slopes of the Great Snow Mountain.

Shwip, shwip, shwip!

One, two, three. Then ten.

Ten streaks of light burst forth one after another, tearing through the air all at once.

Though there had been a slight delay between them, the dazzling streaks lined up side by side and swept across the battlefield, spanning more than two hundred *jang*.

More precisely, they struck the great and small balls of fire that were falling in a direction they had no right to take.

KWA-BOOOOM!

A deafening roar rolled over itself, and the heat from the impact swept across the ground.

Fwoosh, sizzle!

Collars blackened. Hair melted away.

But to those who had already sensed death as they watched the spheres of flame come crashing toward them, pain like this was nothing.

No—their astonishment and shock were so great that, if only for a moment, they forgot the pain.

“H-How…? Cough.”

The old Daoist, the Taeeul Merciless Sword, coughed up a mouthful of blood. He couldn’t finish his sentence; the corners of his eyes trembled.

At the last moment, he had given up everything and closed his eyes. He couldn’t believe he was still among the living.

Beside him, though, someone who had stared death in the face as it bore down on them reacted differently.

“Heh. Heh…”

The Roaring Fury Swordsman let out a weak laugh, not even noticing that one of his arms had been burned black.

He had wanted to die like this. He deserved to die.

And yet he had survived.

Thanks to help he had never expected.

Today, right here, he had seen once more that destructive, dazzling flash he’d witnessed in his distant youth, when his white hair had still been black—and before that dreadful hair had melted away.

*Bow Saint. Is it really you?*

An incredible coincidence? Or Heaven’s grace?

As the words echoed in his heart, the Roaring Fury Swordsman squeezed out what strength remained and rose to his feet.

He didn’t know whether this was mere good fortune or a fate decreed by Heaven.

But one thing was certain.

If there was a reason they were still alive, it was to pay for the sins they had yet to atone for.

“…Primordial Heavenly Venerable.”

At last, the Roaring Fury Swordsman planted both feet on the ground. For the first time in ages, he invoked the Primordial Heavenly Venerable, then looked up at the sky.

Shaa.

As if answering his call, a ray of light slipped through the black clouds blanketing the sky.

Beneath that light, the Zhongnan Sect Disciples—whom he’d thought had already left—were sweeping through their enemies.

Shing! Slice!

Swords flashed, scattering blood.

Beneath the fireballs raining down only on their enemies, a desperate yet powerful battle cry rang out.

“Disciples of the Zhongnan Sect! Don’t you dare retreat!”

“Yaaah!”

KWA-BOOM!

Rrrrmmble!

Flames surged endlessly, and the earth turned over.

Even as they were charred black, the Dark Heaven forces advanced as if possessed, chanting words of worship to the Lord of Heaven.

Yet the Zhongnan Sect Disciples, now fewer than five hundred, never stopped moving—not for a single moment.

“Our path is here!”

Zhongnan One Dragon, Hyuk Sopyung.

His cry, ragged as if he were coughing up blood, roused the minds of all those sunk in exhaustion.

The sight of them fighting with death already accepted, together with the Force arrows raining down one after another, stopped the Gansu Coalition Army from retreating as it staggered backward on the brink of defeat.

“Damn it! Attack!”

“Now! Push them all back!”

“Yaaah! You fucking bastards!”

Unorthodox factions, orthodox factions, dark-path figures. Even the imperial army.

They were jumbled together as chaotically as the battle itself. They still couldn’t make sense of what was happening, but all of them instinctively knew:

If they didn’t seize this chance now, they’d never get another.

And at the front of the group charging at the enemy again with screams that sounded like cries of anguish was a band of fighters who hadn’t retreated for even an instant—not from the beginning, not now.

“Uoooooh!”

Whoom!

The whistle of the weapon alone sent a chill down the spine.

With a battle cry like a beast’s roar, the massive two-section staff swept through the enemies blocking the way.

KRAK-KOOM!

Blood and flesh flew in every direction.

Perched on the shoulder of the giant who stood out even on the battlefield, the small, foreign old man spat out the piece of flesh that had gotten into his mouth and screamed.

“Hey! To the side! Look to the side!”

But before Taishan could understand the foreign old man Namho’s shout, seven enemies rushed in from the flank, swinging Sword Energy.

Shing! Slice!

Three weapons had already cut across the space ahead of them, cleaving through their necks and chests.

Splaash!

Amid the spray of blood, Soul-Chasing Guest Song Ilseom spoke as he shook the sticky blood from his willow-leaf saber.

“Is everyone all right?”

Namho had had his mouth open and swallowed a mouthful of blood. He answered, “No. My stomach’s churning.”

Thwack!

With a horrifying impact, Taishan felled another enemy—or rather, smashed him halfway to pieces. His voice was unusually subdued as he replied,

“Namho. Don’t throw up. Not until we find the Lord.”

“Look at this little shit. Is that how you talk to an old man who’s suffering at his age?”

“Then why’d you come? Did someone threaten you with a knife?”

“……!”

Namho was at a loss for words. Ju Hwaran, who had been cutting down enemies with movements as graceful as a dance, spoke up.

“We’re all right, too. I’m just worried about the Pavilion Master.”

Hyuk Mujin clutched his side, where a long gash had opened during the fight, and muttered, “I’m hurt, though…”

“Everyone’s fine. So stop hesitating and let’s get to the Pavilion Master.”

“No, why didn’t you even ask—”

“Pavilion Master. Danger. Urgent.”

Hyuk Mujin immediately shut his mouth. Ma Junggeol, the leader of the Seven Masters of Baekma Bang, who had somehow ended up here with them, looked sadly back and forth between the dagger stuck in his thigh and Ju Hwaran.

“Do you have something to say?”

“Young Lady, well. It’s just…”

“You don’t.”

“…Right. Let’s say that.”

At the sight of Ju Hwaran, whose eyes had begun to gleam, Ma Junggeol lowered his head gloomily.

They were crazy.

There was no doubt about it. These people were completely insane.

*Why did I come all the way here?*

He didn’t know.

He’d blinked a few times, and somehow he was running with them. Before he knew it, he was fighting on the front line.

How could anyone be unscathed in the middle of a battle unless they were a Supreme Peak master?

He’d been hit by a sword and stabbed with a dagger in the thick of the fighting.

But he had to keep fighting.

No—he was being told to keep fighting.

*Shit…*

More than ever before, Ma Junggeol wished he could see his sworn brothers, who weren’t here.

The image of the Lord, who did nothing but talk nonsense, kept appearing before his eyes.

*You said you’d bring him here in time. You damn bastards.*

Swallowing back tears, Ma Junggeol glanced behind him for no reason.

The Great Snow Mountain—perhaps the last thing he’d ever see—still stood magnificent and radiant, as it always had, even now that tens of thousands of unwelcome visitors had left it behind…

“Hm?”

For a moment, Ma Junggeol doubted his own eyes.

And it wasn’t because of the streaks of light pouring down the slopes of the Great Snow Mountain and into the battlefield one after another.

He already knew, through these suspicious companions, that the legendary Bow Saint had appeared.

But…

*What’s that?*

What had caught Ma Junggeol’s eye at that moment was a golden wave flowing down the Great Snow Mountain.

* * *

The Great Snow Mountain was always white, blanketed in snow that never melted.

In spring, summer, fall, and winter.

It had been that way for a thousand years, and it would still be the same a thousand years from now.

But today, at this very moment, was an exception.

Whoooosh!

The wind howled.

The snow on the ground scattered as figures that had appeared out of nowhere somewhere in the mountain range raced forward in streaks of light.

They raced down the steep mountainside as if it were flat ground, moving like a single wave.

A golden wave, its dazzling radiance undimmed no matter where it went.

“The Embroidered Uniform Guard…!”

When someone’s shout, brimming with barely restrained emotion, swept across the battlefield, a thousand Embroidered Uniform Guards in golden armor were already racing down the mountainside like a wave, picking up speed.

All the while, they repeated two words in their minds: victory.

And listened to the commander’s voice, clear in their ears.

“Do you see them?”

No one answered the question from Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard.

Only their aura, simmering like water in a cauldron, steadily grew stronger.

“Our enemies are there. Evil men who defy the natural order and seek to plunge the world into misery.”

It had been more than a hundred years since the age of warring heroes came to an end and a new dynasty took its place.

The hero of the Zhu clan ascended the throne and at last became the father of all his people. His descendants, the dragon-blooded heirs, called themselves the Sons of Heaven and firmly established their authority.

Among the countless people, those with the greatest martial skill and loyalty were selected and given golden robes and armor. Thus was the Embroidered Uniform Guard born.

“They disturbed the imperial court and sought to bring down this nation, ruled by His Majesty the Emperor!”

As Jeong Hogun’s voice grew stronger, a thousand pairs of eyes glinted beneath their lowered helmets.

From Zhejiang Province, where the Imperial Capital stood, all the way to Shanxi.

Then on through Liaoning and Hebei—and, as though that were not enough, across half the continent to Gansu.

It had been a grueling journey.

It would be a lie to say they weren’t tired.

No matter how elite they were, the finest force of the Great Nation guarding the Imperial Family, their bodies were not made of steel.

But the Will and loyalty they carried in their hearts were harder than steel and shone as brightly as gold.

*Go. You are my sharpest sword and my shield. Protect the Marquis of Shangshan, benefactor of the Imperial Family, and put his enemies to the sword.*

The thousand Embroidered Uniform Guards still remembered it vividly.

No—they would never forget it, not until the moment they died.

The sight of the Son of Heaven they had met the day before leaving the Imperial Capital.

Despite his pallid, sickly complexion, the Emperor had spoken of Jin Taekyung, the Marquis of Shangshan, with a smile—and given them his final command.

*Remember. His enemies are my enemies.*

As the Emperor’s commanding voice echoed in their ears, Jeong Hogun cried out with force,

“Do you all remember the imperial command from that day?”

At their commander’s question, they answered.

In their own way.

Clang, clang, clang!

Countless weapons finally emerged into the open, glinting in the light. Beneath their helmets, their eyes shone toward the enemies drawing rapidly closer.

A thousand weapons shimmering with tangible energy.

A thousand pairs of eyes radiating suffocating fighting spirit.

And a thousand masters, each possessing both.

The enormous golden wave covered the mountainside and poured toward the battlefield.

No—it became a wave and swept away everything in its path.

Shing! KWA-BOOM!

At the very moment the Force arrows fired by the Bow Saint vaporized the enemy ranks—

KRAK-KOOM!

The thousand Embroidered Uniform Guards drove through the opening like awls, changing the course of the battlefield.
```
