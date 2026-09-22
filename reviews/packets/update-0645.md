<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0645.txt",
      "sha256": "734c20479a17e67f285b365040263a287527b2e34cbd6733eb209b7638693c36",
      "bytes": 14750
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b436a6c6e31f84dd1bf2d0633375805506c4a6a5cbc0c1677a7f6b3aa9728f4b",
      "bytes": 2430
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fec34948969962d15d812c093e8635116ebbb3323b354b11a251d0c359fcab47",
      "bytes": 198665
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "5cd920f8077b509c7067cd462c910cfcb23786d77295169d10cd9c90c1fa030f",
      "bytes": 705
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "9018de30f968fd65d9ef0349d960d90364d85f43ddc08946861707c474e2100f",
      "bytes": 560
    },
    {
      "path": "characters/Blood Monk.md",
      "sha256": "25f9bc2412a9a813432a77c9044028abeeef31b0092294c7a3b957ab09397521",
      "bytes": 552
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "860b17d975c5e0136f98c8648a62faf3edb5d359fdc3241f934e51307a40b8dd",
      "bytes": 623
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "65ced859e568c91ef03579fec8d939e449209b20e7061d7b717439c2e809b74c",
      "bytes": 1347
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "81060fa4ff1a286be1bb2c5a19af59422dd2cd2ad749dc41612e07f7309b7f4a",
      "bytes": 1936
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8d94ca38acc6ba85bcbaf35055146a1e35a1fa459374e73069b6da90d18c52ce",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "0442e0569e854a543a70f3173890eaa90a0cb5bf75313b58810a4d29092f9958",
      "bytes": 1043
    },
    {
      "path": "characters/Namho.md",
      "sha256": "87f2eb3756ef1d254f55b3bdc75984b6c8d7a1485c1eb893cb411c398cc050c7",
      "bytes": 843
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "5a7c6afc7c4ff1063dcd9f588d4dd028ae959bd26250c53b86e6aa7509a0124c",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "47c8ce38d35818081d715f4b5e1c1b412f7abbe9cb010bd5883ea7d41f9b3b1e",
      "bytes": 957
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "e0f4e1a3a9afb45de3009ee2053921be4e6843d78916856a9c920f9b7e6331e3",
      "bytes": 528
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "474143e5ce05f5fa02e0dd8f6de4758a77c5a64323645d5393af267835605f83",
      "bytes": 871
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "a58c2b4f0fc4f74557be11deaea7e7ab33a1a1c8b610ba14baff98b24bdb4db8",
      "bytes": 542
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "10fcd9fa94dec9f52a85e4c218c4423d548d7de8f6080bcbc7cfbb966c6683f5",
      "bytes": 204175
    }
  ],
  "estimated_tokens": 15015
}
-->

