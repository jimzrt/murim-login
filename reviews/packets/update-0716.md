<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0716.txt",
      "sha256": "62eb124128bb98b2f745b084f7592c8e0a55a2660f1ba9f16cece6d988b87397",
      "bytes": 12728
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "847dffbd3be2e8237465e6a86c96173c3db562a9e035c3e1f7708b218f761ba7",
      "bytes": 1279
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "253e9b5288386051c82bc2373ba82835eacd1d4a307dbac220c69208d60acf41",
      "bytes": 208264
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "dd8a09e55f5e909659a8f85b6a12ce07f66f6393b874b279e9ae7483ff60428d",
      "bytes": 935
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "fa4135033ddc965340df62e394b914b8e4ff97eddf1d19228631619467471443",
      "bytes": 785
    },
    {
      "path": "characters/Blood Monk.md",
      "sha256": "fd650d608e61b637513cf3317e3dc471e01b8fac63ab4c9eb081319b9f752263",
      "bytes": 542
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "1e9c9d1207e1e18f3c9c3c868684b2a6799b45c97a48d0b9962dbc96db2db0aa",
      "bytes": 1355
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "7a4c339d655f0de010ec2735a12b17077c6b169a0af1923ff8688fb8d1948ab2",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fb47ed6242a090feb6ee4f767eddae77f093e86d35e8c86493569d1f32f85e88",
      "bytes": 1787
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c2de11ce5e9e3fe5d320cfbc9f5b0fa97232d3ae9fd9d220bc203d5ca24ba665",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "b444f39bdb181d7814da9a2d9a9ef2ce11253fb03785b38a79d2ff48312eb074",
      "bytes": 937
    },
    {
      "path": "characters/Namho.md",
      "sha256": "fe47b86beb6065bdfb584907607dcc1372da883ca3dd2a237debb9171ba0924e",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "71101b39bdde05804b180ad6d58626a7a32bdb376c35f14e5ec4f104ce3515bf",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "2e98057f1affc09965568d7d7907b2507cbf3f2f294c76123631378cefd84448",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "9833f3fa87185ad0740b19206d8626684959600fc80aee2a8ec1338108a12480",
      "bytes": 1074
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "ae2f2841300b08f04b8851d95ba538ef1cccb576b14fee7c5aee4a909bba1025",
      "bytes": 715
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "6f07679fad2db0aafba0c644052881bb0c1ed9293eccb72e2f33ded2ead21420",
      "bytes": 787
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "37fe224dbdecc47e43c7f2201fd82e83c0a2013df74a7bb4f20200b251a6ca5c",
      "bytes": 864
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "0c63bcd3de1becca860594b89310b22e606b19ee4b9c84657a5302c2127a6dbb",
      "bytes": 621
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "04e05b397803c14da83d4095d0d350b37c1f097208d8c3b5761113c8a8df99c4",
      "bytes": 218560
    }
  ],
  "estimated_tokens": 15942
}
-->

