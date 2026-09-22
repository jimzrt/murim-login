<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0664.txt",
      "sha256": "dbded26a9f5060b9b98d78693e549c98a92b8f6dd0d1746ef1b62619e12454d0",
      "bytes": 13882
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2c65396d03e5bb6a4ccd0e7fb44076788bd3c0128d1305a10f64e7ae685addaf",
      "bytes": 2002
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8847a29282ee6ae6a3a77ad99bd0c0f9aac2a1888dee0538ff3abe4cc1d1af61",
      "bytes": 201728
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "3f48d058a46461bc4f9bbad04a2f21e48037ade1987f0d523d10846bdee10cbb",
      "bytes": 1158
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "7d019b2855d11853766ccd831ebbaa9c8efeafb8daf4580ed3ecead2b174d85b",
      "bytes": 814
    },
    {
      "path": "characters/Blood Monk.md",
      "sha256": "7220c7c179a1cd21ef208fd2702415d4a2441656ba52d40b9d1020e7da2c5f3f",
      "bytes": 589
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "94e8fbb13bc582263777f755229f6acd9f0336c4275527045b373c6fa15413bb",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "62247d74c5798f07189e2d9d8f4f73e79e62c86f8a0aa9752641da0661c7170e",
      "bytes": 1464
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1d7a3f0e24c1acd1a67eb30d56fa61f6d1bae9fd1ee0f37cee988e568f618679",
      "bytes": 1907
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "19399a08a9b320deaaabe37c575362db184be4e77cb69e09dc1617dfee788bea",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "99e543483b7d2822b55a1208e1243f7653c784c9ac2f6bc72481345223fa894a",
      "bytes": 1196
    },
    {
      "path": "characters/Namho.md",
      "sha256": "1416353cfe3d7d43e2f47b4f0e6b3c07ca55a5e01307de9d5e3d025da8f6695e",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "b2e63effb9b42f34a552009bd30a408e05043a5f0431910355837214eb352a75",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "27137f872d7e3c40b67e93aa2cbfeaae95b33a86f8b78653494f0a571dbb1965",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "5e5748bb8be4d495d40b1354015fe89fa754e5bdc76787c7ccde031bfd6937d3",
      "bytes": 1074
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "a74901e5c4b9528eb3e4367dec62b958d0e1bf8bfb5e3913459eaca4df9d13b3",
      "bytes": 644
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "7d76201692d069f2ace19bbddb5a98e0a1fa3c955333acd0759940e7571697eb",
      "bytes": 871
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4b87566b04466cdedd5a25cae0dece9f1c7e71396058292555cc479cd398e2e7",
      "bytes": 206682
    }
  ],
  "estimated_tokens": 15654
}
-->

