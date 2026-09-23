<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0884.txt",
      "sha256": "707061a95af46c6e9c747594012173dc1462f7e06c13853628e13eaba01f767b",
      "bytes": 12891
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0b5dd8d4e93b3286891f1cbedc2cb5d1e5a4f38f620692123b6eadf941e64fa5",
      "bytes": 3037
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "77f7f9625d663fdeec408b3696199ba3f21d98f335ae9eae4e9465caec345d0f",
      "bytes": 230213
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f50e05aa0d54fd897412a3962fe14f9c21badd3bc06aafbee0d7ddd40858ce77",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "aa638680606f97adcfe8511c82eeda322b545dfbb7ada08ea28d6da421cc6ff7",
      "bytes": 837
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3d65d75eae5ef34b2a615731e06f2bec6d19c0d5e2729eeaead5cf39c2e88fe9",
      "bytes": 1511
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "ea3993396222b580f1e855a00d1e48952dda847710eab1dcb314d0ffa11934ea",
      "bytes": 628
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "d073c65da523d9d239f1d2fc1d73bc9c9c8d5dcce20ba76946f0b3a3a4a07a32",
      "bytes": 699
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "7ee45ab89191c883393d37c713b97cae3e36210369d5a317814288f1570d2a43",
      "bytes": 796
    },
    {
      "path": "characters/Namho.md",
      "sha256": "3ada41bfef2b083e62c6250ccc907c838a34bf43b4b83bb650eacd63f097efc9",
      "bytes": 973
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "5032d67024383b3dbf672a310a40eea3232f3e45f68b6f4b7dff790669ff9f21",
      "bytes": 952
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "cf810e89e0f02b2a9f6c890af0c5f9d064d53ba308c1844e36eb686bfca24f05",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "09b53280f2f55380f3c06063ad7ba1703945c2a87f5ff6dbfc057024484b3303",
      "bytes": 259022
    }
  ],
  "estimated_tokens": 11837
}
-->

