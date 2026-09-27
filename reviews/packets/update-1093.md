<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1093.txt",
      "sha256": "8d5dbcfb70281975595890520b1d91478d756af1fec6b3f906c692686811b60e",
      "bytes": 12374
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9cc6674175ec861b56496a2ded3b8a50a68c6b68a65a18599d3eb93fbbbd750b",
      "bytes": 1474
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bee69e076364377f31e7856d6f9b353d3362d24e22138f2ec1d79723928adc10",
      "bytes": 243843
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "51613356b0af56a63a8901da1a6da0d6995a7e172069e1b68f72beab01e4c084",
      "bytes": 916
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "68b7f51f12300697a02f6d92234c687cc13404633e1b6aa0fd5e23cd52d82710",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "a0cd012b6c599406152fe2d4517cebf3079703de604d2d1e70fcd9ebb3f54faa",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "cae376a19b321c71987bf5d0c4a410209d1698b1145a73328a5ee0c4ad50b76a",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6196048a512530cbb25950c17405935c9cc0d6d4971a186242898fd2512ca6ca",
      "bytes": 623
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "c9bdfd52abb54e64b60799a302559bdaa328e08acda544bb7b885942dabc3b17",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ebe79c16d6adf08cf85ebe92be4ce390014b7513b9c2f13e94caedd0cd180dd5",
      "bytes": 287086
    }
  ],
  "estimated_tokens": 10706
}
-->

# Durable State Update — Chapter 1093

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
1 and safe_through 1093. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1093. Profile updates may replace only one
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
  "chapter": 1093,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1093,
    "continuity_sources": [1093],
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
    "Dark Heaven’s army has arrived at Xining, led by the Blood Lord.",
    "Jin Taekyung has chosen to defend Xining’s civilians against the approaching forces.",
    "Jeok Cheongang supports Taekyung’s decision and intends to use his remaining strength.",
    "Mae Jonghak and the New Murim Alliance prepared an operation against Dark Heaven; Zhuge Feng has the intelligence and tasking to execute it.",
    "The Zhuge Clan left its ancestral home and fled to Mount Wudang.",
    "The Blood Lord is stronger than Taekyung and has an abnormally enlarged, stitched-looking arm with superhuman strength; he attributes it to “his grace.”",
    "Taekyung has been wounded and disarmed in the fight against the Blood Lord.",
    "The Fire King and Slaughter Saint have joined the fight against the Blood Lord.",
    "A streak of lightning descends from the city wall."
  ],
  "continuity_sources": [
    1091,
    1092
  ],
  "open_questions": [
    "Who is the black-robed captive in Qinghai, and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "Who or what caused the lightning strike from the city wall, and what is the outcome of the fight with the Blood Lord?"
  ],
  "safe_through": 1092,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 마교     | **Demonic Cult**                                 |                                                       |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 감숙     | **Gansu**              |
| 화산     | **Huashan**            |
| 노부      | **this old man / I**                                            |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 불장 | **Buddhist Staff** | Generic term in Hong Dao's final words; the specific treasure is 녹옥불장. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |
| 황도 | **Imperial Capital** | The capital where the imperial court resides. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1092
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; strategically manipulates allies and adversaries, and conceals failures from the Lord of Heaven when he fears being discarded.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1092
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1091
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1092
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1092
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1092
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
1093화




콰아아앙!

귓가가 먹먹해지는 굉음에 이어 지면을 타고 전해지는 울림에, 고개를 돌려 등 뒤의 광경을 확인한 적천강이 비로소 안도의 한숨을 내쉬었다.

‘할망구가 나섰군.’

지금 이 순간에도 먼지구름을 뚫고 빗발치는 섬광들.

궁성(弓星)이 진태경을 돕고 있음을 확인하자 비로소 그의 마음 한구석이 편안해지는 듯했다.

궁성이 합류한 이상 자신의 제자는 안전하다.

적어도 적천강이 목적을 이룰, 잠시 동안만큼은.

