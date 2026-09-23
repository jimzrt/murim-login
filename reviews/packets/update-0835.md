<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0835.txt",
      "sha256": "b634a351629f6582a2035dfca0cb493c7b527bb5ec8711505c3deae33a5eeede",
      "bytes": 19058
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "79c9f958b04d70f9f6dc1d0c13b7751ebf0cd9794c83b4006dc4c35116207f3c",
      "bytes": 2385
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ad6965cfcc54bdbb79c84cfefd2d5c0b76d1e8fdd3994cdc0d6cd2934374048b",
      "bytes": 226906
    },
    {
      "path": "characters/Blood Monk.md",
      "sha256": "044041cd5ad4408b4da947643bd7cf485c7ed748e4c3a272ee2d2f9bf3cdd8a5",
      "bytes": 853
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "508f0f59eab8e616b3d8b3fa4c673b3dcd6ddd8a339b7b9c7f6297a6a070eced",
      "bytes": 1325
    },
    {
      "path": "characters/Hanga.md",
      "sha256": "f0e8e7c0abf28418399d61c40ea0bf46a826500c3670e5a7fb79a8813107baaf",
      "bytes": 568
    },
    {
      "path": "characters/Hwangcheon.md",
      "sha256": "a7d107b8f1bec2ca9de0e70bfbf60b29ff43a3bf295dada317f9e69dac7bcf19",
      "bytes": 703
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "93d9707b1eee596e2c9f1ce01b13c6e15e92d2d09f3ce8fc76aa3d2924fce4f9",
      "bytes": 1355
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "1ab70ae57d751e5a2977802b940c922f7ad277bb937ae9edb38d2b599c44f7d6",
      "bytes": 1848
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fac00e85e85f0b560bd0d2c2fe8b1d024a48b5c76d8b0853c8a159d89ea3316b",
      "bytes": 1853
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "cd10f23336db935ff1b2629d0ec495c7849a7281b60f363a7f1d5ea9f966839d",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "5839ad98a473eb84134ef5ced5aa7f5300e6940c51a01a5927cda4dd8a415fc9",
      "bytes": 937
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "2936f4df565023f2c2b7b8b65db75dee37bdc35920247652a6082abe5c9fb3c4",
      "bytes": 1061
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "2ea98853e0c1eebd7c8540cab97fd657823fda7fd36494da75494f2d227c51a6",
      "bytes": 752
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "4f3e0611fdd1c7243ca1c8922036acd2eee53e833c93131c638db4193f0c6d7c",
      "bytes": 1131
    },
    {
      "path": "characters/Namho.md",
      "sha256": "9e9e2a1199bb16d40c4608b7ded625c484997500a66b50bb3544f0f55073f7a5",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "5dec83415fb8f85b855df427ba687605bfa2210a6a9f8bfd8c9bef949ae2d48a",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "1422617c7ab3adf438984acdb374bf583f8e365d819f1615942c20484001ba47",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "70f51b215111257939037ca5571800e4226c704ddee0aa5bba26c17cc658f8f1",
      "bytes": 1074
    },
    {
      "path": "characters/Sudal.md",
      "sha256": "6335d0c224648f79ba77c666b5fa13473cde7705a9544943fd3da94c10a9ebbe",
      "bytes": 605
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "68be789364f57096d49060a8f4ea8fa655e09502da20aa46109d2e513e947f48",
      "bytes": 787
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9efad41a2b865bcf5c939bc36568267e2332e7ce051f57c19cbf5cf82b65cc36",
      "bytes": 251423
    }
  ],
  "estimated_tokens": 20975
}
-->