# Durable State Update — Chapter 645

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 645. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 645. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 645,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 645,
    "continuity_sources": [645],
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
    "Jin Taekyung has been admitted to the Nanman tribal grand council with majority support.",
    "Yayul Cheok formally authorized Jin's attendance as Palace Lord and great chieftain of the Miao people.",
    "Baeksang opposed Jin's admission but accepted the majority decision without blocking it.",
    "Chieftains support Jin because he saved their people at Ailao Mountain or because their tribes owe historical debts to the Fire King and Fire Gate Clan.",
    "The Quest [Tribal Grand Council] requires Jin to secure the Nanman Beast Palace's entry into the alliance; its Reward and failure condition remain unknown.",
    "Approximately two hundred elite warriors of Ailao Mountain remain alive inside the Thousand-Year Spider webs and await evacuation.",
    "The Thousand-Year Spider webs appear to shield their victims from the Poison Mist.",
    "The missing ferocious beasts have not been found in the Poisonblood Grounds.",
    "Dark Heaven's involvement in the Thousand-Year Spider attack remains suspected, and the purpose of Ailao Mountain's Wraith remains unknown.",
    "The nature of the pure-white eggs in the Poisonblood Grounds remains unknown.",
    "An unidentified entity who knows Jin Taekyung has killed two informants after learning of his council attendance and implied a long-standing prior connection.",
    "The Blood Monk is an unidentified bald martial artist carrying a Zen staff who has killed hundreds in Guizhou; the captured witness who might have revealed his destination has died, and Jin suspects a possible connection to Dark Heaven or a threat to Nanman."
  ],
  "continuity_sources": [
    644
  ],
  "open_questions": [
    "Who is the hidden entity that recognizes Jin Taekyung, and what is the nature of their past connection?",
    "Where did the missing ferocious beasts go?",
    "Did Dark Heaven influence the Thousand-Year Spider attack, and is the Blood Monk connected to Dark Heaven or heading toward Nanman?",
    "What does Ailao Mountain's Wraith intend to do?",
    "What are the pure-white eggs in the swamp, and what will emerge from them?"
  ],
  "safe_through": 644,
  "temporary_decisions": [
    "Use Tribal Grand Council for 부족 대회의.",
    "Use Blood Monk for 혈승.",
    "Use Sword Demon for 검마.",
    "Use two-headed horn snake for 쌍두각사.",
    "Use Thousand-Year Spider for 천년지주."
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
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 소국주    | **Young Bureau Head**                        |
| 명성               | **Fame**                       |
| 소저      | **Young Lady**                                                  |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 혈승 | **Blood Monk** | Sobriquet of the unidentified bald martial artist active in Guizhou. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 전광석화 | **Quick Attack** | Warlordmon’s rapid-movement command; used as a Pokémon-style gag. |
| 전광 | **Quick Attack** | Shortened form of Warlordmon’s rapid-movement command. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 귀주 | **Guizhou** | Region whose Murim representatives send a delegate. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 조이 | **Joey** | U.S. military or political official introduced by first name only. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
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
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 야율목 | 남호 | Nanman Young Palace Lord to elderly guest and Hidden Shadow Pavilion agent | old man | respectful and familiar | Yayul Mok uses the honorific 노인장 while praising Namho's knowledge of White Tigers. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 야율목 | 야수묘왕 | son_to_father | Father | formal and deferential | Yayul Mok calls out to the Beast Miao King after the rescue party arrives. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 644
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle; he opposes the Nanman Beast Palace joining the Murim Alliance and Jin Taekyung's attendance at the tribal grand council.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 644
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, and a master among the Ten Kings.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace and is responsible for the forces stationed at Ailao Mountain.

### Blood Monk.md

# Blood Monk (혈승)

- **Safe through:** Chapter 644
- **Aliases:** None
- **Role:** The Blood Monk is an unidentified bald martial artist who carries a single Zen staff and has killed several hundred people in Guizhou; his current destination is unknown.
- **Personality:** Unknown; the captured witness who described him was unable to provide further information before dying.
- **Voice:** Not established.
- **Relationships:** His connection to Dark Heaven and Nanman is unknown.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 644
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung is foolish, easily flattered, and politically dependent on stronger personalities despite leading a powerful tribe.
- **Voice:** Heugung speaks with warm enthusiasm and exaggerated devotion toward Yohi.
- **Relationships:** Yohi and Baeksang keep Heugung under their control, while Heugung responds to Yohi's manipulation with apparent infatuation.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 642
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 644
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 644
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 631
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, an experienced Nanman escort guide with route knowledge from the Escort King's records, and someone who can understand the Miao and Bai languages.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 633
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 627
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 627
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 639
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 643
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 644
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, and manipulates Heugung alongside Baeksang.

## Korean source

```text
＃645화



누가 먼저 선을 넘었을까.

나? 아니면 백상?

그리고 나와 그가 나누었던 말 중, 무엇이 진실이며 거짓일까.

짧은 순간 여러 가지 의문들이 뇌리를 스쳤지만 그런 건 이제 더 이상 중요하지 않았다.

지금부터는 말과 생각이 아니라 오직 힘으로 결과를 논하는, 순수한 무림인들의 시간이니까.

쉭!

귓가를 파고드는 날카로운 파공성.

소리를 듣기도 전에 고개를 꺾어 날아드는 지풍(指風)을 피해 낸 나는, 한 치의 망설임도 없이 앞에 놓인 석탁(石卓)을 짚었다.

쿠웅!

거대한 암석을 깎아 만든 탁자가 진동한다.

동시에 튕겨지듯 허공으로 떠오르는 서른세 개의 술잔. 나는 부드럽게 손을 내뻗어 그중 일부를 밀어 냈다.

퉁.

오직 한 사람. 백상을 향해.

쉬쉬쉬쉭!

그것은 나무를 대충 다듬어 만든 투박한 술잔들에 불과했으나, 내가 흘려보낸 공력을 머금자 무시무시한 흉기로 돌변했다.

화살보다 빠른 속도. 그리고 바위도 부술 만큼의 파괴력.

하지만 상대는 침착했고, 침착하기 이전에 강했다.

후웅, 서걱!

곧게 편 수도(手刀)가 횡으로 휘둘려지자, 보이지 않는 무형의 기가 허공을 격하고 날아들던 술잔들을 갈랐다.

그리고 힘을 잃은 채 산산조각이 난 술잔의 파편이 지면에 떨어지기도 전, 솟구치듯 자리에서 일어난 그의 신형이 흐릿해졌다.

파팟!

대전에 내려앉은 어둠 너머에서 새하얀 옷자락이 유령처럼 흩날린다.

어느덧 석탁 위를 가로질러 오 장에 달하는 거리를 지워 버린 그가 앉아 있던 내 정수리를 향해 일권(一拳)을 내리찍으려던 그 순간.

“선을 넘으시네, 또.”

나는 낮은 뇌까림과 함께 손바닥을 쳐올리듯 내뻗었다.

화륵.

화염신장(火焰神掌).

어둠을 살라 먹으며 타오른 화염이, 눈부신 강기가 서린 백상의 일권과 맞닿는다.

각각 희고 푸른 기운이 뒤섞이며 터져 나온 섬광이 사방을 뒤흔들었다.

콰앙! 구구궁!

내리꽂히는 일권과 쳐올리는 일장. 노인과 청년. 원초적이며 순수한 힘의 충돌.

거센 진동과 굉음이 대전을 뒤흔들었고, 나는 똑똑히 볼 수 있었다.

화아아악!

맞닿은 일점(一點)을 중심으로 폭발하듯 흘러나온 광휘 너머, 크게 뜨인 한 쌍의 눈동자를.

“……!”

언제나 서늘한 빛을 발하던 백상의 눈동자에는 감출 수 없는 놀라움이 서려 있었다.

어떻게?

낯익은 감정. 익숙한 눈빛이다.

지금까지 나와 마주친 이들 중 대부분이 마찬가지였으니까.

그들은 내 이름과 별호가 무림에 알려지기 시작한 이전에도, 그리고 이후에도 간혹 그 사실을 망각한 듯 때 이른 과소평가를 내리고는 했다.

나이가 어려서. 출신 가문이 한미해서. 혹은 전란(戰亂)을 겪어 보지 못한 애송이라서.

그리고 그런 일이 생길 때마다 나는 친절하게 알려 주었다.

말이 아닌 힘으로.

‘바로 지금처럼.’

입 밖으로 새어 나가지 않은 뇌까림과 함께, 나는 전신에 충만한 기운을 한층 더 강하게 끌어올렸다.

콰아아아!

자그마치 삼 갑자에 달하는 강대한 공력이 기지개를 켜며 일어난다.

열양지기가 뿜어내는 끔찍한 열기에 주위의 수분이 증발하고 붉은 아지랑이가 피어올랐다.

츠츠츠츠!

활짝 펼친 손바닥에 가로막혀 있던 주먹이 서서히 밀려 나가기 시작했다.

파르르 떨리는 백상의 눈동자에, 타들어 가는 그의 새하얀 옷자락과 담담한 내 얼굴이 차례대로 스친다.

열기에 쩍쩍 갈라진 백상의 입술 사이로 서늘한 목소리가 흘러나왔다.

“네놈…….”

대단한 평정심이다. 보통 이런 상황에서 내가 들었던 말 중 대부분은 씨발놈, 개새끼, 미친놈이었으니까.

그러나 백전(百戰)을 치르며 단련된 것일까. 아니면 수만의 부족민을 이끄는 대족장이기 때문일까.

백상의 감정은 출렁일지언정 흘러넘치지 않았고, 그의 무위는 내가 생각한 것 이상으로 뛰어났다.

스슥!

까맣게 타들어 간 옷깃이 팔뚝을 스친다. 어느새 굳게 말아쥐고 있던 주먹이, 매의 발톱처럼 펼쳐져 섬광 같은 속도로 내 손목을 움켜쥐었다.

아니, 아마도 틀림없이 움켜쥐었을 것이다.

내 움직임이 그보다 더 빠르고, 강하지 않았다면.

콰득!

이미 인간의 한계를 아득히 벗어난 힘.

무시무시한 악력으로 손목을 조이자, 고통을 느낀 백상의 눈썹이 움찔 떨리며 짧은 신음이 튀어나왔다.

“흡!”

그리고 나는 그 찰나의 빈틈을 놓치지 않았다.

‘지금.’

백상의 손목을 옆으로 틀어 다른 한 손을 봉함과 동시에 중심을 흐트린 다음, 남은 한 손으로 옆구리를 향해 일장(一掌).

퍼엉!

나는 둔중한 파공음이 들리기도 전에 그의 손목을 놔주었다.

수십여 쌍의 시선이 지켜보는 앞에서, 옆구리를 후려친 장력에 의해 튕겨 나간 백상이 허공에서 몸을 틀어 석탁 위에 내려앉았다.

슥.

소리도 나지 않을 만큼 가벼운 몸놀림이었지만 표정은 정반대다.

그리고 무겁게 가라앉은 눈빛으로 나를 노려보던 백상이 재차 움직이려던 그때.

“그만.”

목소리는 크지 않았지만, 깊은 울림과 위엄이 담겨 있었다. 어느덧 자리에서 일어난 야수묘왕이 굳은 얼굴로 입을 열었다.

“물러서라. 두 사람 모두.”

백상의 신형이 흔들렸고, 나는 어깨를 으쓱해 보였다.

“전 안 움직였는데요.”

틀림없는 사실이다. 비록 의자를 좀 뒤로 빼긴 했지만, 먼저 쇄도한 것은 백상이었고 나는 앉은 채로 수를 주고받았을 뿐이었다.

그리고 결과는, 뭐.

귀신에 홀린 듯한 눈으로 나를 바라보는 다른 부족장들의 눈빛이 그 증거고 결과다.

“진태경.”

하지만 최소한의 처신 정도는 해야 했다. 이곳은 내 홈그라운드가 아닌 남만이고, 상대는 백족의 대족장이었으니까.

야수묘왕의 질책 어린 부름에 나는 양손을 들어 보였다.

“죄송합니다. 손을 쓰지 않을 수가 없던 상황이라 저도 모르게 그만.”

물론 그래도 짚고 넘어가긴 해야지.

백번 양보해서 문제의 발단은 나였을지 몰라도, 백상이 펼친 수는 자칫하면 절명에 이를 수 있는 위험한 공격이었다.

“……후우.”

내 말뜻을 알아들었는지, 나직한 한숨을 내쉰 야수묘왕의 시선이 다른 한 사람을 향해 움직였다.

“백상, 경거망동하지 말거라.”

차가운 눈동자에 갈등이 스친다.

등 뒤에서 들려온 야수묘왕의 부름에도 아무런 대답 없이 나를 응시하던 백상이 문득 주위를 둘러봤다.

서른 명이 넘는 부족장들.

그들의 반응은 세 갈래로 나뉘었다. 당장이라도 내게 달려들 것처럼 엉덩이를 들썩이는 이도 있었고, 웃음을 참는 듯 입가를 씰룩이는 자도 있었으며, 내 무위를 목격하고 반쯤 넋이 나간 이들도 있었다.

이건 남만야수궁 내에서 파벌이 존재한다는 증거였다.

그리고 모두가 지켜보는 앞에서 백상의 위상과 명성에는 쉽게 지울 수 없는 흠집이 새겨졌다.

다른 누구도 아닌, 바로 중원에서 온 한족 애송이에 의해서.

“…….”

그런 사실을 모를 리가 없는 백상이다. 입술을 지그시 깨문 그는 야수묘왕을 향해 고개를 숙였다. 억눌린 목소리와 함께.

“분란을 일으켜 송구합니다. 마음을 가라앉힌 후 다시 뵙지요.”

그리고는 곧장 까맣게 그을린 옷자락을 펄럭이며 대전을 빠져나갔다.

동시에 자연스럽게 일어난 요희가 그 뒤를 따랐고, 허둥지둥 움직이는 흑웅과 절반에 달하는 부족장들 역시 눈치를 살피며 자리에서 일어났다.

“궁주님, 송구하지만 그럼…….”

“가, 같이 갑시다.”

저들이 친(親) 백상파로 분류되는 이들일 것이다. 평범한 온건파와는 달리 무림맹 입맹을 결사반대하는 자들.

서른두 명의 부족장 중 대략 절반에 달하는 이들이 그렇게 자리를 비우자, 야율목은 분노로 미간을 찌푸렸고 야수묘왕은 피곤한 목소리로 중얼거렸다.

“결국 이 사달이 났군.”

내가 눈치를 살피며 입을 열었다.

“죄송합니다. 괜히 저 때문에 벌어진 일 같네요.”

“후우, 네가 사과할 일이 아니다. 언제고 터질 문제였지.”

“아하, 그럼 다행이고요. 사실 저도 그렇게 생각하긴 했습니다.”

“…….”

그 순간. 아직 남아 있던 부족장들은 물론이고 야율목과 야수묘왕까지 짜게 식은 눈빛으로 나를 바라봤다.

- 너 때문인 거 맞아. 이 새끼야.

뭐지, 환청인가? 분명히 전음은 아닌데.

희한한 현상에 고개를 갸웃거린 내가 재차 입을 열었다.

“혹시 대회의가 이대로 끝난 건 아니죠?”

“대회의는 축제와 더불어 사흘간 진행된다. 참석 전에 이미 들었을 텐데?”

“듣긴 했는데 혹시나 해서.”

내 천연덕스러운 대답에 야수묘왕이 고개를 절레절레 내저었다.

“꼭 그렇게까지 해야 했느냐?”

“그래도 지나치기에는 너무 찜찜했습니다. 진짜 반응도 궁금했고요.”

“그 호기심 때문에 넌 일만이 넘는 백족을 적으로 만들었다. 백상을 따르는 요희와 흑웅. 두 대족장과 다른 이들까지 합하면 남만의 절반이라고 해도 과언이 아니겠지.”

음. 남만의 절반이라.

“생각보다는 나쁘지 않네요.”

“뭐라?”

“한 이틀 전만 해도 남만 전체가 제 적이었거든요. 대회의는 뭐, 시작도 전에 쫓겨날 판이었고.”

“……허. 참.”

헛웃음을 흘린 야수묘왕이 남아 있던 부족장들에게 시선을 옮겼다.

“장 족장. 그리고 고 족장.”

“예.”

“이번에는 그대들이 도와줘야겠다. 우선은 발 빠른 전사들로 척후대를 꾸리고, 귀주 방면 쪽을 감시하도록.”

“혈승(血僧)이라는 자 때문입니까?”

고개를 끄덕인 야수묘왕이 재차 입을 열었다.

“백상과 진태경의 의견 모두 일리가 있다. 놈이 구태여 남만으로 향할 이유도 없지만, 암천의 인물이라면 그에 따른 대비를 해야 옳겠지.”

“궁주님의 명을 따르겠습니다.”

“존명.”

앞서 떠난 부족장들이 백상에게 속해 있다면, 남은 이들 중 대부분은 야수묘왕에게 충성을 바치거나 상당히 호의적인 중도파다.

중견 부족을 이끄는 두 족장이 묵묵히 명령을 따르자 야수묘왕의 얼굴이 조금은 펴졌다.

“오늘 밤. 희생당한 이들을 위한 위령비를 세우고 그들을 위한 연회를 열 것이다. 대회의는 그 후에 속행할 테니 지금은 이만 물러가도록.”



* * *



“어떻게 됐나?”

거처로 돌아오자마자 득달같이 달려온 남호가 물었다.

“혹시 또 사고를 친 건 아니겠지?”

의심이 가득 담긴 목소리. 내가 뭐라 대답하려던 그때, 혁무진이 버럭 역정을 냈다.

“이보시오. 남 노인! 감히 우리 조장님을 뭘로 보고!”

“뭘로 보긴 뭘로 봐. 미친놈으로 보지.”

“어허. 아무리 조장님이 미친놈이어도 그건 아니지! 다른 자리도 아니고 그토록 중요한 자리에서 사고를 치는 게 말이 된다고 생각하시오!”

“말이 된다고 생각한다. 충분히.”

양심이 찔린다면 정상인가.

나는 머뭇거리며 입을 열었다. 아니, 열려고 했다.

적어도 주화란이 참전하기 전까지는 그랬다.

“남 노야(老爺). 말이 너무 심하세요. 각주님이 미친놈이라니요.”

남호의 급격한 노화 원인이 태산이라면, 유일한 약점은 바로 주화란이다.

그녀의 등장에 조금 전까지만 하더라도 당당하던 남호가 듬성듬성한 정수리를 긁적였다.

“아니, 뭐. 그게.”

“우리 각주님은 무림맹을 대표하셔서 오신 분이에요. 물론 조금 거친 면이 있을 수는 있어도. 입맹을 성사시켜도 모자랄 판에 대회의처럼 중요한 자리에서 분란을 일으키실 분이 아니라고요.”

“…….”

제발 죽여 줘.

이제는 찔리다 못해 고통스러울 지경이다.

그사이 주화란은 열렬한 선거 지지자처럼 다른 이들에게까지 동의 표를 구하고 있었다.

“다들 어떻게 생각하세요? 왜 대답이 없으시죠?”

언제나처럼 조용하던 송일섬이 입맛을 다셨다.

“음. 소국주. 아무래도 그건 당사자의 대답을 들어본 후에…….”

“특별 수당 추가.”

“다시 생각해 보니 맞는 것 같소. 각주가 그럴 리 없지.”

돈에 미친 새끼 컷.

“다른 두 분은 왜 말이 없으시죠?”

“태산이. 배고프…….”

“저녁에 연회가 열린다던데.”

“태산이. 주 소저 말씀에 매우 동의한다.”

“……나도 동의하오.”

식충이 컷. 씹어먹어도 시원치 않을 전 약혼자 컷.

지지 서명 운동은 전광석화처럼 진행되었고, 주화란은 은하수처럼 반짝이는 눈동자로 나를 바라보았다.

“각주님도 뭐라고 한 말씀 해 보세요. 그래서, 입맹하기로 한 건가요?”

일 초가 한 시간 같다.

나는 긴 침묵 끝에 입을 열었다.

“저기. 여러분. 음. 그게. 그…… 사소한 문제가 있었습니다.”

주화란은 얼어붙었고, 남호는 그럴 줄 알았다는 듯 고개를 끄덕였다.

“이거 봐. 미친 각주놈.”

“…….”

“죽였나?”

“아뇨.”

“그럼 때렸군.”

“…….”

“누구야? 멋모르고 덤빈 어느 부족장? 아니면 거슬리는 말을 한 다른 누군가? 설마하니 백족의 대족장은 아니겠지.”

“아.”

“각주님?”

“…….”

“……각주님?”

조금씩 흐려지는 주화란의 목소리에 나는 굳게 입을 다문 채 먼 산을 바라봤고, 남호가 허허 웃으며 입을 열었다.

“거봐. 미친 새끼 맞잖아.”
```

## Final English reading copy

```markdown
# Chapter 645

Who had crossed the line first?

Me? Or Baeksang?

And among the words he and I had exchanged, which had been true and which had been lies?

Several questions flashed through my mind in that brief moment, but they no longer mattered.

From this point on, it was time for true martial artists to settle the result with nothing but force.

*Whoosh!*

A sharp sound of something slicing through the air pierced my ears.

Before I could even hear it properly, I twisted my head aside and dodged the Finger Qi flying toward me. Without a moment’s hesitation, I braced one hand against the stone table in front of me.

*Boom!*

The table, carved from a massive boulder, trembled.

At the same time, thirty-three wine cups sprang into the air as though they had been bounced upward. I smoothly thrust out my hand and knocked several of them away.

*Thwack.*

Toward one person alone.

Baeksang.

*Whoosh-whoosh-whoosh!*

They were nothing more than crude wooden cups that had been roughly carved, but the moment they were filled with the internal energy I had sent into them, they transformed into terrifying weapons.

They flew faster than arrows and possessed enough destructive force to shatter stone.

But my opponent was calm—and before he was calm, he was strong.

*Whoomph! Slash!*

Baeksang swung his straightened hand blade horizontally. Invisible, intangible qi split through the air and sliced apart the cups flying toward him.

Before the fragments of the cups, shattered after losing their momentum, could even reach the ground, Baeksang’s body shot upward from his seat and blurred.

*Papapat!*

Beyond the darkness that had settled over the main hall, the hem of his white robes fluttered like a ghost.

In the time it took him to cross the stone table and erase a distance of nearly five zhang, he raised one fist to drive it down onto the crown of my head.

“You’re crossing the line again.”

As I muttered those words under my breath, I thrust my palm upward.

*Fwoosh!*

Flame Divine Palm.

The flames blazing as they devoured the darkness met Baeksang’s fist, which was wrapped in dazzling Force.

The white and blue energies tangled together, then exploded in a flash of light that shook the entire hall.

*Boom! Rumble-rumble!*

A descending fist and an upward palm.

An old man and a young man.

A collision of raw, pure strength.

The violent tremors and thunderous roar rocked the main hall, and I saw it clearly.

*Fwoosh!*

Beyond the radiance that burst outward from the single point where our attacks met, I saw a pair of eyes opened wide.

“……!”

Baeksang’s eyes, which had always shone with a cool light, held unmistakable surprise.

*How?*

It was a familiar emotion. A familiar look.

Most of the people I had faced until now had made the same expression.

Before my name and sobriquet had begun spreading through the Murim, and even afterward, they would sometimes seem to forget that fact and underestimate me too soon.

Because I was young.

Because my family was insignificant.

Or because I was an inexperienced brat who had never experienced war.

And whenever that happened, I kindly taught them the truth.

Not with words, but with force.

*Just like now.*

Along with the mutter that never escaped my lips, I drew up the energy filling my entire body even more forcefully.

*Waaaaaah!*

The tremendous internal energy of no less than three jiazi stirred to life and stretched.

The terrible heat radiating from the Scorching Yang Qi evaporated the moisture in the surroundings, and red heat haze rose into the air.

*Tsss-tsss-tsss!*

The fist blocked by my fully opened palm began to be pushed backward little by little.

In Baeksang’s trembling eyes, his burning white robes and my calm face appeared in turn.

A cool voice flowed between Baeksang’s lips, cracked from the heat.

“You bastard……”

What remarkable composure.

Most of the things I had heard from people in situations like this were usually “fucking bastard,” “son of a bitch,” or “crazy bastard.”

But whether he had been tempered by a hundred battles or because he was the great chieftain leading tens of thousands of tribespeople, Baeksang’s emotions might have surged, but they never overflowed.

And his martial prowess was far greater than I had expected.

*Swish!*

A blackened collar brushed against my forearm. At some point, the fist he had clenched tightly had spread open like an eagle’s talons and seized my wrist with lightning speed.

No, he almost certainly would have seized it.

If my movements had not been faster and stronger than his.

*Crack!*

This was strength that had already gone far beyond the limits of a human being.

When I tightened my grip around his wrist with terrifying force, Baeksang’s brow twitched from the pain, and a short groan escaped him.

“Ghk!”

And I did not miss that brief opening.

*Now.*

I twisted Baeksang’s wrist aside, simultaneously pinning his other hand and throwing him off balance. Then I struck his flank with my free palm.

*Thud!*

Before the heavy sound of something tearing through the air could even reach my ears, I released his wrist.

In front of dozens of pairs of watching eyes, the palm strike to his side sent Baeksang flying. He twisted his body in midair and landed on the stone table.

*Swish.*

His movement had been light enough not to make a sound, but his expression was the exact opposite.

Just as Baeksang glared at me with heavily lowered eyes and moved to attack again—

“Enough.”

The voice was not loud, but it held a deep resonance and authority. The Beast Miao King had risen from his seat and opened his mouth with a hard expression.

“Stand down. Both of you.”

Baeksang’s figure wavered, while I shrugged.

“I didn’t move.”

That was an undeniable fact. I had pulled my chair back a little, but Baeksang had been the one to charge first. I had exchanged moves with him while remaining seated.

And the result was, well……

The other chieftains were staring at me as though they had seen a ghost.

Their eyes were proof enough.

The result, too.

“Jin Taekyung.”

I did need to show at least a minimum degree of propriety. This was Nanman, not my home ground, and my opponent was the great chieftain of the Bai people.

At the Beast Miao King’s reproachful call, I raised both hands.

“I’m sorry. It was a situation where I couldn’t help using my hands. I just acted without thinking.”

Of course, I still had to make one thing clear.

Even if I conceded that I might have started the whole thing, Baeksang’s attack had still been dangerous enough to kill me.

“……Hoo.”

Perhaps he understood what I meant. The Beast Miao King let out a quiet sigh and turned his gaze toward the other man.

“Baeksang, do not act rashly.”

Conflict flickered in Baeksang’s cold eyes.

Without answering the Beast Miao King’s call from behind him, Baeksang continued to stare at me. Then he suddenly looked around.

More than thirty chieftains.

Their reactions were divided into three camps. Some shifted in their seats as though they might rush at me at any moment. Some twitched at the corners of their mouths, as if trying to hold back laughter. Others, after witnessing my martial prowess, looked half dazed.

This was proof that factions existed within the Nanman Beast Palace.

And before everyone’s eyes, Baeksang’s standing and Fame had suffered a blemish that would not be easily erased.

By none other than a Han Chinese brat from the Central Plains.

“……”

Baeksang could not have been unaware of that fact. He pressed his lips together, then bowed his head toward the Beast Miao King.

His voice was restrained.

“I apologize for causing a disturbance. I will see you again after I have calmed my mind.”

With that, he immediately left the main hall, his blackened robes fluttering behind him.

Yohi rose naturally and followed him. Heugung also hurried after them, while nearly half the chieftains rose from their seats after carefully watching the situation.

“Palace Lord, I’m sorry, but then……”

“Let’s go together.”

They were probably the people who belonged to the pro-Baeksang faction. Unlike the ordinary moderates, they were the ones who absolutely opposed Nanman joining the Murim Alliance.

When roughly half of the thirty-two chieftains left, Yayul Mok knitted his brows in anger, while the Beast Miao King muttered in a weary voice.

“So this is how it ended up.”

I watched the Beast Miao King’s expression and cautiously opened my mouth.

“I’m sorry. It seems this happened because of me.”

“Hoo. This is not something you need to apologize for. It was a problem that was bound to explode sooner or later.”

“Ah, then that’s a relief. To be honest, I thought so too.”

“……”

At that moment, not only the chieftains who remained but also Yayul Mok and the Beast Miao King looked at me with utterly dead eyes.

—It’s definitely because of you, you bastard.

*What? An auditory hallucination? It definitely wasn’t Sound Transmission.*

Baffled by the strange phenomenon, I tilted my head and spoke again.

“The grand council isn’t over just like this, is it?”

“The grand council will continue for three days along with the festival. You must have heard that before attending.”

“I did hear it, but I thought I’d ask just in case.”

At my shameless answer, the Beast Miao King slowly shook his head.

“Did you really have to take it that far?”

“Still, it felt too suspicious to just let it go. I was curious about his genuine reaction too.”

“Because of that curiosity, you made more than ten thousand members of the Bai people your enemies. If you include Yohi and Heugung, the two great chieftains who follow Baeksang, along with the others, it would not be an exaggeration to say that half of Nanman is now against you.”

*Hmm. Half of Nanman.*

“That’s not as bad as I expected.”

“What?”

“Just two days ago, all of Nanman was my enemy. I was about to be kicked out before the grand council even started.”

“……Huh. Well, I’ll be damned.”

The Beast Miao King gave a hollow laugh, then shifted his gaze to the chieftains who remained.

“Chief Jang. And Chief Go.”

“Yes.”

“This time, I will need your help. First, organize a scouting party of fast-moving warriors and have them watch the area toward Guizhou.”

“Is this because of the Blood Monk?”

The Beast Miao King nodded and continued.

“Both Baeksang’s and Jin Taekyung’s opinions have merit. There is no reason for him to deliberately head toward Nanman, but if he is a man of Dark Heaven, then we would be wise to prepare accordingly.”

“We will obey your command, Palace Lord.”

“As you command.”

If the chieftains who had left earlier belonged to Baeksang, most of those who remained either pledged their loyalty to the Beast Miao King or belonged to the moderates who were quite favorably disposed toward him.

When the two chieftains who led middle-sized tribes silently obeyed his command, the Beast Miao King’s expression relaxed slightly.

“Tonight, we will erect a memorial stele for those who lost their lives and hold a banquet in their honor. The grand council will resume afterward, so you may withdraw for now.”

* * *

“What happened?”

The moment we returned to our quarters, Namho came charging over and asked.

“You didn’t cause another incident, did you?”

His voice was filled with suspicion. Just as I was about to answer, Hyuk Mujin erupted in anger.

“Look here, old man Nam! What do you take our Captain for?”

“What else would I take him for? A lunatic.”

“What? Even if our Captain is a lunatic, he wouldn’t do that! Do you really think it makes sense for him to cause a scene at such an important place, of all places?”

“I think it makes perfect sense.”

*If I feel guilty, does that mean I’m normal?*

I hesitated before opening my mouth.

No, I was about to open it.

At least, I was until Ju Hwaran joined the battle.

“Elder Namho, that’s too harsh. How can you call our Pavilion Master a lunatic?”

If Taishan was the reason Namho had aged so rapidly, then Ju Hwaran was his only weakness.

At her appearance, Namho, who had been so bold just moments earlier, scratched at his thinning crown.

“No, well. That’s……”

“Our Pavilion Master came here representing the Murim Alliance. He may be a little rough around the edges, of course, but when he should be doing everything possible to secure Nanman’s entry into the alliance, he isn’t the kind of person who would cause a disturbance at a gathering as important as the grand council.”

“……”

*Please, kill me.*

My conscience was not merely pricking anymore. It was actually painful.

Meanwhile, Ju Hwaran was asking everyone else for their votes like an enthusiastic campaigner.

“What does everyone else think? Why aren’t you answering?”

Song Ilseom, who was always quiet, smacked his lips.

“Hmm. Young Bureau Head, surely we should hear the person in question’s answer first……”

“Add a special bonus.”

“On second thought, I think you’re right. There’s no way our Pavilion Master would do that.”

*Money-crazed bastard—out.*

“Why are the other two of you silent?”

“Taishan. Hungry……”

“I heard there’s a banquet tonight.”

“Taishan. Strongly agrees with what Young Lady Ju said.”

“……I agree as well.”

*Glutton—out. Former fiancé I could chew to bits and still not feel satisfied—out.*

The petition drive proceeded with the speed of Quick Attack, and Ju Hwaran looked at me with eyes sparkling like the Milky Way.

“Pavilion Master, say something too. So, have they decided to join the alliance?”

One second felt like an hour.

After a long silence, I finally opened my mouth.

“Um. Everyone. Well. There was, uh…… a minor problem.”

Ju Hwaran froze, while Namho nodded as though he had expected it.

“See? Crazy Pavilion Master.”

“……”

“Did you kill someone?”

“No.”

“Then you beat someone up.”

“……”

“Who was it? Some chieftain who recklessly picked a fight without knowing better? Or someone else who said something irritating? Surely it wasn’t the great chieftain of the Bai people.”

“Ah.”

“Pavilion Master?”

“……”

“……Pavilion Master?”

As Ju Hwaran’s voice gradually faded, I kept my mouth firmly shut and gazed at a distant mountain.

Namho chuckled and said,

“See? Crazy bastard.”
```