‘걱정이 태산 같았는데…… 괜한 우려였나.’

적천강이 판단하기에, 진태경은 아직 혈주의 상대가 아니었다. 그래서 촌각 전 귓가를 파고든 전음(傳音)을 듣고도 불안을 감출 수 없었다.



‘제가 혈주를 끌어내며 시간을 벌 테니, 두 분은 놈들의 본진을 노리는 게 좋겠습니다.’

‘뭐?’

‘걱정하지 마세요. 제 인생 신조가 뭔지 아시잖아요?’



물론 알고 있었다.

그 두께가 굵건 얇건, 무조건 살아남아 길게 가는 것.

하지만 세상일이 단순히 바라는 대로만 이루어진다면, 천하의 무림인들은 초절정 고수가 됐을 테고, 백성은 무병장수했을 터.

그렇기에 적천강은 단호하게 반대했다.

아니, 반대하려고 했다.

그 태평스러운 대답에 적천강이 뭐라 반응하기도 전, 진태경은 망설임 없이 뛰쳐나가 혈주와 맞서 싸우기 전까지는.

‘제 목숨 아까운 줄도 모르는, 천하의 어리석은 놈 같으니.’

그러나 머릿속 생각과는 달리, 어느덧 적천강의 입가에는 미소가 맺혀 있었다.

그리 멀지 않은 곳에서 한창 혈풍(血風)을 불러일으키고 있던 살성이 참다못해 한마디 할 정도로 선명한 미소가.

“하나뿐인 제자가 예뻐 죽겠는 건 알겠는데, 진짜 이대로 죽고 싶어서 환장…… 흡.”

일순간, 말을 끝까지 잇지 못하고 호흡을 삼킨 살성이 신형을 비틀었다.

쉬쉬쉭!

불현듯 공간을 조각내며 달려든 세 줄기의 검광(劍光)이 한 뼘 차이로 스쳐 지나간다.

그와 동시에 허공에서 몸을 회전시킨 살성의 옷소매 사이로 섬광이 번뜩였다.

카카캉! 퍼걱!

두 개의 불똥과 하나의 섬뜩한 파육음.

머리부터 발끝까지 칠흑 같은 갑주로 무장한 채, 살성을 향해 벼락처럼 짓쳐 들던 세 명의 흑의인이 주춤하며 물러섰다.

보다 정확히는, 두 명의 흑의인이.

쿵.

흑의인 중 하나가 썩은 고목 나무처럼 쓰러졌다.

얼굴조차 보이지 않게 깊게 눌러쓴 투구의 눈구멍 사이에는, 조금 전 살성이 쏘아 보낸 비수 한 자루가 깊숙이 박혀 있었다.

“우선 한 놈.”

아무 일도 없었다는 듯이 부드럽게 착지한 살성의 한 마디에, 지금 막 화염이 실린 일권(一拳)으로 수십여 명의 적들을 쓸어버린 적천강이 고개를 저었다.

“글쎄, 아닐 텐데.”

“……무슨 뜻이지?”

“무슨 뜻이긴.”

적천강이 쓰러져 있는 흑의인을 향해 턱짓하며 덧붙였다.

“저런 뜻이지.”

바로 그 순간.

푹.

죽은 줄로만 알았던 흑의인이 스스로 팔을 움직여 투구에 박힌 비수를 뽑았다.

그리고 이어 비틀비틀 일어나 검을 들어 올렸다.

마치, 잠깐 벌에라도 쏘였던 것처럼.

“……!”

말없이 눈을 깜빡이는 살성의 모습에, 적천강이 고개를 절레절레 저었다.

저 지긋지긋한 괴물을 처음 봤을 때의 자신이 생각나서였다.

“태경이 그 녀석이 말해 주지 않았나? 하늘이 정한 순리를 정면으로 거스르는 빌어먹을 것들이 있다고.”

그제야 눈앞의 적들이 누구인지 깨달은 살성이 침음성을 흘렸다.

“……흑귀(黑鬼).”