# Durable State Update — Chapter 716

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 716. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 716. Profile updates may replace only one
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
  "chapter": 716,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 716,
    "continuity_sources": [716],
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
    "Jin Taekyung has awakened after seven days and nights and has regained his physical clarity and strength.",
    "Jin remembers the deaths at the Inner Palace and is struggling with survivor's guilt over failing to save everyone.",
    "Jeok Cheongang recognizes Jin's guilt and advises him to value survival and mourn the dead.",
    "Jeok Cheongang remains quietly protective of Jin while hiding concern behind gruff teasing and threats.",
    "The Fire Dragon Pavilion members are reunited around Jin in Nanman.",
    "Taishan's enthusiastic arrival destroyed the door and damaged Jin's quarters.",
    "Ju Hwaran is active and present with the Fire Dragon Pavilion.",
    "Ju Hwaran has taken control of the disorder by forcefully demanding proper behavior around Jin."
  ],
  "continuity_sources": [
    715
  ],
  "open_questions": [],
  "safe_through": 715,
  "temporary_decisions": [
    "Retain Old Master for 노야 when Jin addresses Jeok Cheongang.",
    "Retain established renderings of Flame Divine Palm, Flame-Extinguishing Divine Fist, Dance of the Fire God and Demon, Solar Fist, Force, and Skill.",
    "Render 남만당 as Nanman Party.",
    "Render 각주 as Pavilion Master when Taishan addresses Jin."
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
| 십왕     | **Ten Kings**       |
| 남만야수궁  | **Nanman Beast Palace**          |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 표국     | **Escort Bureau**                            |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 혈승 | **Blood Monk** | Sobriquet of the unidentified bald martial artist active in Guizhou. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 정기 | **vital essence** | Energy the Wudang Sect Leader says the monster absorbs from victims. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 소궁주 | **Young Palace Lord** | Title used for Yayul Mok as heir of the Nanman Beast Palace. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 백천대 | **Baekcheon Unit** | Baeksang's secret elite unit, cultivated over decades and held in reserve. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |
| 백천 | **Baekcheon** | Name of the old silk cloth Jin uses to cover Baeksang's face. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
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
| 관리 | 적천강 | government official to legendary martial master | you | formal, then alarmed and deferential | The official questions Jeok Cheongang, insults him as an old man, and later learns that he is the Fire King. |
| 적천강 | 관리 | legendary martial master to government official | you | blunt and mocking | Jeok Cheongang repeatedly echoes the official's formal phrasing while challenging his authority. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
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
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 야율목 | 백상 | nephew_to_father's_sworn_younger_brother | Uncle Baeksang | ceremonial and deferential | Yayul Mok formally greets Baeksang as he arrives at the stone door. |
| 백상 | 야율목 | father's_sworn_brother_to_nephew | you | cold and formal | Baeksang questions Yayul Mok about his return, the pasture fire, and the Palace Lord's whereabouts. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
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
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 야수묘왕 | 남천마후 | allied_Ten_Kings_master_to_hostile_Demon_Empress | you | cold and threatening | The Beast Miao King addresses the Southern Heaven Demon Empress while promising to tear off her limbs and kill her. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 714
- **Aliases:** None
- **Role:** Baeksang was the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman, and he died by the Beast Miao King's hand after confessing to serving Dark Heaven's plan.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of Baekhwi, whom he believed the Great Snow Fiend killed but Dark Heaven has kept alive in a deep sleep; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 714
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang was his sworn younger brother and childhood companion, and the Beast Miao King killed him at his request; Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple and ally.

### Blood Monk.md

# Blood Monk (혈승)

- **Safe through:** Chapter 715
- **Aliases:** Jeok Cheongang; Fire King
- **Role:** The Blood Monk is Jeok Cheongang, the Fire King and legendary martial master who uses a steel Zen staff and the Flame Divine Palm.
- **Personality:** As Jeok Cheongang, the Blood Monk is gruff, blunt, protective toward his Disciple, and prone to profane mockery.
- **Voice:** Not established.
- **Relationships:** His connection to Dark Heaven and Nanman is unknown.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 715
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 715
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 715
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 715
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 715
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 715
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 715
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 665
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 665
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 714
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 715
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 689
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger and speaks Han Chinese haltingly but capably.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and his father, Baeksang is his father's sworn younger brother, and Yayul Mok has risked his position and life to rescue Jin Taekyung, entrusting Muyaho to Jin while he remains behind with the Seven Miao Tigers.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 708
- **Aliases:** None
- **Role:** Yohi is the female Great Chieftain of the Yao people who has returned to the Nanman Beast Palace with Jin Taekyung and now stands against Baeksang.
- **Personality:** Yohi is charismatic, proud, perceptive, and fiercely resistant to Heugung's betrayal and coercion.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, hates Heugung after his betrayal, and is being coerced to support his false account by the threat against Boshan and her people.

## Korean source

```text
＃716화



누가 그랬다. 원래 조용하던 사람이 화를 내면 더 무서운 법이라고.

지금 주화란의 모습이 딱 그랬다.

투두둑.

용봉표국의 금지옥엽이자, 쉰내를 풍기다 못해 맵기까지 한 이 할라피뇨 고추 파티를 환기시켜 주던 인간 공기 청정기의 손에서 목재 파편이 우수수 쏟아진다.

항상 부드럽던 눈매와 목소리는 어느새 가시처럼 뾰족해져 있었다.

“태산 소협.”

첫 타깃이 된 태산이 몸을 움찔 떨었다.

“각주님께서, 진 공자가 우리를 위해서 얼마나 고생하셨는지 몰라요? 그런데 어떻게 그런 소릴 할 수 있어요?”

“태, 태산이 잘못했다.”

“아무리 식탐이 강해도 그렇지, 한 번만 더 불길한 소리 하면 그땐 진짜 남 노야 말대로 재갈을 물릴 거예요.”

주화란의 엄중한 경고에 사마표가 미간을 좁히며 입을 열었다.

“주 소저, 태산이는 짐승이 아니오.”

“그럼 태산 소협 대신 그쪽한테 재갈을 물리면 되나요?”

“…….”

“대답은요.”

잠시 생각하던 사마표가 진중한 얼굴로 입을 열었다.

“그, 생각해 보니 식단 관리 차원에서 가끔 재갈을 물리는 것도 나쁘지 않을 것 같소.”

“앞으로 조심하세요. 악의가 없다는 건 알지만 너무하잖아요.”

“……알겠소. 내 잘 타이르지.”

자신이 발의한 입마개 법안이 아슬아슬하게 무효로 돌아가자, 남호가 안타까운 목소리로 중얼거렸다.

“내가 죽기 전에 저놈한테 재갈 물리는 건 봐야 하는데…….”

하지만 그런 남호 역시, 주화란의 타깃이 되는 건 피하지 못했다.

“남 노야.”

“어, 엉?”

“어르신이면 어른답게 행동하셔야죠. 아직 회복되지도 않은 환자 앞에서 험한 욕 하시는 것도 보기 안 좋아요.”

“뭐? 환자?”

빵빵한 레벨 업과 그간의 휴식으로 윤기가 자르르 흐르는 내 얼굴을 바라본 남호가 떨떠름한 표정을 지었다.

“아니, 그건 둘째 치고 진태경 저놈보다 더한 욕쟁이가 어디 있다고 갑자기 나를…….”

툭.

그 순간, 나는 똑똑히 봤다.

억울한 목소리가 이어지려던 그때, 옆에 있던 혁무진이 슬쩍 팔꿈치로 남호의 옆구리를 찌르는 모습을.

그리고 그 작은 몸짓에 담긴 뜻을 현대식으로 재해석하자면 이랬다.

‘분위기 망치지 말고 ㄹㅇㅋㅋ만 치십쇼.’

첩보원 짬밥만 수십 년인 남호다.

눈동자를 이리저리 굴리던 그는 체념한 듯 고개를 떨구었다.

“알았다. 내 조심하마.”

“좋아요. 그럼 다음으로 혁 소…… 지금 뭐 하세요?”

“조장님의 노고를 풀어 드리기 위해 어깨를 주물러 드리고 있습니다.”

그래. 괜히 혁퀴벌레가 아니지.

눈치 빠르게 내 몸을 안마하는 혁무진의 모습을 보며 흐뭇하게 웃은 주화란이 남아 있는 한 사람을 향해 고개를 돌렸다.

“송 호위.”

처음부터 지금까지, 시종일관 침묵을 지키던 송일섬의 동공에서 지진이 일어났다.

“난 아무 말도 안 했소만.”

“저도 알아요. 계속 그 자세 유지하세요.”

“……알겠소.”

마지막 타깃까지 처리한 주화란의 시선이 나를 향해 옮겨진다.

그녀와 눈이 마주치자마자 반사적으로 입술이 열렸다.

“죄송합니다. 미안합니다. 잘못했습니다.”

“네?”

“예?”

“뭐가요?”

“아, 아니. 그냥…….”

뭔가 그렇게 해야 할 것만 같은 느낌이다. 생존 본능이라고나 할까.

나는 열심히 다리를 주무르고 있는 혁무진에게 눈빛을 보냈다.

‘무슨 일 있었냐? 주 소저 왜 이래.’

혁무진 역시 눈빛으로 대답했다.

‘주 소저께서 조장님 때문에 워낙 노심초사하셔서 저런 거니까, 그냥 그러려니 하십쇼.’

‘아무리 그래도 그렇지. 공기가 달라, 공기가.’

‘눈치가 없으면 그냥 입이라도 다물고 계세…….’

그때, 주화란이 불쑥 입을 열었다.

“두 분. 지금 뭐 하세요?”

“……!”

“……!”

화들짝 놀란 혁무진의 안마 속도가 두 배는 빨라졌다.

“뭐 하긴요. 저야 계속 조장님 다리 주물러 드리고 있죠. 어이구, 여기 근육이 아주 단단하게 뭉치셨네. 좀 더 세게 할까요?”

문득 이상한 기분을 느낀 나는 조심스럽게 녀석의 팔을 가로막았다.

“됐다. 그만해라.”

“예? 왜요?”

“그, 아니다. 이제 괜찮아.”

“우리 조장님 또 이러신다. 시원하고 좋으시면서.”

“아니. 괜찮다니까. 너도 피곤할 텐데 그만해.”

“어허. 사양하지 마십쇼. 저 혁무진, 조장님의 오른팔로서 뭐든 할 수 있습니다. 주 소저도 보셨죠? 우리 조장님께서 자기 사람을 이렇게 챙기신다니까요.”

그리고 주화란을 보며 껄껄 웃는 혁무진을 향해, 나는 비통한 심정으로 전음(傳音)을 흘려 보냈다.

- 방금 그거 다리 아니다…….

“……!”

- 그러니까 당장 치워, 이 새끼야. 손모가지 분질러 버리기 전에.

잠시 침묵하던 혁무진이 슬그머니 손을 뺐다.

경이로움과 두려움이 뒤섞인 눈빛으로 나를 바라보는 녀석의 뒤통수를 갈겨 주고 싶은 마음이 굴뚝같았지만, 다른 사람들 앞이라 간신히 참았다.

아니, 어쩌면…….

‘음. 아니다. 그건 너무 나갔지.’

내심 작게 중얼거린 나는 모두의 얼굴을 차례대로 눈에 담았다.

불과 며칠 전만 하더라도 두 번 다시 못 만날 수도 있을 거라 생각했던 사람들이다.

그만큼 우리에게 주어진 상황은 최악이었고, 모든 것이 한 치 앞도 내다볼 수 없는 안개 속과 같았다.

하지만 살아서 이렇게 함께 모여 있으니 감회가 새롭다.

그들 중 누구도 죽지 않았다는 사실이 나를 기쁘게 만들었다.

“다행이야, 정말로.”

짧은 침묵을 깨트리는 내 한마디에, 모두가 눈을 동그랗게 떴다. 그리고 이내 희미하게 웃었다.

그것으로 충분했다.

어느덧 조금씩 가까워진 우리는 서로의 마음을 알고 있었다.



* * *



모든 이야기를 듣기까지는 제법 오랜 시간이 걸렸다.

같은 시간을 보냈지만 나와 그들은 각자 다른 장소에서 다른 상황을 겪었고, 그 이야기 속에는 내가 의식을 잃은 채 흘려보냈던 지난 칠 주야의 시간 또한 포함되어 있었다.

“그땐 진짜 죽는 줄만 알았습니다. 조장님도 안 계시고, 저희는 포박되어 있는 상태에서 말로만 듣던 그 혈승이 난데없이 쾌조선에서 딱 내리는데, 와…….”

“적 대협을 알아보지 못했다면 한바탕 전투가 일어났을 거예요. 함께 있던 남만 전사들이 워낙 호전적이어서.”

“그때는 정말 모든 게 끝났다고 생각했다. 네 녀석을 구할 지원군을 데려와도 모자랄 판에, 혈승이라는 대마두가 나타났으니까.”

적천강에게 들었던 것보다는 좀 더 자세한 이야기였다.

혈승의 진짜 정체가 밝혀지자 남만인들은 처음에는 반신반의했으나, 하나도 빠짐없이 눈에 멍이 든 수룡채의 수적들까지 나서서 그가 화왕임을 인증해 주자 전투는 시작되기도 전에 끝났다.

그 후 적천강은 전력을 다해 남만야수궁으로 향했고, 한 걸음 늦게 화룡각 대원들과 척후대의 남만인들이 도착했을 때는 모든 것이 끝나 있었다.

“조장님께서 쓰러지시는 걸 보고 처음에는 정말 돌아가신 줄 알았습니다. 몸은 온통 피투성이에, 주위에는 죄다 핏물과 시체뿐이고…….”

이쯤에서 혁무진의 말을 끊으려고 했다.

내 멀쩡한 몸 상태에 관한 이야기가 나온다면, 누구든 의심을 품지 않을 수 없을 테니까.

하지만 다음 순간, 내가 입을 열기도 전에 주화란의 목소리가 이어졌다.

“그런데 적천강 대협께서 나서서 모두를 안심시켜 주셨어요. 단지 피로 때문에 쓰러지신 거라고.”

나는 설마 하는 마음으로 물었다.

“……혹시 노야, 아니 스승님께서 정확히 뭐라고 하셨나요?”

“음. 글쎄요. 그때 당시에는 다들 워낙 경황이 없어서. 하지만 적 대협께서 때맞춰 도착하신 덕분에 진 공자님께서는 그리 큰 부상을 입지 않았다고 하신 것으로 기억해요. 야율 궁주님도 맞다고 하셨고요.”

남호가 고개를 끄덕이며 말을 받았다.

“천운이지, 천운. 저놈이 아무리 뛰어난 고수라고 해도, 어찌 그 지옥도에서 살아남을 수 있겠느냐. 십왕(十王) 중 둘이 나섰으니 남천마후라 해도 어쩔 수 없었겠지.”

사실과는 조금 다른 이야기.

그러나 나는 말없이 고개를 끄덕여 수긍하는 뜻을 내비쳤다.

이건 명백한 보호다. 내가 가진 비밀을 숨기고, 사람들의 의심을 피할 수 있도록 적천강과 야수묘왕이 손을 쓴 것이다.

‘백천대의 생존자들 역시 입을 다물겠지. 그들은 야수묘왕에게 충성을 바치니까.’

죽음은 곧 침묵이다.

그날의 전투는 주로 내궁에서 이루어졌고, 그 자리에 있던 대부분의 사람들은 죽었다.

살아남은 이들이 입을 열지 않는다면 비밀은 지켜진다.

‘아무리 이들과 가까워졌다고 해도, 그 사실을 말할 수는 없어.’

말로는 설명할 수 없는 현상을 현대에서는 마법, 혹은 기적이라 부르고는 한다.

그러나 이곳, 무림에서는 다르게 불릴 것이다.

‘마(魔).’

이해할 수 없는 괴력난신(怪力亂神)의 힘은, 언제나 사람들의 두려움을 불러일으키기 마련이다.

나는 가급적 시스템이라는 이 능력을 다른 이들에게 알리고 싶지 않았다.

‘이미 엎질러진 물이긴 하지만.’

모르겠다. 나로서는 피할 수 없었던 그 날의 선택이 어떤 결과를 불러올지.

하지만 가장 가까이에서 그 모습을 목격한 사람이 적천강이라서 다행이었고, 야수묘왕 역시 어떤 사람인지 알기에 안심할 수 있었다.

“조장님?”

“어?”

“무슨 생각을 그렇게 하세요?”

상념이 길었던 모양이다.

나는 수상쩍다는 눈빛으로 쳐다보는 혁무진을 향해 손을 내저었다.

“별거 아냐. 잠시 다른 생각이 나서. 계속해.”

“아, 예. 그런데 제가 어디까지 얘기했죠?”

“……너 머리 다쳤냐?”

“아뇨. 누구한테 하도 뒤통수를 얻어맞아서 그런가.”

슬쩍 나를 쳐다봄으로써 ‘누구’의 정체를 명확하게 전한 혁무진이 말을 이었다.

“죽은 이들을 한데 모아 화장(火葬)했다는 말은 이미 한 것 같고. 그 와중에 백상 쪽에 붙어먹었다가 도망친 족장들이 모두 뇌옥에 갇혔다는 건 아시죠?”

“어느 정도는.”

“아, 맞다. 그러고 보니 요희 대족장도 스스로 죄를 청했다 하더라고요.”

“요희도?”

“네. 야율 대협께서는 용서할 뜻을 내비치셨는데, 자진해서 뇌옥에 갇혔다고 하던데요.”

요희가 그렇게까지 행동했다는 건 의외였지만, 한편으로는 당연하다는 생각도 들었다.

비록 뒤늦게 뉘우쳤다고는 하나, 요희 역시 부와 권세를 누리기 위해 백상과 결탁했다. 그녀 역시 죽을 고비를 넘기며 깨달은 바가 많았을 것이다.

‘스스로 선택한 거지. 그게 옳다고 생각했을 테고.’

내심 중얼거린 나는 이어지는 이야기들을 들었다.

폐허가 되어 버린 내궁과 상당한 피해를 입은 외궁을 수복하기 위해 그 어느 때보다 많은 숫자의 남만인들이 남만야수궁에 머무르고 있다는 사실.

그로 인해 소궁주인 야율목 역시 눈코 뜰 새 없이 바쁘다는 것 역시도.

“우선 소식은 전했는데, 바로 올지는 모르겠네요. 요새 그림자도 보기 힘들어서.”

“아마 그렇겠지. 아마 야수묘왕도 마찬가지일 거고.”

“야율 대협은…… 저희뿐만 아니라 다른 사람들 눈에도 안 보일걸요?”

“뭐?”

“이틀 전부터 자취를 감추셨어요. 이미 수뇌부는 난리라던데.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 716

They say that when someone who is usually quiet gets angry, they become even more frightening.

That was Ju Hwaran right now.

*Crack.*

Wooden fragments spilled from the hands of the Yongbong Escort Bureau’s precious jewel—the human air purifier who had been ventilating this jalapeño pepper party, which not only reeked of old-man funk but had become downright spicy.

Her usually gentle eyes and voice had grown as sharp as thorns.

“Young Hero Taishan.”

Taishan, her first target, flinched.

“Do you have any idea how much the Pavilion Master—Young Master Jin—has gone through for us? How can you say something like that?”

“Taishan was wrong.”

“No matter how strong your appetite is, that’s going too far. If you say anything ominous one more time, I’ll really put a muzzle on you, just like Elder Namho said.”

At Ju Hwaran’s stern warning, Sama Pyo narrowed his brows and opened his mouth.

“Young Lady Ju, Taishan isn’t a beast.”

“Then should I put a muzzle on you instead of Young Hero Taishan?”

“……”

“Well?”

Sama Pyo thought for a moment, then spoke with a serious expression.

“Come to think of it, putting a muzzle on him occasionally for dietary management might not be a bad idea.”

“Be careful from now on. I know you don’t mean any harm, but that was too much.”

“……Understood. I’ll make sure to correct him.”

As the muzzle bill he had proposed narrowly failed to pass, Namho muttered in a sorrowful voice,

“I have to see that bastard muzzled before I die……”

But even Namho couldn’t avoid becoming Ju Hwaran’s target.

“Elder Namho.”

“Huh? What?”

“If you’re an elder, you should act like one. It’s not a good look to curse so harshly in front of a patient who hasn’t even fully recovered yet.”

“What? Patient?”

Namho looked at my face, which gleamed with health after a massive series of level-ups and all that rest, and made a dubious expression.

“No, put that aside for a moment. Where is there a bigger foulmouth than Jin Taekyung? Why are you suddenly coming after me—”

*Tap.*

At that moment, I saw it clearly.

Just as Namho was about to continue in an aggrieved voice, Hyuk Mujin, who was sitting beside him, discreetly jabbed him in the ribs with his elbow.

If I were to reinterpret the meaning behind that small gesture in modern terms, it would be this:

*‘Don’t ruin the mood. Just hit her with a “for real, lol.”’*

Namho had spent decades working as a spy.

His eyes shifted from side to side before he lowered his head in resignation.

“Understood. I’ll be careful.”

“Good. Then, next is Young Hero Hyuk—what are you doing?”

“I’m massaging the Captain’s shoulders to relieve the fatigue from his hard work.”

Right. He wasn’t called Hyukroach for nothing.

Ju Hwaran gave a satisfied smile as she watched Hyuk Mujin massage my body with remarkable awareness, then turned toward the one person who remained.

“Captain Song.”

A tremor ran through Song Ilseom’s pupils. He had remained silent from beginning to end.

“I haven’t said anything.”

“I know. Keep it that way.”

“……Understood.”

After dealing with her final target, Ju Hwaran shifted her gaze toward me.

The moment our eyes met, my lips opened reflexively.

“I’m sorry. I apologize. I was wrong.”

“What?”

“Yes?”

“What are you apologizing for?”

“Ah, no. It’s nothing……”

I just felt like I had to say it. Perhaps it was a survival instinct.

I sent Hyuk Mujin, who was diligently massaging my legs, a look.

*‘What happened? Why is Young Lady Ju acting like this?’*

Hyuk Mujin answered with his eyes as well.

*‘Young Lady Ju was so worried about you that she became like this, so please just let it go.’*

*‘Even so, this is too much. The air is different. The air.’*

*‘If you can’t read the room, at least keep your mo—’*

At that moment, Ju Hwaran abruptly opened her mouth.

“What are you two doing right now?”

“……!”

“……!”

Startled, Hyuk Mujin doubled the speed of his massage.

“What do you mean? I’m just continuing to massage the Captain’s legs. Goodness, the muscles here are really knotted up. Should I press harder?”

Feeling something strange, I carefully stopped his arm.

“That’s enough. Stop.”

“What? Why?”

“Ah, no. It’s fine now.”

“Our Captain is doing it again. You like it because it feels good, don’t you?”

“No. I said it’s fine. You must be tired too, so stop.”

“Don’t be shy. I, Hyuk Mujin, can do anything as the Captain’s right-hand man. Young Lady Ju, you saw that, right? Our Captain takes such good care of his people.”

Then, as Hyuk Mujin laughed heartily at Ju Hwaran, I sent him a Sound Transmission in profound despair.

—That wasn’t my leg just now…

“……!”

—So get your hand off me right now, you bastard. Before I break your wrist.

After a brief silence, Hyuk Mujin slowly withdrew his hand.

I wanted desperately to smack the back of his head as he stared at me with a gaze filled with a mixture of awe and fear, but I barely managed to hold myself back in front of everyone else.

No, perhaps……

*Hmm. No. That would be going too far.*

After muttering inwardly, I took in everyone’s faces one by one.

These were people I had thought I might never see again just a few days ago.

That was how terrible our situation had been. Everything had been shrouded in fog, with no way to see even an inch ahead.

But now that we were all gathered together like this, alive, I was overcome with emotion all over again.

The fact that not one of them had died filled me with joy.

“I’m really glad.”

At my single sentence, which broke the brief silence, everyone’s eyes widened. Then they smiled faintly.

That was enough.

By now, we had grown close enough to understand each other’s feelings.

* * *

It took quite a while to hear the entire story.

We had spent the same amount of time, but they and I had gone through different situations in different places. Their account also included the seven days and nights that had passed while I was unconscious.

“We really thought we were going to die then. The Captain wasn’t there, and we were bound, when that Blood Monk we’d only heard about suddenly stepped off the swift ship. Wow……”

“If we hadn’t recognized Great Hero Jeok, a battle would have broken out. The Nanman warriors who were with us were incredibly aggressive.”

“I truly thought everything was over. We should have been bringing reinforcements to save you, but a great fiend called the Blood Monk appeared.”

It was a more detailed account than the one I had heard from Jeok Cheongang.

When the Blood Monk’s true identity was revealed, the Nanman people were initially skeptical. But the battle ended before it even began when the bandits of the Water Dragon Stronghold, every last one of them sporting bruises around the eyes, stepped forward to confirm that he was the Fire King.

After that, Jeok Cheongang hurried to the Nanman Beast Palace at full speed. By the time the members of the Fire Dragon Pavilion and the Nanman scouts arrived a step behind him, everything was already over.

“When we saw the Captain collapse, we really thought he had died. His entire body was covered in blood, and all around him there was nothing but pools of blood and corpses……”

At that point, I was about to cut Hyuk Mujin off.

If they started talking about the condition of my perfectly healthy body, anyone would have no choice but to become suspicious.

But before I could open my mouth, Ju Hwaran’s voice continued.

“But Great Hero Jeok stepped forward and reassured everyone. He said that you had only collapsed from exhaustion.”

I asked, feeling uneasy.

“……Old Master—no, Master—what exactly did he say?”

“Hmm. I’m not sure. Everyone was in such a panic at the time. But I remember Great Hero Jeok saying that Young Master Jin hadn’t suffered any serious injuries because he arrived in time. Palace Lord Yayul agreed with him, too.”

Namho nodded and joined in.

“It was heavenly luck. Heavenly luck. No matter how powerful that bastard is, how could he have survived that hellscape? Two of the Ten Kings had stepped in. Even the Southern Heaven Demon Empress wouldn’t have been able to do anything.”

It was a story that differed slightly from the truth.

But I silently nodded to show my agreement.

This was unmistakable protection. Jeok Cheongang and the Beast Miao King had taken action to conceal my secret and keep people from becoming suspicious.

*The survivors of the Baekcheon Unit will keep their mouths shut as well. They’re loyal to the Beast Miao King.*

Death meant silence.

The battle that day had taken place mainly in the Inner Palace, and most of the people who had been there had died.

If the survivors didn’t speak, the secret would be kept.

*No matter how close I’ve grown to these people, I can’t tell them.*

In the modern world, phenomena that couldn’t be explained with words were often called Magic or miracles.

But here, in the Murim, they would be called something else.

*Demon.*

Supernatural powers beyond human understanding inevitably inspire fear.

I wanted to keep the System—this ability of mine—as hidden from others as possible.

*Though what was done was done.*

I didn’t know what consequences the choice I had been unable to avoid that day would bring.

But it was fortunate that Jeok Cheongang had been the person who witnessed it from the closest distance. And knowing what kind of person the Beast Miao King was allowed me to feel at ease as well.

“Captain?”

“Huh?”

“What are you thinking about so hard?”

It seemed I had been lost in thought for quite a while.

I waved a hand at Hyuk Mujin, who was watching me suspiciously.

“It’s nothing. Something else just crossed my mind for a moment. Keep going.”

“Ah, yes. But where was I?”

“Did you hit your head?”

“No. Maybe it’s because someone kept hitting the back of it.”

By glancing subtly at me, Hyuk Mujin made the identity of that “someone” perfectly clear before continuing.

“I think I already mentioned that we gathered the dead and cremated them. And you know that all the chieftains who sided with Baeksang and then fled were locked in the underground prison, right?”

“I know the general details.”

“Oh, right. Come to think of it, I heard that Great Chieftain Yohi asked to be punished as well.”

“Yohi did?”

“Yes. Great Hero Yayul seemed willing to forgive her, but she voluntarily entered the underground prison.”

It was surprising that Yohi had gone that far, but at the same time, it felt natural.

Although she had repented late, Yohi had also allied herself with Baeksang to enjoy wealth and power. She must have learned a great deal after passing through the brink of death herself.

*She chose it herself. She must have thought it was the right thing to do.*

After muttering inwardly, I listened to the rest of the story.

More Nanman people than ever were staying in the Nanman Beast Palace to restore the Inner Palace, which had been reduced to ruins, and the Outer Palace, which had suffered considerable damage.

As a result, Young Palace Lord Yayul Mok was so busy that he barely had time to breathe.

“We passed the news along, but I don’t know if he’ll come right away. It’s been hard to even catch a glimpse of him lately.”

“That’s probably true. The Beast Miao King is probably the same.”

“Great Hero Yayul…… You probably won’t see him either—not just us, but anyone else.”

“What?”

“He’s been missing since two days ago. I hear the entire leadership is already in an uproar.”

“……”
```