# Durable State Update — Chapter 835

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
1 and safe_through 835. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 835. Profile updates may replace only one
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
  "chapter": 835,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 835,
    "continuity_sources": [835],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader.",
    "Jin erased the Doppelganger, but Main Quest [Cataclysm] and its “Stop the Summoning” mission failed.",
    "The Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "The System transferred Jin to Murim while he was unconscious; he has awakened in Nanman after being unconscious for several days.",
    "The System’s Status Window is currently inaccessible; Jin suspects an update may be responsible.",
    "Jin saw a vision in which Ahomed’s ritual summoned a black-haired man who killed Ahomed and unleashed a destructive storm of magical power; whether the vision was real remains unknown.",
    "Jin believes the summoned man is not Asmodeus, but does not know his identity.",
    "The Prophet’s remaining mage disciples completed their prepared ritual, and Ahomed was the mage who led it.",
    "Jin’s [Broken Body] injury remains unresolved, causing pain around his lower dantian; leveling up did not heal it.",
    "Jeok Cheongang has gone to Sichuan to bring the Divine Physician, his former Disciple, to treat Jin.",
    "Taishan returned with a giant beehive as a supposed cure for Jin."
  ],
  "continuity_sources": [
    833,
    834
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, and what is the Ark?",
    "What changed in the System update, and when will its functions return?"
  ],
  "safe_through": 834,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”"
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
| 청풍     | **Cheongpung**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 무신     | **Martial God**               | —              |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 화산파    | **Huashan**                      |
| 장강수로맹  | **Yangtze River Channel League** |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 절정고수                | **Peak master** / **Peak martial artist** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 주화입마   | **qi deviation**                                 |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 선배     | **Senior**                                   |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 혈승 | **Blood Monk** | Sobriquet of the unidentified bald martial artist active in Guizhou. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 황천 | **Hwangcheon** | Second-generation Zhongnan disciple and Commander of the Taeeul Sword Unit. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 수달 | **Sudal** | Deputy Stronghold Lord of the Water Dragon Stronghold and river pirate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 평화 | **Peace Guild** | Guild name. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 박도 | **broad-bladed saber** | Rough weapon swung by the bald swordsman. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 대성 | **Great Completion** | Completion stage of a martial technique. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 외공 | **external arts** | Martial arts focused on extreme bodily training. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 호거아 | **Tiger Giant Child** | Epithet for Taishan. |
| 광서 | **Guangxi** | Region bordering Nanman. |
| 제시 | **Jesse** | The U.S. Secretary of State, introduced by first name. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 금봉 | **golden bee** | A venomous bee said to strip a tiger to its bones in half a gak. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 대지모신 | **Earth Mother Goddess** | New deity proclaimed by Jin Taekyung as Nanman's One God. |
| 콩고 | **Congo** | Country named in a report about protesters stopping. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 진태경 | 항아 | visiting_adult_to_local_child | little one | friendly and coaxing | Questions Hanga and offers food in exchange for information. |
| 혁무진 | 항아 | visiting_adult_to_local_child | little one | coaxing and encouraging | Questions Hanga with an artificially kind smile and offers two food bundles. |
| 항아 | 노인 | child_to_elder_stranger | Grandpa | childlike-familiar | Hanga calls the unnamed old man 할부지 after he arrives at her family’s home; this is distinct from her address to Jang Taebo. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 청풍 | hostile Zhongnan Elder to younger martial artist | Sword Saint's heir / you | hostile and threatening | Song Il identifies Cheongpung as the Sword Saint's heir and demands that he face the consequences of injuring Gong Ilhyuk. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 시비 | 진태경 | household_servant_to_visiting_young_hero | Young Hero Jin | formal-polite | The maid summons Taekyung to meet the Family Head. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 청풍 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Cheongpung among the Benefactors when greeting Taekyung's companions. |
| 황천 | 진태경 | sect_disciple_to_hostile_younger_martial_artist | you bastard | hostile and commanding | Orders Taekyung to release Hwangbo Eom. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 수하 | 채주 | subordinate_to_stronghold_lord | Stronghold Lord | deferential | The subordinate calls Mu Song 채주 while reporting the nearby vessel. |
| 진태경 | 무송 | junior_martial_artist_to_senior_martial_artist | Senior | formal-polite | Taekyung uses 선배님 after recognizing Mu Song as a senior martial artist and disciple of the Seafaring King. |
| 무송 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | familiar-teasing | Mu Song calls Taekyung 후배 and jokes about his supposed taste for men. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |
| 청풍 | 무송 | young martial companion to stronghold lord | you | cheerful and familiar | Offers Mu Song his last dumpling and then induces him to buy more in Guang'an. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
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
| 부채주 | 진태경 | Water Dragon Stronghold deputy to honored ally | Great Hero Jin | deferential | The Deputy Stronghold Lord reports Mu Song's orders and addresses Taekyung upon arrival. |
| 진태경 | 부채주 | Fire Dragon Pavilion Master to Water Dragon Stronghold deputy | Deputy Stronghold Lord | casual and commanding | Taekyung orders him to set off and later summons him with Jang Pil. |
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
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 수하 | 수달 | subordinate_to_deputy_stronghold_lord | Deputy Stronghold Lord | deferential but alarmed | Sudal's subordinates challenge his plan to raid Guizhou. |
| 수달 | 수하 | deputy_stronghold_lord_to_subordinates | boys | casual and commanding | Sudal orders his subordinates to raid Guizhou. |
| 혈승 | 수달 | unknown_hostile_encounter | you | casual and probing | The Blood Monk questions Sudal after taking control of the crewless swift ship. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |

## Listed compact profiles

### Blood Monk.md

# Blood Monk (혈승)

- **Safe through:** Chapter 716
- **Aliases:** Jeok Cheongang; Fire King
- **Role:** The Blood Monk is Jeok Cheongang, the Fire King, who disguised himself as a monk to evade Dark Heaven and uses a steel Zen staff and the Flame Divine Palm.
- **Personality:** As Jeok Cheongang, the Blood Monk is gruff, blunt, protective of his Disciple, and prone to profane mockery, but acts decisively to protect others.
- **Voice:** He speaks roughly and informally, often curses or teases with insults, and calls himself 'this old man' while addressing Jin as a brat.
- **Relationships:** Jeok Cheongang is Jin Taekyung's master and protective ally; he opposes Dark Heaven and is recognized by the Nanman as the Fire King.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 682
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Hanga.md

# Hanga (항아)

- **Safe through:** Chapter 724
- **Aliases:** None
- **Role:** Local village girl, Jang-pal’s daughter, who lives near Jang Taebo and regularly visits him.
- **Personality:** Curious, energetic, observant, and already attentive to the value of information and food.
- **Voice:** Childlike, direct, and inquisitive, with an occasional surprisingly worldly remark.
- **Relationships:** Calls Jang Taebo Grandpa; Jang Taebo is his elderly neighbor and only conversational companion.

### Hwangcheon.md

# Hwangcheon (황천)

- **Safe through:** Chapter 325
- **Aliases:** None
- **Role:** Second-generation disciple of the Zhongnan Sect and Commander of the Taeeul Sword Unit, Hwangcheon is a Peak master who serves under Hwangbo Eom.
- **Personality:** Loyal to Zhongnan and its elders, initially reactive and defensive, but willing to obey Hyuk Sopyung's corrective command.
- **Voice:** Loud, urgent, and deferential toward senior disciples, becoming defensive when Zhongnan's honor is challenged.
- **Relationships:** Hwangbo Eom is his Senior Martial Uncle, Hyuk Sopyung is his Senior Brother, and he commands the Taeeul Sword Unit.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 834
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 834
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 834
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 834
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 834
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 682
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 818
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 617
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan, belongs to the Yangtze River Channel League's moderate faction, and is an exceptionally skilled ship captain.
- **Personality:** Ambitious, domineering, impatient with interruptions, strongly attached to life on the water, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song belongs to the Yangtze River Channel League's moderate faction, regards Hwang Chung, his senior and Uncle Hwang, as family, must weigh whether the League will support the New Murim Alliance while the Seafaring King retains authority over major League decisions, and has instructed his subordinates to aid Jin Taekyung and the Jin Family of Taiyuan in repayment for past help.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 834
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 834
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 834
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 834
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Sudal.md

# Sudal (수달)

- **Safe through:** Chapter 664
- **Aliases:** None
- **Role:** Sudal is the Deputy Stronghold Lord of the Water Dragon Stronghold and a river pirate who commands three swift ships.
- **Personality:** Adventurous, opportunistic, irreverent, and willing to bully his subordinates to pursue a scheme.
- **Voice:** Blunt, profane, boastful, and theatrically commanding.
- **Relationships:** He serves the Water Dragon Stronghold's Stronghold Lord, commands its subordinates, and is currently leading a raid toward Guizhou.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 834
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃835화



촤아아악.