감숙에서의 일은 살성 역시 이미 들어서 알고 있었다.

죽여도 죽여도 다시 일어나는 괴물들이 있으며, 놈들의 정체는 하나같이 과거 마교를 주름잡았던 마두(魔頭)들이었다고.

“전설로만 내려오는 생강시(生僵尸)와 비슷한 존재라던데. 사실이었나 보군.”

“생강시보다도 더 개 같은 놈들이지. 움직임만 봐도 느낌이 올 텐데?”

살성의 곁에 선 적천강은 대답과 함께 다시금 공력을 일으켰다. 어느덧 여섯으로 불어난 흑귀들이 사방을 점한 채 다가오는 중이었다.

“쓰러트리는 방법은?”

“노부가 듣기로는 두 가지 방법밖에 없다더군. 첫째, 죽을 때까지 죽이거나.”

화륵.

적천강의 양손을 타고 백색의 불길이 넘실거린다.

유독 어둡게 느껴지는 공간 속, 기이한 소리를 내며 가까워지는 흑귀들과 빽빽하게 주위를 감싼 적들의 모습이 밝아졌다.

그 거대한 포위망의 깊은 곳에 숨어서 그들을 조종하는, 또 다른 존재들의 모습도 함께.

“둘째, 머리를 잘라서 팔다리를 무력화시키거나.”

그리고 그 순간.

퍼어엉!

적천강은 온 힘을 다해 쌍장(雙掌)을 떨쳤다.

넘실거리는 화염의 파도를 사방으로 흩뿌리는 동시에, 지면을 박차며 쏘아졌다.

“방(防)!”

- 그아아아아!

인간과 괴물의 고함이 한데 뒤섞인다.

전후좌우를 빈틈없이 뒤덮은 적들의 사이로 불의 길이 만들어지고, 이에 굴하지 않고 적천강의 앞을 막아선 흑귀들의 사각(斜脚)으로 한 줄기의 예리한 바람이 불었다.

쉭. 서걱!

적천강을 향해 휘둘려지던 검이 허공으로 솟구친다.

가장 먼저 달려든 흑귀의 팔을 일검에 베어 버린 살성이 힘주어 외쳤다.

“어서!”

짤막한 외침이었으나 그 안에 담긴 의미는 선명하다. 작게 고개를 끄덕인 적천강은 거침없이 전진하며 일권(一拳)을 말아쥐었다.

그그극.

아지랑이로 뒤덮인 공간의 중심, 극의에 다다른 멸염신권(滅炎神拳)이 백색의 화염을 머금는다.

무려 삼 장에 달하는 거구의 괴물도, 촘촘한 방어진을 구축하고 있던 암천의 교도들도 그 열기를 느끼고 눈을 크게 떴다.

그리고 일순간 시간이 멈춘 듯한 그 세상 속에서.

“노부가 바로.” 

적천강의 일권이 바람을 짓뭉개며 뻗어 나갔다.

“화왕(火王)이니라!”

콰아아아아아!

공간이 일그러진다. 지면이 주저앉는다.

끔찍하리만치 거대한 열기가 가로막는 모든 것의 뼈와 살을 녹이고, 화염이라고 하기에는 믿을 수 없을 만큼 새하얀 섬광이 시야를 가렸다.

화악, 쿠구구구궁!

찰나의 명멸(明滅)과 함께, 비로소 눈앞의 광경을 마주한 적천강은 참았던 숨을 내뱉었다.

후욱.

마치 지친 화룡이 불을 뿜듯, 파르르 떨리는 입술 사이로 뿜어져 나오는 열기.

그러나 적천강에게는 전력을 쏟아부은 피로감보다도, 원하는 바를 이루었다는 기쁨이 더욱 크게 느껴졌다.

치익, 치지지직.

푸르르던 지면은 더 이상 그곳에 없다. 화산지대처럼 검게 그을린 땅과 희뿌연 수증기 사이로 펼쳐진 한 폭의 지옥도(地獄道)만이 있을 뿐.