# Durable State Update — Chapter 664

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 664. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 664. Profile updates may replace only one
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
  "chapter": 664,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 664,
    "continuity_sources": [664],
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
    "Jin Taekyung remains bound in the Nanman Beast Palace's underground prison with sealed internal energy and iron balls, and his public execution is scheduled in two days.",
    "Jin intends to escape and stop Baeksang rather than submit to execution.",
    "Baeksang believes Jin's compassion for the Han Chinese under his command caused him to surrender instead of fleeing.",
    "Baeksang's only child Hwi was killed during the Great Snow Mountain battle, and the memory continues to drive his grief and revenge.",
    "Baeksang accepted an offer from an unidentified beautiful woman decades ago in pursuit of revenge and believes he cannot return from that path.",
    "Jin identifies the Miao village massacre, the Thousand-Year Spiders' escape from the Poisonblood Grounds, and the Western Yao Estate incident as a connected plot that killed more than three hundred people.",
    "Baeksang is wavering over the path of revenge and the consequences of completing it.",
    "Taishan is imprisoned above Jin's cell after being punished for eating too much and has discovered the broken ceiling."
  ],
  "continuity_sources": [
    663,
    662
  ],
  "open_questions": [
    "Who was the unidentified beautiful woman who offered Baeksang a means to achieve revenge?",
    "Will Baeksang's wavering alter his execution plan or alliance with Dark Heaven?",
    "How can Jin escape the underground prison before his execution?",
    "Was the connected plot behind the Miao village massacre, the Poisonblood Grounds incident, and the Western Yao Estate attack carried out as Jin suspects?",
    "What will Taishan do after discovering Jin through the broken ceiling?"
  ],
  "safe_through": 663,
  "temporary_decisions": [
    "Use Head Elder for 대장로.",
    "Use Hwi for 휘 and retain the note that 輝 means shining.",
    "Use revenge fiend for 복수귀.",
    "Use human compassion for 인정.",
    "Retain underground prison for 뇌옥."
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
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 남만야수궁  | **Nanman Beast Palace**          |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 살기     | **killing intent**                               |                                                       |
| 사부     | **Master**                                   |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 혈승 | **Blood Monk** | Sobriquet of the unidentified bald martial artist active in Guizhou. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 선장 | **Zen staffs** | Staff weapons carried by the Hundred and Eight Arhats. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 본단 | **League headquarters** | The League headquarters to which Hwang Tae-gu will be transported. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 대장군 | **Great General** | Military title used for the official who claimed credit after the Demonic Cult withdrew. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 철구 | **iron balls** | Training weights attached to Taekyung. |
| 선미 | **stern** | The rear of the swift ship. |
| 귀주 | **Guizhou** | Region whose Murim representatives send a delegate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 운남성 | **Yunnan Province** | The formal name of the destination region commonly called Nanman in the Central Plains. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |

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
| 수하 | 채주 | subordinate_to_stronghold_lord | Stronghold Lord | deferential | The subordinate calls Mu Song 채주 while reporting the nearby vessel. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
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
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
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

- **Safe through:** Chapter 663
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman; he has imprisoned Jin Taekyung and joined forces with twenty tribal chieftains to arrange Jin's execution at noon in two days.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with a deep but guarded attachment to his sworn elder brother and enduring grief, hatred, and betrayal over Baekhwi's death.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of his deceased only child Baekhwi, whom the Great Snow Fiend killed during the Great Faction War; he opposes the Nanman Beast Palace joining the Murim Alliance, distrusts the Central Plains because of the alleged wartime betrayal, and is alleged by Heugung to have colluded with Dark Heaven.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 662
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, is responsible for the forces stationed at Ailao Mountain, has ordered Ju Hwaran, Song Ilseom, and Hyuk Mujin to investigate the Blood Monk in Guizhou, and met the Martial God twice more than fifty years ago.

### Blood Monk.md

# Blood Monk (혈승)

- **Safe through:** Chapter 660
- **Aliases:** None
- **Role:** The Blood Monk is an unidentified, apparently middle-aged bald and beardless martial artist who carries a steel Zen staff and has killed several hundred people in Guizhou; his current destination is unknown.
- **Personality:** Unknown; the captured witness who described him was unable to provide further information before dying.
- **Voice:** Not established.
- **Relationships:** His connection to Dark Heaven and Nanman is unknown.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 663
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 661
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 663
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he is currently imprisoned under Baeksang's order with a public execution scheduled for noon in two days.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 663
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 659
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, an experienced Nanman escort guide with route knowledge from the Escort King's records, someone who can understand the Miao and Bai languages, and a volunteer accepted for the scouting mission to investigate the Blood Monk in Guizhou; she is currently alive but subdued with a Pressure-Point Strike.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 658
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 658
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 660
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 660
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 663
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate, a member of the Fire Dragon Pavilion, and a prisoner held above Jin Taekyung after eating too much.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 661
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

## Korean source

```text
＃664화



무림에 존재하는 뇌옥(牢獄)은 죄수 인권이라는 단어로 적당히 버무려진 현대의 교도소와 달리, 제 역할을 아주 톡톡히 해내는 장소다.

이곳에는 애초에 인권이라는 단어 자체가 없다.

사실 사천당가의 뇌옥만 해도 죄수를 가둔다는 목적보다는 고문실에 가까웠다.

당시 암천의 습격으로 죽었던 간수 할배만 해도 수십여 년 경력의 고문 기술자였는데, 그는 종종 자신의 전성기를 회상하며 흐뭇하게 웃고는 했다.



‘정마대전 직후가 참 좋았지요. 매일 악명 높은 마두가 서너 마리씩은 붙잡혀 들어 왔으니까요.’

‘……마리요? 명이 아니라?’

‘예에. 그중 열댓 마리를 주르륵 앉혀 놓고 작업을 시작하면 호응이 대단했습니다요. 아주 좋아서 자지러졌지요.’



사람을 세는 단위부터가 ‘마리’다.

나는 굳이 당시의 상황을 자세히 캐묻지 않았지만, 그가 혁대에 소중히 꽂혀 있던 소도(小刀)로 예쁜 이레즈미 타투를 새겨 주면 죄수들이 좋아서 자지러지는 광경은 상상하기 어려웠다.

‘타투는 개뿔.’

뻔하지.

뼈와 살이 갈라지고 피가 난무하는, 뭐 그런 거.

말이 조금 샜는데, 어쨌든 무림에서 뇌옥이라는 장소는 약간의 차이만 있을 뿐 대부분 비슷했다.

차갑고, 음습하며, 십중팔구는 땅속 깊숙한 지하에 있다.

지금 내가 갇혀 있는 남만야수궁의 뇌옥처럼. 그리고…….

“태산이. 배고프다. 밥 너무 먹는다고 뇌옥에 갇혔다.”

“아.”

저 웬수 같은 놈과 내 차이는, 고작 한 층에 불과했다.

예를 들자면 지하 3층과 4층 정도?

‘이게 이렇게 되네.’

어떤 의미로는 뇌옥의 노후화와 부실 공사. 거기에 상당한 충격이 가해져 나온 우연의 일치다.

멍하니 입을 벌린 채 천장을 바라보던 나는, 작은 구멍 사이로 커다란 눈을 껌뻑거리는 태산을 향해 피식 웃어 보였다.

“각주, 왜 웃나?”

“반가워서.”

“반가워? 각주는 태산이가 반갑나?”

“그래, 인마. 아주 반가워서 미치겠다.”

“오오. 그럼 태산이도 반갑다.”

이게 무슨 맥락 없는 대화인가 싶지만, 틈새 사이로 비치는 녀석의 눈동자를 볼 때마다 자꾸 웃음이 새어 나왔다.

반가운 얼굴을 마주한 건 둘째치고, 잘하면 예상보다 빠르게 이곳을 빠져나갈 수도 있겠다 싶어서.

물론 지금부터 머리를 굴리는 것과는 별개로, 내가 가장 신경 쓰이는 부분에 관해 답해 줄 유일한 사람이기도 하다.

“너 말고 다른 사람들은? 전부 잘 지내고 있지?”

내 물음에, 송아지처럼 커다란 눈동자가 축축하게 젖어든다.

“너 지금…… 우냐?”

“흐윽. 각주.”

설마?

순간 엄습하는 불길함. 나는 황급히 입을 열었다.

“질질 짜지 말고 제대로 말해 봐. 무슨 일이 있었는지.”

“태산이. 흐윽. 어쩔 수 없었다. 너무 원통하다.”

“……!”

빌어먹을. 눈앞이 캄캄해진다. 이미 머릿속에는 싸늘한 시신이 되어 누워 있는 화룡각 대원들의 모습이 떠오르는 중이었다.

‘아니면 고문? 하지만 어떻게 그럴 수가.’

순순히 투항하는 조건으로 화룡각 대원들의 안위를 보장받은 지 고작 한나절이 지났을 뿐이다.

다른 누구도 아닌 야수묘왕이 직접 약속했던 사안인데, 아무리 백상의 세력이 강해졌다고 해도 이럴 수는 없었다.

‘만약 그들이 해를 입었다면, 나는 도대체 뭘 위해서…….’

그리고 내가 허망하게 마음속으로 뇌까리던 그 순간, 태산이 축축한 목소리로 입을 열었다.

“아직도 믿을 수 없다. 지금쯤이면 다들 태산이만 쏙 빼고 밥을 먹고 있을 거라는 게.”

“……?”

“주군도 밉고, 남호도 밉다. 태산이 너무 원통하다.”

“……!”

“각주. 그런 의미에서 혹시 먹을 거 있나?”

이게 도대체 무슨 상황이지.

잠시 침묵하던 나는 진심을 담아 대답했다.

“없어. 이 씨벌놈아.”

“힝. 태산이 배고픈데.”

“……내려와. 너 지금 당장 내려와.”

개새끼가 진짜. 뒈질라고.

솟구치는 혈압과 동시에 분노가 전신을 지배한다. 나는 뇌옥에 갇힌 이래 가장 격렬한 몸부림으로 분노를 표출했다.

촤르륵, 철컹!

이 빌어먹게 무거운 철구만 없었어도 당장 저놈 죽탱이에 한 방 후리고 시작하는 건데.

씨근덕거리는 내 모습을 흥미롭게 관찰하던 태산이 입을 열었다.

“남호와 주군은 잘 지내고 있다. 각각 다른 곳에 억류되어 있어서 잘은 모르지만, 백호 주인이 알려 줬다.”

“백호 주인? 야율목?”

“오, 태산이 기억났다. 맞다. 야율목.”

다행히 야수묘왕이 손을 쓴 모양이군. 분노의 몸부림을 멈춘 나는 안도의 한숨을 내쉬었다.

“그것부터 말했어야지, 미친놈아. 사람 심장 떨어지게.”

“태산이. 벌써 두 시진이나 굶어서 정신이 혼미하다.”

“……보통은 두 시진 가지고 굶었다고 안 해. 그런데 넌 어쩌다가 여기에 갇힌 거냐? 어지간하면 야율 대협 선에서 막아 줬을 텐데. 정말 밥 많이 먹었다고 갇혔을 리는 없고.”

“태산이. 억울하다. 어떤 남만인이 밥을 쥐똥만큼만 주고 가려고 하길래, 더 달라고 손목을 붙잡았더니 뼈가 부러졌다.”

“…….”

“놀라서 다른 한쪽 손목을 붙잡았는데, 그것도 부러졌다. 이건 함정이 분명하다.”

촤르륵! 철컹! 철컹!

“각주. 진정해라. 태산이도 화가 났지만, 각주처럼 꾹 참고 투항했다.”

“……너 내려와. 이번엔 진짜 내려와.”

가뜩이나 몸 사려도 모자랄 판에, 밥 주러 온 남만인 양팔을 부러트려?

이제는 이틀 뒤 정오가 되기 전에 화병으로 죽을 지경이다.

‘내가 저런 새끼 살리겠다고 범 아가리에 들어오다니.’

깊은 빡침을 간신히 가라앉힌 내가 물었다.

“그럼 남호나 사마표 말고. 다른 사람들은?”

“으음. 아.”

커다란 눈동자를 뒤룩뒤룩 굴리며 생각하던 태산이 대답했다.

“붙잡혔다고 들었다.”

“붙잡혀?”

“응. 하지만 여기로는 안 온다고 했다. 태산이는 잘 모르겠는데, 백호 주인은 그게 더 안전하다고 했다.”

주화란과 송일섬. 그리고 혁무진.

척후대에 포함된 세 사람마저 붙잡혔다는 소식에 잠깐 마음이 무거워졌지만, 야율목의 말처럼 그편이 훨씬 안전할 거라는 의견에는 나 역시 동의했다.

‘지금 당장은 그곳까지 백상의 영향력이 미치지 못할 테니까.’

척후대를 이끄는 두 명의 부족장은 야수묘왕의 충신 격인 인물들.

더군다나 내가 독혈지에서 구한 남만인 중 그들의 혈족이 포함되어 있기까지 하니, 이번에 백상 쪽으로 돌아선 다른 부족장들처럼 쉽사리 말을 바꿔 타진 않을 것이다.

‘그 세 사람이 지금보다 더 위험해질 가능성은…… 척후대가 혈승(血僧)과 맞닥트릴 때겠지.’

혈승은 초절정의 무위를 앞세워 홀로 귀주성을 피로 물들인 정체불명의 노괴(老怪).

그에 관하여 알려진 정보는 거의 없지만, 만약 내 의심처럼 혈승이 남천마후의 수하라면 상황은 최악으로 치닫는다.

그렇다면 놈은 분명히 남천마후의 명령으로 남하(南下)할 테고, 척후대와 마주한다면 그 안에 포함된 세 사람 역시 혈승의 수중에 떨어질 테니까.

“……빌어먹을.”

하지만 현재로서는 거기까지 신경 쓸 틈이 없었다.

그들은 지금 이 순간에도 이동 중이며, 나는 지하 깊숙한 뇌옥에 갇혀 옴짝달싹 못 하는 상황이니까.

‘부디 혈승에 관한 내 짐작이 틀렸기를 바랄 수밖에.’

그러니까 지금 내가 할 수 있는 것은 단 두 가지뿐이다.

첫 번째는 기도.

두 번째는…….

‘탈옥.’

띠링.



- 새로운 퀘스트가 생성되었습니다!



연계 퀘스트, [남생크 탈출]을 확인하시겠습니까?

Y   /   N



나는 고개를 끄덕이며 생각했다.

도대체 어떤 놈이 시스템 개발자인지는 몰라도, 퀘스트 제목 한번 개같이 지었다고.

“그래서 각주. 먹을 거 없나?”

……정정. 저 새끼가 제일 개 같다.



* * *



수적이란 직업군은, 대륙에 존재하는 수많은 무림인 중에서도 특히 거칠고 자유분방한 족속들이다.

각종 법규에 억압받기 싫고, 관가에 잡혀가기도 싫고, 그렇다고 착하게 살기도 싫은.

수룡채(水龍寨)의 부채주인 수달 역시 그렇게 수적이 됐다.

착한 어부로 생을 마감한 아버지와는 다르게, 풍운아로 살다 죽겠다는 당찬 포부와 함께.

그렇게 나름 잘나가는 수적의 삶을 살았던 그가, 자신이 하는 일에 부쩍 회의감이 들기 시작한 것은 비교적 최근의 일이었다.

‘이게 뭐 하는 짓인가.’

하는 게 없다. 매일 뱃머리에 앉아 잔잔한 강물을 바라보고, 햇볕이 뜨거우면 헤엄도 치지만 그게 전부다.

사천의 장강을 호령하는 직속 상관은 지엄하신 맹주의 호출을 받아 본단으로 떠났는데, 자신과 수하들은 촌동네인 운남까지 지류를 타고 내려와 허송세월만 보내고 있었다.

‘지금쯤 사천에서는 온갖 재물을 실은 상선(商船)이 오가고 있겠지.’

지금의 장강은 노다지다.

무르익어 가는 전운(戰雲)과 함께 각종 물자가 오고 가는 상황.

그 사실을 아는 수달은 당장이라도 돌아가고 싶은 마음이 굴뚝 같았지만, 그럴 때마다 한 사람의 존재가 자꾸만 눈앞에 아른거렸다.



‘부르시면 언제든지 달려오겠습니다!’



그가 칠주야 전 했던 호언장담. 당연하게도 한 근의 영혼도 담겨 있지 않은 빈말이었다.

하지만 수달에 비해 새파랗게 젊은 상대방은, 푸근한 미소를 지으며 이렇게 답했다.



‘어이구. 잘됐네. 그럼 근처에 남아 계세요.’

‘예?’

‘허허. 귓구녕에 청새치라도 박으셨나. 남아 계시라고. 돌아갈 때도 부탁 좀 하게.’

‘그, 진 대협. 송구하지만 저희도 생업이…….’

‘생업이라. 생업 좋지. 근데 그거. 살아 있어야 할 수 있는 거 아닌가?’

‘……!’

‘아, 부탁 좀 하자고! 부탁 좀!’

‘허어억.’

‘시바 거. 확 그냥 돛대고 뭐고 죄다 분지르고 싹 다 태워 버릴라. 헤엄쳐서 사천까지 가고 싶어?’



말이 부탁이지, 실상은 협박이다.

하지만 뭐 어쩌겠나. 무림에서는 무공 강한 놈이 왕이다.

심지어 저 괴물 같은 젊은 놈의 사부는, 진짜 왕이라고 불리는 미친 노괴였다.

‘진태경. 이 개새끼…….’

수달은 눈물을 삼키며 고개를 끄덕였고 결국 칠 주야가 넘는 시간 동안 조각배도 안 보이는 운남성 끝자락 지류에서 물고기나 잡으며 자리를 지켜야 했다.

아니, 불과 하루 전 어떤 생각이 들기 전까지는 그랬다.

‘잠깐만. 굳이 이럴 필요가 있나? 어차피 진태경 그놈이 돌아오려면 시간도 꽤 남았을 텐데.’

비록 장강에서만 활동한 수적이지만, 수달도 안다. 남만이 얼마나 빌어먹을 똥 땅인지.

진태경의 임무가 정확히 무엇인지는 몰라도 여기까지 온 것을 보면 결코 간단한 것이 아닐 터.

한데 굳이 이 자리에 없는 놈을 신경 쓰며 똥 마려운 개처럼 끙끙거릴 필요가 있나.

수달은 자신이 살아온 모험심 가득한 삶을 진지하게 돌아보았고, 이내 수하들에게 명령했다.



‘야들아. 바람 좀 쐬러 가자.’

‘예?’

‘어디로요?’

‘바로 옆 동네가 귀주잖냐. 가까우니까 한 번 쭉 돌아보면서 털고 오자.’



그리고 수달의 이 야심찬 계획은, 수하들에게 그리 환영받지 못했다.



‘부채주. 돌았소?’

‘시바. 죽으려면 혼자 죽지. 수장도 아니고 화장당할 일 있나.’



하지만 이미 큰 포부를 품은 수달에게는 다 계획이 있었다.



‘저 새끼 담가. 그 장강. 장강…….’

‘장강 찍먹이요?’

‘그래. 진태경 그놈이 자주 하던 그거.’



그렇게 두 명을 연달아 담그자 볼멘소리는 쏙 들어갔고, 수달의 신명난 지휘 아래 서쪽 지류를 타고 귀주로 향한 세 척의 쾌조선은 마침내 오랜만의 표적을 발견할 수 있었다.

바로 지금 이 순간처럼.

“전방 이백 장 밖, 선박 한 척이 보입니다!”

“나포하라! 놓쳐서는 안 된다!”

이 얼마만의 약탈인가. 천하대장군처럼 선미에 우뚝 선 수달은 빠르게 가까워지는 선박을 보며 흐뭇하게 웃었다.

그리고 불과 일각(一刻)이 채 흐르기도 전. 무언가 잘못되었음을 깨달았다.

촤아아악!

어느새 코앞까지 가까워진 선박에는, 선원도 선장도 없었고 오직 한 사람만이 그들을 기다리고 있었다.

“장강수로맹의 쾌조선이라. 마침 잘됐군.”

“……!

얼어붙은 수달을 향해, 피에 젖은 선장(禪杖)을 든 민머리의 중년인이 활짝 웃어 보였다.

“이 배, 남만도 가느냐?”
```

## Final English reading copy

```markdown
# Chapter 664

Unlike modern prisons, where the concept of human rights has been mixed in just enough to make them palatable, the underground prisons found throughout the Murim served their purpose exceptionally well.

The word *human rights* did not exist here in the first place.

The underground prison of the Sichuan Tang Clan, for example, had been closer to a torture chamber than a place meant merely to lock up criminals.

Even the old guard who had died during Dark Heaven’s attack had been a torture expert with several decades of experience. He would often reminisce about his prime with a pleased smile.

“Those days right after the Great Faction War were wonderful. We caught three or four notorious fiends every day—counting them like animals, of course.”

“…Like animals? Not people?”

“Yes. When we lined up fifteen or so of the beasts and got to work, the response was incredible. They were so happy they nearly passed out.”

He even counted people the way one counted animals.

I had never bothered to ask for details about what had happened back then, but it was difficult to imagine prisoners nearly passing out from happiness just because he had given them pretty tattoos with the small knife he kept so carefully tucked into his belt.

*Like hell they were tattoos.*

It was obvious.

Bones and flesh splitting apart, blood spraying everywhere—something like that.

I had gone a little off track, but in any case, most underground prisons in the Murim were more or less the same, with only minor differences.

Cold, damp, and nine times out of ten, buried deep underground.

Just like the underground prison of the Nanman Beast Palace where I was currently locked up. And…

“Pavilion Master. Taishan hungry. Got locked in underground prison because Taishan eats too much.”

“Ah.”

The difference between me and that accursed bastard was only one floor.

The third and fourth underground floors, for example.

*So this is how it turned out.*

In a way, it was the result of an old, poorly built prison and a considerable impact coming together in one incredible coincidence.

I stared blankly at the ceiling. Then I gave a quiet laugh toward Taishan, who was blinking his enormous eyes through the small hole above me.

“Pavilion Master, why laugh?”

“Because I’m happy to see you.”

“Happy? Pavilion Master happy to see Taishan?”

“Yeah, you bastard. I’m so happy I could die.”

“Oh. Then Taishan happy to see Pavilion Master too.”

It might have seemed like a completely pointless conversation, but every time I saw his eyes peering through the gap, I couldn’t stop a laugh from escaping.

Meeting a familiar face was one thing. More importantly, I might be able to get out of here sooner than expected.

Of course, there was also the fact that he was the only person who could answer the question that concerned me most.

“What about everyone else? They’re all doing okay, right?”

At my question, his enormous calf-like eyes grew damp.

“Are you… crying?”

“Sniff. Pavilion Master.”

*No way.*

A sense of foreboding rushed over me. I hurriedly opened my mouth.

“Don’t just bawl. Tell me properly. What happened?”

“Taishan… sniff. It couldn’t be helped. It’s so unfair.”

“……!”

Damn it. My vision went dark. I could already see the members of the Fire Dragon Pavilion lying before me as cold corpses.

*Or torture? But how could they do that?*

It had only been half a day since I surrendered on the condition that the Fire Dragon Pavilion members would be kept safe.

This was something the Beast Miao King himself had promised. No matter how powerful Baeksang’s faction had become, this was impossible.

*If they were harmed, then what the hell did I surrender for…?*

Just as I was muttering those words hollowly inside my head, Taishan spoke in a damp voice.

“I still can’t believe it. By now, everyone must be eating without Taishan.”

“……?”

“I hate Lord too. I hate Namho too. Taishan is so unfairly treated.”

“……!”

“Pavilion Master. In that case, do you have anything to eat?”

What the hell was going on?

After remaining silent for a moment, I answered with all the sincerity in my heart.

“No, you fucking bastard.”

“Aw. Taishan hungry.”

“…Come down. Come down right now.”

That son of a bitch. He really wanted to die.

As my blood pressure soared, rage took control of my entire body. Since being locked in the underground prison, I had never thrashed around so violently in anger.

Clatter! Clank!

If not for these goddamn heavy iron balls, I would have started by punching that bastard in the mouth.

Taishan watched me panting with interest before speaking.

“Namho and Lord are safe. They are being held in different places, so Taishan doesn’t know much, but the White Tiger’s master told Taishan.”

“The White Tiger’s master? Yayul Mok?”

“Oh. Taishan remembers. Right. Yayul Mok.”

It seemed the Beast Miao King had made arrangements after all. I stopped thrashing around in anger and let out a sigh of relief.

“You should’ve said that first, you lunatic. You nearly gave me a heart attack.”

“Taishan has been hungry for two shichen already. Taishan’s mind is hazy.”

“…People don’t usually call it hunger after two shichen. More importantly, how did you end up locked in here? Great Hero Yayul would’ve stopped it before it got this far. There’s no way you were locked up just for eating too much.”

“Taishan was treated unfairly. A Nanman man was going to leave after giving Taishan food the size of mouse droppings, so Taishan grabbed his wrist and asked for more. His bone broke.”

“……”

“Taishan was surprised and grabbed his other wrist. That one broke too. This was obviously a trap.”

Clatter! Clank! Clank!

“Pavilion Master, calm down. Taishan was angry too, but Taishan held it in and surrendered, just like Pavilion Master.”

“…Come down. This time, really come down.”

I was already struggling to keep a low profile, and this bastard had broken both arms of the man who came to feed him?

At this rate, I was going to die of rage before noon two days from now.

*I entered the tiger’s den to save a bastard like that?*

After barely calming my fury, I asked,

“Then what about the others? Not Namho or Sama Pyo. Everyone else?”

“Hmm. Ah.”

Taishan rolled his enormous eyes around as he thought, then answered.

“I heard they were captured.”

“Captured?”

“Yes. But they said they weren’t coming here. Taishan doesn’t know why, but the White Tiger’s master said it was safer that way.”

Ju Hwaran, Song Ilseom, and Hyuk Mujin.

Hearing that even the three members of the reconnaissance squad had been captured made my heart feel heavy for a moment. But I agreed with Yayul Mok that they would be much safer there.

*Baeksang’s influence can’t reach that place for now.*

The two tribal chieftains leading the reconnaissance squad were loyal to the Beast Miao King.

What was more, some of the Nanman people I had rescued from the Poisonblood Grounds were their kinsmen. Unlike the other chieftains who had turned to Baeksang’s side, they wouldn’t easily switch allegiances.

*The three of them are more likely to be in danger than they are now if the reconnaissance squad runs into the Blood Monk.*

The Blood Monk was an unidentified old monster who had stained Guizhou with blood all by himself, wielding Supreme Peak martial prowess.

Almost nothing was known about him. But if he really was a subordinate of the Southern Heaven Demon Empress, as I suspected, then the situation would become the worst it could possibly be.

He would certainly head south on the Southern Heaven Demon Empress’s orders. And if he encountered the reconnaissance squad, the three people among them would fall into his hands as well.

“…Damn it.”

But for now, I had no time to worry about that.

They were still on the move at that very moment, while I was trapped in a prison deep underground, unable to move an inch.

*All I can do is hope my guess about the Blood Monk is wrong.*

So there were only two things I could do right now.

The first was prayer.

The second was…

*Escape.*

Ding.

> **System**
>
> A new Quest has been generated!
>
> Would you like to check the linked Quest, **Escape from Namshank**?[^1]
>
> **Y** / **N**

I nodded and thought,

*I have no idea who developed the System, but they came up with one hell of a shitty Quest title.*

“So, Pavilion Master. Do you have anything to eat?”

…Correction. *That* bastard was the shittiest of all.

[^1]: A pun on *The Shawshank Redemption*, replacing “Shaw” with “Nam,” referring to Nanman.

* * *

Among the countless martial artists in the continent, river pirates were an especially rough and free-spirited bunch.

They didn’t want to be oppressed by various laws, didn’t want to be arrested by the authorities, and didn’t particularly want to live decent lives, either.

Sudal, the Deputy Stronghold Lord of the Water Dragon Stronghold, had become a river pirate for exactly those reasons.

Unlike his father, who had ended his life as a good fisherman, Sudal had boldly resolved to live and die as a man of adventure.

He had lived the life of a fairly successful river pirate.

But lately, he had begun to feel increasingly doubtful about what he was doing.

*What the hell am I doing?*

He wasn’t doing anything.

Every day, he sat at the bow and stared at the calm river. When the sunlight became too hot, he went swimming.

That was all.

His immediate superior, who lorded over the Yangtze in Sichuan, had been summoned to League headquarters by the venerable Alliance Leader. Meanwhile, Sudal and his men had drifted down the tributaries all the way to the backwater of Yunnan, wasting their time.

*By now, merchant ships loaded with all kinds of valuable goods must be traveling through Sichuan.*

The Yangtze was a gold mine right now.

All kinds of supplies were moving back and forth as the clouds of war gathered.

Sudal knew that and desperately wanted to return immediately. But every time he did, one man’s presence kept flashing before his eyes.

“I’ll come running whenever you call!”

That was the boast he had made seven days and nights ago.

Naturally, it had been empty words without even a single ounce of sincerity behind them.

But the much younger man had merely smiled warmly and answered,

“Oh, good. Then stay nearby.”

“Excuse me?”

“Heh heh. Did someone stick a marlin in your ear? I said stay here. I’ll need to ask you for another favor when we head back, too.”

“Great Hero Jin, forgive me, but we have a livelihood to maintain…”

“A livelihood. That’s nice. But you need to be alive to make a living, don’t you?”

“……!”

“Come on, I’m asking a favor! Just a favor!”

“Gasp.”

“For fuck’s sake. I might just snap every mast and burn the whole lot down. Want to swim to Sichuan?”

It was called a favor, but in reality, it was a threat.

But what could Sudal do? In the Murim, the one with stronger martial arts was king.

And to make matters worse, that monstrous young man’s Master was a crazy old monster who was actually called a king.

*Jin Taekyung, you bastard…*

Swallowing his tears, Sudal had nodded. In the end, he had spent more than seven days and nights catching fish in a tributary at the edge of Yunnan where not even a small boat could be seen.

That was how things had been until an idea occurred to him just yesterday.

*Wait a minute. Do I really need to do this? There’s still plenty of time before that Jin Taekyung bastard comes back.*

Although he had only operated along the Yangtze, Sudal knew what a godforsaken dump Nanman was.

He didn’t know exactly what Jin Taekyung’s mission was, but considering that he had come all the way here, it could not possibly be simple.

But did he really need to worry about someone who wasn’t even here and whine like a dog that needed to shit?

Sudal seriously reflected on the adventurous life he had lived. Then he gave his men an order.

“Hey, boys. Let’s go get some fresh air.”

“Excuse me?”

“Where?”

“Guizhou’s right next door. It’s close, so let’s make a sweep through it, raid the place, and come back.”

Sudal’s ambitious plan was not well received by his subordinates.

“Deputy Stronghold Lord, have you lost your mind?”

“Fuck. If you want to die, die alone. You’re not even the boss—why should we all end up cremated?”

But Sudal had already formed a grand plan.

“Dunk that bastard. In the Yangtze. The Yangtze…”

“The Yangtze dip?”

“Yeah. That thing Jin Taekyung does all the time.”

After sending two of them into the water one after another, the complaints disappeared. Under Sudal’s spirited command, three swift ships traveled along the western tributary toward Guizhou.

At last, after all this time, they found a target.

Just like now.

“There’s a ship roughly two hundred zhang ahead!”

“Seize it! Don’t let it get away!”

How long had it been since their last raid?

Sudal stood tall at the stern like a Great General, smiling with satisfaction as the ship drew rapidly closer.

Then, before fifteen minutes had even passed, he realized that something was wrong.

Whoosh!

The ship had drawn so close that it was almost right in front of them. There was no crew. No captain.

Only one person was waiting for them.

“A swift ship of the Yangtze River Channel League. How fortunate.”

“……!”

The bald, middle-aged man holding a blood-soaked Zen staff smiled broadly at the frozen Sudal.

“Does this ship go to Nanman too?”
```
