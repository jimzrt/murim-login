<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0647.txt",
      "sha256": "e1a85bb50b9245bbd68a47793b7ae041b724aad9c098d2da277368fb592305ad",
      "bytes": 13109
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "16618720ed0aab6e38f4fb1c7439ef6778af4f4d0f84ae24904a6b0505275b43",
      "bytes": 2260
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "67280f84cf6b3e6011e196fcbc150d3527fc2ebd2b1fc13e843baae8a3f7d03e",
      "bytes": 198968
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "f8d0bb686d6ec41541652097c4b931cdf662a1d110716362a3c32b587cd50893",
      "bytes": 865
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "bb3c088e0bb9e2d88eeec54328fbe3cf13d7053e824a207820d2892b67304a34",
      "bytes": 638
    },
    {
      "path": "characters/Blood Monk.md",
      "sha256": "014a2a85b78e0654933e08f5e76a0f82b955f95e9f736cf0fd32e17e977db9ae",
      "bytes": 589
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "7d86535e39459ac0ea86429c1364552958a1dc8c2a741b53e3c902bd31ca5c0f",
      "bytes": 752
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d4fa2d347f05b382f627ceac8246070db1149097c3f585badeae8a681ecd3dc9",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "29c68f48cada7873e964ed4a997d3669b87c0391f7c0af2d562bbeebb1699c51",
      "bytes": 623
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "f824fcf02c85257496a7a23405d257b1f79b05feb9f8cb99f62bbdd4570f12fc",
      "bytes": 1347
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "6d9e077f39bacd56b75ae8d6d11e047fc0911e695830f887cd62872fd9d6eae5",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "09d2b8e715c38f12bd9e5b82900a37b1262043ad0e5e59abf889b961c41665ad",
      "bytes": 1936
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0559085fa860b1f1f3d76c68930c3833e6b17e62352629868bca04d62487ee1f",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "84d3a8f181a410c1ba7c96447216980002a4c8db0b9d3cb468c8ed95eea9a3e7",
      "bytes": 1131
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "d550b74cdf690ed7d7fac21ae29c55857f33bdc52ba42b5318ee5c838111f7e2",
      "bytes": 1061
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "bb0eb7a4513bbc3f4f85da9e4aa16d3089d1418d7e74d13b3f5d5366d6adca46",
      "bytes": 1252
    },
    {
      "path": "characters/Namho.md",
      "sha256": "85cd7dfd692ae21b683be5e3253f6eb0a309e869a354a5fe147e18ccac0bd40e",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "fd12586f02f59a5eab4f96bd08a07182ca92d43c8185c088192e007e9626ba45",
      "bytes": 899
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "85e46c5f53bea4601f7ba03c5fa887b405fae1f189f5f74c4391a4d386068cb6",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "57c87b1be6c7fdafb092eeb44c3c71ce9dc85aeb75670b348986c6db9243bf48",
      "bytes": 957
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "4a73db64adbe4bbe08ac973fbc9f500a5062a2079d2bf39c397e7948f9aa7353",
      "bytes": 528
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "0f35409556a476813f83d7325f03edf6cefe214c1cfe7208575cc8235c3f18c0",
      "bytes": 542
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "634ee76740dd1f8888e7e9c7f86b94b96db9ad200ed419b7980b365e55bf3084",
      "bytes": 204908
    }
  ],
  "estimated_tokens": 17136
}
-->