푸스슥.

어디선가 불어온 뜨거운 열풍(熱風)에 간신히 형태를 유지하고 있던 사체들이 바스라진다.

괴물도, 인간도. 심지어는 운 나쁘게 적천강의 정면을 가로막았던 어느 흑귀조차도 예외는 아니었다.

단 한 번의 일격으로 수백에 달하는 적들은 그렇게 잿가루가 되어 흩어졌고, 이는 어느덧 반경 수십여 장을 뒤덮은 짙은 수증기 너머의 상황도 마찬가지였다.

아니, 적어도 적천강만큼은 그럴 것이라 생각했다.

바로 그때, 그의 오감을 통해 불현듯 전해진 이질감을 느끼기 전까지는.

스아아아.

지면과 공기를 타고 은밀하게 전해지는 무형(無形)의 기운을 감지함과 동시에, 적천강은 즉각 그 이질감의 정체를 깨달았다.

‘……이건.’

전력을 쏟아낸 직후 잠시 지쳐 있던 탓일까.

돌이켜 보면 처음부터 이상했다.

어찌 이토록 짙고 커다란 수증기가 만들어질 수 있었는지.

더불어 왜 저 수증기 너머의 적들은 어떤 반응도 보이지 않는지.

‘냉기(冷氣).’

뇌리를 관통하는 두 글자와 함께, 적천강은 어느새 조금 전의 그 끔찍했던 열기를 잊고 조금씩 얼어붙어 가는 지면을 짓밟았다.

파슥.

발끝을 따라 느껴지는 서늘한 기운.

그와 동시에 떠오르는, 누군가의 모습.

적천강은 침잠하게 가라앉은 눈빛으로 수증기를 응시하며 입술을 뗐다.

“어른을 뵈었으면 응당 인사를 올려야 마땅하거늘, 버르장머리라고는 눈곱만큼도 찾아볼 수 없는 년이로군.”

그 순간.

쩌저저적!

적천강의 앞을 가로막고 있던 수증기가 갈라졌다.

아니, 허공에서 산산이 부서졌다.

그리고 소름이 끼칠 정도로 서늘한 냉기 너머로, 광범위하게 펼쳐진 얼음의 장벽이 그 실체를 드러냈다.

앞서 적천강이 떠올렸던 한 사람의 모습도 함께.

“용케도 알아차렸네. 역시 당신다워.”

대술사(大術士)의 대답에, 적천강이 가래를 탁 뱉었다.

“그래, 네년일 줄 알았지.”

다름 아닌 그 자신이 전력을 다한 일격이었다.

무수한 적들 사이에 숨어 있던 술사들마저 단숨에 잿더미로 만들어 버리기에는 차고 넘치는.

설령 그와 비견되는 초절정 고수가 있다 하더라도, 그 피해를 완전히 막아 내는 건 불가능에 가까운 일이었다.

단 하나, 진태경이 마법(魔法)이라 부르는 저 기이한 사술만 아니라면.

“그 녀석의 말이 맞았군. 용케도 살아 있었어.”

“진작 죽어서 흙으로 돌아갔어야 할 늙은이도 이렇게 멀쩡히 돌아다니는데, 이까짓게 뭐 대수라고.”

대술사가 조소 띤 얼굴로 말을 이었다.

“그만큼 늙었으면 이제 뒷방에서 손주 재롱이나 보며 쉬셔야지, 왜 이곳까지 와서 불장난을 벌이실까.”

“하나뿐인 제자 놈이 재롱을 부린다는데, 그깟 불장난이야 백번 천번도 할 수 있지 않겠느냐?”

“너무 무리하지 말아요. 나이도 생각해야지.”

“걱정 말거라. 노부가 아무리 늙었다지만 네년을 잡아 죽이는 것 정도는 충분히 이룰 수 있을 테니.”

일순간, 면사에 가려진 대술사의 눈동자가 깊게 가라앉았다.

