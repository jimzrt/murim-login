<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0658.txt",
      "sha256": "06e632195d8dd440830ec8c7bbebe3bf95739ca49b83dcef2cce5fbee531c2d2",
      "bytes": 13286
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b002f6a1e9c812274ea1851ef9fcbedfbfb7af47d3571ab1fcf1a593d2f1d6a8",
      "bytes": 2478
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ad1a49ceb4f059b7cbc76e6443ae3f2e0e94626f045fc0cb6ab217ce14e6c7d2",
      "bytes": 200768
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "866b25b592bb36f0f76adb4845f0f4eef70808de753a9e7b0d22e5d9db3eae59",
      "bytes": 828
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "346ea62da324a76333e02b1a9d74d145922b960867a88b444eca081ecb6e2285",
      "bytes": 814
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0647fe63508a500f745b2371111e71f7233d0ae6fbc6c2b4fb12819fd1daa414",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "80294b38c866d59b949f6f077829d7a3b41a0f55a5e61ab77c08969ecaa17d58",
      "bytes": 1347
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3bc11417173f40b125e49e3fa1eedf01a388e76f9d8d45377acaf2ce194ff8a7",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "28365b8db7b2e73efef29dd454c61325106531ba4ba92bf55982d6c556ff44a9",
      "bytes": 1936
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2c4a17854171aadb0b2a108e11d2361b8fef011e7fe5b1fac23428a60094e2ea",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "8c12e4607cba3fca289438d9881a2ccf074765680203824248a1196ed4587f38",
      "bytes": 1131
    },
    {
      "path": "characters/Namho.md",
      "sha256": "3179bc33c75ffb6ad08487af0af7e01bab59ee1e7b0f36052f1ba885865257fa",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "0534eeed48582b0862201255104482324859393ccce38356a942f0eace583997",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "e4962fb2709505c214b5b7eeab3c4466aaea768ed35d9428657c4510d7391618",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "860d0c59e3aee94200cf40ff7d3b82607fc735534b5853dfa7ee5db1688e4cbf",
      "bytes": 957
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "e7bd16499da42acea39b325ba7ed0aa76bd9c8fbf852575f5471878983c6df7e",
      "bytes": 585
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "50fb8eee27c548f1a2eaa56315699cd3a54733f50b9eb7a024c6fbcd620d85e5",
      "bytes": 871
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "098a1ce01242254b7502f0c5a38e3cfbec98f3242da5d957ce843b30d6ce6e8b",
      "bytes": 206298
    }
  ],
  "estimated_tokens": 15459
}
-->