# Durable State Update — Chapter 647

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 647. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 647. Profile updates may replace only one
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
  "chapter": 647,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 647,
    "continuity_sources": [647],
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
    "Jin Taekyung has majority-backed admission to the Nanman tribal grand council.",
    "Baeksang attacked Jin Taekyung at the council and withdrew with the pro-Baeksang faction after being stopped.",
    "More than ten thousand Bai people and roughly half of Nanman's chieftains remain hostile to Jin.",
    "The Blood Monk is an unidentified bald, beardless, apparently middle-aged martial artist using a steel Zen staff who has killed several hundred people in Guizhou.",
    "Namho considers it highly likely that Dark Heaven is behind the Blood Monk, though this remains unconfirmed.",
    "Selected Nanman scouts and warriors, including some Fire Dragon Pavilion members, will investigate the Blood Monk in Guizhou.",
    "Ju Hwaran volunteered for the mission, and Jin Taekyung accepted her participation.",
    "Baeksang's hostility toward the Central Plains may come from grief over losing his only child or from a grudge against the orthodox Murim.",
    "Baeksang's possible alliance with Dark Heaven could endanger all of Nanman.",
    "Approximately two hundred Ailao Mountain warriors remain inside the Thousand-Year Spider webs, which appear to shield them from the Poison Mist.",
    "The missing ferocious beasts, Ailao Mountain's Wraith, and the pure-white eggs in the Poisonblood Grounds remain unexplained.",
    "An unidentified entity who recognizes Jin Taekyung has killed two informants."
  ],
  "continuity_sources": [
    646
  ],
  "open_questions": [
    "What are the Blood Monk's identity, purpose, destination, and connection to Dark Heaven?",
    "Is Baeksang acting from grief, resentment toward the orthodox Murim, or an alliance with Dark Heaven?",
    "Where did the missing ferocious beasts go?",
    "What does Ailao Mountain's Wraith intend to do, and what will emerge from the pure-white eggs?",
    "Who is the hidden entity that recognizes Jin Taekyung, and what is the nature of their past connection?"
  ],
  "safe_through": 646,
  "temporary_decisions": [
    "Use Tribal Grand Council for 부족 대회의.",
    "Use Blood Monk for 혈승.",
    "Use Soul-Chasing Guest for 추혼객.",
    "Use Killing Buddha for 살불.",
    "Use Fire Courtyard for 화원."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 천태민    | **Cheon Taemin**  |
| 무신     | **Martial God**               | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 남만야수궁  | **Nanman Beast Palace**          |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 사숙     | **Martial Uncle**                            |
| 상태               | **Status**                     |
| 로그인              | **Login**                      |
| 대격변     | **Great Cataclysm**   |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 혈승 | **Blood Monk** | Sobriquet of the unidentified bald martial artist active in Guizhou. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 추혼객 | **Soul-Chasing Guest** | Song Ilseom’s former epithet; he was known by it ten years earlier. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 진수 | **Jinsu** | Named budding talent who receives Taekyung's autograph. |
| 귀주 | **Guizhou** | Region whose Murim representatives send a delegate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |

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
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 문경 | 남천마후 | legendary_assassin_to_hostile_demon_empress | you | polite and grave | Warns her to stop the killing. |
| 문경 | 혁무진 | traveling_companion_to_traveling_companion | Martial Warrior Hyuk | formal-polite | Mungyeong asks Mujin to deliver water to Taekyung and lets Mujin receive the credit. |
| 혁무진 | 문경 | traveling_companion_to_traveling_companion | Mungyeong | casual-familiar | Mujin recognizes Mungyeong while reacting to Taekyung's dismantling work. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
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
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 646
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle; he opposes the Nanman Beast Palace joining the Murim Alliance, attacked Jin Taekyung at the tribal grand council, withdrew with the pro-Baeksang faction after being stopped, and may resent the orthodox Murim over the loss of his only child or be secretly aligned with Dark Heaven.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 646
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, and a master among the Ten Kings.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is responsible for the forces stationed at Ailao Mountain, and has ordered scouts toward Guizhou because of the possible Blood Monk threat.

### Blood Monk.md

# Blood Monk (혈승)

- **Safe through:** Chapter 646
- **Aliases:** None
- **Role:** The Blood Monk is an unidentified, apparently middle-aged bald and beardless martial artist who carries a steel Zen staff and has killed several hundred people in Guizhou; his current destination is unknown.
- **Personality:** Unknown; the captured witness who described him was unable to provide further information before dying.
- **Voice:** Not established.
- **Relationships:** His connection to Dark Heaven and Nanman is unknown.

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 607
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 644
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 645
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung is foolish, easily flattered, and politically dependent on stronger personalities despite leading a powerful tribe.
- **Voice:** Heugung speaks with warm enthusiasm and exaggerated devotion toward Yohi.
- **Relationships:** Yohi and Baeksang keep Heugung under their control, while Heugung responds to Yohi's manipulation with apparent infatuation.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 646
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 640
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 645
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 645
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 646
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, an experienced Nanman escort guide with route knowledge from the Escort King's records, someone who can understand the Miao and Bai languages, and a volunteer accepted for the scouting mission to investigate the Blood Monk in Guizhou.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 626
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 635
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; he was the sole survivor of an assassin training cohort that began with three hundred candidates and passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung and has now ended that direct training after teaching him martial principles and giving him a custom fire-qi pill, Cheongpung is accompanying him while learning his martial arts through observation, and Mu Song plus five Water Dragon Stronghold subordinates know he is an exceptionally powerful master but not that he is the Slaughter Saint.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 646
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 646
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 646
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 646
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 646
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 645
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, and manipulates Heugung alongside Baeksang.

## Korean source

```text
＃647화



연회가 벌어진 장소는 내궁(內宮) 안에 존재하는 커다란 연무장이었다.

천여 명의 전사들을 수용할 수 있다는 그곳에는 온갖 진수성찬이 차려졌고 부족장을 위시한 사람들로 붐볐다.

그리고 연무장의 가장 상석에서, 한 사람이 나를 기다리고 있었다.

“왔군.”

호랑이 가죽으로 장식된 태사의(太史椅)에 앉아 있던 야수묘왕이 날 발견하고 손짓했다.

“앉거라. 자리를 마련해 두었으니.”

내가 배정받은 자리는 야수묘왕의 바로 옆, 왼쪽 자리였다.

외부인이라는 걸 감안하면 파격적인 대우였지만, 사실 내 신분이나 지난 밤에 세웠던 공을 생각하면 그리 이상한 일도 아니다.

물론 그렇다고 해서 화룡각 대원들 모두가 나와 같은 대접을 받는 것도 아니었지만.

“이번 연회에는 그대들의 자리도 정해 두었다. 마음껏 먹고 마시며 즐기…….”

“태산이! 고기!”

덥석! 와구와구!

대뜸 탁자 앞의 고기를 쓸어 담는 태산의 모습에, 야수묘왕이 황당한 눈빛으로 나를 바라보았다.

“……이놈은 도대체 뭐지?”

“……그냥 미친놈입니다. 너무 신경 쓰지 마세요.”

내 눈짓에 한숨을 푹 내쉰 태산맘, 아니 사마표가 태산을 붙들더니 질질 끌고 갔고, 살수처럼 호시탐탐 기회를 노리던 남호는 가까이에 있는 술병을 잡아 태산의 정수리를 갈겼다.

콰창!

‘물도 없는 곳에서 저 정도의 수둔을……?’

저 정도면 아주 작정하고 후린 건데.

하지만 태산은 머리 위에서 터진 술 분수를 받아 마시며 해맑게 외쳤다.

“남호! 고맙다! 태산이 마침 목말랐다!”

“죽어. 제발 죽어……!”

그 모습을 지켜보던 야수묘왕이 떨떠름한 시선으로 나를 응시했다.

“음. 수하들이 아주 사이가 좋군.”

“좋죠. 둘 중 하나가 죽어도 모를 만큼.”

“그래서 저들을 보내지 않은 건가?”

잠시 멈칫한 내가 대답했다.

“들으셨습니까? 소식이 빠르네요.”

“나는 모든 일에 관여하지는 않지만 모든 소식을 들을 수 있지. 남만야수궁의 궁주는 그런 자리다.”

하긴, 척후대에 외부인들이 끼었으니 부족장들을 통해 이미 보고가 올라갔어도 이상하지 않다.

나는 지금쯤 북동쪽 어딘가로 향하고 있을 세 사람을 떠올리며 내심 중얼거렸다.

‘괜찮을까.’

내가 심사숙고 끝에 선별한 인원은 총 셋이었다.

주화란. 송일섬. 그리고 혁무진.

내 걱정과는 별개로 주화란은 또래의 후기지수들에 비해 뛰어난 무위와 경험의 소유자고, 송일섬은 말할 필요도 없으며, 마지막 멤버인 혁무진은…….

‘다른 건 몰라도 생존력 하나는 바퀴벌레지.’

저래 보여도 혁무진은 산서성에서부터 지금까지, 나와 함께 숱한 전장에서 죽음의 위기를 헤쳐 나온 녀석이다.

얼마나 요리조리 잘 살아남는지, 언제 한 번은 적천강이 이렇게 말한 적도 있었다.



‘저렇게 약해 빠지고 겁 많은 놈이 지금까지 어떻게 살아남은 거냐?’



그래서 나는 이렇게 대답했다.



‘약하고 겁이 많아서 살아남은 거죠.’



혁무진의 무공이 다른 이들에 비해 떨어지는 것은 사실이다. 겁이 많다는 것도 틀린 말이 아니다.

하지만 그건 조심성이 많다는 의미로도 해석될 수 있었다.

‘가장 위험한 곳은 귀신같이 피해 가고, 피할 수 없을 때는 죽을힘을 다해 싸우고.’

그러니 매번 살아 돌아올 수밖에. 별호를 혁퀴벌레로 바꿔도 이상하지 않다.

“그들은 잘해 낼 겁니다. 무슨 일이 벌어져도.”

개인적인 바람을 담아 중얼거린 나는 문득 야수묘왕의 어깨너머를 바라보았다.

“그나저나 자리가 많이 비었네요. 연회가 이미 시작되었는데도.”

“늦지 않게 곧 올 것이다.”

말은 그렇게 했지만 야수묘왕의 눈빛은 무겁게 가라앉아 있었다. 특히 텅 비어 있는 바로 오른편의 자리를 바라볼 때는 더욱 그랬다.

‘백상.’

그를 따라 대전을 나섰던 부족장들은 이미 착석해 있었으나 백상과 요희, 흑웅은 아직 돌아오지 않은 상태다.

유심히 그들의 빈 자리를 바라보던 야수묘왕은 말없이 술병을 기울였다.

또르륵.

해는 이미 서산(西山)으로 기운 지 오래.

하지만 남만야수궁의 전경은 어둠 속에서도 환하게 빛나고 있었다. 곳곳에서 벌어지는 축제 때문이다.

일 년에 단 한 번 열리는 부족 대회의는 화합의 장이기도 했고, 거리로 쏟아져 나온 수많은 부족민은 밝은 얼굴로 웃고 떠들며 즐겼다.

아니, 아마 그러고 있을 것이다. 당장 보이지는 않지만, 외궁(外宮)으로부터 들려오는 환호와 폭죽 소리만으로도 충분히 짐작할 수 있었다.

쉬익, 퍼버벙!

와아아아아-!

소리만 들으면 최소 삼바 페스티벌인데.

나는 떨떠름한 표정으로 야수묘왕에게 물었다.

“그, 뭐. 이래도 되는 겁니까?”

“뭐가 말이냐?”

“죄다 기억 상실증에 걸린 것 같아서요. 겨우 하루 전에 애뇌산에서 무슨 일이 벌어졌는지 다들 알고 있을 텐데.”

야수묘왕이 대수롭지 않은 표정으로 대답했다.

“알지. 그러니 더욱 성대한 축제를 벌이는 것이다.”

“저게요?”

“그래. 그들은 하나같이 용맹한 전사였고, 남만을 위해 싸우다가 죽었다. 그러니 저마다 각 부족이 믿고 있는 신의 품으로 돌아갔을 거라 믿는 게지. 비록 이승에서는 죽었으나 신의 전사로 거듭났을 거라 생각하면서.”

“…….”

이거 어디서 많이 들어 본 얘기인데.

갑자기 로그인 전에 때려잡은 중동 테러 단체가 생각난다.

‘무슨 십자군이나 고대 바이킹들도 아니고.’

중원에도 온갖 미신이 판을 치긴 하지만, 확실히 남만은 수많은 토착 신앙이 존재하는 곳이라 그런지 확연한 차이점이 있었다.

물론 21세기에서 나고 자란 나로서는 영 이해가 가지 않았지만.

“야율 대협도 그렇게 생각하십니까?”

내 물음에 술잔을 기울이려던 야수묘왕이 피식 웃었다.

“재미있군.”

“뭐가요?”

“그럴 만도 하지 않느냐. 남만에서 나고 자란 묘족 늙은이, 그것도 감히 남만야수궁주에게 이런 질문을 한다는 것이.”

“아.”

“하지만 웃음이 나온 건 다른 이유 때문이다. 아주 오래전, 다른 누군가에게도 너와 같은 질문을 받았던 것이 생각나서였지.”

이 정도면 대충 감이 온다. 나는 그럼 그렇지, 하는 눈빛으로 입을 열었다.

“저희 노야, 아니 스승님이요?”

“적 노? 아니다. 그분은 토착신들의 존재 유무에는 관심도 없었어. 다만 마교도 놈들이 남만에 불을 낸다면 불러 달라고 하신 적은 있었지. 한 번 정도는 기쁜 마음으로 도와주겠다면서.”

“…….”

그 엉덩이 무거운 양반이 출장 살육까지 약속하다니. 구화산의 원한이 아주 뼛속 깊숙이 사무쳐 있던 모양이다.

반사적으로 고개를 끄덕인 내가 되물었다.

“그럼 누가 그런 질문을 한 겁니까?”

그리고 다음 순간 들려온 야수묘왕의 대답은, 실로 간단명료하면서도 의문투성이였다.

“신(神).”

“예? 뭐요?”

이해할 수 없는 대답에 순간 멍해진 그때, 야수묘왕이 가득 채워진 술잔을 어루만지며 말을 이었다.

“무신(武神). 이름도, 나이도, 심지어는 얼굴조차 제대로 알려지지 않은 자. 사람으로 태어나 그 이상의 존재로 거듭난 신인(神人). 그분께서 내게 물으셨다. 그대의 신이 진정 존재하리라 믿느냐고.”

“……!”

“그래서 나는 대답했지. 사실 잘 모르겠습니다. 하지만 지금 마주하고 있는 것 같습니다.”

술잔에 담긴 초승달이 출렁인다. 술과 달을 한입에 털어 넣은 야수묘왕이 소리 내어 웃었다.

“멍청한 대답이었지만, 그럴 수밖에 없었다. 그날 무신께서는 초절정의 경지에 오른 다섯 명의 마두와, 오백의 혈귀대(血鬼隊)를 홀로 쓰러트리셨으니까. 그것이 신선처럼 새하얀 수염을 휘날리던 그분과의 첫 만남이었고, 마지막이 되어 버린 두 번째 만남에서는 앳된 소년의 모습을 하고 계셨지.”

“……”

“어언 오십여 년이 흘렀건만, 아직도 그날의 기억이 또렷하게 기억나는구나.”

입을 벌린 채 이야기를 듣던 나는 말문이 막혔다.

혈귀대. 익히 들어 본 이름이다. 적천강이 라떼썰을 풀 때마다 한번 등장했던 이름이기도 했으니까.

십만 마병의 선두에서 중원을 휩쓸던 마교의 대표 타격대인 혈귀대는 한 사람, 한 사람이 절정 고수로 이루어져 있다고 했다.

‘오백여 명의 절정 고수. 거기에 더해 초절정의 경지에 이른 마두가 다섯.’

그런데 그 엄청난 전력을 단신으로 괴멸시켰다니.

아무리 야수묘왕이 한 말이라 해도 단순한 헛소리로 치부했을 것이다. 그 앞에 붙은 무신이라는 두 글자가 아니었다면.

‘……도대체 어느 정도지?’

적천강. 문경. 매종학. 기타 등등.

나는 이 유구한 무림사에서 거인(巨人)이라 칭해도 부족함이 없는 이들에게 무신에 관한 이야기를 귀에 피가 나도록 들었다.

하지만 아직도 모르겠다. 그가 도무지 어느 정도의 경지에 오른 고수인지. 아니, 정말 사람이 맞기는 한 것인지.

그리고…… 그토록 위대하고도 대단한 존재가 왜 어느 날 돌연 자취를 감추었으며, 지금 이 순간 어디에서 무엇을 하고 있는지.

꼬리에 꼬리를 물고 이어지는 생각. 더불어 동시에 문득 떠오르는 한 사람의 이름.

‘……잠깐.’

순간, 생각과 함께 탁자를 두드리던 손가락이 우뚝 멈췄다.

반사적으로 크게 뜨인 눈이 향한 곳은 바로 앞에 펼쳐진 연회장도 아니고, 무림도 아니었다.

저 멀리서 불어오는 후텁지근한 바람과 공기. 그리고 말로는 설명할 수 없는 어떤 미지의 영역 너머에 존재하는 또 다른 세상과 그곳에 존재하는 한 사람이다.

‘천태민.’

마왕 아스모데우스로부터 인류를 구원한 구세주. 불멸의 신화이자 자신의 추종자들에게는 살아 있는 신으로 불리는 남자.

그러나 어느 날 세상으로부터 단절되어 깊은 잠에 빠진 존재.

이 순간 내 머릿속에 천태민이 떠오른 이유는 명백했다.

‘닮았다. 무신과.’

단순한 착각일 수도 있지만, 별것 아닌 일처럼 넘어가기에는 두 사람의 공통점이 너무나도 많았다.

정마대전과 대격변에서의 활약, 그 직후에 보여 준 행보까지.

‘설마? 아니. 아니야. 그건 불가능할 텐데.’

하지만 내 생각은 더이상 이어지지 못했다. 어느덧 멈춘 악공들의 흥겨운 연주와 무희의 춤사위, 그리고 사람들의 시선을 한 몸에 받으며 계단을 오르는 한 사람 때문이었다.

“어서 오게, 아우.”

의형제인 야수묘왕의 환대에, 마치 궁주처럼 양옆에 대족장들을 거느린 백상이 대답했다.

“늦었습니다, 궁주.”

상념에서 깨어난 나는 마침내 마주할 수 있었다.

사방을 얼려 버릴 듯한 그의 냉담한 시선을.



* * *



- 연회가 시작되었습니다.

- 평소보다 외궁의 경비가 강화되었습니다.

- 내궁에 속한 정예 전사 이백여 명이 북문을 통해 이동 중입니다.

연달아 귓가를 파고드는 수하들의 전음에, 어둠에 파묻힌 누군가가 자리에서 일어났다.

- 마지막 보고. 목표는?

- 귀주의 혈승(血僧)입니다. 표적들은 척후와 만일의 전투를 목적으로 이동 중이며, 진태경의 지시로 용봉표국의 소국주 주화란과 추혼객 송일섬. 그리고 태원진가의 혁무진이 포함되어 있습니다.

극소수만이 알고 있는 송일섬의 과거를 알고 있다는 것은 놀라운 일이었지만, 그림자와 그의 수하들에게는 아니었다.

“하.”

작게 소리 내어 웃은 그림자의 신형이 빙글 돌아섰다.

딱. 어둠 속에서 맞부딪친 손가락이 소리를 냄과 동시에, 한 줄기 불꽃이 어둠을 밝히며 피어 올랐다.

화륵.

어둡고, 불길한 적갈색의 불꽃. 일렁이는 그것을 보며, 남천마후(南天魔后)는 싱긋 웃었다.
```

## Final English reading copy

```markdown
# Chapter 647

The banquet was being held in a large training ground inside the Inner Palace.

The place was large enough to accommodate more than a thousand warriors. Every kind of delicacy had been laid out, and the grounds were packed with people, including the tribal chieftains.

And at the most honored seat in the training ground, someone was waiting for me.

“You’ve arrived.”

The Beast Miao King, seated in a tiger-skin-decorated high-backed chair, spotted me and beckoned.

“Come sit. I had a place prepared for you.”

The seat assigned to me was directly beside the Beast Miao King, on his left.

It was an extravagant show of favor for an outsider, but when I considered my status and what I had accomplished the previous night, it wasn’t all that strange.

Of course, that didn’t mean every member of the Fire Dragon Pavilion was being treated the same way.

“I’ve prepared places for all of you at this banquet as well. Eat, drink, and enjoy your—”

“Taishan! Meat!”

Grab! Chomp, chomp, chomp!

At the sight of Taishan suddenly sweeping up all the meat in front of him, the Beast Miao King stared at me with an utterly baffled expression.

“……What in the world is that fellow?”

“……He’s just insane. Don’t pay him too much attention.”

At my glance, Taishan’s mom—no, Sama Pyo—let out a deep sigh, grabbed Taishan, and dragged him away. Meanwhile, Namho, who had been lurking like an assassin and watching for an opportunity, seized a nearby wine bottle and smashed it against the top of Taishan’s head.

Crash!

*Water Style without any water……?*

He had really put his whole body into that swing.

But Taishan drank from the fountain of wine bursting over his head and shouted brightly,

“Namho! Thank you! Taishan was thirsty!”

“Just die. Please, just die……!”

The Beast Miao King watched the scene with an uncomfortable look.

“Hmm. Your subordinates are very close.”

“They are. Close enough that neither of them would notice if the other died.”

“Is that why you didn’t send them?”

I paused for a moment before answering.

“You heard about it? News travels fast.”

“I may not involve myself in every matter, but I can hear every piece of news. That is the position of the Palace Lord of the Nanman Beast Palace.”

He had a point. Since outsiders had joined the scouts, it wouldn’t have been strange for a report to have already reached him through the great chieftains.

I thought of the three people who should be heading somewhere northeast by now and muttered inwardly.

*I wonder if they’re all right.*

After much deliberation, I had selected three people in total.

Ju Hwaran. Song Ilseom. And Hyuk Mujin.

Regardless of my concerns, Ju Hwaran possessed exceptional martial prowess and experience compared to other young prodigies. Song Ilseom needed no explanation, and the last member, Hyuk Mujin, was……

*Whatever else you could say about him, he had the survival instincts of a cockroach.*

Despite how he looked, Hyuk Mujin had survived countless battlefields alongside me, from Shanxi Province to the present day, escaping death at every turn.

He was so good at wriggling his way out of danger that Jeok Cheongang had once said,

*How has someone so weak and cowardly managed to survive this long?*

And I had answered,

*Because he’s weak and cowardly.*

It was true that Hyuk Mujin’s martial arts were inferior to those of the others. And it wasn’t wrong to call him cowardly.

But that could also be interpreted as being extremely cautious.

*He avoids the most dangerous places as though he has eyes in the back of his head, and when he can’t avoid them, he fights with everything he has.*

That was why he always came back alive. It wouldn’t have been strange to change his nickname to Hyukroach.

“They’ll do well. No matter what happens.”

I muttered that with a personal wish behind it, then glanced over the Beast Miao King’s shoulder.

“By the way, there are quite a few empty seats. Even though the banquet has already begun.”

“They’ll be here soon.”

He said it casually, but the Beast Miao King’s eyes had grown heavy and dark. This was especially true whenever he looked at the empty seat directly to his right.

*Baeksang.*

The chieftains who had left the main hall following him were already seated, but Baeksang, Yohi, and Heugung had yet to return.

The Beast Miao King stared at their empty seats for a while before silently tilting the wine bottle.

Drip.

The sun had already sunk behind the western mountains long ago.

Yet the entire Nanman Beast Palace shone brightly even in the darkness. Festivals were taking place everywhere.

The Tribal Grand Council, held only once a year, was also an occasion for unity, and the countless tribespeople who had poured into the streets were laughing and talking with bright faces as they enjoyed themselves.

Or, at least, they probably were. I couldn’t see them from here, but the cheers and firecracker explosions drifting over from the Outer Palace were more than enough to tell me.

Whoosh! Boom!

Waaaaaaah!

If I only listened to the noise, I would have thought it was at least a Samba Festival.

I asked the Beast Miao King with an uneasy expression,

“So, um…… Is this really okay?”

“What do you mean?”

“You know. Everyone seems to have amnesia. They all know what happened at Ailao Mountain barely a day ago.”

The Beast Miao King answered with an unconcerned expression.

“They know. That is why they are holding an even grander festival.”

“That?”

“Yes. Every one of them was a brave warrior who fought and died for Nanman. So they believe that each of them has returned to the arms of the god their tribe worships. Though they died in this world, they believe they were reborn as warriors of their god.”

“……”

I had heard something very similar somewhere before.

Suddenly, I thought of the Middle Eastern terrorist group I had beaten up before logging in.

*They aren’t Crusaders or ancient Vikings.*

All kinds of superstitions ran rampant in the Central Plains as well, but Nanman was clearly different. Perhaps it was because so many indigenous faiths existed here.

Of course, as someone born and raised in the twenty-first century, I couldn’t understand it at all.

“Great Hero Yayul, do you believe that too?”

At my question, the Beast Miao King, who had been about to raise his wine cup, let out a short laugh.

“That is amusing.”

“What is?”

“Isn’t it only natural? You asked that question of an old Miao man born and raised in Nanman—and of the Palace Lord of the Nanman Beast Palace, at that.”

“Oh.”

“But I laughed for another reason. It reminded me of someone else who asked me the same question a very long time ago.”

I had a pretty good idea by then. I opened my mouth with an expression that said *of course*.

“My Old Master—no, my Master?”

“Old Jeok? No. He had no interest in whether the indigenous gods existed or not. He once told me to call him if those Demonic Cult bastards ever set Nanman on fire, though. He said he would gladly come help at least once.”

“……”

That old man, who hated going anywhere, had actually promised to travel out and slaughter people. His grudge against Mount Jiuhua must have been carved into his bones.

I reflexively nodded and asked,

“Then who asked you that question?”

The Beast Miao King’s answer, which came the next moment, was simple and clear—and filled with questions.

“God.”

“Sorry? What?”

As I stood there, momentarily dumbfounded by the incomprehensible answer, the Beast Miao King continued while stroking his full wine cup.

“The Martial God. Someone whose name, age, and even face are not properly known. A divine man who was born human and became something beyond humanity. That person asked me whether I truly believed my god existed.”

“……!”

“So I answered, ‘I honestly don’t know. But I think I may be looking at one right now.’”

The crescent moon reflected in his wine cup rippled. The Beast Miao King downed the wine and moon together, then burst into laughter.

“It was a foolish answer, but I had no choice. That day, the Martial God defeated five fiends who had reached the Supreme Peak realm and five hundred members of the Blood Ghost Squad all by himself. That was my first meeting with him, when he wore a white beard that fluttered like an immortal’s. During our second and final meeting, he had the appearance of a young boy.”

“……”

“More than fifty years have passed, but I still remember that day as clearly as ever.”

I listened with my mouth hanging open, unable to speak.

The Blood Ghost Squad. It was a name I had heard many times before. It also came up whenever Jeok Cheongang launched into one of his “back in my day” stories.

The Blood Ghost Squad had been the Demonic Cult’s premier strike force, sweeping across the Central Plains at the head of a hundred thousand demonic troops. Every single member was said to have been a Peak master.

*Five hundred Peak masters. And on top of that, five fiends who had reached the Supreme Peak realm.*

And the Martial God had annihilated that overwhelming force alone.

Even coming from the Beast Miao King, I would have dismissed it as sheer nonsense—if not for the title *Martial God*.

*……Just how powerful was he?*

Jeok Cheongang. Mungyeong. Mae Jonghak. And others.

I had heard stories about the Martial God until my ears bled from people who deserved to be called giants in the long history of the Murim.

And yet I still didn’t know. What kind of realm had that master reached? No—was he even human at all?

And…… why had such a great and extraordinary being suddenly vanished without a trace one day, and where was he now? What was he doing?

My thoughts followed one another in an endless chain. Along with them, another person’s name suddenly came to mind.

*……Wait.*

The fingers tapping against the table stopped dead.

My eyes flew open, but they were not looking at the banquet hall before me. Nor were they looking at the Murim.

They were looking beyond the hot, heavy air blowing in from far away—beyond some unknown realm that could not be explained in words—to another world and the person who existed there.

*Cheon Taemin.*

The savior who had rescued humanity from the Demon King Asmodeus. An immortal legend and a living god to his followers.

And yet he was a being who had become cut off from the world one day and fallen into a deep sleep.

The reason Cheon Taemin had come to mind at that moment was obvious.

*They were alike. Cheon Taemin and the Martial God.*

It might have been a simple mistake, but there were too many similarities between them to dismiss it as nothing.

The Martial God’s exploits in the Great Faction War and Cheon Taemin’s in the Great Cataclysm—even their actions immediately afterward.

*No way. No. No, that’s impossible.*

But my thoughts could go no further.

The lively music of the musicians had stopped. So had the dancers’ movements. Everyone’s attention had turned toward one person as he climbed the stairs.

“Welcome, little brother.”

In response to the Beast Miao King’s welcome, Baeksang answered from between the great chieftains on either side of him, as though he were the Palace Lord himself.

“I’m late, Palace Lord.”

Snapping out of my thoughts, I finally met his cold gaze, which seemed capable of freezing everything around him.

* * *

*The banquet has begun.*

*The Outer Palace’s security has been reinforced.*

*More than two hundred elite warriors belonging to the Inner Palace are moving through the North Gate.*

As the Sound Transmissions from his subordinates pierced the darkness one after another, someone buried in the shadows rose from their seat.

*Final report. What is the target?*

*The Blood Monk of Guizhou. The targets are moving for reconnaissance and possible combat. At Jin Taekyung’s order, the group includes Ju Hwaran, the Young Bureau Head of the Yongbong Escort Bureau; Song Ilseom, the Soul-Chasing Guest; and Hyuk Mujin of the Jin Family of Taiyuan.*

Knowing Song Ilseom’s past, which only a select few knew, would have been remarkable—but not when it came to the Shadow and his subordinates.

“Ha.”

After letting out a quiet laugh, the Shadow turned around in one smooth motion.

Snap.

As fingers clicked together in the darkness, a strand of flame blossomed and illuminated the shadows.

Fwoosh.

It was a dark, ominous reddish-brown flame.

Watching it flicker, the Southern Heaven Demon Empress smiled.
```