그 말에 담긴 의미가, 적천강의 확신이 느껴져서였다.

치이익.

멸염신권의 열기를 완전히 이겨 내지 못한 채, 지금 이 순간에도 조금씩 녹아내리는 빙벽이 그것을 뒷받침한다.

‘……화왕 적천강. 허명(虛名)은 아니라는 건가.’

내심 뇌까린 대술사가 신중하게 기운을 끌어모으던 그때였다.

침잠한 시선으로 그런 대술사와 그녀를 호위하는 세 명의 흑귀를 응시하던 적천강이, 문득 입술을 뗀 것은.

“하지만, 오늘만 날은 아니지.”

실상 초조한 것은 적천강 역시 마찬가지였다.

시간이 없다.

여섯. 아니 이제는 다섯으로 줄어든 흑귀들에게 둘러싸여 분투를 벌이고 있는 살성이 있고, 결코 죽어서는 안 되는 제자가 혈주와 싸우고 있다.

이제 약속된 시간은 끝났고, 조금은 아쉽더라도 충분한 성과를 거두었다.

“길을 터라. 모조리 불태워 버리기 전에.”

수십여 장의 거리를 사이에 둔 채, 불그스름하게 달아오른 적천강의 시선과 얼음처럼 차가운 대술사의 시선이 부딪힌다.

그리고 짧지만 긴 침묵 끝에, 대술사의 나직한 목소리가 울려 퍼졌다.

“그분을 위해서라도 반드시 당신을 죽일 거야. 당장 오늘이 아니더라도.”

“더 지껄일 개소리가 남았느냐?”

대답이 없는 대술사를 향해 피식 웃은 적천강이, 쾌속하게 신형을 돌렸다.
```

## Final English reading copy

```markdown
# Chapter 1093

KWA-A-A-ANG!

After the deafening boom, a tremor traveled through the ground. Jeok Cheongang turned to check what was happening behind him, then finally let out a sigh of relief.

*The old hag’s joined the fight.*

Even now, flashes of light streaked through the cloud of dust.

Once he confirmed that the Bow Saint was helping Jin Taekyung, a corner of his heart finally seemed to settle.

Now that the Bow Saint had joined them, his Disciple was safe.

At least for the brief time Jeok Cheongang needed to accomplish his goal.

*I was worried sick… Maybe there was nothing to worry about after all.*

In Jeok Cheongang’s judgment, Jin Taekyung still wasn’t a match for the Blood Lord. That was why he hadn’t been able to hide his unease, even after hearing the Sound Transmission that had reached his ear moments ago.

*“I’ll draw out the Blood Lord and buy us time. You two should target their main force.”*

*“What?”*

*“Don’t worry. You know my life motto, right?”*

Of course he knew.

No matter how long or short life was, survive at all costs and make it last.

But if everything in the world went according to one’s wishes, every martial artist in the land would be a Supreme Peak master, and the common people would live long, healthy lives.

So Jeok Cheongang had firmly opposed the idea.

No—he’d meant to oppose it.

Before Jeok Cheongang could even respond to that carefree answer, Jin Taekyung had already charged out without hesitation to face the Blood Lord.

*You idiot. You don’t even know enough to value your own life.*

And yet, contrary to what he was thinking, Jeok Cheongang had gradually found a smile on his lips.

It was such a clear smile that the Slaughter Saint, who was in the middle of stirring up a bloodstorm not far away, couldn’t hold back a comment.

“I know you adore your one and only Disciple, but are you really so eager to die that you—”

The Slaughter Saint stopped mid-sentence and sucked in a breath, his body twisting aside.

Whoosh-whoosh-whoosh!

Three streaks of sword light suddenly carved through the air, passing within inches of him.

At the same time, a flash of light glinted from the Slaughter Saint’s sleeve as he spun in midair.

KLANG! Thud!

Two sparks—and one sickening sound of flesh being pierced.

Three black-robed men, clad head to toe in pitch-black armor and charging at the Slaughter Saint like bolts of lightning, faltered and stepped back.