장강수로맹(長江水路盟)에 속한 수적이자 호북성을 주름잡는 수룡채(水龍寨)의 부채주인 수달은, 물살을 가르며 빠르게 나아가는 뱃머리에 앉아 깊은 생각에 잠겨 있었다.

‘돌이켜보면, 지금까지는 그럭저럭 잘나갔지.’

수달이 이 바닥에서 차지하는 입지는 상당했다.

소속된 수적만 오백 명이 넘는 대형 수채의 부채주. 거기에 더하여 한참 늦긴 했어도 절정에 오른 무위까지.

곧 오십 줄에 접어드는 나이에도 사지 멀쩡히 현역에 있다는 것만으로도 성공한 수적의 표본이지만, 수달은 이미 그 이상을 이루어 냈다.

‘이만하면 돈도 꽤 모아 뒀고.’

수백 명이나 되는 전력을 갖춘 수채는 드물다.

게다가 수룡채의 주인인 선화아(船火兒) 무송은 수완이 좋았고, 장강수로맹주의 직계 제자라는 막강한 뒷배를 지니고 있었기에 부채주인 수달은 떨어지는 콩고물만 주워 먹어도 배가 불렀다.

물론 그렇게 벌어들인 재물 중 상당수는 기루로 흘러 들어갔지만.

‘호북 변두리라면 괜찮은 장원 한 채 정도는 살 수 있지 않을까? 집값 또 올랐을 텐데. 시부랄 거. 그런 집은 기둥에 금칠이라도 해 뒀나.’

수달은 울적한 표정으로 거칠게 갈라지는 물살을 바라보았다.

‘내가 이런 생각까지 할 줄이야.’

은퇴? 정착?

몇 년 전, 아니 몇 달 전만 해도 그런 말랑말랑한 단어 따위는 머릿속에 존재하지도 않았다.

수달은 스스로를 타고난 뱃사람이요, 수적이라고 자부했으니까.

그러나 이제는 아니다. 순탄하기 그지없던 약탈자의 삶도, 패기로운 뱃사람으로서의 삶도 서서히 끝장나고 있었다.

심지어 지금 이 순간에도.

“저어, 부채주?”

등 뒤에서 들려온 수하의 조심스러운 부름에, 수달은 두 눈을 질끈 감았다.

‘좆 됐다.’

이건 짐작이 아니라 확신이다.

지금으로부터 닷새 전, 지긋지긋한 운남 땅을 떠난 이후로 수없이 찾아온 악몽이 또다시 반복되고 있었다.

‘웬일로 오늘 하루는 잘 넘어가나 했더니…….’

결국 올 것이 오고야 말았다.

하지만 수달은 피하지 않았다. 용맹한 수적답게 맞서리라 결심하며 대답했다.

“듣고 있다. 말해라.”

“그게 그러니까, 허 참.”

“말할래, 줘 터질래.”

“이 나이에 줘 터지긴 싫으니까 말하겠소. 다름이 아니라 그, 혹시 소고기 있소?”

수달은 천천히 돌아섰다. 그리고 익숙한 얼굴을 한 수하를 향해 반문했다.

“진짜 줘 터지고 싶어서 환장했느냐?”

“그럴 리가 있겠소.”

“그럼 다시 말해 봐. 뭔 고기?”

“소고기가 필요하오. 정확히는 좀 매콤하게 양념 재운 걸로.”

“소고기, 매콤 양념…….”

말꼬리를 흐린 수달은 크게 심호흡했다. 근래의 경험으로 그는 지난 수십여 년간 잊고 살았던 평정심을 배워 가고 있었다.

“우리가 지금 어디에 있는지는 알지?”

수하가 호쾌하게 고개를 끄덕였다.

“알다마다. 대 장강수로맹의 상징, 수룡채의 자랑! 쾌조선 아니오.”

“그 쾌조선은 어디에 있느냐?”

“드디어 빌어먹을 운남을 떠나 장강을 가로질러 사천으로 향하고 있소만.”

“그럼 마지막. 장강 한복판에서, 그것도 육지를 밟은 지 한 달도 훌쩍 지난 이 시점에서 양념 된 소고기를 구할 수 있을까?”

“없지.”

“정답이다. 생각보다 똑똑하군.”

“일단 고맙소.”

오랜만의 칭찬에 쑥스럽게 웃던 수하가 문득 정색했다.

“그런데 가져가야 하오.”

“아니, 없다니까.”

“없으면 만들어서라도 가져오라던데.”

“혹시…… 그 새낀가?”

주위를 둘러본 수하가 한껏 억누른 목소리로 대답했다.

“역시나 그 새끼요.”

혹시나 하면 역시나.

이름은 말하지 않았지만, 두 사람 모두 알고 있었다.

장강을 가로지르는 배 위에서 매콤하게 양념한 소고기를 요구할 만큼 정신 나간 놈은 현재로서 ‘그 새끼’가 유일했으니까.

‘호거아(虎踞兒) 태산.’

수적으로 삼십 년을 살았다는 건, 온갖 병신과 머저리를 봤다는 소리. 하지만 잔뼈 굵은 수달도 그런 놈은 처음 봤다.

도무지 인간 같지 않은 덩치와 식성. 어지간히 못 배워 먹은 수적들마저 경악할 만한 단순함까지.

아니, 사실 덩치는 한참 작아도 비슷한 유형의 미친놈을 한번 본 적 있긴 했다.

“하 시바, 잠깐 잊고 있었는데 갑자기 그 자식까지 생각나네.”

“누구 말하는 거요?”

“그놈.”

“아, 그놈.”

두 사람은 동시에 떠올렸다.

생긴 건 멀쩡하게 생겨서 무슨 귀신이라도 붙었는지, 틈만 날 때마다 만두며 당과를 처먹던 젊은 놈을.

아련한 눈빛으로 몇 달 전의 과거를 회상한 수달이 문득 한숨을 내쉬었다.

호북 땅이 피로 물들기 전만 하더라도, 그는 평화롭고 슬기로운 수적 생활을 이어 가고 있었다.

“그래도 그놈 있을 때가 훨씬 나았지. 적어도 제가 먹을 건 직접 챙겨 왔으니까.”

“무슨 개소리요? 그거 금방 다 처먹고 빙당호로 달라고 얼마나 지랄을 떨었는데.”

“세상에. 그게 사실이냐?”

