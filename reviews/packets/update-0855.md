<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0855.txt",
      "sha256": "e5bd53d57161b4481d938de2beb9552e6c240c1dc4a4cb636fdd635b0fe507b9",
      "bytes": 14109
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9b59a4686b0fd3fa8af759734e9bfca910bee7329a5414fbf3ae18a64b941eca",
      "bytes": 2648
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c71f13dfc442c6e46aa85633ed364d93f329588811e408d32dcd5604f9a1a746",
      "bytes": 228458
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a03ec8da46bb4754bd057fc4d83ef01af555ba2aa1986406501fafee32d1f274",
      "bytes": 759
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "e2a6f3917c37b6a74b4a3241c3f826dbe196b0089dbc315a44334438add33e22",
      "bytes": 1355
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "a7fffa92a3c7d8e47831f60a85084f23869f1777bf3ab2e92fa74a0d33967d79",
      "bytes": 1573
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6cca03f917a0b58bdf2dc983600c4d92b527c4bab51407d25f88523c432df596",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "18244820c2dc86b0f873bdde0d7e9615b629d7d691d2e810451de7d5b62f0e1a",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "f54e01c3d3ca399b031b28bea884c267c478ca9ea602e4d3292702f22c5d9897",
      "bytes": 973
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "27784dc16b23d48d1e2681e39d75b3f946f415ee4b8bb806c5a34554e3e730ee",
      "bytes": 1061
    },
    {
      "path": "characters/Namho.md",
      "sha256": "aeba880f911da65751c8f87d1b3b1e2719c36701b77003306248acbfc3e724c5",
      "bytes": 973
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "57e3e7108a923c166bfe3f32e9c191e909b3f344a383a2a7552aab1ccff795b0",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "1eecbb78904f7f4380c0279f3bb368c7512a04862aa6553f3008a4908b42c715",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "058fb36d154803acbe512803aaa9a42278afa36d85a1d0c8f620fee1627c57e4",
      "bytes": 1074
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "1431e5a73eb1a4ca2f100c0f560d1b292a9910186d37eb6a7aca8b0e30c70d3b",
      "bytes": 787
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "cc5d369594aaa700470c4324ebb5e5eca4369f4e6e06ade6420e9961524dc80a",
      "bytes": 253241
    }
  ],
  "estimated_tokens": 15636
}
-->

