<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0723.txt",
      "sha256": "dc66121b0496eb9eb953fbf6b8828c6cb7a5d5a38210328bc74dda2eee770a3c",
      "bytes": 14528
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b9d18e9bbb2170243dfaf8f686cd1f12321520b930ede1e1f45847de369c8346",
      "bytes": 2065
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4a46cd799a59ed789d120031db670abbf4a71de47752c7ca66f24f3ec2458932",
      "bytes": 209329
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "1d003ccdf0c3bed7d5de85508d73216c111f38d4b312e793787a1b091d00144a",
      "bytes": 935
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "0c1f8389271cf0a37c226fe7db923110a7a1fc76a1888e82c867fda9ea0945f8",
      "bytes": 968
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "cf5281ea862615031edb9a8b328ce48b7b7f7d4834a46335ba4fa2db77b7b2ef",
      "bytes": 553
    },
    {
      "path": "characters/Hanga.md",
      "sha256": "7882f1bada8f5e464c21b098fd9244d29da3301944c39fe718013c64cd4e3d91",
      "bytes": 568
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "5fba310e5450ce91870c75e297fd0b954a0c333511c79d81d46ea4631d2daedf",
      "bytes": 784
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "6a806de0c8dff7d7839c353a02b1c354118ec8d34882bf1e91694679f48dd334",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "86ca50aaed66ae080f69c6c9c4cc81bc7d0406c2fa740afaa7bd17750ec67c5b",
      "bytes": 1787
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "afdfbda0db19e533bed9374a045bac04b34502a4aea5bdd0a9561df2f53b7817",
      "bytes": 622
    },
    {
      "path": "characters/Namho.md",
      "sha256": "620b4a9de63843f8872383e4703847a4ba57af590a5cd30728250dbf0fce7b59",
      "bytes": 843
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "7b5803056eff2fdde70e845544ce08eb8ed597a4d967271aa9559c2583136930",
      "bytes": 787
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "8b71b930dcfb195433e8b7dd23584000c4e7d5fc7326aaabff625d664bc9d5c1",
      "bytes": 899
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "c243b285a72dbb9a311c359d0f8566040929f2102086da17d3b2a9b9b4342b95",
      "bytes": 925
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "4dabe1abb8131965554ad97d987fc9e0817ef581bb8269194b45c05ce5fb9342",
      "bytes": 659
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9dea8b4187f83ff9e3ad17cb4601943617d80ed52fb46c971ef5bc835fdcdfc6",
      "bytes": 219534
    }
  ],
  "estimated_tokens": 15164
}
-->