Or, more precisely, two of them did.

Thump.

One of the black-robed men fell like a dead tree.

A dagger the Slaughter Saint had just thrown was buried deep between the eyeholes of the helmet, which was pulled so low that not even the man’s face was visible.

“One down.”

The Slaughter Saint landed smoothly, as if nothing had happened. Jeok Cheongang, who had just swept away dozens of enemies with a flaming punch, shook his head.

“I don’t think so.”

“…What do you mean?”

“What do you think?”

Jeok Cheongang jerked his chin toward the fallen black-robed man.

“That.”

At that very moment—

Thrust.

The black-robed man, whom they’d thought dead, moved his own arm and pulled the dagger from his helmet.

Then he staggered to his feet and raised his sword.

As if he’d only been stung by a bee for a moment.

“…!”

The Slaughter Saint blinked silently. Jeok Cheongang shook his head.

It reminded him of the first time he’d laid eyes on that loathsome monster.

“Didn’t that brat Taekyung tell you? There are damned things that openly defy the natural order set by Heaven.”

Only then did the Slaughter Saint realize who the enemies before them were. He let out a low groan.

“…Black Ghosts.”

The Slaughter Saint had already heard about what happened in Gansu.

There were monsters that got back up no matter how many times you killed them, and every one of them had been fiends who once dominated the Demonic Cult.

“I heard they were like the legendary living jiangshi. So it was true.”

“Worse bastards than jiangshi. You can tell just by watching them move, can’t you?”

As he answered, Jeok Cheongang stood beside the Slaughter Saint and gathered his internal energy once more. The Black Ghosts, now six in number, were closing in as they took up positions all around them.

“How do you take them down?”

“As I understand it, there are only two ways. First, keep killing them until they die.”

Fwoosh.

White flames rolled over Jeok Cheongang’s hands.

In the space that seemed darker than it should have, the approaching Black Ghosts made strange noises, while the enemy forces packed tightly around them came into view. Deeper within that vast encirclement, so did the other figures hiding and controlling them.

“Second, cut off their heads and disable their arms and legs.”

And at that moment—

BOOM!

Jeok Cheongang threw out both palms with all his might.

As waves of rolling flame scattered in every direction, he kicked off the ground and shot forward.

“Defend!”

—GRAAAAAH!

The shouts of humans and monsters tangled together.

A path of fire opened through the enemies covering every direction. But the Black Ghosts stood their ground before Jeok Cheongang. A sharp gust of wind swept past their angled legs.

Whoosh. Slice!

The sword swinging toward Jeok Cheongang shot up into the air.

The Slaughter Saint, who had sliced through the arm of the first Black Ghost to charge, shouted with force.

“Go!”

It was a short cry, but its meaning was clear. Jeok Cheongang nodded slightly and pushed forward without slowing, drawing back a fist.

Rrrrrk.

At the heart of the space, now veiled in shimmering heat, the Flame-Extinguishing Divine Fist—mastered to its utmost—gathered white flame.

The heat made even the monstrous figure standing nearly thirty feet tall and the Dark Heaven faithful, who had formed a dense defensive line, open their eyes wide.

And in that world, where time seemed to stop for an instant—

“I am the—”

Jeok Cheongang’s fist shot forward, crushing the wind.

“Fire King!”

KWA-A-A-A-A!

Space warped. The ground sank.

Heat so enormous it was horrifying melted the flesh and bones of everything in its path. A flash so impossibly white it was hard to believe it was flame blocked his view.

Fwoosh—KRRRUMBLE!

With that momentary flash of light, Jeok Cheongang finally saw what lay before him and exhaled the breath he’d been holding.

Huu.

Heat poured between his trembling lips, like a weary fire dragon breathing flame.

But more than the exhaustion of pouring out all his strength, Jeok Cheongang felt the joy of having achieved what he wanted.

Sizzle. Szzzz.