# Durable State Update — Chapter 658

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 658. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 658. Profile updates may replace only one
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
  "chapter": 658,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 658,
    "continuity_sources": [658],
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
    "Jin remains in the Nanman Beast Palace's Inner Palace as the Third Young Master of the Jin Family of Taiyuan and head of the Fire Dragon Pavilion.",
    "The Fire Dragon Pavilion was attacked after Jin left, and Dark Heaven is suspected of organizing or enabling the assault.",
    "Yohi's Western Yao Estate was attacked by a Supreme Peak master, killing more than a hundred Yao warriors and beasts.",
    "Jin and Yayul Mok believe Dark Heaven directly intervened and likely deployed a Supreme Peak master, but the motive is unknown.",
    "Baeksang and the Beast Miao King are the only two known Supreme Peak masters in Nanman.",
    "Heugung genuinely loves Yohi and had promised to cooperate with Jin.",
    "Heugung and Yohi remain missing after the attack, and Heugung's apparent death remains unconfirmed.",
    "Faint footprints indicate that a third party abducted or confronted Heugung and Yohi rather than the incident being their staged attack.",
    "Yohi's nearly scentless pouch remains a possible clue.",
    "Baeksang has publicly accused Jin of the Inner Palace massacre and now relies on Utu-ri's eyewitness testimony and circumstantial evidence to demand his arrest.",
    "The Beast Miao King has halted Baeksang's attempted arrest, but Baeksang threatens pursuit across Nanman and reprisals against Jin's Han Chinese subordinates.",
    "The second day of the Tribal Grand Council may decide whether Jin lives or dies, while the System's Either-Or Quest is active."
  ],
  "continuity_sources": [
    657
  ],
  "open_questions": [
    "Who was the Supreme Peak attacker, and what did Dark Heaven seek by intervening directly?",
    "Are Heugung and Yohi alive, and where were they taken?",
    "What can be learned from Yohi's nearly scentless pouch?",
    "Is Baeksang truly colluding with Dark Heaven despite the evidence of third-party intervention?",
    "What will the Tribal Grand Council decide about Jin's life, and what choice does the Either-Or Quest require?"
  ],
  "safe_through": 657,
  "temporary_decisions": [
    "Retain Force for 강기 and Supreme Peak for 초절정.",
    "Retain Sound Transmission for 전음.",
    "Retain Western Yao Estate for 서요부, Eastern Yi Estate for 동이부, Southern Bai Estate for 남백부, and scent pouch for 향낭.",
    "Retain No words for 무언 and net over heaven and earth for 천라지망.",
    "Render 양자택일 as Either-Or."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무림맹    | **Murim Alliance**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 몬스터     | **monster**           |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 보옥 | **Treasured Jade** | Missing Fire Gate Clan treasure sought by Jeok Cheongang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천라지망 | **net over heaven and earth** | Jeok Cheongang's figurative threat to pursue a culprit everywhere. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 철구 | **iron balls** | Training weights attached to Taekyung. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 대회의 | **Tribal Grand Council** | Nanman's council of great chieftains. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 아빠 | 진태경 | father to son | Taekyung | affectionate informal | Addresses his young son warmly as Taekyung. |
| 진태경 | 아빠 | son to father | Dad | childlike informal | Taekyung addresses his father as Dad in the childhood flashback. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 야율목 | 남호 | Nanman Young Palace Lord to elderly guest and Hidden Shadow Pavilion agent | old man | respectful and familiar | Yayul Mok uses the honorific 노인장 while praising Namho's knowledge of White Tigers. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 야율목 | 야수묘왕 | son_to_father | Father | formal and deferential | Yayul Mok calls out to the Beast Miao King after the rescue party arrives. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 657
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle, opposes the Nanman Beast Palace joining the Murim Alliance, remains distrustful of the Central Plains, and is alleged by Heugung to have colluded with Dark Heaven.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 657
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, is responsible for the forces stationed at Ailao Mountain, has ordered Ju Hwaran, Song Ilseom, and Hyuk Mujin to investigate the Blood Monk in Guizhou, and met the Martial God twice more than fifty years ago.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 655
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 652
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 650
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 657
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 657
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 652
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, an experienced Nanman escort guide with route knowledge from the Escort King's records, someone who can understand the Miao and Bai languages, and a volunteer accepted for the scouting mission to investigate the Blood Monk in Guizhou.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 657
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 654
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 652
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 652
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 656
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 657
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

## Korean source

```text
＃658화



띠링.



- 돌발 퀘스트, [양자택일(兩者擇一)]이 생성되었습니다!



갑작스럽게 울리는 시스템 알림. 동시에 반투명한 홀로그램 창이 허공으로부터 불쑥 솟구쳤다.



퀘스트



[양자택일(兩者擇一)]



이제 당신에게 남은 선택지는 오직 두 가지뿐입니다.

전력을 다해 저항하여 이 자리를 벗어날지. 혹은 순순히 투항하여 저들에게 사로잡힐지.

선택은 오롯이 당신의 몫이며, 모든 선택에는 그에 상응하는 결과가 뒤따를 것입니다.



등급 : 無

제한 : 진태경

임무 : [투항] or [저항] (미완료)

보상 : ???

실패 : ???

- 해당 퀘스트에는 두 가지 선택지가 존재하며, 반드시 이 중 하나만을 선택해야 합니다.

- 선택에 따라 주위의 여러 가지 요소가 변화합니다. 그 과정에서 특정 인물이 사망할 수도 있습니다.



어떻게 하시겠습니까?

투항하기 / 저항하기



시스템 창을 확인한 뒤 드는 생각은 하나뿐이었다.

‘상황 참 거지 같네.’

양자택일.

갑작스럽게 발동한 퀘스트는 제목 그대로의 내용을 품고 있었다.

투항할 것인가. 저항할 것인가.

선택지는 오직 두 가지뿐이고 나는 반드시 무언가를 택해야만 한다.

현재의 상황이, 그리고 곳곳에서 흘러나오는 목소리의 주인들이 그것을 요구하고 있었다.

“백상 대족장의 말씀에 찬성합니다.”

“옳소! 궁주께서 독단이라 생각하신다면, 지금 이 자리에서 대회의를 열겠소!”

“죄가 없다면 순순히 투항하여 조사에 임하면 될 터. 무엇이 문제란 말입니까?”

친(親) 백상파에 속한 부족장들의 외침을 듣고 있자니 실소가 흘러나왔다.

뭐가 문제냐고?

여기가 현대가 아니라 무림이라는 게 가장 큰 문제다.

21세기에서도 온갖 사법 비리가 벌어지는 마당에, 백상의 주도하에 구금된 내가 어떤 취급을 받을지는 안 봐도 뻔했다.

‘시작부터 죄인으로 낙인찍고, 그 방식 그대로 끝까지 몰아가겠지.’

그 과정에서 공명정대(公明正大)라는 단어는 찾아볼 수 없을 거다. 내가 얕은 생각으로 한 거짓말은 이미 들통났고, 백상은 증인과 명백한 정황을 내놓은 상황이니까.

이건 치밀하게 파 놓은 함정이다. 한번 발을 디딘 이상 추락할 수밖에 없는.

물론 이런 와중에도 내게 손을 내밀어 주는 이들 역시 있었다.

“미쳤군. 다들 정신이 나간 게야. 진태경을 척살하겠다고? 중원 무림 전체와 전쟁이라도 벌일 심산인가!”

“심지어 아직 그가 정말 흉수인지에 대한 여부도 확실하지 않소. 무림맹의 각주이자 화왕의 제자가 도대체 무슨 이유로 이런 짓을 벌인단 말이오?”

“그가 애뇌산에서 구출한 전사가 자그마치 이백여 명이다. 한데 그가 흉수라고? 아무리 한족이 싫어도 그렇지, 어찌 은혜도 모르는 금수(禽獸)와 같이 행동한단 말이냐!”

이번에는 야수묘왕을 따르는 부족장들의 외침이 울려 퍼졌다.

하지만 그 십수 명 중 정작 앞으로 나서는 이들은 소수였고, 적지 않은 부족장들은 혼란스러운 눈빛으로 상황을 지켜보거나 입을 굳게 다무는 것을 택했다.

‘그렇겠지. 어차피 나는 결국 외인(外人)이니까.’

애초에 남만인들은 한족에 대한 감정이 좋지 못했다.

한족인 내가 파격적으로 대회의에 참석할 수 있었던 건 애뇌산에서의 활약 덕분이었고, 그들이 허락할 수 있는 부분은 딱 거기까지였던 거다.

탓할 생각은 없다. 저들은 대세(大勢)를 읽었을 뿐이니까.

백상의 말처럼 당장 이 자리에서 대회의가 열린다고 해도 이 상황을 뒤집을 수는 없었다.

설령 야수묘왕이라 하더라도.

- 저, 아무래도 좆 된 것 같은데요.

내가 흘려보낸 전음(傳音)을 들은 야수묘왕의 미간에 깊은 골이 파였다.

- ……미친놈.

- 왜요?

- 지금 같은 상황에서도 농이 나오느냐?

- 사실대로 말한 건데요, 뭐. 그렇다고 어린애처럼 엉엉 울고 있을 수는 없잖습니까. 상황이 나아질 것도 아닌데.

담담하게 현실을 직시하는 내 전음에, 아수묘왕이 입술을 질끈 깨물었다.

- 미안하다. 만약 백상의 말대로 대회의가 열린다면…… 나로서도 어쩔 수 없구나.

- 그래도 다행이네요. 야율 대협은 제 말을 믿어 주시는 것 같아서.

- 당연히 믿는다. 그래서 더 미안한 거고.

- 그럼 미안해하지만 말고 저 새끼들 아가리 한 대씩 때려 주시면 안 됩니까? 정 껄끄러우시면 제가 때리고요.

- …….

- 아니면 화염신장.

- 허, 이 정도면 적 노의 제자가 아니라 혈육이라 해도 되겠군.

적천강이라.

이름 석 자와 함께 문득 눈앞을 스치는 익숙한 얼굴에 입맛이 씁쓸해진다. 만약 이 상황에서 적천강이었다면 어떻게 대처했을까.

‘아니, 노야였다면 이 상황까지 오지도 않았겠지.’

나는 아직 적천강만큼 강하지도 않고, 무림에 익숙해졌다고 생각했던 것이 무색할 만큼 미숙했으며, 적들은 생각 이상으로 철저하고 교활했다.

‘바둑으로 치면…… 내 행동은 악수(惡手)쯤 되려나.’

나는 바둑을 모른다. 하지만 내가 어렸을 적, 생전 아버지는 가끔 컴퓨터 앞에 앉아 인터넷 바둑을 두시고는 했다.

닉네임은 진세돌이었지만 승률은 형편없었고, 중국 국적의 유저에게 질 때면 ‘짱깨 새끼 바둑 좆같이 두네…… 타이완 넘버원.’이라고 중얼거리시다가 엄마한테 등짝을 얻어맞기 일쑤였다. 애 듣는 앞에서 욕하지 말라고.

전부 케케묵은 과거의 일이다.

아버지는 몇 해 뒤 몬스터 웨이브로 인해 갑작스럽게 돌아가셨고, 패배로 점철되긴 했어도 꾸준했던 아버지의 바둑 계정은 휴면 계정이 되었다.

하지만 어째서일까. 어느 날 바둑에서 지고 있던 아버지를 지켜보던 그 날의 기억이 문득 떠올랐다.



‘아빠. 또 지고 있어?’

‘또 지다니. 아빠 이번 판만 진 거야. 아니, 아직 끝나지도 않았어.’

‘하지만 어제도, 그제도 지고. 아까도 지는 거 봤는걸!’

‘……귀여운 내 새끼. 벌써 이렇게 커서 애비 가슴에 대못을 박는구나.’

‘근데 왜 아빠는 맨날 져?’

‘음. 아빠가 악수를 뒀거든.’

‘악수?’

‘그 악수 말고. 나쁜 수라는 뜻이야. 어제 태경이가 체육대회에서 축구 했을 때, 실수로 공이 아니라 민준이 다리를 걷어차는 바람에 경기에서 진 거랑 비슷한 거란다. 나쁜 선택. 이해되니?’

‘웅웅. 이해됐어. 그럼 악수 두면 바둑 지는 거야?’

‘꼭 그런 건 아니지.’

‘왜?’

‘악수 한 번 뒀다고 승부가 끝나는 건 아니거든. 단지 악수를 반복해서 두다 보니까 지는 거지. 흠, 그러지 말아야 했는데.’

‘하지만 난 어제 바로 퇴장당했는데?’

‘아들. 그건 민준이 다리에 금이 가서 그런 게 아닐까?’

‘아항.’

‘……아항은 무슨. 민준이 부모님한테 사과하느라 아빠는 허리가 부러질 뻔했는데. 어쨌든 중요한 건 악수를 반복해서 두지 않는 거란다.’

‘악수를 반복해서 두면 어떻게 되는데?’

‘바둑으로 치자면, 소중한 돌들을 잃고 결국 지게 되겠지. 나쁜 선택을 한 대가로.’

‘나 알았어! 그래서 아빠가 맨날 지는 거구나!’

‘……여보! 태경이 좀 데려가! 여보!’



갑자기 왜 이런 기억이 떠오르는지 모르겠다. 아니, 사실은 알 것 같기도 하다.

덕분에 마음의 결정을 내릴 수 있었으니까.

- 하나만 약속해 주실 수 있습니까?

- 갑자기 왜 말이 없…… 약속?

- 네. 약속.

나는 야수묘왕을 똑바로 직시하며 전음을 흘려 보냈다.

- 만약 앞으로의 일이 어떻게 되더라도, 다른 사람들은 멀쩡하게 중원으로 돌아갈 수 있게 해 주겠다는 약속이요.

- ……!

- 그거 하나면 됩니다.

- 네 녀석. 설마…….

- 약속했다는 뜻으로 이해하겠습니다.

무언가를 짐작한 듯, 눈을 크게 뜬 채 나를 바라보던 야수묘왕이 이내 착잡한 얼굴로 고개를 끄덕인다.

- 약속하마. 내가 할 수 있는 모든 힘을 다해 네 수하들을 지킬 것이다. 네가 뒤집어쓴 누명 역시 밝혀 주마.

그래, 그럼 된 거지.

내심 중얼거린 나는 백상을 향해 걸음을 옮겼다.

아니, 옮기려고 했다.

덥석.

그 순간 등 뒤에서 뻗어 나온 두 개의 손이 내 옷자락을 움켜잡지 않았다면 그랬을 거다.

“진태경. 도대체 어쩔 셈이지?”

굳은 얼굴로 묻는 야율목. 그리고 이미 내 마음을 읽은 남호의 한 마디가 이어졌다.

“멍청한 놈 같으니. 스스로 범 아가리에 들어갈 셈이냐?”

“범 아가리인지, 개새끼 아가리인지는 잘 모르겠고.”

내가 어깨를 으쓱하며 말을 이었다.

“이렇게 된 이상, 뭐 어쩌겠습니까.”

그런 나를 바라보는 남호의 눈빛이 그 어느 때보다 깊숙하게 가라앉았다.

“나와 다른 대원들 때문이냐? 네 녀석이 이 자리를 피하면 우리가 해를 입을까 봐?”

“음. 글쎄요.”

“그런 생각이라면 썩 집어치워라. 그건 우리 중 누구도 바라지 않는…….”

“저도 압니다. 다들 그럴 거라는 걸.”

부드러운 어조로 남호의 말을 끊어낸 내가 말을 이었다.

“하지만 그 반대였어도 마찬가지일 겁니다. 다른 대원들이 제 입장이었다면. 남 노인이 지금의 저였다면, 혼자 도망치진 않았을 거예요.”

“……!”

“나중에 보자고요.”

대답 대신 흔들리는 눈동자. 옷자락을 붙잡은 손을 떼어 낸 나는, 두 사람에게 눈인사를 건네고 걸음을 옮겼다.

저벅. 저벅.

어느새 주위에 내려앉은 침묵.

홀로 움직이는 내 발걸음 소리는 천둥처럼 울리는 듯했고, 그런 나를 응시하는 백상은 흔들림 없는 호수처럼 잔잔했다.

“드디어 현실을 깨달았나?”

“아주 오래전에 누가 그러더라고. 바둑에서 악수를 여러 번 두면 소중한 돌을 잃고 질 수밖에 없다고.”

차라리 이게 대국이었다면, 나는 악수고 나발이고 내키는 대로 나갔을 거다.

설령 지더라도 뭐 어떤가. 어느 유명 프로 기사는 그래 봤자 바둑, 결국 바둑이라는 명언을 남겼지만, 내게는 그래 봤자 바둑일 뿐이니까.

지고 난 후에는 아버지가 그랬던 것처럼 ‘짱깨 새끼 바둑 좆같이 두네.’ 하면서 바둑판으로 백상 뚝배기를 깨 버리면 된다.

하지만 이건 단순한 놀이가 아니고, 악수를 두면 돌 대신 내 사람을 잃게 된다.

‘주화란. 혁무진. 송일섬. 사마표. 태산. 남호…….’

만약 이 자리를 벗어난다 해도 그들 모두와 함께 남만야수궁의 천라지망(天羅蜘網)을 뚫는 건 불가능에 가깝다.

나를 믿고 지금껏 따라와 준 이들이니, 반드시 살려야 한다.

무슨 방법을 써서라도.

“악수를 계속해서 두게 되면 소중한 돌을 잃고 패배한다…… 누구인지는 모르겠지만, 현명한 자로군.”

“좋은 분이셨지. 최소한 너처럼 좆 같은 새끼는 아니었어.”

차차창!

약속이라도 한 것처럼 사방에서 뽑혀 나오는 병장기. 그와 동시에 좁혀지는 포위망을 힐끗 바라본 백상이 소매를 내저었다.

“이번만큼은 악수를 두지 않은 것을 칭찬해 주마. 제아무리 화왕의 제자라 해도 어쩔 수 없었겠지.”

“너 같은 새끼 칭찬 듣자고 이러는 거 아니다.”

“뭐든 상관없다. 넌 이 길로 뇌옥(牢獄)에 갇힐 테니.”

“뇌옥이라. 그리 반가운 말은 아닌데.”

“수천 근의 철구도 준비되어 있을 테니, 기대해도 좋다.”

“그래. 기대감 때문에 벌써부터 불알이 다 떨린다.”

어느 정도는 예상했던 일. 담담하게 대답한 나는, 천천히 검을 거두는 백상을 향해 말을 이었다.

“그런데 넌 왜 기대 안 해?”

“뭐?”

“아까 그러지 않았나? 만약 도망치면 내 사람들도 전부 죽이겠다고.”

“갑자기 그게 왜…….”

이어지는 뒷말은 들을 이유도, 들을 필요도 없었다.

‘나한테 그딴 개소리를 했으면, 한 대 처맞을 것 정도는 알았어야지.’

들리지 않을 한 마디와 함께, 나는 빛살처럼 일권(一拳)을 뻗었다.

콰직!

그리고 결과를 확인하지도 않은 채, 재빨리 외쳤다.

“아, 항복! 항보옥!”

어쩔 건데, 시벌.
```

## Final English reading copy

```markdown
# Chapter 658

Ding.

A System notification suddenly rang out. At the same time, a translucent holographic window shot up into the air.

> **System**
>
> An unexpected **Quest**, **Either-Or**, has been generated!
>
> **Quest**
>
> **Either-Or**
>
> Only two choices remain to you now.
>
> Will you resist with all your strength and escape this place? Or will you surrender quietly and allow yourself to be captured by them?
>
> The choice is entirely yours, and every choice will be followed by a corresponding result.
>
> **Grade:** None
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Surrender or Resist (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???
>
> - This Quest contains two choices, and you must select exactly one of them.
>
> - Various factors around you will change depending on your choice. A certain person may die in the process.
>
> How will you proceed?
>
> Surrender / Resist

I had only one thought after checking the System window.

*What a shitty situation.*

Either-Or.

The Quest that had suddenly activated contained exactly what its title said.

Would I surrender? Or would I resist?

There were only two choices, and I had to choose one of them.

The current situation—and the owners of the voices rising from every direction—demanded it.

“I agree with Great Chieftain Baeksang.”

“Exactly! If the Palace Lord thinks this is an arbitrary decision, then let us convene the Tribal Grand Council right here and now!”

“If he is innocent, he should surrender quietly and submit to an investigation. What is the problem?”

As I listened to the shouts of the tribal chieftains who belonged to the pro-Baeksang faction, a hollow laugh escaped me.

*What is the problem?*

The biggest problem was that this was Murim, not the modern world.

Even in the twenty-first century, where all kinds of judicial corruption took place, it was obvious what would happen to me if I were detained under Baeksang’s orders.

*They’ll brand me a criminal from the beginning and force the entire process to end that way.*

There would be no fairness or impartiality to be found anywhere along the way. The lie I had told without thinking had already been exposed, and Baeksang had produced both a witness and clear circumstantial evidence.

This was a carefully dug trap. Once I stepped into it, I could only fall.

Of course, even in this situation, there were those who reached out to me.

“You’re all insane. Have you lost your minds? You intend to execute Jin Taekyung? Are you planning to start a war with the entire Murim of the Central Plains?”

“Moreover, it has not even been established that he is truly the culprit. Why would the Pavilion Master of the Murim Alliance and the Fire King’s Disciple do something like this?”

“He rescued no fewer than two hundred warriors from Ailao Mountain. And you claim he is the culprit? Even if you hate the Han Chinese, how can you act like ungrateful beasts?”

This time, the shouts of the tribal chieftains who followed the Beast Miao King rang out.

But among the dozen or so of them, only a few actually stepped forward. Quite a few chieftains chose to watch the situation with confused expressions or kept their mouths firmly shut.

*Of course. In the end, I’m still an outsider.*

The Nanman people had never held particularly favorable feelings toward the Han Chinese.

The only reason I, a Han Chinese man, had been allowed to attend the Tribal Grand Council in the first place was because of what I had accomplished at Ailao Mountain. That was exactly where the extent of what they were willing to permit ended.

I had no intention of blaming them. They were simply reading the way the tide was turning.

Even if the Tribal Grand Council were convened here and now, as Baeksang had suggested, there was no way to overturn this situation.

Not even for the Beast Miao King.

*I think I’m pretty fucked.*

The Beast Miao King’s brow furrowed deeply as he heard the Sound Transmission I had sent him.

*You crazy bastard.*

*Why?*

*You can still joke at a time like this?*

*I’m just telling the truth. It’s not like I can sit here bawling like a child. It won’t make the situation any better.*

At my Sound Transmission, which calmly faced reality, the Beast Miao King bit down hard on his lip.

*I’m sorry. If the Tribal Grand Council is held as Baeksang says… there will be nothing I can do.*

*Still, it’s a relief that Great Hero Yayul seems to believe me.*

*Of course I believe you. That is why I am even more sorry.*

*Then don’t just be sorry. Could you punch those bastards in the mouth once each? If that makes you uncomfortable, I’ll do it.*

*……*

*Or maybe use Flame Divine Palm.*

*Hah. At this point, you may as well be Old Master Jeok’s flesh and blood rather than his Disciple.*

Jeok Cheongang.

At the three syllables of his name, a familiar face suddenly flashed before my eyes, and my mouth turned bitter. If Jeok Cheongang were in this situation, how would he have handled it?

*No. If it were Old Master Jeok, things never would have reached this point.*

I was nowhere near as strong as Jeok Cheongang. I was still so inexperienced that my belief I had grown accustomed to Murim seemed laughable, and my enemies had been more thorough and cunning than I had imagined.

*If this were Go… my actions would probably count as a bad move.*

I didn’t know how to play Go. But when I was young, my father would sometimes sit in front of the computer and play online.

His username was Jin Sedol, but his win rate was terrible. Whenever he lost to a user from China, he would mutter, “That Chink bastard plays Go like shit… Taiwan number one,” before Mom smacked him across the back.

She told him not to swear in front of the kid.

It was all a stale memory from the distant past.

A few years later, my father died suddenly in a monster wave, and the Go account he had kept playing on despite its long record of defeats fell dormant.

But why was it that, all of a sudden, I remembered that day when I had watched my father losing at Go?

*Dad. Are you losing again?*

*What do you mean, “again”? Dad only lost this game. No, it isn’t even over yet.*

*But you lost yesterday and the day before that, too. And I saw you losing earlier!*

*……My adorable boy. You’ve grown up so fast, and now you’re driving a nail into your father’s heart.*

*But why do you always lose, Dad?*

*Well. I made a bad move.*

*A bad move?*

*Not that kind of move. It means a bad play. It’s like when Taekyung played soccer at the sports festival yesterday and lost the game because he accidentally kicked Minjun’s leg instead of the ball. A bad choice. Do you understand?*

*Uh-huh, uh-huh. I understand. So if you make a bad move, you lose at Go?*

*Not necessarily.*

*Why?*

*The match doesn’t end just because you make one bad move. You lose because you keep making bad moves. Hmm. I shouldn’t have done that.*

*But I got sent off right away yesterday.*

*Son. Wasn’t that because Minjun’s leg was fractured?*

*Oh.*

*……What do you mean, “oh”? Your father nearly broke his back apologizing to Minjun’s parents. Anyway, the important thing is not to keep making bad moves.*

*What happens if you keep making bad moves?*

*In Go, you lose your precious stones and eventually lose the game. It’s the price you pay for making bad choices.*

*I know! That’s why you always lose, Dad!*

*……Honey! Take Taekyung away! Honey!*

I didn’t know why this memory had suddenly come back to me.

No. Maybe I did.

Because it had allowed me to make up my mind.

*Can you promise me just one thing?*

*Why are you suddenly quiet… Promise?*

*Yes. A promise.*

I stared straight at the Beast Miao King as I sent him another Sound Transmission.

*No matter what happens from this point on, promise me you’ll make sure the others can return safely to the Central Plains.*

*……!*

*That’s all I need.*

*You… Don’t tell me…*

*I’ll take that as a promise.*

The Beast Miao King had stared at me with widened eyes, as if he had guessed what I was planning. Then he nodded with a troubled expression.

*I promise. I will protect your subordinates with every bit of strength I possess. And I will also clear your name.*

*All right. That’s enough.*

I muttered inwardly and began walking toward Baeksang.

No.

I was about to walk toward him.

Grab!

If two hands had not reached out from behind me at that moment and seized the hem of my clothes, I would have.

“Jin Taekyung. What exactly are you planning to do?”

Yayul Mok asked the question with a rigid expression. Then Namho, who had already read my mind, added a single sentence.

“You foolish bastard. Are you planning to walk into a tiger’s mouth on your own?”

“I’m not sure whether it’s a tiger’s jaws or a fucking mutt’s.”

I shrugged and continued.

“But things have come to this. What else can I do?”

Namho’s gaze sank more deeply than ever as he looked at me.

“Is this because of me and the other members? Because you’re afraid we’ll be harmed if you flee from here?”

“Hmm. I don’t know.”

“If that is what you’re thinking, then throw it away at once. None of us wants—”

“I know. I know you all feel that way.”

I interrupted Namho gently and continued.

“But it would be the same if our positions were reversed. If the other members were in my place, or if Elder Namho were me right now, you wouldn’t run away alone either.”

“……!”

“See you later.”

Instead of answering, Namho’s eyes trembled.

I freed my clothes from their grip, met both of their eyes in farewell, and began walking.

Step. Step.

Silence had settled over the surroundings.

The sound of my footsteps as I moved alone seemed to thunder through the area, while Baeksang, watching me, remained as calm as an undisturbed lake.

“Have you finally come to your senses?”

“Someone told me a long time ago that if you make too many bad moves in Go, you lose your precious stones and have no choice but to lose.”

If this had been an actual Go match, I would have played however I pleased—to hell with bad moves.

Even if I lost, so what? A famous professional Go player had once said, “It’s still just Go—in the end, it’s only Go.” To me, it really would have been nothing more than Go.

After losing, I could simply smash Baeksang’s head open with the Go board while saying, just like my father had, “That Chink bastard plays Go like shit.”

But this was not a simple game, and when I made a bad move, I would lose my people instead of stones.

*Ju Hwaran. Hyuk Mujin. Song Ilseom. Sama Pyo. Taishan. Namho…*

Even if I escaped this place, breaking through the net over heaven and earth of the Nanman Beast Palace with all of them would be nearly impossible.

They had trusted me and followed me this far.

I had to keep them alive.

No matter what method I had to use.

“If you continue making bad moves, you lose your precious stones and suffer defeat… Whoever that person was, he was wise.”

“He was a good man. At least he wasn’t a piece of shit like you.”

Shing! Shing! Shing!

As if they had made an agreement beforehand, weapons were drawn from every direction.

At the same time, Baeksang glanced at the tightening encirclement and waved his sleeve.

“For once, I will commend you for not making a bad move. Even if you are the Fire King’s Disciple, you could not have done otherwise.”

“I’m not doing this to hear praise from a piece of shit like you.”

“It matters not. You will be confined in the underground prison.”

“An underground prison. That’s not exactly a pleasant thing to hear.”

“Several thousand pounds of iron balls will be prepared as well, so you may look forward to it.”

“Sure. My balls are already trembling from anticipation.”

It was more or less what I had expected.

I answered calmly, then continued speaking to Baeksang, who was slowly sheathing his sword.

“But why aren’t you looking forward to it?”

“What?”

“Didn’t you say so earlier? That if I ran away, you would kill every one of my people.”

“Why are you suddenly bringing that up—”

I had no reason to hear the rest of his words. Nor did I need to.

*If you said that kind of bullshit to me, you should have known you’d get punched.*

Along with a final word he could not hear, I thrust out a single fist like a ray of light.

Crack!

And without even checking the result, I hurriedly shouted,

“Ah, I surrender! I surrenderrr!”

What are you going to do about it, you fucker?
```