# Durable State Update — Chapter 723

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 723. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 723. Profile updates may replace only one
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
  "chapter": 723,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 723,
    "continuity_sources": [723],
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
    "The Sacred Land is distinct from the Poisonblood Grounds and is Nanman's life-filled heart.",
    "The Sacred Land's Pond of Life heals living bodies and purifies evil or impure energy.",
    "The corrupted sacred artifact was purified in the Pond of Life and became a new sacred stone that remains in Nanman.",
    "The Pond of Life released its remaining life energy as healing rain across Nanman, which also caused flowers and sprouts to bloom.",
    "Muyaho is the new guardian spirit of the sacred stone and is affectionate toward Jin Taekyung.",
    "The Nanman Beast Palace is being rebuilt after the Inner Palace's devastation and the Outer Palace's heavy damage.",
    "The Earth Mother Goddess is now Nanman's public supreme deity, and the Beast Miao King is her sole publicly recognized priest.",
    "The Beast Miao King is using the Earth Mother Goddess's faith to unify and reform Nanman.",
    "The old local gods have been placed beneath the Earth Mother Goddess's authority, and a scripture for the new religious system is being planned.",
    "The traitorous tribal chieftains were publicly executed after ten days in the underground prison.",
    "The formerly divided thirty-two tribes now publicly regard themselves as one united Nanman people.",
    "Nanman's people are openly preparing for the coming Great War."
  ],
  "continuity_sources": [
    721,
    722
  ],
  "open_questions": [
    "How will Muyaho's new role as guardian spirit develop?",
    "When will the Pond of Life recover its lost energy?",
    "How will Nanman's new religious system and scripture develop?",
    "How will the newly unified Nanman respond when the Great War arrives?"
  ],
  "safe_through": 722,
  "temporary_decisions": [
    "Render 대지모신 as Earth Mother Goddess.",
    "Render 목신 as Wood God and 화신 as Fire God.",
    "Render 제사장 as priest when used for the Beast Miao King.",
    "Render 알쓸잡신 as useless gods.",
    "Render 성우 as Sacred Rain and 성경 as Bible."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 일신     | **One God**         |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 칭호               | **Title**                      |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 화룡각주 | **Fire Dragon Pavilion Master** | Unique Title awarded to Jin Taekyung. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 소궁주 | **Young Palace Lord** | Title used for Yayul Mok as heir of the Nanman Beast Palace. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 북문 | **North Gate** | The gate where Jin Taekyung and Yohi arrive. |
| 대지모신 | **Earth Mother Goddess** | New deity proclaimed by Jin Taekyung as Nanman's One God. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 성우 | **Sacred Rain** | Name later given to the rain released as the Earth Mother Goddess's blessing. |
| 성경 | **Bible** | Proposed scripture containing Nanman's history and the word of God. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 항아 | visiting_adult_to_local_child | little one | friendly and coaxing | Questions Hanga and offers food in exchange for information. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 야율목 | 야율척 | Young_Palace_Lord_to_Palace_Lord | Palace Lord | ceremonial and deferential | Yayul Mok kneels with his guards and formally greets Yayul Cheok upon his arrival. |
| 야율척 | 야율목 | Palace_Lord_to_Young_Palace_Lord | Mok | authoritative and familiar | Yayul Cheok questions Mok's unannounced departure and later addresses him as 목아 while discussing Nanman's tribes. |
| 야율척 | 진태경 | Nanman_Beast_Palace_Palace_Lord_to_Jeok_Cheongang's_Disciple | you / Disciple of Old Master Jeok / Jin Taekyung | rough, testing, and later welcoming | Yayul Cheok questions Taekyung as a suspected culprit, strikes him as a test, and then welcomes him after recognizing Jeok's Disciple. |
| 진태경 | 야율척 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Palace_Lord | Great Hero Yayul Cheok | formal and deferential | Taekyung gives Yayul Cheok a formal greeting as the nineteenth successor of the Fire Gate Clan. |
| 야율척 | 남호 | Palace_Lord_to_Hidden_Shadow_Pavilion_agent_and_guest | old man | blunt and inquisitive | Yayul Cheok calls on the old man beside Taishan to identify him. |
| 야율척 | 태산 | Palace_Lord_to_Fire_Dragon_Pavilion_member | you | puzzled and blunt | Yayul Cheok asks Taishan, standing beside Hwaran, to identify him, receiving only Taishan's declaration that he is hungry. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
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
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |
| 백상 | 부족장 | Palace Lord to subordinate tribal chieftain | you | cold, final, and detached | Baeksang refuses the chieftain's plea for mercy and tells him not to consider the exchange unjust. |
| 야수묘왕 | 적천강 | junior allied master to legendary senior martial master | Old Master Jeok | formal-deferential | The Beast Miao King respectfully addresses Jeok while asking him to sit and consulting him about the demonic stone. |
| 적천강 | 야수묘왕 | senior allied martial master to Nanman Beast Palace Lord | you | blunt, commanding, and mocking | Jeok orders the Beast Miao King to stand aside and mocks his inability to destroy the corrupted artifact. |
| 부족장 | 야수묘왕 | subordinate tribal chieftain to Nanman Beast Palace Lord | Palace Lord | urgent, deferential, and confrontational | The attending tribal chieftains repeatedly address the Beast Miao King as 궁주 while challenging or supporting the Earth Mother Goddess doctrine. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 722
- **Aliases:** None
- **Role:** Baeksang was the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman, and he died by the Beast Miao King's hand after confessing to serving Dark Heaven's plan.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of Baekhwi, whom he believed the Great Snow Fiend killed but Dark Heaven has kept alive in a deep sleep; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 722
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, Great Chieftain of the Miao people who has resumed leadership of Nanman after the rift disaster, the publicly recognized sole priest of the Earth Mother Goddess, and the leader of Nanman's religious unification and reform.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang was his sworn younger brother and childhood companion, and the Beast Miao King killed him at his request; Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple and ally.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 722
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hanga.md

# Hanga (항아)

- **Safe through:** Chapter 636
- **Aliases:** None
- **Role:** Local village girl, Jang-pal’s daughter, who lives near Jang Taebo and regularly visits him.
- **Personality:** Curious, energetic, observant, and already attentive to the value of information and food.
- **Voice:** Childlike, direct, and inquisitive, with an occasional surprisingly worldly remark.
- **Relationships:** Calls Jang Taebo Grandpa; Jang Taebo is his elderly neighbor and only conversational companion.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 692
- **Aliases:** Beast Miao King
- **Role:** Heugung is the secret identity of the Beast Miao King, a Supreme Peak master and long-term Dark Heaven contingency who concealed himself through the Bone-Shrinking Technique.
- **Personality:** Heugung is calculating, patient, ruthless, and obsessive, masking coercion and strategic intent behind warmth and romantic devotion toward Yohi.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung is obsessed with Yohi and is willing to threaten her and the Yao people to force her compliance while secretly serving the Southern Heaven Demon Empress.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 722
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 721
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 721
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 717
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 716
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 708
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty former Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 717
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger and speaks Han Chinese haltingly but capably; he is currently occupied with rebuilding the damaged Palace.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and his father, Baeksang is his father's sworn younger brother, and Yayul Mok has risked his position and life to rescue Jin Taekyung, entrusting Muyaho to Jin while he remains behind with the Seven Miao Tigers.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 720
- **Aliases:** None
- **Role:** Yohi is the female Great Chieftain of the Yao people who returned to the Nanman Beast Palace with Jin Taekyung and voluntarily entered the underground prison after siding with Baeksang.
- **Personality:** Yohi is charismatic, proud, perceptive, and fiercely resistant to Heugung's betrayal and coercion.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, hates Heugung after his betrayal, and is being coerced to support his false account by the threat against Boshan and her people.

## Korean source

```text
＃723화



하루. 이틀. 그리고 사흘.

어느덧 성우(聖雨)라 명명된 빗줄기는 지금도 남만 전역을 적시고 있었고, 자애로우신 대지모신의 은총 아래 하나가 된 남만인들을 막을 수 있는 것은 아무것도 없었다.

쿵, 쩌저적!

중늙은이의 도끼질 한 번에 아름드리나무가 꺾이고, 마른 체구의 여인이 산더미처럼 쌓인 장작을 아무렇지 않게 번쩍 들어 올린다.

창가에서 그 모든 광경을 지켜보던 나는 작게 중얼거렸다.

“이야, 버프 오지게 받았네.”

“버, 뭐?”

곧장 돌아오는 반문. 이미 불청객의 존재를 알고 있던 나는 돌아서며 대답했다.

“별거 아냐. 그런데 무슨 일이냐? 지금쯤이면 한창 정신없어야 할 놈이.”

“지나가는 길에 들렀다. 그리고 이제는 전처럼 바쁘지도 않아. 모든 것이 눈 깜짝할 사이에 수습되고 있지.”

“그래?”

불청객치고는 꽤 반가운 얼굴이다. 나는 남만야수궁의 소궁주, 야율목을 바라보며 말을 이었다.

“그거 좋은 소식이네. 누구 덕분이래?”

내 물음에 야율목이 어깨를 으쓱해 보였다.

“아버님께 듣기로는 어느 한족 덕분이라는데. 아마 착각하신 거겠지.”

“글쎄. 내가 아는 바에 의하면 착각이 아닐 텐데.”

“아니, 착각이다. 비열하기 짝이 없는 한족이 우리를 도울 리 없으니까.”

“하긴 원래 중원에서 온 놈들이 다 그렇지. 도무지 믿을 수가 없어.”

“이제야 좀 말이 통하는군.”

짧은 침묵이 흘렀고, 우리는 약속이라도 한 듯이 동시에 피식 실소를 흘렸다.

“모두 네 덕분이다, 진태경.”

“다 같이 고생하긴 했는데, 사실 맞아. 내 공이 크긴 했지.”

내 천연덕스러운 대답에 야율목의 입가에 맺혀 있던 웃음이 한층 더 짙어졌다.

“한족들은 다 너처럼 겸손을 모르는 성격인가?”

“아니, 나만.”

“다행이군.”

“왜?”

“한족들을 지금보다 더 좋아할 수 있을 것 같거든.”

“오…….”

나는 새삼스러운 눈빛으로 야율목을 바라봤다.

녀석이 저런 말을 할 줄이야.

그전부터 조금씩 느끼긴 했지만, 중원에 대한 적대감으로 가득하던 모습은 더 이상 찾아볼 수 없었다.

“너무 좋아하진 마라. 막상 가 보면 미친놈들 많다.”

“어린애 취급하는군. 사람 사는 곳이라면 어디나 엇비슷하다는 것쯤은 알고 있다. 남만도, 중원도.”

“그래? 처음 만났을 때만 해도 몰랐던 것 같은데?”

“……그건 네놈이 들판을 불바다로 만들었으니까 그런 거고.”

과거 자신의 모습이 생각났는지, 약간 머쓱한 얼굴로 대답한 야율목이 내가 서 있는 창가로 다가왔다.

반쯤 열린 창문 사이로 보이는 광경을 응시하던 녀석이 불쑥 입을 열었다.

“아직도 실감이 안 나는군. 내가 평생을 나고 자란 곳에서 이런 일이 벌어졌다는 것이.”

“재앙? 아니면 기적?”

“둘 다.”

짤막하게 대답한 야율목이 한 마디를 덧붙였다.

“하지만 이 역시 신의 뜻이겠지.”

“……너도 대지모신 믿냐?”

“글쎄. 적어도 신이 존재한다는 것은 믿는다. 그렇지 않고서야 설명할 수 없는 일을 겪었으니까.”

불가해(不可解)의 영역을 접한 인간은 누구나 신을 떠올리기 마련이다.

저 까마득히 높은 하늘 위에 누가 있는지는 몰라도, 필시 대단한 양반이겠구나 하고 짐작하는 거다.

‘그건 나도 마찬가지고.’

뒷말을 삼킨 나는 자연스럽게 화제를 돌렸다.

“그래서, 뒤처리는 잘하고 있고?”

“수복 작업을 말하는 거라면 이미 마무리 단계에 접어들었다. 늦어도 수일 이내에 최종 성과가 나오겠지.”

내궁이 초토화되고, 외궁에서만 수백 채가 넘는 가옥과 전각이 무너졌다는 걸 생각하면 실로 기함할 만한 속도.

그러나 나는 놀라는 대신 작게 고개를 끄덕였다.

‘뭐, 버프가 워낙 끝내주니까.’

지금 이 순간에도 내리고 있는 저 빗줄기에는 생명과 정화의 힘이 담겨 있다.

끊임없는 활력을 불어넣어 주는 데다가 신체 능력까지 올려 주는 범위형 버프다.

‘물론 비가 그치면 효력도 끝나겠지만, 그 며칠만으로도 충분하지.’

옛말에 백지장도 맞들면 낫다는데, 이번에는 무려 수만에 달하는 남만인들이 밤낮을 가리지 않고 수복 작업을 이어 가고 있다.

자신들의 터전을, 고향을 새롭게 일구기 위해서.

그리고 그런 그들의 노력은 엄청난 속도로 결실을 이뤄 내고 있었다.

“다른 쪽은?”

내 물음에 담긴 뜻을 알아차린 야율목이 대답했다.

“남아 있을 부족 간의 우위와 경계를 없애기 위해 대족장 제도를 폐지했다. 우리 묘족은 물론이고 다른 사대 부족의 동의를 모두 얻었지.”

“잘했네. 아, 그렇게 되면 요희도?”

야율목이 고개를 끄덕였다.

“가장 먼저 대족장 폐지를 주장한 이가 그녀였다.”

백상과 손을 잡았던 부족장들은 수많은 이들이 지켜보는 앞에서 처형당했지만, 요희 만큼은 유일하게 면죄부를 받을 수 있었다.

뒤늦게나마 자신의 과오를 뉘우친 점. 그리고 결정적으로 맹수들을 이끌고 외궁의 부족민들을 피신시키는 데에 상당히 중요한 역할을 했기 때문에 그녀의 사면(赦免)에 관해서는 별다른 이의가 제기되지 않았다고 했다.

“백상이나 흑웅, 그리고 자신과 같은 선례(先例)를 남길 수는 없다는 말을 하더군.”

“맞는 말이지. 그전에는 대족장들의 힘이 너무 컸으니까.”

“아버님을 포함한 다른 부족장들도 동의하셨다. 이번 일로 우리 남만야수궁은 궁주 일인 체제로 움직일 것이며, 만일의 사태를 대비하여 대회의는 존속될 것이다. 그리고…….”

이어지는 야율목의 이야기를 들은 나는, 다시 한번 남만야수궁이 새롭게 거듭났음을 깨달았다.

궁주에 제사장까지 겸하게 된 야수묘왕의 권위는 전과 비교할 수 없이 강력해졌고, 불안하던 민심은 대지모신의 등장과 함께 안정을 되찾았으며, 사람들은 부족과 신앙을 떠나 하나로 뭉쳤다.

남만야수궁이 탄생한 이래 수백여 년간 서른두 조각으로 나뉘어 있던 이 땅의 균형이 마침내 하나로 단결(團結)된 것이다.

‘이 정도면 정말 소왕국(小王國)이라 불러도 되겠는데.’

자그마치 수만을 헤아리는 부족민과 일만에 달하는 전사.

그리고 그들이 부리는 맹수들까지 생각한다면 결코 과장이 아니다.

비록 남만 전사들의 수준이 중원 무림의 무학(武學)에 비해 떨어진다는 것을 감안하더라도 엄청난 전력.

나는 새삼스러운 눈빛으로 야율목을 바라보았다.

“……왜 그런 눈으로 날 보는 거지?”

“아니, 지금 보니까 귀티가 좀 나는 것 같아서. 알고 보니 왕자님, 뭐 그런 거 있잖아.”

“……왕자?”

떨떠름한 목소리로 중얼거린 야율목이 문득 실소를 흘렸다.

“왜 웃냐. 지금 상황 보면 영 틀린 말도 아닌데.”

“생각해 보니 영광이라서.”

“뭐?”

“위대하신 대지모신의 사도(使徒)께서 왕자라 칭해 주시는데, 영광이 아니고 뭐겠나.”

“……?”

이건 또 무슨 소리야.

말을 이해하지 못해 눈을 깜빡거리는 내게, 야율목이 품에서 꺼낸 무언가를 건네주었다.

“받아라.”

“이건…….”

“모신전(母神傳)이라 부르기로 했다. 아버님께서 네게 전해 달라시더군.”

내가 얼떨떨한 마음으로 죽편(竹片) 꾸러미를 받아 든 그 순간.

띠링.



― [모신전]을 획득하셨습니다.

― [모신전]은 [대지모신]의 기록을 다룬 경전입니다.

― 누군가가 믿음을 가질 때, 신은 비로소 존재할 수 있습니다.

― [대지모신]이 [남만]의 유일신으로 알려집니다!

― [대지모신]을 따르는 수많은 신도들이 열광합니다!

― [모신전]의 기록에 따라, 당신의 이름이 새롭게 알려집니다!

― 이것까지 하는 놈이 있나 싶은 업적, [종교 개혁]을 달성하셨습니다!

-칭호, [대지모신의 사도]를 획득하셨습니다!



시스템 알림과 함께 허공을 가득 메우는 홀로그램 창들.

그 광경을 멍하니 지켜보던 나는 황급히 손에 든 죽편 꾸러미를 펼쳤다.

그리고 깨알처럼 적힌 기록을 읽은 뒤 어이가 없어 웃음을 터트렸다.

“뭐냐, 이거.”

내 반응을 본 야율목이 어깨를 으쓱였다.

“적힌 그대로다. 대지모신께서는 태고부터 이 땅과 함께하신 어머니 신으로서, 남만이 위기에 처할 때마다 친히 당신의 사도를 보내어 그들을 구하셨는데…….”

“그게 나다?”

“그렇지. 삼백 년 전에는 초대 궁주셨던 내 선조. 그리고 이백 년 전에는 네가 속해 있는 열화문의 당대 문주였고.”

그걸 이렇게 짜 맞출 줄이야.

물론 내가 몇 가지 힌트를 던져 준 건 사실이지만, 내 이름 석 자가 떡하니 박혀 있을 줄은 몰랐다.

아니, 정확히 말하자면 ‘우리’의 이름이.

차라락.

뒷부분까지 훑어보니 제법 익숙한 이름들이 등장한다.

적천강은 물론이고 화룡각 대원들, 심지어는 남호의 이름까지.

이거 명색이 성경 같은 건데 이래도 되는 건가.

“아무리 급조했다지만 어이가 없네. 이거 설정 짠 새끼 누구야?”

“아버님.”

“어쩐지 훌륭하더라. 어쩜 이리 설정을 촘촘하게 짜셨대?”

“…….”

나는 야율목의 시선을 외면하며 죽편을 품에 넣었다.

‘대지모신의 사도라.’

사주팔자에도 없던 신의 사도 노릇을 하게 됐지만, 기분이 썩 나쁘지는 않다.

아니, 지금 같은 상황에서는 오히려 큰 수확이었다.

‘남만인들이 중원인들에게 품고 있던 악감정이 희석될 테니까.’

마음속으로 뇌까리던 그때, 야율목이 불쑥 물었다.

“그래서, 준비는 다 끝났나?”

“응?”

“남만을 떠날 준비 말이다.”

“……!”

잠시 침묵하던 내가 입맛을 다셨다.

“눈치 빠르네.”

“모르면 이상하지.”

“어떻게 알았냐?”

“다른 이들은 둘째 치고 전날부터 그 덩치 큰 놈이 정신없이 음식을 챙기고 있었다. 먼 길이라도 떠나려는 사람처럼.”

덩치 큰 놈이면 말할 것도 없다. 범인의 정체를 짐작한 나는 한숨을 내쉬었다.

“태산이, 이 미친 새끼. 조용히 움직이라고 그렇게 말했는데.”

“네 스승이신 화왕 적천강 대협은 과실주를 다섯 항아리나 빼돌리시더군.”

“…….”

아, 제발. 노야.

눈을 질끈 감은 그때, 야율목의 목소리가 귓가를 파고들었다.

“떠나기 전에 인사 정도는 해야지. 모두 기다리고 있다.”



* * *



야율목이 말한 ‘모두’라는 두 글자가 절대 과장이 아니라는 것은, 북문(北門)에 가까워진 후에야 깨달았다.

‘이건.’

수천, 어쩌면 수만.

북문 밖, 생명의 힘이 담긴 소나기 덕분에 싱그러운 풀과 꽃으로 뒤덮인 들판을 가득 메운 수많은 인파들 사이로 익숙한 얼굴들이 보인다.

과실주 항아리가 실린 수레 앞에서 딴청을 피우는 적천강.

비장한 표정으로 양손에 고기를 든 태산이와 각각 맹수에 올라탄 화룡각 대원들.

그리고…….

“드디어 왔군.”

야수묘왕 야율척. 이 땅의 모든 남만인들을 대표하는 남만야수궁의 주인이 굳은 얼굴로 입을 열었다.

“왜 말도 없이 떠나려고 했느냐?”

나는 뒤통수를 긁적였다.

“말씀은 드리려고 했는데.”

“했는데?”

“그, 서신으로.”

“고작 서신으로?”

“아니, 워낙 바빠 보이셔서…….”

“그게 말이 된다고 생각하느냐?”

“…….”

이게 물음표 살인마인가 하는 그거냐.

할 말을 찾지 못해 머뭇거리는 나를, 머리 하나는 더 큰 야수묘왕이 물끄러미 내려다보았다.

“열화신룡 진태경.”

나직한 부름. 야수묘왕이 준엄한 목소리로 말을 이었다.

“네게는 목적이 있었다. 우리의 고향을, 이 땅을 찾아온 이유가. 그렇지 않느냐?”

“…….”

“한데 오늘의 넌 목적을 이루지 못했음에도 말없이 떠나려 하는구나. 낯선 땅에서 죽을 위기를 수없이 넘기고, 수많은 이들의 목숨을 구했으면서도. 그럼에도 단 한 번도 정당한 대가를 요구하지 않았지.”

야수묘왕의 힘 있는 시선과 목소리는 나를 향하고 있지만, 이 자리의 모두가 듣고 있다. 모두가 보고 있었다.

“이유가 무엇이냐.”

그리고 야수묘왕의 물음에, 나는 문득 입을 열었다.

“그냥 사람이 사람을 살리려고 한 것뿐입니다.”

“……!”

“대가를 얻기 위해 한 일이 아니라서. 다시 한번 누군가의 희생을 요구할 수가 없어서. 그래서 떠나려고 했습니다.”

침묵이 흘렀다.

수만 명이 군집했음에도 숨소리조차 들리지 않는 긴 침묵.

그렇기에 머리 위로 떨어져 내리는 이 빗줄기가 유난히도 크게 들렸다. 그 너머로 우뚝 선 야수묘왕의 신형이 움직였다.

스륵.

단단한 기둥과도 같은 허리가, 다른 이에게 굽혀져서는 안 되는 남만야수궁주의 허리가 나를 향해 기운다.

그리고 곧이어 모두가 지켜보는 앞에서, 정중하기 그지없는 포권지례(抱券之禮)를 취한 야수묘왕이 입을 열었다.

“야수묘왕 야율척. 이 땅의 모든 이들을 대표하여 화룡각주 진태경 대협께 무림맹으로의 입맹(入盟)을 청합니다.”

빗줄기가 서서히 그쳐 가는, 어느 날의 일이었다.
```

## Final English reading copy

```markdown
# Chapter 723

One day. Two days. And then three.

The rain that had come to be called the Sacred Rain was still drenching all of Nanman, and beneath the benevolent grace of the Earth Mother Goddess, nothing could stop the Nanman people who had become one.

Boom. Crack!

With a single swing of an ax from an older man, a massive tree snapped, while a thin woman casually hoisted a mountain of firewood.

Watching the entire scene from beside the window, I muttered under my breath.

“Wow. They got one hell of a buff.”

“B-buff?”

The question came immediately. I had already known there was an uninvited guest, so I turned around and answered.

“Nothing important. But what brings you here? Shouldn’t you be right in the middle of being swamped?”

“I stopped by on the way. And I’m not as busy as I was before. Everything is being sorted out in the blink of an eye.”

“Really?”

For an uninvited guest, he was a fairly welcome sight. I looked at Yayul Mok, the Young Palace Lord of the Nanman Beast Palace, and continued.

“That’s good news. Who do they say they have to thank?”

At my question, Yayul Mok shrugged.

“According to what my father told me, it is thanks to some Han Chinese man. He must have been mistaken.”

“Perhaps. But as far as I know, he wasn’t mistaken.”

“No, he was. There is no way a despicable Han Chinese man would help us.”

“True. The ones from the Central Plains are all like that. You can never trust them.”

“Now you’re speaking sense.”

A short silence passed, and as if we had planned it, we both let out quiet laughs at the same time.

“It’s all thanks to you, Jin Taekyung.”

“We all worked hard, but that’s true. I did contribute quite a lot.”

At my shameless reply, the smile at the corner of Yayul Mok’s mouth deepened.

“Are all Han Chinese people as incapable of humility as you?”

“No. Just me.”

“That’s a relief.”

“Why?”

“Because now I think I might be able to like Han Chinese people more than I did before.”

“Oh…”

I looked at Yayul Mok with renewed interest.

Who would have thought he could say something like that?

I had sensed it little by little before now, but the hostility that had once filled his attitude toward the Central Plains was nowhere to be found.

“Don’t like them too much. Once you actually go there, you’ll find plenty of crazy people.”

“You take me for a child. I know that every place where people live is more or less the same. Nanman and the Central Plains alike.”

“Really? You didn’t seem to know that when we first met.”

“……That was because you turned the fields into a sea of fire.”

Perhaps he had remembered what he had been like back then. Yayul Mok answered with a slightly embarrassed expression before approaching the window where I stood.

He stared at the scene visible through the half-open window, then suddenly spoke.

“It still doesn’t feel real. That something like this happened in the place where I was born and raised.”

“A disaster? Or a miracle?”

“Both.”

After his brief answer, Yayul Mok added one more thing.

“But this, too, must be a god’s will.”

“……Do you believe in the Earth Mother Goddess, too?”

“I’m not sure. At the very least, I believe a god exists. I’ve experienced something that couldn’t be explained otherwise.”

Anyone who encounters something beyond human understanding is bound to think of a god.

They might not know who was up there in that impossibly distant sky, but they would figure that whoever it was had to be one impressive fellow.

*I’m no different.*

Swallowing the rest of my thought, I smoothly changed the subject.

“So, is the cleanup going well?”

“If you mean the restoration work, it has already entered its final stage. We should see the final results within a few days at the latest.”

Considering that the Inner Palace had been reduced to a wasteland and more than several hundred houses and pavilions in the Outer Palace had collapsed, it was a truly astonishing pace.

But instead of being surprised, I gave a small nod.

*Well, the buff is pretty incredible.*

The rain still falling at this very moment contained the powers of life and purification.

It was an area-wide buff that constantly infused everyone with vitality while also enhancing their physical abilities.

*Of course, its effect will end when the rain stops. But even a few days will be enough.*

There was an old saying that even a single sheet of paper was easier to lift with two people. This time, tens of thousands of Nanman people were working around the clock to rebuild the Palace.

They were rebuilding their home. Their homeland.

And their efforts were bearing fruit at an astonishing speed.

“What about the other matters?”

Yayul Mok understood what I meant and answered.

“To eliminate the remaining superiority and boundaries between the tribes, we abolished the Great Chieftain system. We received the agreement of not only the Miao people but also all four of the other great tribes.”

“Good work. Ah, then what about Yohi?”

Yayul Mok nodded.

“She was the first person to call for the abolition of the Great Chieftain system.”

The tribal chieftains who had joined hands with Baeksang had been executed in front of countless witnesses, but Yohi alone had received a full pardon.

She had repented of her mistakes, albeit belatedly. More importantly, she had played a vital role in leading the beasts and evacuating the tribespeople from the Outer Palace. Because of that, no one had raised any serious objection to her pardon.

“She said that she couldn’t leave behind the same precedent as Baeksang, Heugung, and herself.”

“She was right. Before this, the Great Chieftains had wielded far too much power.”

“My father and the other tribal chieftains agreed as well. Because of what happened, the Nanman Beast Palace will now operate under the sole authority of the Palace Lord. The Tribal Grand Council will remain in place to prepare for any unforeseen situations. And…”

As I listened to the rest of Yayul Mok’s explanation, I realized once again that the Nanman Beast Palace had been reborn.

The authority of the Beast Miao King, who now served as both Palace Lord and priest, had become incomparably greater than before. The unsettled public mood had stabilized with the appearance of the Earth Mother Goddess, and the people had united regardless of their tribes or faiths.

After hundreds of years, the balance of this land, which had been divided into thirty-two pieces since the Nanman Beast Palace was founded, had finally become one.

*At this point, I could really call it a small kingdom.*

Tens of thousands of tribespeople and nearly ten thousand warriors.

And if you counted the beasts they commanded, it was by no means an exaggeration.

Even allowing for the fact that the Nanman warriors were inferior to the martial arts of the Central Plains, they still represented an immense military force.

I looked at Yayul Mok with renewed interest.

“……Why are you looking at me like that?”

“No, now that I look at you, you seem to have a touch of nobility. So you’re actually a prince, or something like that?”

“……A prince?”

Yayul Mok muttered in an awkward voice, then suddenly let out a quiet laugh.

“Why are you laughing? Looking at the current situation, it’s not entirely wrong.”

“Now that I think about it, I suppose it is an honor.”

“What?”

“The Apostle of the great Earth Mother Goddess is calling me a prince. How could that not be an honor?”

“……?”

What was he talking about now?

As I blinked at Yayul Mok, unable to understand him, he handed me something he had taken from inside his robe.

“Take it.”

“This is…”

“We decided to call it the Mother Goddess Scripture. My father told me to give it to you.”

The moment I accepted the bundle of bamboo strips with a bewildered expression—

Ding.

> **System**
>
> — You have acquired Mother Goddess Scripture.
>
> — Mother Goddess Scripture is a scripture containing records of the Earth Mother Goddess.
>
> — A god can exist only when someone believes in it.
>
> — The Earth Mother Goddess has become known as the One God of Nanman!
>
> — Countless believers who follow the Earth Mother Goddess are ecstatic!
>
> — According to the records in Mother Goddess Scripture, your name has become known anew!
>
> — You have achieved Religious Reformation, an achievement that makes one wonder whether anyone would actually go this far!
>
> — You have acquired the Title Apostle of the Earth Mother Goddess!

Holographic windows filled the air along with the System notifications.

I stared blankly at the sight, then hurriedly unfolded the bundle of bamboo strips in my hand.

After reading the tiny writing etched across them, I burst out laughing in disbelief.

“What is this?”

Seeing my reaction, Yayul Mok shrugged.

“It says exactly what it means. The Earth Mother Goddess has been with this land since ancient times as its mother goddess, and whenever Nanman fell into crisis, she personally sent her apostle to save the people…”

“That’s me?”

“Of course. Three hundred years ago, it was my ancestor, the first Palace Lord. And two hundred years ago, it was the Sect Leader of the Fire Gate Clan at the time—the clan you belong to.”

They had managed to force everything together like this.

It was true that I had dropped a few hints, but I never expected to see my three-character name written right there.

No. To be precise, it was *our* names.

Flip.

When I skimmed through the rest, I found quite a few familiar names.

Jeok Cheongang, of course. The members of the Fire Dragon Pavilion. Even Namho’s name.

This was supposed to be something like a Bible. Was this really allowed?

“I know it was thrown together in a hurry, but this is ridiculous. Who the hell came up with this setting?”

“My father.”

“No wonder it’s so impressive. How did he manage to make the setting this detailed?”

“……”

I avoided Yayul Mok’s gaze and tucked the bamboo strips into my robe.

*The Apostle of the Earth Mother Goddess.*

I had somehow become a god’s apostle, something that had never been written in my fate, but I didn’t feel particularly bad about it.

No. In a situation like this, it was actually a major gain.

*The ill feelings Nanman’s people have toward the people of the Central Plains should be diluted now.*

As I was muttering inwardly, Yayul Mok suddenly asked,

“So, have you finished preparing?”

“Hm?”

“Preparing to leave Nanman.”

“……!”

After a brief silence, I smacked my lips.

“You’re sharp.”

“It would be strange if I hadn’t noticed.”

“How did you know?”

“Leaving aside everyone else, that huge fellow has been frantically gathering food since yesterday. Like someone preparing to set out on a long journey.”

There was no need to ask who he meant by “that huge fellow.” Guessing the culprit, I sighed.

“Taishan, you crazy bastard. I told you to move quietly.”

“Your Master, the Fire King Jeok Cheongang, secretly took five jars of fruit wine.”

“…….”

Oh, come on. Old Master.

I squeezed my eyes shut, and Yayul Mok’s voice pierced my ears.

“You should at least say goodbye before you leave. Everyone is waiting.”

* * *

Only after we drew near the North Gate did I realize that the two words Yayul Mok had used—“everyone”—were not an exaggeration in the slightest.

*This is…*

Thousands. Perhaps tens of thousands.

Among the countless people filling the field outside the North Gate, where fresh grass and flowers had spread thanks to the life-giving downpour, I saw several familiar faces.

Jeok Cheongang, pretending not to notice anything in front of a cart loaded with jars of fruit wine.

Taishan, holding meat in both hands with a solemn expression, along with the members of the Fire Dragon Pavilion, each mounted on a beast.

And then…

“You’ve finally arrived.”

The Beast Miao King, Yayul Cheok, spoke with a stern expression. As the master of the Nanman Beast Palace, he represented every Nanman person on this land.

“Why were you trying to leave without saying a word?”

I scratched the back of my head.

“I was going to tell you.”

“You were?”

“Through a letter.”

“Just a letter?”

“No, it’s just that you looked so busy…”

“Do you think that makes sense?”

“……”

Was this what they called a question-mark murderer?

Unable to think of anything to say, I hesitated. The Beast Miao King, who was at least a head taller than me, silently looked down at me.

“Blazing Flame Divine Dragon Jin Taekyung.”

It was a quiet summons. The Beast Miao King continued in a solemn voice.

“You had a purpose. There was a reason you came to our homeland—to this land. Was there not?”

“……”

“But today, you are trying to leave without a word even though you have not achieved your purpose. You crossed a foreign land and survived countless brushes with death. You saved the lives of countless people. And yet you never once demanded a rightful price.”

The Beast Miao King’s powerful gaze and voice were directed at me, but everyone present was listening. Everyone was watching.

“What is the reason?”

At the Beast Miao King’s question, I suddenly opened my mouth.

“I was simply a person trying to save people.”

“……!”

“I didn’t do it to receive a reward. And I couldn’t ask for another sacrifice. That’s why I was going to leave.”

Silence fell.

Even though tens of thousands of people had gathered together, the silence was so deep that not even a breath could be heard.

Because of that, the rain falling over our heads sounded especially loud. Beyond it, the Beast Miao King’s towering figure moved.

Ssshh.

His back, firm as a pillar—the back of the master of the Nanman Beast Palace, which should never have bowed before another—leaned toward me.

Then, before everyone watching, the Beast Miao King performed the most courteous of clasped-fist bows and spoke.

“I, Yayul Cheok, the Beast Miao King, on behalf of everyone who lives on this land, formally petition Great Hero Jin Taekyung, Fire Dragon Pavilion Master, for our admission into the Murim Alliance.”

It happened on a certain day when the rain was slowly coming to an end.
```