The green ground was gone. All that remained was a hellscape spread between the scorched earth, black as a volcanic region, and a pale haze of steam.

Fsssh.

A hot wind blew from somewhere, and the bodies that had barely held their shape crumbled.

Monsters and humans alike. Even one unlucky Black Ghost who had stood directly in Jeok Cheongang’s path.

With a single strike, hundreds of enemies had turned to ash and scattered. The same had happened beyond the thick veil of steam, which now spread dozens of yards in every direction.

Or at least, that was what Jeok Cheongang thought.

Until he felt something strange suddenly reach his senses.

Ssshhh.

The moment he sensed an invisible force passing subtly through the ground and air, Jeok Cheongang immediately recognized what felt wrong.

*…This is.*

Maybe it was because he was briefly exhausted after using all his strength.

Looking back, things had seemed strange from the start.

How had such a thick, vast cloud of steam formed?

And why had the enemies beyond it shown no reaction at all?

*Cold qi.*

As the two words pierced his mind, Jeok Cheongang stamped down on the ground, which was slowly freezing over. He had already forgotten the horrifying heat from moments ago.

Crack.

A chill followed the tip of his foot.

At the same time, someone’s face came to mind.

Jeok Cheongang looked at the steam with a sunken gaze and parted his lips.

“Anyone with the slightest bit of manners would greet an elder properly. You’ve got less respect than an eyelash, you little brat.”

At that moment—

KRRRACK!

The steam blocking Jeok Cheongang’s way split apart.

No—it shattered in midair.

Beyond the chilling cold, an immense wall of ice revealed itself.

And with it, the person Jeok Cheongang had just thought of.

“You noticed. That’s just like you.”

At the Grand Mage’s reply, Jeok Cheongang spat.

“Yeah. I knew it was you.”

That had been his own full-strength strike.

It was more than enough to turn even the sorcerers hiding among the countless enemies into ash in an instant.

Even a Supreme Peak master comparable to him would have found it nearly impossible to completely block the damage.

Unless they had that bizarre sorcery Jin Taekyung called Magic.

“So that brat was right. You managed to stay alive.”

“An old man who should’ve long been dead and buried is still wandering around in perfect health. What’s one little thing like this?”

The Grand Mage continued, her face twisted in a sneer.

“If you’re that old, you should be resting in the back room, watching your grandchildren play. Why come all this way to play with fire?”

“If my one and only Disciple is putting on a show for me, I can play with fire a hundred times over. A thousand, even.”

“Don’t overdo it. You should think about your age.”

“Don’t worry. No matter how old I am, killing you is well within my reach.”

For an instant, the Grand Mage’s eyes sank deep behind her veil.

She could feel the certainty in Jeok Cheongang’s words.

Sizzle.

The ice wall, unable to fully withstand the heat of the Flame-Extinguishing Divine Fist, was still melting little by little. It only confirmed his claim.

*…Jeok Cheongang, the Fire King. So his reputation isn’t empty.*

Just as the Grand Mage thought this to herself and cautiously gathered her energy, Jeok Cheongang, who had been watching her and the three Black Ghosts guarding her with a sunken gaze, suddenly spoke.

“But today isn’t our only chance.”

In truth, Jeok Cheongang was just as pressed for time.

There wasn’t much time.

The Slaughter Saint was fighting desperately, surrounded by the six—or, now, five—Black Ghosts. And his Disciple, who absolutely could not be allowed to die, was fighting the Blood Lord.

The time they’d agreed on was up, and although it was a little short of what he’d wanted, they’d accomplished enough.

“Clear the way. Before I burn you all to ashes.”

Across the distance of dozens of yards, Jeok Cheongang’s reddish-hot gaze met the Grand Mage’s ice-cold one.

After a brief but long silence, the Grand Mage’s quiet voice rang out.

“For that person’s sake, I’ll kill you. Even if it isn’t today.”

“Got any more bullshit to say?”

Jeok Cheongang gave a quiet laugh at the Grand Mage’s silence, then swiftly turned around.
```