“그렇다니까. 눈만 마주치면 빙당호로 달라고 땡깡을 피우는데, 시부럴 놈이 아주 그냥 호로 새끼가 따로 없었소.”

어느 놈은 양념까지 된 소고기를, 또 어느 놈은 빙당호로를 내놓으라니.

수달은 그 극악무도함에 치를 떨었지만, 그때나 지금이나 할 수 있는 것은 아무것도 없었다.

소고기를 원하는 미친놈은 사파(邪派)중에서도 첫손가락에 꼽히는 흑룡마문의 절정고수. 심지어 후계가 확실시되는 소문주의 오른팔이었고, 앞서 언급한 호로 새끼는 그보다도 까마득히 윗줄에 있는 거물이었으니까.

‘화산신룡(華山神龍) 청풍이면, 거물 중에서도 거물이지.’

검성 매종학을 스승으로, 화산파 장문인을 사형으로 둔 정신 나간 뒷배.

무림의 배분으로만 따져도 구파일방의 장문인들과도 눈높이를 나란히 하는데, 무공에 대한 재능도 고금(古今)을 통틀어 능히 세 손가락 안에 드는 천재라는 것이 세인들의 평가였다.

‘하늘도 무심하시지. 어찌 그런 놈에게.’

수달이 맑은 하늘을 올려다보며 한탄하던 그때.

우드득!

무언가 부서지는 소리와 함께, 짐승의 포효와도 같은 고함이 울려 퍼졌다.

- 소. 고. 기! 태산이 소고기! 매콤한 양념!

외침을 들은 수하가 창백하게 질린 얼굴로 입을 열었다.

“큰일이군. 저 정도면 벌써 중노(中怒)요.”

“중노?”

“지난 닷새 동안 동태를 파악하며 단계를 매겨뒀소. 대노(大怒)부터는 거의 사람 새끼가 아니오.”

“이미 처음부터 그랬던 것 같은데…….”

“여하튼 우선 뭐든 주시오! 쾌조선에 구멍 몇 개 뚫리기 전에 당장!”

“뭣이!”

정신이 번쩍 든 수달은 술안주로 꿍쳐 놓았던 비상식량의 위치를 알려 주었다.

“내가 쓰는 선실 구석에 항아리 하나가 있다.”

“소고기?”

“아니. 소금에 절여 둔 돼지고기다. 특상품이지.”

“아무리 그래도 그걸로는 부족할 텐데?”

“당연히 부족하지. 그놈 식성이면 항아리 채 처먹어도 이상하지 않으니까. 하지만 흑룡마문의 소문주와 함께 간다면 어떨까?”

“헛.”

“가라. 이 배의 운명이 네게 달렸다.”

“역시, 역시 우리 부채주요!”

엄지를 척 치켜세운 뒤 황급히 자리를 뜨는 수하의 뒷모습을 바라보며, 수달은 뿌듯한 미소와 함께 콧잔등을 문질렀다.

“녀석…….”

그러나 그 미소는 순식간에 사라졌다.

가진 것을 뺏지는 못할망정, 배까지 태워 주는 마당에 이런 걱정까지 해야 하다니.

심지어 괜찮은 해결책을 제시했다는 생각에 뿌듯함까지 느꼈던 수달은, 문득 치밀어 오르는 서러움에 눈시울을 붉혔다.

‘내가 이러려고 수적이 됐나.’

순간 짙은 회의감이 들었지만, 수달은 애써 고개를 내저었다.

아니다. 조금만 더 버티면 된다.

운남을 떠난 지 벌써 닷새. 하늘의 도움으로 바람만 잘 탄다면 하루 안에 도착할 수도 있었다.

그럼 저 지긋지긋한 놈들과도 작별할 수…….

“거, 앞에 막지 말고 좀 비켜 봐라.”

“엉?”

상념에서 깨어난 수달이 눈을 깜빡였다. 척 봐도 꼬장꼬장해 보이는 늙은이 하나가 낚싯대를 들고 그의 앞에 서 있었다.

“당신은…….”

“당신?”

“아니, 노인장은…….”

“노인장?”

“……제가 뭐라 불러 드려야 합니까.”

“그냥 노 선배라고 불러라. 뱃머리에서 그 흉악한 얼굴도 치우고. 네놈 면상 보면 바람 쐬러 올라오던 용왕도 도망가겠다.”

“아, 예. 알겠습니다, 노 선배님.”

약 두 달 전, 사천에서 운남으로 향할 때만 하더라도 없었던 노인.

돌아가기 위해 항해를 시작한 지 닷새가 흐른 지금에도 정확히 누군지는 모르겠지만, 왠지 이렇게 보니 고수 같은 느낌이 들었다.

특히…….

‘저 이마.’

먹칠이라도 한 것처럼 시커멓게 물들어 있는 데다, 다른 이들보다 두 배는 크게 부풀어 오른 노인의 이마가 자꾸만 눈에 밟혔다.

‘저런 외공(外功)에 대해 들어본 적이 있는데.’

냉큼 뱃머리에서 떨어진 채 노인을 관찰하던 수달이 조심스럽게 입을 열었다.

남만에 은거하던 정체불명의 노고수에게 잘 보여서 무공 구결이라도 얻는다면, 그것만 한 기연이 어디 있겠는가.

“저어, 그런데…….”

“말 걸지 마라. 집중 중이다.”

“옙.”

한 마디와 함께 순식간에 내려앉은 침묵.

수달이 눈치만 살피던 그 순간, 뱃머리에 앉아 낚싯대를 드리우고 있던 노인이 버럭 외쳤다.

“갈! 네 이놈!”

“예?”

“세상에서 가장 혐오스러운 인간 군상이 무엇인 줄 아느냐!”

“무, 무엇입니까?”

“바로 하던 말을 끝까지 하지 않는 놈이니라!”

“아니, 그건 노 선배님께서…….”

“그 간사한 주둥이 닥치고 하려던 말이나 마저 해라. 궁금해서 미칠 것 같으니까.”

이미 미친 것이 틀림없어 보이는 눈앞의 노인을, 수달은 아연한 눈빛으로 바라보았다.

‘이제 겨우 화왕을 벗어났나 싶었는데, 정신 나간 늙은이가 하나 더 있었구나!’

화왕 적천강은 이미 그들보다 먼저 또 다른 쾌조선을 타고 사천으로 떠났다.