# Durable State Update — Chapter 884

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
1 and safe_through 884. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 884. Profile updates may replace only one
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
  "chapter": 884,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 884,
    "continuity_sources": [884],
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
    "The Emperor has confined Prince Shangshan in Qianqing Palace; Taekyung returned without him.",
    "The Emperor plans a banquet attended by Shangshan and civil and military officials; Hong Jin suspects it could be a trap.",
    "Ma Sanbao spread rumors using information Jin Taekyung gave him; the Emperor ordered the arrested rumor-spreaders released.",
    "Ma Sanbao is a central figure in a covert faction of survivors seeking to overthrow the Emperor; they have signed a pact and expect the banquet to become a confrontation.",
    "Ma Sanbao says the person his allies asked about is safe and expects the young martial artist to help; he believes the martial artist’s master could be decisive.",
    "Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.",
    "The late Emperor died after a period of mental confusion while confined; Taekyung suspects Blood Soul Gu may have been involved, but this is unconfirmed.",
    "The City Lord of Sichuan Province showed strange symptoms before his death, and Blood Soul Gu was found in his corpse.",
    "Jeok Cheongang received two letters, burned them, and said the group was formally invited to the imperial palace; their contents remain unknown.",
    "Jin Taekyung’s group has an official invitation to perform as the Blazing Flame Troupe at the imperial banquet.",
    "Jeok Cheongang’s group is inside the Outer Palace disguised as a circus troupe; the Divine Physician gave them Energy-Dispersing Poison to conceal their martial skill during screening, while Jeok can conceal his aura without it.",
    "A courtesan seeking revenge against the Emperor died by her own hand during Jeong Hogun’s screening; her companions were taken to prison, and a familiar but unidentified young man has approached Hogun."
  ],
  "continuity_sources": [
    882,
    883
  ],
  "open_questions": [
    "Is Aehyang pregnant, and what does the Emperor intend for her and Shangshan?",
    "Will the banquet become a confrontation, and what does the Emperor intend?",
    "Did the Emperor or Dark Heaven use Blood Soul Gu against the late Emperor and the City Lord of Sichuan Province?",
    "Who is the person Ma Sanbao’s allies asked about, and what preparations has the faction made?",
    "Who is the familiar young man who approaches Jeong Hogun, and what will happen when Hogun questions Taishan?"
  ],
  "safe_through": 883,
  "temporary_decisions": [
    "Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”",
    "Use “imugi,” not “dragon,” for the creature Taekyung killed at Dongting Lake.",
    "Render 연판장 as “a pact bearing their signatures”; retain “Hongmen Banquet” for 홍문연.",
    "Treat 거산 as an uncertain name variant for Taishan, not a confirmed separate person; render 열화단 as “Blazing Flame Troupe” and 마희단 as “circus troupe.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 태원진가   | **Jin Family of Taiyuan**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 기녀     | **courtesan**                                    |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 노부      | **this old man / I**                                            |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 근골 | **Muscles and Bones** | System attribute increased by 2 during the climb. |
| 대성 | **Great Completion** | Completion stage of a martial technique. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 역용술 | **disguise technique** | Technique used by the Third Fiend to conceal his identity. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 외공 | **external arts** | Martial arts focused on extreme bodily training. |
| 요녕 | **Liaoning** | Northeastern region from which the Murong Family arrives. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 거산 | **Geosan** | Jeok Cheongang's uncertain variant for Taishan's name; not confirmed as a separate person. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 관리 | 적천강 | government official to legendary martial master | you | formal, then alarmed and deferential | The official questions Jeok Cheongang, insults him as an old man, and later learns that he is the Fire King. |
| 적천강 | 관리 | legendary martial master to government official | you | blunt and mocking | Jeok Cheongang repeatedly echoes the official's formal phrasing while challenging his authority. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 홍진 | 마삼보 | Longtime friend and former East Depot cohort | Ma Constable; Eunuch Ma | Familiar and respectful | Hong uses both forms while acknowledging Ma’s former and current standing. |
| 마삼보 | 홍진 | Longtime friend and former East Depot cohort | Hong Constable | Familiar and respectful | Ma addresses Hong by his former East Depot title. |
| 정호군 | 상산왕 | imperial guard officer escorting the prince | His Highness | formal and deferential | Hogun formally reports that he has come to escort the prince. |
| 정호군 | 홍진 | Embroided Uniform Guard officer addressing a senior imperial official | Deputy Military Commissioner | formal and admonishing | Hogun tells Hong Jin to mind his words. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 홍진 | 정호군 | Embroided Uniform Guard officers of equal rank | Thousand Captain Jeong | polite and direct | Hong Jin addresses Jeong Hogun by rank and surname. |
| 정호군 | 기녀 | guard officer addressing a courtesan under examination | you | formal and controlled | He tells her that she knows the reason for the questioning and asks whether she will explain herself. |
| 정호군 | 태산 | guard officer questioning a performer | you | blunt and direct | He calls Taishan forward and asks whether he belongs to the circus troupe. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 883
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 880
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care; the Fourth Prince spared him because of their old ties, and his longtime friend and former East Depot cohort Ma Sanbao stayed behind in the palace.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 883
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 883
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 883
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 881
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language, using calm reassurances and strategic metaphors to maintain unity while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 883
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he now guides the Fire Dragon Pavilion.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 882
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 883
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃884화



눈 앞에 펼쳐진 상황을 본 순간, 나는 생각했다.

‘내 이럴 줄 알았지.’

물론 내가 용한 무당도 아니고, 신기(神氣)가 알려 주는 대로 갑작스럽게 찾아온 건 아니다.

아무래도 직접 가 봐야 할 것 같다는 생각이 든 것은 홍진에게 그 소식을 들은 직후였다.



‘조금 전에 진 공자 쪽 사람들이 입궁했어요. 마희단(馬戲團)으로 위장해서. 그런데…….’

‘무슨 문제라도 생겼습니까?’

‘맞아요. 그 과정에서 생각보다 이목을 많이 끌었나 봐. 그 왜, 일행 중에 엄청나게 덩치 큰 사람 있죠?’

‘아니 시팔. 그러지 말라니까.’

‘……아직 아무 말도 했는데?’

‘들어 봤자 뭐 해요. 평소 하는 꼬라지를 생각해 보면 뻔하지. 안 되겠어요. 저 좀 나갔다 오겠습니다.’

‘잠깐. 마 태감이 뭔가 조치를 취해 놨을 테니 조금만 더 기다려 봐요.’

‘제 일행들은 제가 더 잘 알아요. 만일을 대비해서라도 직접 가 보는 게 나을 겁니다.’

‘조장님 말씀이 백번 옳습니다. 제가 모시고 금방 다녀올 테니 홍 동지께서는 마음 푹 놓고 기다리십쇼.’

‘무진아.’

‘예. 조장님.’

‘깝치지 말고 여기 남아 있어.’

‘…….’

‘이 새끼가 가서 또 무슨 사고를 치려고.’



일말의 망설임도 없이 즉각 전각을 빠져나온 것이 지금으로부터 한 식경 전.

무슨 이유에선지는 모르겠으나 황제를 알현했던 이틀 전을 기점으로 전각을 에워싸고 있던 금의위는 멀찍이서 감시만 할 뿐 별다른 제재를 가하진 않았고, 홍진이 알려 준 장소는 생각보다 훨씬 가까웠다.

물론 수상쩍어 보이지 않게 빙 둘러 가야 한다는 단점이 있었지만, 다행히도 아슬아슬한 타이밍에 도착할 수 있었다.

바로 지금 이 순간에.

“어, 호군이. 여기서 뭐 하니?”

내가 천연덕스럽게 뱉은 그 한 마디에, 활시위처럼 팽팽하게 당겨져 있던 주위의 공기가 느슨하게 풀어진다.

그리고 곧장 내 얼굴을 향해 우수수 날아와 꽂히는 시선들.

그중에는 낯설면서도 익숙한 얼굴들 역시 포함되어 있었다.

‘인피면구인지 뭔지는 몰라도, 역용술(易用術) 하나는 기가 막히게 했네.’

사람의 외모란 묘한 것이어서 이목구비의 작은 변화만으로도 인상이 확 바뀌기 마련.

자연스럽게 좌중을 쓸어보는 척, 한쪽 구석에 옹기종기 모여 있던 일행들을 확인한 나는 정호군을 향해 손을 흔들어 주었다.

“옛말에 웃는 얼굴에 침 못 뱉는다는데, 우리 호군이 보면 꼭 그런 것도 아닌 것 같아. 사람이 말을 걸면 대답이라도 좀 해 줄래?”

정호군이 가라앉은 얼굴로 입을 열었다.

“누구더러 우리 호군이냐.”

“그럼 느그 호군이.”

“언제나 생각하는 거지만, 도무지 말이 안 통하는군.”

“냄새나고 새카만 불알들끼리 서로 통해 봤자 뭐 하려고. 혹시 나한테 관심 있어?”

“전혀. 하지만 네놈이 난데없이 이곳에 나타난 목적이 무엇인지에 대해서는 관심이 생기는군.”

역시 금의위라고 해야 하나?

무뚝뚝한 말투와는 달리 그 안에 담겨있는 뜻은 바늘 끝처럼 날카롭다. 하지만 나도 지금껏 무림에서 구르고 넘어지며 무력만 단련한 것은 아니다.

그리고 앞서 허비한 한 식경은, 적들의 의심을 피하고 그에 따른 대응을 생각하기에 충분한 시간이었다.

“목적은 뭔 개 같은 놈의 목적. 그냥 심심해서 근처 한 바퀴 돌던 와중에 분위기가 심상찮아서 와 본 거지.”

나는 필시 어느 누군가의 몸에서 흘러나왔을, 지면에 흩뿌려진 핏물을 가리키며 말을 이었다.

“혹시나 해서 와 봤는데, 역시나네?”

“…….”

“오는 길에 보니까 한 열댓 명이 줄줄이 엮여서 끌려가던데, 역모라도 저질렀나?”

대답 대신 한참이나 나를 빤히 바라보던 정호군이 불쑥 입을 열었다.

“그래, 기녀로 위장해서 연회에 참여하려고 했더군.”

오는 길에 끌려가는 이들을 봤다는 건 결코 거짓이 아니다.

나는 문득 금의위 중 하나가 멍석에 둘둘 말아 끌고 가던 시신을 떠올렸다.

아마도 지금 정호군이 언급했던 기녀가 바로 그 시신의 정체였을 것이다.

‘무슨 이유 때문이었을까.’

나로서는 딱히 알 도리가 없었다.

황제에 의해 멸문지화(滅門之禍)를 당했던 가문의 생존자였을 수도 있고, 충의지사를 자처하는 누군가가 보낸 암살자였을 수도 있으니까.

어차피 경우의 수는 많다. 문제는 그로 인해 더욱 촉각이 곤두선 정호군이 아군을 의심할 수 있다는 것이다.

‘시작부터 이러면 곤란하지.’

나는 최대한 자연스럽게 입을 열었다. 지금껏 해 왔던 것처럼 약간의 경멸을 담은 눈빛과 목소리로.

“감히 황제 폐하께 칼을 들이대려던 역적을 처단하셨으니, 이번에는 무조건 승진하시겠네. 우리 정 천호님.”

“내가 죽인 것이 아니다. 스스로 자결했지.”

“직접 죽인 거나 다름없지. 그 여자가 왜 자결했겠어? 이대로 끌려가서 죽을 때까지 고문당하는 것보다야 그게 더 편안하니까. 어차피 실패한 마당에 깔끔하게 죽는 게 백배 천배 나으니까 그런 선택을 했다는 거…… 당신도 알잖아?”

잠시 침묵하던 정호군이 담담한 목소리로 대답했다.

“그래, 맞는 말이지.”

뭐지?

원래 저런 놈이긴 했지만, 내 날 선 말에도 희한할 만큼 별다른 반응이 없는 정호군의 모습에 나는 내심 중얼거렸다.

‘뭔가 눈치챘나?’

다른 금의위들에 비해서도 유난히 촉이 좋아 보이는 놈이니 혹시 모를 일. 그렇다면 이대로는 곤란하다.

나는 빙글빙글 웃으며 앞으로 걸음을 내디뎠다.

“모처럼 인정하는 모습이 보기 좋네. 어때, 기왕 온 김에 한 손 거들어 줘?”

“돕겠다고?”

“어렵지 않지. 혹시 아나, 금의위도 솎아 내지 못한 역적을 내가 잡으면 지엄하신 황제 폐하께서 소원이라도 하나 들어주실지.”

“무슨 속셈이지?”

“이거 또 이러네. 인마, 너 그거 직업병이야. 이 정도 중증이면 신의(神醫)가 와도 못 고쳐.”

지금만큼은 모든 시선이 나를 향해 있는 것이 천만다행이다.

사람들 사이에서 반사적으로 움찔하는 신의를 못 본 척한 나는 정호군을 향해 어깨를 으쓱해 보였다.

“여하튼 싫으면 말고. 괜찮다 하면 쓱 둘러보고. 아무래도 그런 쪽으로는 내가 너보다는 조예가 깊거든. 알지?”

이건 그냥 하는 말이 아니다.

감시와 취조에는 정호군이 압도적으로 앞설 수 있어도, 단순히 그 사람의 무위를 판가름하는 데에 있어서만큼은 초절정의 벽을 넘어선 내가 한 수 위임이 틀림없으니까.

아니, 지금은 사용할 수 없는 [기감]으로 정확한 정보를 알아낼 수 있다면 오히려 나야말로 금의위에 최적화된 인재였다.

물론 이런 내 제안이, 다른 이들의 귀에는 조금 이상하게 들렸겠지만.

- 아니, 이런 미친놈을 보았나…….

- 무슨 짓을 꾸미고 있는 거냐.

아니나 다를까. 두 줄기의 전음이 차례대로 도착했다.

첫 번째 전음은 적천강이 흘린 것이었고, 두 번째는 정호군이었다.

그리고 피식 웃은 나는 똑같이 전음으로 답했다.

빈틈 하나라도 놓치지 않겠다는 듯이 날 뚫어져라 응시하는 한 사람. 정호군에게만.

- 뭘 또 전음씩이나 보내. 얼마나 대단한 일이라고.

- 제대로 답해라. 이러는 이유가 뭐지?

- 이유? 그야 뻔한 거 아닌가?

나는 정호군을 똑바로 응시하며 입술을 달싹였다.

- 연회 때 어느 정신 나간 놈이 칼부림이라도 벌이면? 그래서 네가 좋아 죽는 그 지엄하신 황제 폐하께서 다치기라도 하면. 그거 다 누가 뒤집어쓸 것 같은데?

- ……!

- 네가 모시는 주인을 위해서가 아니라, 상산왕 전하를 지키기 위해서 이러는 거라고. 이 병신아.

이거야말로 누가 들어도 앞뒤가 완벽하게 떨어지는 해명 아닌가.

오는 길에 급하게 생각해 낸 대안이지만, 효과는 확실했다.

딱딱하게 굳어 있던 정호군의 안면 근육이 조금이나마 부드럽게 풀리는 것을 확인했으니까.

‘성공이다.’

하지만 아직 끝나지 않았다.

당장이라도 새어 나오려는 안도의 한숨을 삼킨 나는 혀를 차며 돌아섰다.

마지막 쐐기를 박는 전음과 함께.

- 뭐 보아하니 지금 당장은 딱히 수상쩍은 놈이 없긴 한데…… 앞으로도 일 똑바로 하라고. 나나 당신이나. 각자 지켜야 할 사람이 있잖아. 안 그래?

그게 끝이었다.

나는 처음 왔던 그대로, 느긋한 발걸음을 옮겨 고요해진 사람들 사이를 가로질렀다. 얼굴은 바뀌어도 떡대만큼은 여전한 태산의 앞에서 멈칫하며 반응해 주는 것도 잊지 않았다.

“와, 미친. 덩치 보소. 도대체 뭘 먹고 이렇게 컸어요?”

태산이 더듬더듬 대답했다.

“오향, 오향장육 좋아한다.”

“거짓말.”

“……어?”

“입에 들어가는 건 다 좋아할 것 같은데.”

“아, 어어. 좋다.”

“근골이 아주 그냥 제정신이 아니네. 외공(外功)도 익혔죠?”

“거산이. 어릴 때 마희단에 팔렸다. 살려면 익혀야 했다.”

마희단은 천하를 유랑하며 공연하는 일종의 서커스단.

어지간한 규모의 도시라면 꼭 한 번은 마주칠 수 있는 부류였고, 따라서 주로 몸을 혹사하는 그들이 외공을 익히는 것도 결코 이상한 일은 아니다.

‘이상한 건 저 타고난 덩치지.’

내심 중얼거린 나는 근육으로 똘똘 뭉친 태산의 팔다리를 주무르며 말을 이었다.

“이 정도면 진짜 어지간한 일류 고수도 주먹으로 때려잡을 수준인데…… 혹시 어디서 왔어요?”

옆에 있던 까무잡잡한 피부의 노인, 남호가 잽싸게 허리를 굽히며 대답했다.

“장강(長江) 이북을 거점으로 두고 있습니다요. 주로 하북과 요녕성을 중심으로 공연을 하고 있습죠.”

“어, 가깝네. 생각 있으면 산서성 태원진가에도 한 번 들러요. 이 사람이 시기를 좀 놓치긴 했어도, 어느 정도의 공력만 받쳐 준다면 무림인으로도 대성할 수 있을 테니까.”

“제안은 감사하지만 그건 좀. 보셔서 아시겠지만 남들보다 머리가 모자라긴 해도 저희 마희단의 보배라…….”

확실히 은영각 출신이라 그런지 애드립 한번 끝내준다.

나는 충무로의 블루칩을 쪼인트 까는 연기력을 보여 주는 남호와 몇 마디를 더 주고받은 뒤, 잔뜩 아쉬운 표정으로 사라졌다.

내심 확신하며.

‘됐어.’

이제 조금 전의 대화를 들은 사람들은 알게 되었을 것이다.

저 엄청난 거인이 딱 일류 고수를 쓰러트릴 정도의 외공을 익혔고, 그들이 속한 마희단은 황도와 엄청나게 떨어진 장강 이북에서 활동하고 있었으며, 크게 의심할 여지는 없다는 것을.

그리고 결정적으로, 배불뚝이 관리는 내가 생각지도 못했던 아군이었다.

“더 조사할 게 없다면 저들은 통과시킵시다. 이미 몇 차례에 걸쳐 충분히 검증된 이들이기도 하고, 처리해야 할 일이 산더미요.”

그와 동시에 뇌리를 스치는 홍진의 한 마디.



‘잠깐. 마 태감이 뭔가 조치를 취해 놨을 테니 조금만 더 기다려봐요.’



그 말은 결코 거짓이 아니었다.

마삼보는 동창을 움직여 눈에 띄는 대신, 보이지 않는 아군을 심어 둔 것이 틀림없었다.

‘내 등장도 거기에 더해 다행히 잘 맞아떨어졌고.’

그렇게 천천히 십여 장을 걸었을 때쯤, 나는 한껏 곤두선 청력을 통해 정호군의 무뚝뚝한 목소리를 들을 수 있었다.

“통과.”

나는 쾌재를 불렀고, 곧이어 날아든 적천강의 전음에 잠시 할말을 잃었다.

- 역시, 네 녀석은 다 계획이 있구나. 노부는 굳게 믿고 있었느니라.

- …….

아니, 노야.

조금 전에는 미친놈이라면서요.
```

## Final English reading copy

```markdown
# Chapter 884

The moment I saw the situation spread out before me, I thought:

*I knew this would happen.*

Of course, I wasn’t some gifted shaman who’d been summoned here by a divine message. I hadn’t suddenly rushed over on a hunch, either.

The thought that I should probably go see for myself had come right after I heard the news from Hong Jin.

“People from Young Master Jin’s group entered the palace a little while ago. Disguised as a circus troupe. But…”

“Did something go wrong?”

“That’s right. I guess they attracted more attention than we expected. You know that huge guy in the group?”

“Ah, shit. I told them not to do that.”

“…I haven’t even said anything yet.”

“What’s the point of hearing it? Given the way they usually act, I can guess. This won’t do. I’m going out for a bit.”

“Wait. Eunuch Ma must have taken some measures. Let’s wait a little longer.”

“I know my companions better than anyone. Even if it’s just to be safe, I should go see for myself.”

“Captain, you’re absolutely right. I’ll escort you and bring you back in no time, so Comrade Hong can relax.”

“Mujin.”

“Yes, Captain.”

“Don’t go picking a fight. Stay here.”

“……”

“That bastard’s going to go start another mess.”

I’d left the pavilion without a moment’s hesitation half an hour ago.

For some reason, ever since I’d met the Emperor two days earlier, the Embroidered Uniform Guard surrounding the pavilion had only watched from a distance and hadn’t tried to stop me. The place Hong Jin had told me about was much closer than I’d expected.

The downside was that I had to take a long detour so I wouldn’t look suspicious, but fortunately, I made it just in time.

Right now.

“Oh, Hogun. What are you doing here?”

At my casual greeting, the tension in the air—which had been pulled taut as a bowstring—eased.

Then eyes came pouring down on me.

Among them were a few faces that looked both unfamiliar and familiar.

*I don’t know if those are human-skin masks or what, but they did a hell of a job with the disguise technique.*

People’s impressions could change completely with the smallest alteration to their features.

I naturally pretended to sweep my gaze over the crowd and spotted my companions huddled together in one corner. Then I waved to Jeong Hogun.

“There’s an old saying that you can’t spit in the face of someone who’s smiling, but looking at you, Hogun, I guess that’s not always true. When someone talks to you, could you at least answer?”

Jeong Hogun’s face remained still as he spoke.

“Who are you calling ‘our Hogun’?”

“Fine, then. Your Hogun.”

“As always, it’s impossible to have a sensible conversation with you.”

“What’s the point of a bunch of smelly, black balls understanding each other? Are you interested in me, by any chance?”

“Not at all. But I am curious why you suddenly appeared here.”

That was the Embroidered Uniform Guard for you.

His tone was blunt, but the meaning behind it was sharp as a needle. Still, I hadn’t spent all my time stumbling around Murim training only my martial skills.

And the half-hour I’d just wasted had been more than enough to think through how to avoid the enemy’s suspicions—and how to respond if I drew them anyway.

“What the hell do you mean, ‘why’? I was bored, so I was taking a walk around the area. The mood seemed strange, so I came to see what was going on.”

I pointed to the blood splattered across the ground—blood that had to have flowed from someone—and continued.

“I had a feeling I’d find something, and look at that.”

“……”

“On the way here, I saw about fifteen people being dragged off in a line. Did they commit treason or something?”

Jeong Hogun stared at me for a long while without answering, then abruptly spoke.

“They were trying to attend the banquet disguised as courtesans.”

It was no lie that I’d seen people being dragged off on my way here.

I suddenly remembered a corpse that one of the Embroidered Uniform Guard had been hauling away, rolled up in a straw mat.

The courtesan Jeong Hogun had just mentioned was probably that corpse.

*I wonder why she did it.*

I had no way of knowing.

She could have been a survivor of a family destroyed by the Emperor, or an assassin sent by someone who fancied themselves a champion of loyalty and righteousness.

There were plenty of possibilities. The problem was that this incident had put Jeong Hogun even more on edge, and he might start suspecting our allies.

*This can’t be how things go from the start.*

I spoke as naturally as I could, with the same hint of contempt in my eyes and voice I’d used until now.

“You brought down a traitor who dared raise a blade against His Majesty the Emperor. You’re definitely getting promoted this time, Thousand Captain Jeong.”

“I didn’t kill her. She took her own life.”

“It’s basically the same thing. Why do you think she killed herself? Because being dragged off and tortured to death would’ve been worse. She’d failed anyway, so dying cleanly was a hundred, a thousand times better. You know that too, don’t you?”

Jeong Hogun was silent for a moment, then answered in an even voice.

“Yes. You’re right.”

What?

He’d always been like that, but there was something strange about how little my sharp words seemed to affect him. I wondered to myself,

*Has he noticed something?*

He seemed sharper than the other members of the Embroidered Uniform Guard. It wasn’t impossible. If so, I couldn’t let things continue like this.

I walked forward with a broad smile.

“It’s nice to see you admit I’m right for once. How about I lend you a hand while I’m here?”

“You want to help?”

“It’s easy enough. Who knows? If I catch a traitor even the Embroidered Uniform Guard couldn’t weed out, maybe His Majesty the Emperor will grant me a wish.”

“What are you up to?”

“There you go again. Hey, that’s a professional habit. You’re so bad, even the Divine Physician couldn’t cure you.”

It was a good thing everyone’s attention was on me right now.

I pretended not to notice the Divine Physician flinching on reflex among the crowd, then shrugged at Jeong Hogun.

“Anyway, if you don’t want me to, just say so. If you’re fine with it, I’ll take a quick look around. I know a thing or two about that sort of thing—more than you do, anyway. You know that.”

I wasn’t just saying that.

Jeong Hogun was far better at surveillance and interrogation, but when it came to simply judging someone’s martial skill, I was definitely a step ahead of him. I’d crossed the threshold of Supreme Peak, after all.

No—if I could use Qi Sense, which I couldn’t right now, to get precise information, I’d be the perfect person for the Embroidered Uniform Guard.

Of course, my offer probably sounded a little strange to everyone else.

—Is this guy out of his mind…?

—What are you plotting?

Two messages reached me one after the other through Sound Transmission.

The first had come from Jeok Cheongang. The second was from Jeong Hogun.

I gave a quiet laugh and replied the same way, looking only at Jeong Hogun, who was staring at me as if he didn’t want to miss a single opening.

—Why are you sending a message through Sound Transmission? It’s not that big a deal.

—Answer me properly. Why are you doing this?

—Why? Isn’t it obvious?

I stared straight at Jeong Hogun and moved my lips.

—What if some lunatic starts swinging a sword at the banquet? And what if that stern Emperor you love so much gets hurt? Who do you think’s going to take the blame for it all?

—……!

—This isn’t for the sake of the master you serve. I’m doing this to protect His Highness Prince Shangshan. You idiot.

It was the perfect explanation. Anyone who heard it would think it made complete sense.

I’d come up with the alternative in a hurry on the way here, but it had worked.

I saw the muscles in Jeong Hogun’s stiff face relax, just a little.

*Success.*

But it wasn’t over yet.

I swallowed the sigh of relief that was about to escape me, clicked my tongue, and turned away.

With one last message to drive the point home.

—Well, there doesn’t seem to be anyone particularly suspicious right now, but do your job properly from here on out. Both of us. We each have someone to protect, don’t we?

That was it.

I walked back the way I’d come, at an easy pace, crossing through the now-quiet crowd. I didn’t forget to pause and react when I reached Taishan, whose face had changed but whose massive build hadn’t.

“Whoa, damn. Look at the size of you. What on earth do you eat to get that big?”

Taishan answered haltingly.

“I like five-spice pork.”

“Liar.”

“…Huh?”

“You look like you’d eat anything.”

“Oh. Uh-huh. I like it.”

“Your muscles and bones are completely ridiculous. You’ve trained in external arts, haven’t you?”

“Geosan. Sold to circus troupe when young. Had to learn to survive.”

A circus troupe was a kind of traveling show that wandered the land performing for people.

You could find one in just about any sizable city, so it wasn’t strange for performers who put their bodies through the wringer to learn external arts.

*The strange part is how naturally huge he is.*

I thought to myself, then ran my hands over Taishan’s arms and legs, which were packed with muscle.

“With a build like this, you could beat most First Rate masters with your bare fists… Where are you from?”

Namho, an old man with dark skin standing beside us, promptly bowed and answered.

“We’re based north of the Yangtze, sir. We mostly perform in Hebei and Liaoning.”

“Oh, that’s close. If you’re interested, stop by the Jin Family of Taiyuan in Shanxi Province sometime. He may have missed his chance, but if he has enough internal energy to back it up, he could still become a great martial artist.”

“We’re grateful for the offer, but we’d rather not. As you can see, he’s not as bright as other people, but he’s the treasure of our circus troupe…”

He certainly had a talent for improvisation, probably thanks to his Hidden Shadow Pavilion background.

Namho was showing the kind of acting that could kick one of Chungmuro’s rising stars in the shins. After exchanging a few more words with him, I left with an exaggeratedly disappointed look.

Feeling certain inside.

*Good.*

Anyone who’d heard that conversation would now know that the enormous man had trained in external arts to the point where he could take down a First Rate master, that his circus troupe operated north of the Yangtze, far from the imperial capital, and that there was little reason to suspect them.

And, most importantly, the potbellied official was an ally I hadn’t even known about.

“If there’s nothing else to investigate, let them through. They’ve already been thoroughly vetted several times, and I have a mountain of things to take care of.”

Hong Jin’s words came to mind at the same time.

“Wait. Eunuch Ma must have taken some measures. Let’s wait a little longer.”

Those words hadn’t been a lie.

Rather than mobilize the East Depot and draw attention, Ma Sanbao must have planted allies where no one would notice them.

*And fortunately, my appearance seems to have fit right in with that.*

After I’d walked several dozen yards, I heard Jeong Hogun’s blunt voice with my keen hearing.

“Let them through.”

I cheered inwardly, then fell momentarily speechless at the Sound Transmission that came flying in from Jeok Cheongang.

—As expected, you had everything planned out. This old man believed in you all along.

—……

No, Old Master.

A moment ago, you called me crazy.
```