# Durable State Update — Chapter 855

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
1 and safe_through 855. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 855. Profile updates may replace only one
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
  "chapter": 855,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 855,
    "continuity_sources": [855],
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
    "The Divine Physician secured the Blood Soul Gu found in the deceased City Lord of Sichuan Province; it weakens hosts, causes episodes of madness, and eventually kills them.",
    "Jin suspects Dark Heaven’s covert killing of the City Lord is part of a scheme targeting the Great Nation, possibly its imperial family.",
    "Prince Shangshan Zhu Bao is traveling with fifty Embroidered Uniform Guard members; their expected route from Shanxi passes through Shandong and Jiangsu toward Zhejiang.",
    "Hong Jin joined Prince Shangshan in Shanxi after requesting support from the Lower District Sect.",
    "A Shanxi tracking team was wiped out while following the group, and its operation was suspended over concern about official intervention.",
    "The Hidden Shadow Pavilion issued an Alliance Leader-approved order for Jeok Cheongang, Jin Taekyung, and the entire Fire Dragon Pavilion to escort Prince Shangshan.",
    "Jin and his party have departed to intercept Prince Shangshan in Jiangsu before the first of next month.",
    "A caravan of three trading companies, about five hundred people, was attacked by over a thousand bandits and river pirates at Yuhua Mountain; after three days of pursuit and the burning of their ten ships, fewer than a hundred survived.",
    "Two of the caravan’s three company masters were killed; survivors say the attackers fought with unnatural ferocity.",
    "A middle-aged man traveling with about ten companions has appeared before the survivors and asked who set their ships on fire.",
    "Jang Il is a gate commander at Yichang’s West Gate and is corrupt, though he considers himself moderate."
  ],
  "continuity_sources": [
    853,
    854
  ],
  "open_questions": [
    "Why did Dark Heaven secretly kill the City Lord of Sichuan Province?",
    "Is Dark Heaven targeting the Great Nation’s Emperor or imperial family, and is it influencing the Son of Heaven?",
    "What is the Embroidered Uniform Guard’s purpose in traveling with Prince Shangshan, and can Jin’s party reach him in time?",
    "What prompted the imperial decree against Hong Jin, and what will happen to him and Prince Shangshan?",
    "Who is the middle-aged man, and what explains the attackers’ unnatural ferocity and the assault on the caravan?"
  ],
  "safe_through": 854,
  "temporary_decisions": [
    "Render 혈혼고 as “Blood Soul Gu.”",
    "Render 독혈지 as “Poisonblood Grounds.”",
    "Render 대국 as “Great Nation.”",
    "Render 금의위 as “Embroidered Uniform Guard.”",
    "Render 옥화산 as “Yuhua Mountain.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 사천당가   | **Sichuan Tang Clan**            |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 내공     | **internal energy**                              |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 강소 | **Jiangsu** | Province at the eastern end of the Yangtze route. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |

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
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
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
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 854
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 849
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 853
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; they trust each other deeply but have never formalized their bond. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to the late Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and is a long-standing rival of Peng Cheolhu.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 853
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 853
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 849
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 853
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 853
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he now guides the Fire Dragon Pavilion.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 842
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 849
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 849
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 849
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃855화



“어떤 호로 새끼가 불을 질렀냐?”

착 내리깔린 음성.

뒤이어 칼날처럼 예리한 시선으로 주위를 훑은 혁무진이 탄성과 함께 부르르 몸을 떨었다.

“크으. 진짜 그때만 생각하면 저까지 지릴 것 같습니다! 역시 적 대…….”

“주둥이 닥치고 앉아라. 호되게 처맞고 똥오줌 지리기 전에.”

“옙.”

“저놈의 주둥이는 도무지 쉬는 법을 모르는군. 남만에서도 저랬느냐?”

적천강의 한숨 섞인 물음에, 옆에 있던 주화란이 조심스럽게 대답했다.

“네. 혁 소협이야 항상 그랬으니까요.”

“입마개라도 하나 있었으면 좋겠는데, 당장 어디서 구하지도 못하니 미칠 노릇이군.”

적천강은 입맛을 다시며 주위를 둘러보았지만, 그런다고 딱히 뾰족한 수가 생기는 것은 아니었다. 그들은 지금 풀과 나무로 가득한 숲길을 이동하고 있었으니까.

드물게 한 번씩 사람을 마주치긴 했어도, 어느 미친놈이 사람에게 채울 만한 입마개를 들고 산을 오르겠는가.

“하나 있긴 한데, 드립니까?”

“……?”

있었다. 그런 미친놈이.

심지어 바로 지척에.

“아니, 도대체 그런 걸 왜 들고 다니나?”

당혹스러움이 묻어나는 적천강의 물음에, 남호가 작은 목소리로 속삭였다.

“누구에게나 입마개를 채우고 싶은 놈 하나쯤은 있는 것 아니겠습니까.”

“……자네도 어지간하군.”

“여하튼 필요하시면 사양 말고 말씀하십시오. 물론 아예 드리는 건 아니고, 잠깐만 빌려드리는 겁니다. 저도 기회가 오면 바로 써야 해서요.”

남호는 의미심장한 눈빛으로 슬쩍 뒤를 돌아보았다. 때마침 얼마 떨어지지 않은 개울가에서 물속을 빤히 들여다보던 태산이 울상을 짓고 있었다.

“태산이. 도저히 못 찾겠다. 나이 많고 머리 좋은 남호의 도움이 필요하다.”

“흠.”

아무리 싫어도 웃는 얼굴에 침 뱉을 수는 없는 법.

눈이 마주치자마자 한 소리 하려던 남호가 약간 누그러진 목소리로 물었다.

“앞에 말이 좀 마음에 걸리긴 하는데…… 그래, 뭘 도와달라고?”

“고기를 찾고 있는데 안 보인다. 남호는 태산이랑 달리 똑똑하지 않나.”

“오늘따라 맞는 말만 하는군. 한데 뭘 잡으려고 거기에서 죽치고 앉아 있었느냐. 잉어? 붕어?”

“둘 다 아니다.”

“그럼?”

“오향장육.”

“이런 씨팔……!”

돌멩이를 움켜잡고 태산을 향해 미친 들소처럼 돌진하던 남호의 질주는 금세 가로막혔다.

적천강의 눈짓과 동시에, 어디선가 빛살처럼 나타난 사마표와 송일섬이 좌우에서 그의 양팔을 붙잡았기 때문이었다.

“놔, 이거 안 놔? 머리에 피도 안 마른 것들이 감히!”

“진정하시오, 남 노인.”

“우리도 이러고 싶진 않소.”

“지금부터 정확히 셋을 센다. 돌이킬 수 없는 일이 벌어지기 전에 노부를 놓아주는 것이 신상에 이로울 것이다. 자. 하나, 둘, 둘의 반. 둘의 반의반…….”

끝내 완성되지 못한 셋과 함께, 풀숲 어딘가로 질질 끌려가는 남호의 모습을 지켜보던 혁무진이 슬픈 목소리로 중얼거렸다.

“아쉽네요. 그동안 정이 많이 들었는데.”

“무슨 소리냐. 누가 들으면 진짜 죽이기라도 하는 줄 알겠군.”

“헛, 아닙니까? 저는 또 적 대협께서 이미 그런 명령을 내리신 줄 알고.”

“…….”

도대체 이놈은 자신을 뭐라고 생각하는 걸까.

적천강의 타오르는 눈빛에 당황한 혁무진이 주절주절 말을 늘어놓았다.

“아니 그, 며칠 전에 그 많던 산적 놈들을 싹 다 썰어 버리셨잖습니까.”

“노부가 무슨 푸줏간 백정이냐, 썰어 버리게? 그리고 산적뿐 아니라 수적 놈들도 포함되어 있었다.”

“그게 그거 아닙니까?”

“엄연히 다르다. 전부 죽어 마땅할 놈들이었다는 사실은 변하지 않지만.”

“불을 질러서요?”

“그야 당연……이 아니라 놈들이 애꿎은 인명을 해했기 때문이다.”

적천강은 황급히 말을 바꿨지만, 그 모습을 본 혁무진은 다시 한번 확신했다.

‘불 질러서 그런 거 맞네. 그래서 죽인 거네.’

희한하게도 적천강은 세상에 존재하는 수많은 죄악 중에서도 방화(放火)를 가장 으뜸으로 쳤다.

어쩌면 당연한 일일지도 모른다. 정마대전 당시, 정파에 합류해 달라는 검성 매종학의 부탁마저 거절했던 그가 세상에 나오게 된 계기는 마교도들의 방화 때문이었으니까.

사흘 전의 전투도 바로 그런 이유에서였다.

‘아니, 사실 그걸 전투라고 부르는 것도 민망하긴 하지.’

혁무진은 내심 앞서 했던 생각을 정정했다.

전투가 아닌 학살극으로.

그만큼 일방적이었고, 잔혹했다.

자그마치 삼백여 명에 달하던 산적과 수적들은 불과 반 시진 만에 전멸당했다.

그 뒤, 혁무진과 그의 일행은 호북에서 왔다는 상단주들의 인사를 듣는 둥 마는 둥 하며 떠났다.

그 불길 속에서도 용케 살아남은 유일한 상선 한 척을 목숨을 구해 준 대가로 받아 타고.

물론 상대방의 동의는 구하지 않았지만, 아무튼 그랬다.

“어라, 그러고 보니 지금쯤이면 그 사람들도 호북에 도착했겠는데요?”

“갑자기 무슨 딴소리냐?”

“그 사람들이요. 저희가 구해 준.”

“……그게 칼도 몇 번 안 휘두른 놈이 할 소리냐?”

“그래도 휘두르긴 했잖습니까.”

이런 뻔뻔한 놈을 보았나.

어이없는 눈빛으로 혁무진을 노려보던 적천강은 이내 고개를 절레절레 내저었다.

지금까지 겪은 바에 의하면 화룡각이라는 놈들은 하나같이 제정신이 아니다. 괜히 깊게 생각해 봤자 간신히 치유한 노환이 도질 것 같았다.

‘그나마 한 사람이라도 멀쩡한 걸 다행으로 여겨야 하나.’

적천강은 슬쩍 옆으로 시선을 돌렸다. 이 대환장 집단에서 유일한 정상인이라 할 수 있는 주화란이 그곳에 있었다.

‘보면 볼수록 마음에 드는 아이란 말이지.’

무언가에 쫓기듯이 사천당가를 떠난 지도 어언 칠 주야.

사람들의 이목을 최대한 피하고자 밤낮을 가리지 않고 인적 드문 험지(險地)만을 골라 이동했거늘, 주화란은 지금껏 불평 한마디 없이 밝은 모습을 보였다.

유일한 여인인 만큼 힘든 점이 한둘이 아닐 텐데도.

‘척 보아하니 무공 수련도 게을리하지 않은 것 같고, 심성도 아주 올곧아. 표왕이 손녀 하나는 아주 잘 뒀군.’

객기를 미덕으로 여기는 젊은이들이 어디 한둘인가.

길거리 왈패들에게만 해당하는 말이 아니다. 이른바 후기지수라 불리는 명문 대파의 제자 중에서도 한심한 놈들은 널리고 널렸다.

타고난 재능만을 믿고 노력을 게을리하며, 사문의 후광을 등에 업고 어깨에 힘이나 주고 다니는 멍청한 것들.

적천강으로서는 하도 많이 봐서 이제는 지긋지긋하게까지 느껴지는 부류였다. 그렇기에 주화란이 더 기특하게 느껴질 수밖에 없었다.

물론 흑심(黑心)이 아예 없다고는 말할 수 없지만.

‘지금 구파일방의 장로니, 장문인이니 하며 꺼드럭거리는 것들도 젊었을 적에 싹수가 노란 놈들이 한 바구니였거늘. 이 정도면 태경이 녀석한테는 과분……. 아니지. 그 녀석이 뭐가 부족해서? 인물 훤칠하고 풍채 좋지, 무공은 말할 것도 없어.’

머릿속에서 벌어지는 팽팽한 접전.

떡 줄 사람은 생각도 안 하는데 소면 국물부터 들이켜고 있던 적천강은, 다음 순간 불현듯 귓가를 파고든 목소리에 흠칫 놀랐다.

“적 대협, 괜찮으신가요?”

“으, 응?”

“다름이 아니라 표정이 복잡해 보이셔서…….”

“그게 그러니까. 크흠.”

걱정스러워하는 주화란을 향해 무심코 대답하려던 적천강이 황급히 헛기침을 내뱉었다.

그냥 손녀뻘도 아니고, 최소 증손녀뻘인 어린아이에게 늙은이의 괜한 주책까지 들키고 싶진 않았다.

“아무것도 아니다. 그저 강소성까지 남은 거리를 생각해 보고 있었다.”

“아, 지금 같은 속도라면 닷새 안에는 도착할 거예요. 만약 사정이 생겨 늦어진다 해도 칠 주야 정도로 예상합니다.”

“어찌 그리 확신하느냐?”

“이 년 전에 근방으로 표행(鏢行)을 온 적이 있거든요. 조부님 때부터 내려오는 지도도 따로 챙겨 두었고요.”

“호오. 대단하구나, 대단해.”

“감사합니다. 하지만 적 대협께서 과찬하실 수준은 아니에요.”

얼마 전까지 몸져누운 아비를 대신해서 몇 년간 표국을 이끌었다더니, 대답부터가 아주 딱 부러진다.

갑작스러운 칭찬에 몸 둘 바를 몰라 하는 주화란의 모습에, 적천강은 흐뭇한 미소를 머금었다.

“너는 다 계획이 있구나. 그 녀석과는 다르게 아주 야무져.”

“네? 그게 무슨…….”

“그냥 혼잣말이었다. 그나저나 자꾸 듣다 보니 호칭이 너무 딱딱하게 느껴지는데, 앞으로는 편하게 할아버님…….”

슬쩍 주화란의 눈치를 살핀 적천강이 말을 바꿨다.

아무래도 할아버님은 그가 생각하기에도 아직 너무 이르다. 모든 관계는 천천히 한 걸음씩 시작해야 한다.

괜히 한참 앞서갔다가 주화란이 경계심이라도 품게 되면, 하나뿐인 제자와 그녀의 관계에도 분명 악영향을 끼칠 테니까.

“……이 아니라 노야라고 부르거라.”

“정말요?”

적천강을 그런 호칭으로 부르는 이들은 이미 과거부터 선대와의 인연이 있거나, 구파일방 혹은 오대세가의 주인 된 자들뿐.

생각지도 못한 파격적인 제안에 주화란이 눈을 동그랗게 뜬 그때, 오가는 이야기를 듣고 있던 혁무진이 환하게 웃으며 끼어들었다.

“감사합니다, 노야. 그렇지 않아도 저 역시 호칭이 너무 딱딱하다고 생각…….”

“바위보다 딱딱한 노부의 주먹에 처맞을 테냐. 아니면 그 주둥이를 닥치고 있을 테냐.”

“…….”

“네놈은 안 된다. 꿈도 꾸지 말거라.”

어느 때보다 단호하게 못 박은 적천강이 험악한 얼굴로 혁무진을 노려보던 그 순간이었다.

“참나, 왜 애를 괴롭히고 그러세요? 불쌍하게.”

저 멀리, 그러나 바로 앞에서 말하는 것처럼 선명한 누군가의 목소리.

하지만 적천강은 그 목소리를 듣기도 전에 상대가 누구인지 알아차렸다.

심후한 내공을 지닌 절정 고수라 해도 듣지 못할 미세한 발걸음 소리와 호흡. 그것만으로도 충분했다.

만약 그의 이름 앞에 화왕(火王)이라는 별호가 붙지 않았어도, 혹은 초절정 고수가 아니었더라도 그 사실은 달라지지 않았을 것이다.

스승에게 있어 하나뿐인 제자의 존재란, 언제나 그런 것이었으니까.

“허어, 저 느려터진 놈 보게.”

그러나 적천강은 습관처럼 얼굴을 찡그리며 반가운 기색을 최대한 숨겼다. 조금 전 주화란을 대할 때와는 달리 퉁명스러운 목소리도 잊지 않았다.

“뭐 하다 이제야 설렁설렁 기어 오느냐? 네놈 때문에 꼬박 반나절은 기다렸다.”

“반나절이요?”

‘조장님!’을 외치며 달려든 혁무진의 정강이를 호되게 걷어찬 진태경이 헛웃음을 흘렸다.

“과장이 심하시네. 반나절은 무슨. 끽해야 겨우 한 식경 지났는데. 안 그래요?”

침이며 약재가 한가득 든 보따리를 들고 뒤따라오던 신의가 점잖게 대꾸했다.

“저는 말을 아끼겠습니다, 진 소협.”

“왜요?”

“뻔하지 않습니까. 굳이 대답해 봤자 말이 통할 리도 없고…….”

“이야, 의술만 뛰어나서 신의가 아니시네. 통찰력이 아주.”

“별말씀을. 그저 누구나 겪으면 알게 되는 자연스러운 일일 뿐이지요.”

“……아주 지랄들을 하는구나.”

가늘어진 눈으로 두 사람을 응시하던 적천강은 한바탕 쏘아붙이는 대신 입맛을 다셨다.

결국 이러니저러니 해도 저 버릇없는 젊은 놈은 미워하려야 미워할 수 없는 하나뿐인 제자고, 바로 옆의 늙은 놈은 그 젊은 놈의 치료를 위해 먼 길까지 동행하기로 한 의원이다.

더 뭐라 말할 수 있겠는가.

그저 아무렇지 않은 척, 걱정을 숨기며 이렇게 묻는 것이 고작이었다.

- 몸은 어떠하냐?

적천강의 전음(傳音)을 들은 진태경이 피식 웃으며 고개를 끄덕였다.

정말 괜찮은지, 괜찮은 척하는 것인지는 모르겠지만 전에 들었던 신의의 말이 사실이라면 분명 조금이라도 차도가 있을 터.

‘지금 당장은 괜찮다. 언제 벽에 가로막힐지는 모르겠지만…… 최대한 방법을 찾아봐야지.’

그리고 문득 말이 없어진 적천강의 모습에, 살짝 쓴웃음을 흘린 진태경은 굳어 있던 몸을 풀며 입을 열었다.

“이제 얼마나 남았죠? 사흘? 나흘?”

주화란이 마치 기다렸다는 듯이 대답했다.

“사흘 정도요.”

“사흘이라……. 초하루까지 시간은 남았지만 그래도 아슬아슬한데?”

진태경은 동쪽 어딘가를 바라보며 말을 이었다.

“남은 시간. 이틀로 줄여 보죠.”
```

## Final English reading copy

```markdown
# Chapter 855

“Which son of a bitch set the fire?”

A voice dropped low.

Hyuk Mujin swept his surroundings with a gaze sharp as a blade, then shuddered with a gasp.

“Damn. Just thinking about that time makes me feel like I’m about to piss myself! As expected of Great Hero Je—”

“Shut your mouth and sit down before I beat you so badly you piss and shit yourself.”

“Yes, sir.”

“That mouth of his never seems to take a break. Was he like that in Nanman, too?”

At Jeok Cheongang’s sighing question, Ju Hwaran, who was standing beside him, answered cautiously.

“Yes. Young Hero Hyuk has always been like that.”

“I wish I had a muzzle for him, but there’s no way to find one around here. It’s enough to drive me mad.”

Jeok Cheongang clicked his tongue and looked around, but that didn’t produce any particular solution. They were traveling along a forest path full of grass and trees.

They did occasionally encounter people, but what kind of lunatic would carry a muzzle meant for a person up a mountain?

“I do have one. Shall I give it to you?”

“……?”

There was such a lunatic.

And he was right nearby.

“Why on earth are you carrying something like that?”

At Jeok Cheongang’s bewildered question, Namho whispered in a small voice.

“Doesn’t everyone have at least one person they’d like to put a muzzle on?”

“……You’re quite something yourself.”

“Anyway, if you need it, just say the word. I won’t give it to you outright, of course. I’ll only lend it to you for a little while. I’ll need it myself as soon as I get the chance.”

Namho glanced meaningfully over his shoulder. Not far away, by a stream, Taishan was staring intently into the water with a troubled look.

“Taishan. I can’t find it at all. I need Namho’s help. He’s old and smart.”

“Hm.”

No matter how much you disliked someone, you couldn’t spit in the face of a smile.

Namho had been about to say something the moment their eyes met, but his tone softened a little as he asked,

“I’m not too sure about that first part, but… fine. What do you need help with?”

“I’m looking for meat, but I can’t see any. Namho’s smart, unlike Taishan.”

“You’ve said nothing but true things today. But what were you sitting there waiting for? Carp? Crucian carp?”

“Neither.”

“Then what?”

“Five-spice pork.”

“Fuck…!”

Namho grabbed a rock and charged at Taishan like a mad bison, but his run was quickly cut short.

At Jeok Cheongang’s glance, Sama Pyo and Song Ilseom appeared like streaks of light from somewhere and grabbed his arms from either side.

“Let go! Let go of me, you brats! You brats are still wet behind the ears!”

“Calm down, Elder Namho.”

“We don’t want to do this either.”

“I’m going to count to three. It would be in your best interest to let go of this old man before something irreversible happens. Now. One, two, two and a half. Two and three-quarters…”

Before he could reach three, Namho was dragged off into the undergrowth. Watching him go, Hyuk Mujin murmured sadly,

“That’s a shame. I’d grown quite attached to him.”

“What are you talking about? Anyone listening would think we were actually going to kill him.”

“Wait, we aren’t? I thought Great Hero Jeok had already given the order.”

“……”

What on earth did this guy think he was?

Flustered by Jeok Cheongang’s burning gaze, Hyuk Mujin started rambling.

“I mean, a few days ago, you cut down every last one of those bandits. All those men…”

“What am I, a butcher? ‘Cut them down’? And it wasn’t just bandits. River pirates were mixed in, too.”

“Isn’t that basically the same thing?”

“They’re distinctly different. Though it doesn’t change the fact that every last one of them deserved to die.”

“Because they set the fire?”

“Of course… No. Because they harmed innocent people.”

Jeok Cheongang hurriedly changed his answer, but watching him only confirmed Hyuk Mujin’s suspicion.

*It was because they set the fire. That’s why he killed them.*

Strangely enough, of all the countless sins in the world, Jeok Cheongang considered arson the worst.

Perhaps that made sense. During the Great Faction War, Sword Saint Mae Jonghak had asked him to join the orthodox faction, but Jeok Cheongang had refused. What finally brought him out into the world was the Demonic Cult’s arson.

The battle three days ago had been for exactly that reason.

*Actually, it’s embarrassing to even call that a battle.*

Hyuk Mujin quietly revised his earlier thought.

It hadn’t been a battle. It had been a massacre.

It was that one-sided—and that brutal.

A full three hundred bandits and river pirates had been wiped out in less than an hour.

Afterward, Hyuk Mujin and the others had left, barely listening to the trading company masters from Hubei thank them.

They’d taken the only merchant ship that had somehow survived the flames as payment for saving their lives.

Of course, they hadn’t asked for the other party’s consent. But anyway, that was what happened.

“Oh, come to think of it, those people must be in Hubei by now, right?”

“Why are you suddenly changing the subject?”

“Those people. The ones we saved.”

“……Is that something a man who barely swung his sword a couple of times should say?”

“But I did swing it.”

What nerve.

Jeok Cheongang glared at Hyuk Mujin in disbelief, then shook his head.

From what he’d seen so far, every last one of those Fire Dragon Pavilion fellows was out of his mind. Thinking too hard about it would only bring back the infirmities of old age he’d barely managed to cure.

*I suppose I should be grateful there’s at least one normal person among them.*

Jeok Cheongang turned his gaze slightly to the side. The one person he could call sane in this band of lunatics, Ju Hwaran, was there.

*The more I see her, the more I like her.*

It had been seven days since they’d left the Sichuan Tang Clan as if something were chasing them.

They’d been traveling day and night, choosing only remote, rugged terrain to avoid drawing attention. Yet Ju Hwaran hadn’t complained once. She’d remained cheerful the whole time.

There must have been any number of hardships, especially as the only woman in the group.

*She’s clearly kept up with her martial arts training, and her character is upright, too. The Escort King has himself one fine granddaughter.*

How many young people mistook recklessness for a virtue?

And that wasn’t limited to street thugs. Even among the disciples of the great sects who were known as young prodigies, there were plenty of fools.

They trusted only in their natural talent, neglected to work hard, and strutted around with their sect’s prestige at their backs.

Jeok Cheongang had seen that sort so often he was sick of them. That was why he couldn’t help finding Ju Hwaran all the more admirable.

Though, of course, he couldn’t say he had no ulterior motives at all.

*Even the ones swaggering around as Elders and Sect Leaders of the Nine Sects and One Gang now were a whole basket of no-good brats when they were young. Compared to them, Hwaran is more than Jin Taekyung deserves… No. What’s he lacking? He’s handsome, well-built, and there’s no need to mention his martial arts.*

A fierce battle was underway in his head.

Jeok Cheongang had already started sipping the broth before the person who’d give him the noodles had even considered it, when a voice suddenly pierced his ears and startled him.

“Great Hero Jeok, are you all right?”

“Hm? What?”

“You looked troubled, so I was wondering…”

“Ah. Ahem.”

Jeok Cheongang had started to answer without thinking, but he hurriedly cleared his throat.

He didn’t want a young girl who was at least young enough to be his great-granddaughter to discover an old man’s foolish preoccupations.

“It’s nothing. I was just thinking about how far we have left to Jiangsu.”

“Oh. At our current pace, we’ll arrive in five days. Even if something comes up and delays us, I expect it’ll take about seven days.”

“How can you be so sure?”

“I came through this area on an escort mission two years ago. I also brought along a map that’s been passed down from my grandfather’s time.”

“Ho. Impressive. Very impressive.”

“Thank you. But I’m not worthy of such high praise from you, Great Hero Jeok.”

They said she’d led the Escort Bureau for several years in place of her father, who had been bedridden until recently. Her answer was every bit as crisp as he’d expect.

Ju Hwaran looked flustered by the sudden praise, and Jeok Cheongang smiled warmly.

“You’ve got everything planned out. You’re so capable, unlike that brat.”

“Pardon? What do you mean…?”

“I was just talking to myself. Still, the more I hear you address me that way, the more stiff it sounds. From now on, you can just call me Grandpa—”

Jeok Cheongang checked Ju Hwaran’s expression and changed his mind mid-sentence.

Grandpa was still far too soon, even by his own reckoning. Every relationship had to start with one step at a time.

If he got ahead of himself and made Ju Hwaran wary, it would surely affect her relationship with his one and only Disciple, too.

“……No. Call me Old Master.”

“Really?”

The only people who called Jeok Cheongang that were those who had known his predecessors, or the heads of the Nine Sects and One Gang and the Five Great Families.

Ju Hwaran’s eyes widened at his unexpected offer. At that moment, Hyuk Mujin, who’d been listening to their conversation, chimed in with a bright smile.

“Thank you, Old Master. I thought the same thing—that the way I address you is too stiff…”

“Would you rather be hit by this old man’s fist, which is harder than a rock? Or keep your mouth shut?”

“……”

“You’re not allowed. Don’t even dream about it.”

Jeok Cheongang made the ruling more firmly than ever and glared at Hyuk Mujin with a fierce expression.

“Good grief. Why are you picking on the poor kid?”

A voice spoke from far away, yet it was as clear as if the speaker were right in front of them.

But Jeok Cheongang knew who it was before he even heard the voice.

A faint footstep and breath—so subtle that even a Peak master with deep internal energy wouldn’t have heard them. That alone was enough.

It wouldn’t have made a difference even if the title Fire King hadn’t come before his name, or if he weren’t a Supreme Peak master.

That was simply what having a one and only Disciple was like for a Master.

“Heh. Look at that slowpoke.”

But Jeok Cheongang instinctively frowned, hiding his delight as much as possible. Unlike when he’d spoken to Ju Hwaran, he didn’t forget to keep his voice gruff.

“What took you so long? Why are you crawling along at a leisurely pace now? I’ve been waiting half a day because of you.”

“Half a day?”

Hyuk Mujin ran toward Jin Taekyung shouting, “Captain!” and Jin Taekyung kicked him hard in the shin. Then he let out a hollow laugh.

“You’re exaggerating. Half a day, my ass. It’s only been half an hour at most. Isn’t that right?”

The Divine Physician, who had followed behind them carrying a bundle stuffed with needles and medicinal herbs, replied calmly.

“I’ll refrain from commenting, Young Hero Jin.”

“Why?”

“Isn’t it obvious? Even if I answer, there’s no point. There’s no reasoning with you anyway…”

“Wow. So you’re not called the Divine Physician just because of your medical skills. You’ve got some insight, too.”

“You’re too kind. It’s simply something anyone would come to understand after experiencing it.”

“…What the fuck is wrong with you two?”

Jeok Cheongang watched them with narrowed eyes, but instead of laying into them, he clicked his tongue.

One way or another, that rude young brat was his one and only Disciple, whom he couldn’t bring himself to hate. And the old man right beside him was a physician who’d agreed to travel a long way to treat that young brat.

What more could he say?

All he could do was pretend nothing was wrong, hide his worry, and ask this:

*How are you feeling?*

Jin Taekyung heard Jeok Cheongang’s Sound Transmission and gave a quiet laugh as he nodded.

Whether he was really all right or only pretending, if what the Divine Physician had told him was true, there should be at least some improvement.

*I’m all right for now. I don’t know when I’ll hit a wall, but… I’ll have to find a way, as best I can.*

Then, noticing Jeok Cheongang had fallen silent, Jin Taekyung gave a faint, bitter smile. He loosened his stiff body and spoke.

“How much farther? Three days? Four?”

Ju Hwaran answered as if she’d been waiting for the question.

“About three days.”

“Three days… We still have time before the first of the month, but it’s going to be close.”

Jin Taekyung looked somewhere to the east and continued,

“Let’s cut the time left down to two days.”
```