간신히 숨통이 트였다고 착각했던 수달은 서러움을 참으며 입을 열었다.

“다름이 아니라, 혹 철두공(鐵頭功)을 익히셨는지 여쭙고자 했습니다.”

“철두공?”

“예. 이 후배가 아는 바에 의하면, 철두공을 극한까지 연마한 고수들은 이마가 검고 강철도 깨트린다는 이야기가 있어서…….”

“흠. 어디서 주워들었는지는 몰라도 제법 잘 알고 있군. 맞다. 철두공에도 수준과 종류가 있지만, 대성한다면 검기(劍氣)조차 손쉽게 막아 낼 수 있지.”

“오오. 그럼 혹시 노 선배님께서 그 유명하신 철혈노(鐵血老) 대협이십니까?”

노인이 코웃음 쳤다.

“대협은 무슨. 철혈노 그놈은 잡놈 중의 잡놈이야. 무림에서 반드시 죽여 없애야 할 인간말종 중 하나지. 아, 이미 죽었을지도 모르겠군. 정마대전 내내 간만 보는 척하다가 뒷구멍으로는 온갖 더러운 짓을 해 댔으니.”

“아. 그럼 철혈노 대협. 아니 그 말종 놈이 아니셨군요.”

“당연하지. 지금 노부한테 시비 거는 게냐?”

“절대 아닙니다. 그럼 실례지만 누구신지…….”

“나?”

노인이 가슴을 쭉 펴며 대답했다.

“노부의 존함은 남호라 한다.”

“헛, 남호라면!”

“맞다. 바로 그 남호가 바로 이 몸이니라.”

노인, 남호는 젊은 시절을 생각하며 흐뭇하게 웃었고 수달은 고민했다.

‘남호가 도대체 누구지.’

전대의 노 고수라 그런지, 아무리 생각해도 처음 들어 보는 이름이다.

하지만 뒤이어 들려온 말을 듣자 긴가민가하던 수달도 깜짝 놀랄 수밖에 없었다.

“정마대전 때 노부가 척살한 마두만 수십 명이 넘지.”

“헉, 수십 명!”

“그뿐인 줄 아느냐? 노부 덕분에 목숨을 구명한 정파의 무림인들만 일천이요, 그로 인해 죽은 마교도의 머릿수는 그 두 배쯤 되느니라.”

“와! 천 받고 이천 더! 정마대전이 낳은 영웅!”

“구파일방. 오대세가? 세지, 엄청 세지. 그러나 닥치고 돌격해서 날붙이나 휘두르는 게 능사가 아니다. 중요한 건 전투에서의 승리야!”

“와! 승리!”

“소싯적에 이 몸이 전서구 한 번 날렸다 하면, 어? 이름만 들어도 다 아는 명문 대파가 움직이고 가끔은 삼성, 십왕도 후다닥 달려 나가고 그랬어!”

“와! 삼성! 십왕! 그 정도면 최소 무신!”

“그게 바로 이 몸, 남호였단 말이다!”

“와아아! 천세! 천세! 우리 노 선배님 천천세!”

두 팔을 번쩍 치켜들고 부르짖던 그때. 문득 이상함을 느낀 수달이 눈을 깜빡였다.

“저기, 방금 뭐라고 하셨습니까?”

“뭘 말이냐?”

“아니, 그. 전서구를 날리셨다고 들은 것 같아서 말입니다.”

“어. 그랬지. 후방에서.”

“……?”

“무슨 문제라도 있느냐?”

당당한 남호를 바라보며 잠시 침묵하던 수달이 입술을 뗐다.

“그럼 노 선배님. 혹시 별호가?”

“없다.”

“무공은……?”

“그런 걸 왜 익혀야 하는데.”

“……?”

“무림인 그거, 더럽게 위험하고 힘들다. 젊을 때는 나대다가 칼 맞아 뒈지고, 나이 들어서는 골병들기 딱 좋거든.”

“……!”

“이거 봐. 네놈도 지금 몸을 떨고 있잖느냐. 나이는 먹고 무공은 어중간하니 슬슬 몸이 맛탱이가 가기 시작한 게지. 그거 중풍일 수도 있으니까 생각 있으면 따라오거라. 때마침 용한 의원을 찾아가는 중이니까.”

남호의 말은 절반 정도는 사실이었다.

수달은 이미 맛탱이가 가 버렸다. 단, 중풍이 아닌 분노로 몸을 떨고 있을 뿐이었다.

그나마 아직 끊어지지 않은 이성의 끈이, 마지막 남은 의문을 해결하기 위해 입술을 움직이고 있었다.

“그, 그럼 아까 말했던 철두공은.”

“익히 안다고 했지, 익혔다고는 한 적 없는데.”

“아니, 철두공도 안 익혔는데 도대체 이마는 왜 그렇게…….”

“벌에 쏘였다.”

“……!”

“어떤 금수 같은 놈이 꿀을 처먹겠답시고 흑금봉(黑金蜂)의 벌집을 건드린 덕분에 황천길 건널 뻔했지. 어찌어찌 독기는 간신히 빼내긴 했는데, 붓기가 너무 안 빠지네 이거.”

검게 부풀어 오른 이마를 살살 어루만지는 남호의 모습에, 수달은 벌에 쏘인 것처럼 눈앞이 아찔해지는 것을 느꼈다.

‘뭐 이런 개 같은 상황이……!’

두 달.

무려 두 달이다. 재물과 곡식을 가득 실은 상선들을 뒤로한 채 반협박으로 본거지인 호북을 떠나 사천, 거기에 이어 운남까지 끌려온 것이.

심지어 거기서 끝이 아니다.

대기 시간은 하염없이 길어지고, 잠깐 용돈이나 벌 생각으로 광서에 들렀다가 이번에는 혈승(血僧)이라 불리고 있던 화왕 적천강에게 붙잡혀 끌려왔다.

말이 좋아서 두 달이지, 천하에서 가장 못생기고 못 배워먹은 놈들과 함께 꼼짝없이 배에만 갇혀 있으니 두 달이 이 년 같았다.

‘이제 저것들을 사천까지만 데려다주면 호북으로 돌아갈 수 있는데, 마지막까지 이 모양 이 꼴이라니.’

웬 짐승 같은 놈은 주둥이에 뭐든 쑤셔 넣기 바쁘고, 이번에는 난생처음 보는 힘없는 노인한테 속아 욕만 잔뜩 얻어먹었다.

그뿐인가. 다른 연놈들도 도저히 제정신이 아니다.

이미 몇 번 봐서 익숙한 혁무진이라는 놈은 수하들에게 대지모신이니 뭐니 하는 종교를 전파하고 다니질 않나, 처음부터 사이가 안 좋아 보이던 송일섬과 사마표는 갑판에서 비무를 벌이다가 돛대를 반쯤 부숴 놨다.

십봉룡(十鳳龍)이자 사천제일미라는 주화란?

분명 두 달 전 남만으로 향할 때만 해도 선녀 같았던 그녀는, 틈만 나면 갑판에 나와 사람들을 감시하는 게 일상이었다.

그리고 어디선가 작은 소리라도 나면, 귀를 쫑긋거리며 마치 들으라는 듯이 이렇게 중얼거렸다.



‘아. 각주님 아직 쉬셔야 하는데. 저 나무통을 꼭 지금 옮겨야 하나.’

‘아. 저 밧줄 스치는 소리 진짜 너무 크네. 각주님 편하시게 그냥 싹 다 잘라 버릴까.’

‘아. 물을 왜 저렇게 벌컥벌컥 마시지. 그냥 물 안 마시고 서서히 말라비틀어지면 안 되는 건가?’

‘아. 파도가 진짜 너무 심하네. 각주님 운기조식 하시다가 파도 소리 때문에 주화입마라도 걸리면 어쩌지? 명색이 수적인데 파도 하나 어떻게 안 되나?’



아니 무슨 용왕도 아니고, 거친 강물까지 어떻게 잠재우란 말인가.

이만하면 참을 만큼 참았다. 닷새 동안 못 본 꼴이 없고, 안 들어 본 소리가 없었다.

‘그래, 더 이상은 물러설 곳도 없다. 오늘은 반드시 결판을 낸다.’

분노에 휩싸인 수달은 허리춤에 꽂아 넣은 박도를 뽑아 들었다.

아니, 뽑아 들려고 했다.

바로 그 순간, 등 뒤에서 낯익은 목소리가 들리기 전까지는.

“어우, 푹 쉬었더니 이제 좀 한결 낫네. 아저씨. 지금 어디까지 왔어요?”

수달은 천천히 돌아섰다. 그리고 꼬박 닷새만에 모습을 드러낸 진태경을 향해, 눈을 치켜뜨며 대답했다.

“헤헤. 금방 도착합니다요.”

그날 밤.

쾌조선은 사천에 도착했고, 수달은 은퇴를 결심했다.
```

## Final English reading copy

```markdown
# Chapter 835

*Splaaash.*

Sudal, a river pirate belonging to the Yangtze River Channel League and Deputy Stronghold Lord of the Water Dragon Stronghold, which held sway over Hubei Province, sat at the bow of a ship cutting swiftly through the current, lost in thought.

*Looking back, things have gone pretty well so far.*

Sudal had made quite a name for himself in his line of work.

He was the deputy lord of a major stronghold with more than five hundred river pirates under its command. And though it had taken him a long time, he had finally reached the Peak level of martial arts.

Simply staying active and in one piece as he approached fifty made him a model of a successful river pirate. But Sudal had already achieved more than that.

*I’ve saved up a decent amount of money, too.*

It was rare for a water stronghold to have hundreds of fighters.

On top of that, Mu Song, the Ship-Fire Boy who headed the Water Dragon Stronghold, was a shrewd man with powerful backing: he was a direct Disciple of the Alliance Leader of the Yangtze River Channel League. As his deputy, Sudal had made plenty just by picking up the scraps that fell his way.

Of course, a good deal of that wealth had gone to pleasure houses.

*Could I buy a decent manor somewhere out in Hubei? Though property prices have probably gone up again. Damn it. Do they plate the pillars in gold or something?*

Sudal stared gloomily at the current, which broke into rough waves around the ship.

*I never thought I’d be thinking about stuff like this.*

Retirement? Settling down?

A few years ago—not even a few months ago—those soft, mushy words wouldn’t have crossed his mind.

Sudal had always thought of himself as a born sailor and river pirate.

But not anymore. His carefree life as a raider, and his life as a bold man of the water, were both slowly coming to an end.

Even at this very moment.

“Um, Deputy Stronghold Lord?”

At the cautious call from behind him, Sudal squeezed his eyes shut.

*We’re fucked.*

It wasn’t a guess. He was certain.

Ever since they’d left the wretched land of Yunnan five days ago, the same nightmare had come around again and again.

*I thought we might make it through the whole day for once…*

In the end, the inevitable had arrived.

But Sudal didn’t run. He resolved to face it like a brave river pirate and answered.

“I’m listening. Speak.”

“Well, you see, it’s just—”

“Talk, or get your ass kicked.”

“I’m too old to want a beating, so I’ll talk. It’s just… do we have any beef?”

Sudal turned around slowly and looked at the familiar face of his subordinate.

“Are you really that eager to get your ass kicked?”

“Of course not.”

“Then say it again. What meat?”

“I need beef. Specifically, beef marinated in a spicy sauce.”

“Beef, spicy marinade…”

Sudal trailed off and took a deep breath. Recent experience had been teaching him to rediscover the composure he’d forgotten over the past few decades.

“You know where we are right now, don’t you?”

His subordinate nodded enthusiastically.

“Of course. We’re aboard the swift ship, the pride of the Water Dragon Stronghold, symbol of the mighty Yangtze River Channel League!”

“And where is that swift ship?”

“We’ve finally left that godforsaken Yunnan behind and are crossing the Yangtze on our way to Sichuan.”

“Then one last question. In the middle of the Yangtze, after more than a month without setting foot on land, do you think we can get our hands on marinated beef?”

“No.”

“Correct. You’re smarter than you look.”

“Thanks, I guess.”

The subordinate smiled awkwardly at the rare praise, then suddenly turned serious.

“But we have to bring some back.”

“I said we don’t have any.”

“They told me to make some if we don’t.”

“Could it be… that bastard?”

His subordinate looked around before answering in a voice kept low with great effort.

“Sure enough, it’s that bastard.”

You could always count on him to be the one.

Neither of them said the name, but they both knew who they meant.

At the moment, there was only one lunatic who’d demand spicy marinated beef aboard a ship crossing the Yangtze.

*Taishan, the Tiger Giant Child.*

Spending thirty years as a river pirate meant seeing all kinds of idiots and morons. But even a seasoned pirate like Sudal had never seen anyone like him.

A build and appetite that barely seemed human. A level of simple-mindedness that could shock even the most uncultured river pirates.

Actually, Sudal had once met another lunatic of the same sort, albeit one considerably smaller.

“Shit. I’d almost forgotten him, and now I’m thinking about that bastard too.”

“Who’re you talking about?”

“That guy.”

“Oh. That guy.”

They both thought of him at the same time.

The young man who looked perfectly normal, but seemed possessed by some kind of ghost, and would stuff his face with dumplings and sweets whenever he got the chance.

Sudal gazed wistfully back on the past, a few months ago, then let out a sigh.

Before Hubei was stained with blood, he’d been living a peaceful, sensible life as a river pirate.

“Still, things were a lot better when he was around. At least he brought his own food.”

“What the hell are you talking about? He’d gobble it all up, then raise hell demanding candied hawthorn skewers.[^1]”

“Oh, really? That’s what happened?”

“I’m telling you. The second he made eye contact with you, he’d start whining for candied hawthorn skewers. That son of a bitch was a real pain in the ass.”

One lunatic demanded beef with the sauce already on it, and another demanded candied hawthorn skewers.

Sudal shuddered at their cruelty. But then, as now, there was nothing he could do.

The lunatic who wanted beef was a Peak master from the Black Dragon Demon Gate, one of the foremost factions among the unorthodox. He was also the right-hand man of its Young Sect Leader, who was all but certain to inherit the sect. And that little shit he’d mentioned was a far, far bigger figure than even him.

*If it’s Cheongpung, the Huashan Divine Dragon, he’s a big shot among big shots.*

His backing was insane: the Sword Saint, Mae Jonghak, was his Master, and the Sect Leader of Huashan was his Senior Brother.

In terms of seniority alone, he stood on equal footing with the Sect Leaders of the Nine Sects and One Gang. And according to public opinion, his talent for martial arts was among the top three throughout history.

*The heavens are cruel. Why give all that to a bastard like him?*

As Sudal looked up at the clear sky and lamented his fate—

*Crack!*

Something broke, followed by a shout like the roar of a beast.

“Beef! Taishan wants beef! Spicy sauce!”

Sudal’s subordinate turned pale as he spoke.

“This is bad. He’s already at moderate rage.”

“Moderate rage?”

“I’ve watched him for the past five days and worked out the stages. Once he reaches full-blown rage, he’s barely human.”

“Pretty sure he’s been like that from the start…”

“Anyway, give him something, anything! Right now, before he puts a few holes in the swift ship!”

“What?!”

Sudal snapped out of it and told him where he’d hidden his emergency rations for drinking snacks.

“There’s a jar in the corner of the cabin I use.”

“Beef?”

“No. Salted pork. Top quality.”

“That still won’t be enough, will it?”

“Of course it won’t. With his appetite, he could eat the whole jar and still want more. But what if you take it over with the Young Sect Leader of the Black Dragon Demon Gate?”

“Ah!”

“Go. The fate of this ship is in your hands.”

“That’s our Deputy Stronghold Lord, all right!”

The subordinate raised a thumb and hurried off. Sudal watched him go with a proud smile and rubbed the bridge of his nose.

“That boy…”

But the smile disappeared in an instant.

Instead of taking their possessions, he was giving them a ride—and he still had to worry about this.

He’d even felt proud of himself for coming up with a decent solution. Now, all of a sudden, the misery welled up in him, and his eyes grew wet.

*Is this why I became a river pirate?*

A sudden sense of futility weighed on him, but Sudal forced himself to shake his head.

No. He only had to hang on a little longer.

It had already been five days since they left Yunnan. With the heavens on their side, and a good wind, they could arrive within a day.

Then he could say goodbye to those wretched people…

“Hey, don’t block the way. Move over.”

“Huh?”

Sudal snapped out of his thoughts and blinked. An old man who looked stern as hell stood before him, holding a fishing rod.

“You’re…”

“Me?”

“No, Elder…”

“Elder?”

“……What should I call you, then?”

“Just call me Senior No. And get that hideous face of yours away from the bow. The Dragon King would turn tail if he came up here for some fresh air and saw your mug.”

“Ah, yes. Understood, Senior No.”

The old man hadn’t been with them when they sailed from Sichuan toward Yunnan about two months ago.

Now, five days into their voyage back, Sudal still didn’t know exactly who he was. But looking at him now, the old man somehow gave off the air of a master.

Especially…

*That forehead.*

The old man’s forehead was black as if it had been painted, and swollen to twice the size of anyone else’s. Sudal couldn’t take his eyes off it.

*I’ve heard of external arts like that.*

Sudal quickly moved away from the bow and studied him before speaking cautiously.

If he could get on the good side of the mysterious old master who’d been living in seclusion in Nanman and obtain the formula for a martial art, what better fortuitous encounter could there be?

“Um, so…”

“Don’t talk to me. I’m concentrating.”

“Yes, sir.”

Silence settled at once after that single sentence.

Just as Sudal was watching for a chance to speak, the old man sitting at the bow with his fishing line cast suddenly shouted.

“Enough! You brat!”

“Me?”

“Do you know what kind of person I hate most in this world?”

“W-what kind?”

“A man who never finishes what he’s saying!”

“But, Senior, you’re the one who—”

“Shut that crafty mouth of yours and finish what you were going to say. I’m going out of my mind wondering.”

Sudal stared at the old man before him, who already looked like he was out of his mind.

*I thought I’d finally escaped the Fire King, and now there’s another crazy old man!*

The Fire King, Jeok Cheongang, had already left for Sichuan ahead of them on another swift ship.

Sudal had foolishly thought he could breathe easy again. Swallowing his misery, he spoke.

“I was wondering if you’d learned Iron Head Technique.”

“Iron Head Technique?”

“Yes. As far as this junior knows, masters who’ve trained Iron Head Technique to its limits have black foreheads and can even break steel…”

“Hm. I don’t know where you heard that, but you know your stuff. That’s right. Iron Head Technique has different levels and forms, but once you reach Great Completion, you can easily block even Sword Energy.”

“Ooh! Then could you be the famous Great Hero Ironblood Elder?”

The old man scoffed.

“Great Hero? What nonsense. That Ironblood Elder is the lowest of the low. One of the scum of the Murim who absolutely must be hunted down and killed. Though he might already be dead. He spent the entire Great Faction War pretending to sit on the sidelines, while he was up to all kinds of dirty business behind the scenes.”

“Oh. So you aren’t Great Hero Ironblood Elder. I mean, that scum.”

“Obviously not. Are you picking a fight with this old man?”

“Absolutely not. Then, if you don’t mind, who are you?”

“Me?”

The old man puffed out his chest and replied.

“My name is Namho.”

“Ah! Namho?”

“That’s right. This Namho is none other than the very man standing before you.”

The old man, Namho, smiled fondly as he thought back on his youth. Sudal wondered.

*Who the hell is Namho?*

Perhaps because he was an old master from the previous generation, but Sudal couldn’t recall ever hearing that name.

Then the old man spoke again, and Sudal, who’d been unsure, couldn’t help but jump in shock.

“I killed dozens of fiends during the Great Faction War.”

“Dozens!”

“That’s not all. A thousand orthodox martial artists owe their lives to me, and twice that many members of the Demonic Cult died because of me.”

“Wow! A thousand, and two thousand more! A hero born of the Great Faction War!”

“Sure, the Nine Sects and One Gang? The Five Great Families? They’re strong, very strong. But charging in and swinging a blade isn’t the only thing that matters. What matters is victory in battle!”

“Wow! Victory!”

“When I was young, whenever I sent out a messenger pigeon, the great sects everyone had heard of would move, huh? And sometimes the Three Saints and Ten Kings would rush right out!”

“Wow! The Three Saints! The Ten Kings! You must be the Martial God at the very least!”

“And that man was me, Namho!”

“Wooo! Long live! Long live! Long live our Senior No!”

Sudal threw both arms up and shouted along. Then something struck him as odd, and he blinked.

“Um, what did you say just now?”

“What are you talking about?”

“Er, I thought I heard you say you sent out a messenger pigeon.”

“Yeah. I did. From the rear.”

“……?”

“Is that a problem?”

Sudal stared at Namho, who remained completely unashamed. After a brief silence, he parted his lips.

“Then, Senior, do you have a title?”

“No.”

“Your martial arts…?”

“Why would I learn something like that?”

“……?”

“Martial artists have it filthy dangerous and hard. When they’re young, they show off and get stabbed to death. When they’re old, they’re practically guaranteed to end up with their bodies wrecked.”

“……!”

“Look at you. You’re trembling right now. You’re getting old, your martial arts are mediocre, and your body’s starting to give out. Might be a stroke, so if you’re interested, come along. I’m on my way to see a famous physician.”

About half of what Namho said was true.

Sudal had already lost it. But he wasn’t trembling from a stroke—he was trembling with rage.

The last thread of reason he had left was moving his lips to resolve one final question.

“T-then what about that Iron Head Technique you mentioned?”

“I said I knew about it. I never said I’d learned it.”

“But if you haven’t even learned Iron Head Technique, why is your forehead so—”

“I got stung by a bee.”

“……!”

“Some beastly bastard disturbed a Black Gold Bee’s hive because he wanted the honey, and I nearly died for it. We somehow managed to draw out the venom, but this swelling just won’t go down.”

As Namho gently rubbed his black, swollen forehead, Sudal felt the world go dizzy, as though he’d been stung by a bee himself.

*What kind of fucked-up situation is this…?*

Two months.

A whole two months. He’d left the merchant ships laden with wealth and grain behind, and under what was practically a threat, he’d been dragged away from his home base in Hubei to Sichuan, and then all the way to Yunnan.

And it still wasn’t over.

The waiting had gone on forever. He’d stopped in Guangxi for a chance to make some pocket money, only to be caught by the Fire King, Jeok Cheongang—who was known as the Blood Monk—and dragged along.

It was easy to call it two months, but being trapped on a ship with the ugliest, most uneducated people in the world had made those two months feel like two years.

*All I have to do is take them to Sichuan, then I can go back to Hubei. And this is what happens at the very end.*

One beast of a man spent all day shoving whatever he could into his mouth. This time, he’d been tricked by a powerless old man he’d never met before and showered with insults.

That wasn’t all. The rest of them were just as crazy.

Hyuk Mujin—the one he’d already seen enough times to know—was going around preaching some religion called the Earth Mother Goddess, or something. Song Ilseom and Sama Pyo, who’d looked like they disliked each other from the start, had dueled on deck and half destroyed the mast.

And Ju Hwaran, the Ten Dragons and Phoenixes and the most beautiful woman in Sichuan?

Just two months ago, when they’d set out for Nanman, she’d looked like a fairy. Now she spent her days coming out onto the deck to keep an eye on everyone.

And whenever she heard even the slightest sound somewhere, she’d prick up her ears and mutter as though she wanted everyone to hear.

*Oh. The Pavilion Master still needs to rest. Does that barrel really have to be moved right now?*

*Oh. That rope scraping is so loud. Should I just cut every rope so the Pavilion Master can be comfortable?*

*Oh. Why’s he gulping down water like that? Couldn’t he go without drinking and slowly dry up instead?*

*Oh. The waves are so rough. What if the Pavilion Master suffers qi deviation while circulating his qi because of all the noise? You’re river pirates, aren’t you? Can’t you do something about a single wave?*

What was he, the Dragon King? How was he supposed to calm a raging river?

He’d been patient long enough. Five days of seeing things he couldn’t stand and hearing things he didn’t want to hear.

*That’s it. I’ve got nowhere left to retreat. I’m settling this today.*

Overcome with fury, Sudal drew the broad-bladed saber tucked into his waistband.

Or, he tried to.

Until a familiar voice sounded behind him.

“Whew. I feel so much better after getting a good rest. Hey, mister, how far have we come?”

Sudal slowly turned around. He looked up at Jin Taekyung, who’d shown himself for the first time in five whole days, and answered with a grin.

“Hehe. We’ll be there soon.”

That night, the swift ship arrived in Sichuan, and Sudal decided to retire.

[^1]: Candied hawthorn skewers are a traditional Chinese street snack made by coating hawthorn fruit with hardened sugar.
```
