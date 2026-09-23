<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0926.txt",
      "sha256": "a5966fd03af25750891690a56bbdc89c9f7677215a9cb8148da48b895e3f78aa",
      "bytes": 13653
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8427600ae38e2d1e6986adb7290249e64ba3ca31fbf72d2ad50acde1ca8c895e",
      "bytes": 1277
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0666305ef3a14502bbfe5c72134a55888b76af6f3fad7264eaf0463c809292b0",
      "bytes": 231946
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "2eff213ef26e841293146a0f31a0af50bf2881a2a2dbeac2a82b08e109d45778",
      "bytes": 837
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4d08368232c2a78e2d7bb7fbe30b827365bef3f8f453b4ebf7bd1730e61e25d3",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "73360eb383bd49729c2140e802eaa102a9bcbb2c5b990d004583357719b0f65b",
      "bytes": 838
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "7e71d83091b0375c09b2ed1211f0ec883a92356a33555952c86a40e1b93b63aa",
      "bytes": 837
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "d475d14977200d83388011c02d481111034a47426f785e0c4ebfe1c5e08a73ac",
      "bytes": 1244
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "189367226d7708f98088540ec98fb4cd76b8e2eeeb9e2016626acd0d2109a03c",
      "bytes": 1289
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "dc34def8300164fea5eccdf62219d374528d76abaf22323b00e4153778e0ab3e",
      "bytes": 752
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "80803e0a8179b795bcafff8ef990c0c34fea43ad71aa519b9864dfad266d44de",
      "bytes": 1042
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f4cb7597df6e2e3b6621149821277f1cbaab9bc9cf705d626aaacff9cc908122",
      "bytes": 266209
    }
  ],
  "estimated_tokens": 11766
}
-->

# Durable State Update — Chapter 926

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
1 and safe_through 926. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 926. Profile updates may replace only one
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
  "chapter": 926,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 926,
    "continuity_sources": [926],
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
    "Prince Shangshan Zhu Bao accepted the imperial command and is now Crown Prince; the Emperor is his older brother and kept the succession seat empty to protect him.",
    "The Emperor declared that Aehyang and her unborn child are unrelated to him and that the child is the late City Lord of Sichuan Province’s.",
    "The Emperor ordered memorials for the battle dead, civilians sacrificed in the realm’s struggles, and the Maoshan Sect, in the Crown Prince’s name.",
    "Jin Taekyung signed the pledge; Hong Jin helped him stop the Grand Academician from escaping."
  ],
  "continuity_sources": [
    925
  ],
  "open_questions": [
    "Where is Ma Sanbao, and what is his current status?",
    "What did Wei Zhong tell Jin Taekyung through Sound Transmission?",
    "What does the Martial God’s reference to a chosen one mean for Jin Taekyung, and what story has So Gyo kept to herself?",
    "Will the Salcheonmun pursue Mungyeong or discover that Jin Taekyung killed Gye Yabu?"
  ],
  "safe_through": 925,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기.",
    "Render 반정 as “restoration,” while preserving that it was disguised as a rebellion."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 적천강    | **Jeok Cheongang** |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 성군 | **sage king** | Desired form of rulership proclaimed for Prince Shangshan. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 대역 | **stand-in** | Jin's term for the substitute Go Jun used to fake Song Cheonwoo's departure. |
| 신수 | **divine beast** | A more exalted category than a spiritual creature. |
| 불신지옥 | **Unbeliever Hell** | Slogan threatening unbelievers with damnation. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진위경 | 홍진 | political_host_to_deputy_military_commissioner | Comrade Hong | formal-polite and playful | Jin Wikyung adopts Hong Jin's requested casual address, 홍 동지. |
| 홍진 | 진위경 | deputy_military_commissioner_to_lesser_family_head | Lesser Family Head Jin | formal and teasing | Hong Jin addresses Jin Wikyung as 진 소가주님 while flattering and joking with him. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 주표 | 백연 | prince addressing an imperial military officer | Commander Baek Yeon | formal and authoritative | Addresses Baek Yeon by name and office while insisting that he answer. |
| 백연 | 주표 | imperial officer addressing a prince | Your Highness | formal and deferential | Uses 전하 when apologizing to and answering Prince Shangshan. |
| 홍진 | 백연 | imperial aide confronting a senior military officer | you | angry and confrontational | Uses 당신 in an indignant outburst. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 황제 | 백연 | Emperor to the imperial court’s foremost military commander and trusted comrade | Baek Yeon | Direct and familiar; framed as a request rather than an order | The Emperor asks Baek Yeon to sound the war drum. |
| 상산왕 | 동천마군 | young imperial prince addressing the enemy who killed his parents and brothers and suffered at the hands of his grandfather | you | formal-polite | He apologizes for his grandfather’s actions using 당신 and deferential speech. |
| 황제 | 주표 | older brother addressing his younger brother and newly appointed Crown Prince | Bao’er | intimate and authoritative | The Emperor uses a warm childhood-style name before commanding Zhu Bao to accept the succession. |
| 주표 | 황제 | younger brother and Crown Prince addressing the Emperor | Your Majesty | formal and deferential | Zhu Bao formally accepts the Emperor’s command. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 925
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor, carrying out the late Emperor’s final command to plan for the future alongside the fourth prince; he treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 925
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 925
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 925
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care; the Fourth Prince spared him because of their old ties, and his longtime friend and former East Depot cohort Ma Sanbao stayed behind in the palace.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 923
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts Jin Taekyung, his publicly acknowledged second Disciple and intended heir; warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and is the target of an attack by the assassin Heaven's Slaughter.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 632
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung's eldest brother and future Family Head who protects and mentors him, commands Wipeng and the Jin Family's forces, has worked with Jeok Cheongang, maintains a political connection with Hongcheon, Prince Shangshan's hidden loyal retainer, and wants Taekyung to tell him his untold stories when the current crisis is over; Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 922
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, appearing first as a white-bearded elder and later as a young boy; Mae Jonghak received several teachings from him, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 925
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s thirteen-year-old younger brother, an exceptionally skilled young swordsman, and the newly appointed Crown Prince.
- **Personality:** Earnest and compassionate, he takes responsibility for others’ suffering and dreams of a peaceful age founded on justice, care for the people, wise counsel, and accountability, even when doing so demands personal sacrifice.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Zhu Bao is the Emperor’s younger brother and Crown Prince, and Hong Jin has been his steadfast caretaker since childhood. He admires Jin Taekyung and calls him a friend; his compassion for the Eastern Heaven Demon Lord reflects the different path made possible by those who supported him.

## Korean source

```text
＃926화



누구나 잘못된 선택을 할 때가 있다.

최소한 인생을 살면서 몇 번.

아니, 일상 속에 존재하는 사소한 것까지 포함하면 수천 번까지도.

하지만 잘못된 선택을 했다 한들 인생이 끝나는 건 아니다.

단지 자신의 선택을 후회하고 반성하며 이를 발판으로 다음에는 더 올바른 길로 향하면 된다.

물론, 바로 그 ‘다음’이라는 것이 주어졌을 때의 이야기지만.

“나, 나는 아무런 죄가 없소! 오해요!”

“폐하! 폐하!”

“네 이놈들! 감히 누구에게 손을 대는 것이냐!”

두려움. 간절함. 분노.

제각각의 감정에 휩쓸려 목소리를 높이는 수십여 명의 사람들.

한바탕 죽음이 할퀴고 간 자리에서도 윤기를 잃지 않은 비단옷과 피둥피둥한 살집은 그들의 신분이 얼마나 높은지를 말해 주고 있었지만, 지금껏 누려 왔던 부귀영화도 지금 이 시간 부로 끝장이었다.

대역죄인(大逆罪人)의 말로는 그런 것이니까.

“모조리 추포하라!”

“충(忠)!”

쉬쉬쉭!

백연의 엄명이 떨어지기 무섭게 사방을 에워싸고 있던 금의위들이 포승줄이며 검집을 휘두른다.

이미 체념한 어느 문관은 조용히 포박당했고, 휘황찬란한 갑옷을 걸친 늙은 장군은 제법 뛰어난 무공을 펼치며 저항했다.

그리고 뚝배기가 깨졌다.

빡!

“네놈들이 감…… 커헉!”

“벌써부터 진 빼지 말고 조용히 갑시다. 소리는 앞으로 실컷 지르시게 해 드릴 테니.”

“나, 나를 어쩔 셈이냐!”

“이미 아시잖소. 도독첨사(都督僉事) 영감.”

“……!”

금의위의 입가에 걸린 서늘한 미소에, 늙은 장군은 넋 나간 얼굴로 주저앉았다.

지금 자신의 정수리를 뜨뜻하게 적시며 흘러내리는 핏물이, 앞으로 흘려야 할 양에 비하면 조족지혈이나 다름없다는 것을 깨달은 것이다.

그리고 이 난장판을 종횡무진 가로지르는 한 사람이 있었다.

“오랜만이네요. 마지막에 봤을 때는 저한테 불알도 없는 고자 새끼라고 하셨던 것 같은데.”

한 명.

“저 안 잊으셨죠? 아, 처음 본다고? 개소리 집어치워. 난 다 기억하고 있거든.”

두 명.

“어머, 이게 누구야. 너무 살이 쪄서 못 알아볼 뻔했네. 괜찮아요. 이번에 내가 홀쭉하게 만들어 드릴게.”

“…….”

멘트 치는 것마다 살벌한 거 봐라.

홍진이 마치 십 년 만에 동창회에 참석한 사람처럼 반갑게 말을 건넬 때마다, 황금빛 갑옷을 걸친 다이어트 보조제들이 걸어와 사람들을 끄집어냈다.

한동안 비어 있던 금의위 형옥을 한가득 채워 줄 뉴비들의 야한 냄새에 잔뜩 상기된 얼굴로.

“자, 잠깐! 홍 첩형(貼刑)!”

“나 첩형 아니에요. 산서성 도지휘동지로 임명된 지가 언젠데. 괜히 시끄럽게 사람 부르지 말고 먼저 가 있어요. 아, 불알 잘 닦아 놓고.”

과거 홍진에게 불알 없는 고자라며 사실 적시 명예 훼손죄를 가한 누군가가 질질 끌려 나가자, 초면임을 어필했던 두 번째 인물이 마른침을 꿀꺽 삼키며 입을 열었다.

“저기, 홍 동지. 뭔가 오해가 있으신 모양인데…….”

“누가 당신 동지야?”

“예?”

“당신 나 알아? 그리고 오해는 무슨. 당장 이 역적 새끼 끌고 가서 형옥에 처박아요.”

눈앞에서 일사천리로 진행되는 상황을 지켜보던 나는 내심 중얼거렸다.

‘피바람이 불겠군.’

몇이나 죽을지 짐작도 되지 않는다. 수백? 수천?

아니면 지난번처럼 수만 명?

모르긴 몰라도 오늘 이 자리에 없는 배반자들과 그들의 가족까지 더한다면, 그야말로 대규모 숙청(肅淸)이 벌어질 터였다.

“저들을 동정하는 것이냐?”

불쑥 들려온 황제의 물음에, 나는 작게 고개를 내저었다.

“저 새끼들이야 죽을죄를 지었으니 당연한 족쳐야죠. 단지 마음에 걸리는 건…….”

“역모와는 아무런 관련도 없는 이들이 희생당할까 봐 신경 쓰이는 거겠지.”

“…….”

“어쩔 수 없다. 국법은 지엄한 것이니. 그것이 역모에 관련된 것이라면 더더욱.”

“압니다. 충분히 이해하고요.”

복수는 복수를 낳는 법,

만약 이 숙청에서 원한을 품은 자가 살아남아 후일을 도모한다면, 또 다른 재앙의 씨앗이 될 수도 있었다.

동천마군이 그러했듯이.

“하지만, 간혹 예외도 있을 수 있지.”

뜻밖의 선언에 나도 모르게 눈이 커졌다.

“그 말씀은…….”

“모든 인과 관계를 명명백백히 하여 죄 없는 이들만큼은 구명해달라. 조금 전 표아(標兒)가 짐에게 했던 말이다.”

황제가 흐릿하게 웃으며 덧붙였다.

“황태제(皇太弟)이자 아우로서 처음으로 건넨 부탁이기도 하고.”

“……!”

“저 아이는 태평성대를 이룩할 성군이 될 것이다. 누구보다 백성들을 아끼고, 백성들에게 사랑받는 성군이.”

웃음이 이렇게 많은 사람이었나.

언제나 차갑고 음울했던 황제의 얼굴은 훨씬 밝아져 있었다.

눈이 마주치자 아직 어색한지 고개를 꾸벅 숙여 보이는 상산왕.

아니, 이제는 황태제가 된 주표를 바라보는 시선에는 숨길 수 없는 온기가 뚝뚝 묻어 나왔다.

‘아무리 황제라 해도, 결국 어쩔 수 없는 형이라는 건가.’

내심 실소를 흘린 내가 입을 열었다.

“맞습니다. 분명 성군이 되실 겁니다.”

“무예 역시 출중하니, 언젠가는 저 장성(長城)을 넘어 드넓은 초원을, 북해의 고토와 사막 또한 정복할 것이다.”

“예?”

“왜 그러지?”

“음. 아닙니다. 가능하죠.”

무예랑 그거랑 뭔 상관이냐 묻고 싶었지만, 일단 참았다.

그런데 왜 슬슬 진위경이 생각날까.

“그렇지. 가능하고말고.”

“암요.”

“그뿐이 아니다. 황금으로 도시를 세우고, 천 년이 지나도 사라지지 않을 대제국을 건설하겠지.”

“……천 년은 좀.”

“설마 지금 무리라고 생각하는 건가?”

아니, 아무리 생각해도 그건 좀 무리 아니냐.

하지만 그 순간 가늘어진 황제의 눈매에, 목 끝까지 차오른 말을 삼킨 나는 눈부신 순발력을 발휘했다.

“좀, 짧게 잡으셨다고요. 전 만 년 생각하고 있었는데.”

“만 년은 무리지.”

“…….”

“무림인이라 그런지 확실히 허무맹랑한 구석이 있군. 좀 현실적인 사고방식을 기르거라.”

이 시벌놈 보게.

애써 맞장구 쳐줬더니 정색을 해 버리는 황제의 모습에 내가 말문이 턱 막혀 버린 그때, 누군가의 손길이 은밀하게 내 옆구리를 파고들었다.

쿡.

굳이 고개를 돌려 확인하지 않아도 상대가 누구인지 안다.

나는 황제를 향한 분노를 누그러트리며 입술을 달싹였다.

― 괜한 걱정 마십시오. 제가 아무리 미친놈이어도 그렇지, 설마 황제를 두들겨 패겠습니까?

적천강 역시 전음(傳音)으로 대답했다.

― 네 녀석이 충분히 그러고도 남을 만한 놈인 건 맞다만, 노부가 말하려던 건 그게 아니다.

― 그게 아니라면, 설마?

눈을 부릅뜬 채 고개를 돌린 나를 향해, 적천강이 무겁게 고개를 끄덕였다.

― 설마 노야께서 직접 때리시게요?

― …….

― 세상에, 또 노망나셨어요? 안 됩니다. 황제한테 손대면 싹 다 끝장이에요. 우리한테 열 받아서 암천이랑 눈 맞으면 대국이 아니라 암천국이 돼 버린다니까? 그런데 이제 지옥을 곁들인.

영등포역에서 예수천국 불신지옥을 부르짖는 포교사처럼 필사적으로 설득을 이어 가고 있던 그때, 적천강이 짜게 식은 눈빛으로 내 어깨 너머를 향해 턱짓했다.

― 그 개눈깔 뽑아 버리기 전에, 저 뒤에서 누가 기다리고 있는지나 보거라.

그리고 고개를 돌린 나는, 저 멀리서 담담하게 가라앉아 있는 눈동자로 이곳을 응시하고 있는 한 사람의 모습을 볼 수 있었다.

‘궁성(弓星).’

허공에서 시선이 맞닿자, 언제부터인가 전신을 감싸고 있던 안도와 기쁨이 순식간에 씻겨 나가는 듯했다.

지금 이 순간, 폐부로 스며드는 알 수 없는 한기(寒氣)와 함께.

― 그래, 너였구나.

아직 해결하지 못한 의문이, 그 목소리가 새벽에 불어온 바람처럼 아스라이 귓가를 맴돌았다.

― 무신(武神)께서 말씀하셨던, 선택받은 자가.

그건 무슨 뜻이었을까. 어떤 진실이 숨어 있던 것일까.

나도 모르게 파르르 떨려오는 눈빛.

그런 나를 향해 살짝 고개를 끄덕여 보인 궁성이, 조용히 신형을 돌려 걷기 시작했다.

사람들의 이목이 없는 어딘가로.

지금껏 숨겨온 비밀을 밝힐 수 있는, 은밀한 장소로.



* * *



나는 궁성을 따라 말없이 걸음을 옮겼다.

대연회장에서 벌어진 전투가 전부가 아니라는 것을 증명하듯이, 넓고 깨끗하던 황궁 곳곳에는 미처 치우지 못한 시체와 핏물로 가득했다.

그러나 빠르지도, 느리지도 않은 발걸음으로 황궁을 가로지르는 나와 궁성을 막아서는 이는 누구도 없었다.

아니, 오히려 멈칫하며 이내 목례와 함께 길을 텄다.

그들도 알아본 것이다.

우리가 누구인지.

황제와 동천마군 중 누구의 편에 서서 싸웠는지.

하지만 그들과 달리 나는 여전히 알지 못했다.

뜻 모를 궁성의 말에 담겨 있던 의미도. 그리고 거의 모든 것이 베일에 싸여 있는 한 존재에 대해서도.

‘무신.’

어느 날 홀연히 나타나 홀연히 사라졌던, 정마대전이 낳은 불세출의 영웅.

아니, 천하 무림을 굽어보는 하늘 그 자체가 된 인물.

세인들은 말하곤 했다.

무신과도 같은 이는 지금껏 없었으며, 앞으로도 없을 것이라고.

삼성(三星)과 십왕(十王)이라 불리는 강자들이 있으나, 무신은 그 누구도 닿을 수 없는 영역에 있다고.

그렇기에 하늘이며, 신이라 불리는 것이라고.

하지만…… 무신은 이제 없다.

무림의 상징이자 중심이었던 그는 무림맹을 해산한 직후, 허깨비처럼 사라졌다.

마치 존재하지 않았던 사람처럼.

처음부터 이렇게 되기를 기다려 왔던 것처럼.

그렇게 무신이 한순간에 자취를 감추고 세월이 흐르자, 온갖 소문들이 잡초처럼 무성하게 자라났다.

누군가는 그가 천마(天魔)와의 마지막 생사결에서 입은 내상을 회복하지 못해 죽었다고 했고, 혹자는 무신이 어느 심산유곡에서 여생을 보내고 있다고 했다.

그뿐인가.

깨달음을 얻은 끝에 마침내 신선이 되었다는 설.

무신이란 본래 중원을 수호하는 신수(神獸)와 같은 존재라, 더는 인간의 모습으로 나타나지 않는다는 허무맹랑한 소문들도 심심찮게 나돌았다.

모든 것이 의문투성이에 둘러싸인 무신은 언제나 흥미로운 이야깃거리였다.

그와 관련된 영웅담은 신화처럼, 설화처럼 느껴지기에 충분했다.

가장 가까이에서 무신이라는 존재를 보고 접했던 이들에게도, 그리고 나에게도.

그런데…….

‘바로 그 무신이 이렇게 갑작스럽게 등장하다니.’

무신의 새끼손가락조차 보지 못한 나지만, 그 별호가 언급된 것만으로도 전신의 털이 곤두서는 기분이었다.

마침내 목적지에 이르러 발걸음을 멈춘 지금 이 순간에는 더더욱.

사박.

어느덧 깊은 밤을 지나 새벽으로 나아가는 시각.

축축하게 젖은 풀잎이 스치는 소리마저 서늘하게 울려 퍼진 그때, 천천히 주위를 둘러보던 궁성이 뒤도 돌아보지 않은 채 불쑥 입을 열었다.

“이곳, 와 본 적이 있지?”

겉모습만 보자면 이제 갓 이립 어림에 접어든 젊은 여인이지만, 궁성은 아득한 세월을 살아온 노강호.

나는 최소한의 예의를 차려 대답했다.

“예.”

“죽일 듯이 달려들던 네 모습이 생각나는구나. 제법 인상 깊었어.”

궁성이 손을 뻗어 아직 피지 않은 꽃봉오리를 톡, 하고 건드렸다.

헤아릴 수도 없을 만큼 수많은 기화요초(琪花瑤草)로 가득한 이곳은, 며칠 전 그녀와 내가 마주쳤던 바로 그 버려진 공간이었다.

“속이 답답할 때마다 이곳에 와서 거닐곤 했지. 금지(禁地)처럼 인식되는 바람에 개미 새끼 한 마리 없었으니까.”

“그럼 그날도…….”

“맞아. 한 가지 고민이 있었거든. 아무리 생각해도 쉽게 결론이 나지 않아서 이곳을 걸으면서 생각해 볼 참이었지.”

궁성이 돌아섰다. 그녀의 반달처럼 휘어진 눈매가, 그 안에 숨어 있는 눈동자가 깊게 가라앉아 있었다.

“무신께서 말씀하신 선택받은 자인 네가, 죽음조차 피할 수 있는 괴력난신(怪力亂神)의 힘을 지녀야 했을 네가…… 어째서 회복 불능의 상태인지.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 926

Everyone makes the wrong choice sometimes.

At least a few times in life.

No—if you include all the little things in everyday life, maybe thousands of times.

But making the wrong choice doesn’t mean your life is over.

You regret it, reflect on it, and use it as a stepping stone to take a better path next time.

Of course, that only applies if you’re given a “next time.”

“I—I’ve done nothing wrong! This is a misunderstanding!”

“Your Majesty! Your Majesty!”

“You scoundrels! How dare you lay hands on me!”

Fear. Desperation. Anger.

Dozens of people raised their voices, each swept up in their own emotions.

Their silk robes had lost none of their sheen, and their plump bodies spoke to just how high their station had been—even in a place death had just torn through. But all the wealth and glory they had enjoyed until now were over, effective this very moment.

That was the fate of those guilty of high treason.

“Arrest every last one of them!”

“Loyalty!”

*Shing!*

At Baek Yeon’s stern command, the Embroidered Uniform Guards surrounding the area swung out their ropes and scabbards.

One civil official had already given up and was quietly bound. An old general clad in dazzling armor put up a fight, displaying a fair amount of skill in martial arts.

And then his head got cracked open.

*Whack!*

“You bastards, how dare you—Guh!”

“Let’s not wear ourselves out this early. Come quietly. You’ll have plenty of chances to shout later.”

“W-what are you going to do with me?”

“You already know, don’t you, old Assistant Military Commissioner?”

“……!”

At the Embroidered Uniform Guard’s cold smile, the old general sank to the ground, his face blank.

He’d realized that the blood now running warm from the crown of his head was a mere drop compared to what he’d be forced to shed from here on.

And one man was weaving his way through the chaos.

“It’s been a while. Last time we met, I think you called me a eunuch bastard with no balls.”

One man.

“You haven’t forgotten me, have you? Oh, you’ve never seen me before? Cut the crap. I remember everything.”

Two men.

“Oh, look who it is. You’ve gotten so fat I almost didn’t recognize you. Don’t worry. I’ll slim you down this time.”

“……”

Talk about making every line sound murderous.

Whenever Hong Jin greeted someone with the enthusiasm of a man attending his first school reunion in ten years, gold-armored diet supplements came marching over and dragged the person away.

Their faces were flushed with excitement at the prospect of filling the Embroidered Uniform Guard’s jails, which had been empty for a while, with a fresh batch of prisoners.

“W-wait! Torturer Hong!”

“I’m not a torturer anymore. It’s been ages since I was appointed Deputy Military Commissioner of Shanxi Province. Don’t make a scene calling me over. Go on ahead. Oh, and make sure you wash your balls.”

As one of the people who’d once slandered Hong Jin by calling him a eunuch with no balls was dragged away, the second man—the one who’d claimed they’d never met—swallowed hard before speaking.

“Um, Comrade Hong. I think there’s been some misunderstanding…”

“Who’s your comrade?”

“Pardon?”

“Do you know me? And what do you mean, a misunderstanding? Drag this traitorous bastard to the jail and throw him in.”

Watching everything unfold at lightning speed right before my eyes, I murmured to myself.

*There’s going to be a bloodbath.*

I couldn’t even guess how many would die. Hundreds? Thousands?

Or tens of thousands, like last time?

Even so, if you counted the traitors who weren’t here today, along with their families, this would be a massive purge.

“Do you pity them?”

At the Emperor’s sudden question, I gave a small shake of my head.

“They deserve whatever they get. They committed crimes worthy of death. It’s just that what bothers me is…”

“You’re worried that people with nothing to do with the treason will be sacrificed.”

“……”

“It cannot be helped. The law of the land is solemn. All the more so when it concerns treason.”

“I know. I understand.”

Revenge begets revenge.

If someone with a grudge survived this purge and plotted for the future, they could become the seed of another disaster.

Just as the Eastern Heaven Demon Lord had.

“But there can be exceptions now and then.”

My eyes widened at that unexpected declaration.

“You mean…”

“Make the truth of every connection clear and spare at least those who are innocent. That was what Bao’er asked of Me just now.”

The Emperor added with a faint smile, “It was also the first request he made of Me as Crown Prince and as My younger brother.”

“……!”

“That boy will become a sage king and usher in an age of peace. A king who cares for his people more than anyone and is loved by them in return.”

Had this man always smiled so much?

The Emperor, whose face had always been cold and gloomy, looked much brighter now.

His eyes rested on Prince Shangshan—or rather, Zhu Bao, now Crown Prince—as the boy met his gaze and awkwardly bowed his head. The warmth in the Emperor’s eyes was impossible to hide.

*Even the Emperor is still just an older brother, in the end.*

I let out a quiet snort and said, “That’s right. He’ll definitely be a sage king.”

“He is also a peerless martial artist. One day he’ll cross that Great Wall and conquer the vast grasslands, the lost lands of the Northern Sea, and even the deserts.”

“Huh?”

“Why?”

“Um. Nothing. He could.”

I wanted to ask what martial arts had to do with any of that, but I held back.

Why was I starting to think of Jin Wikyung?

“That’s right. He absolutely could.”

“Of course.”

“Not only that. He’ll build cities of gold and establish a great empire that will endure for a thousand years.”

“……A thousand years is a bit much.”

“Do you think that’s impossible right now?”

No, even if I thought about it as hard as I could, that seemed a bit much.

But the Emperor’s eyes narrowed, and I swallowed the words that had risen to the tip of my tongue, showing off my dazzling reflexes.

“I just thought you were aiming a little low. I was thinking ten thousand years.”

“Ten thousand years is impossible.”

“……”

“Perhaps it’s because you’re a Murim practitioner, but you do have a rather fanciful streak. You should try to develop a more realistic outlook.”

This son of a—

I was so stunned that I couldn’t speak. I’d gone along with him, and now he was being dead serious. Just then, someone’s hand slipped discreetly into my side.

*Poke.*

I didn’t need to turn around to know who it was.

Suppressing my anger toward the Emperor, I moved my lips.

—Don’t worry. Even if I am crazy, do you really think I’d beat up the Emperor?

Jeok Cheongang replied through Sound Transmission.

—It’s true you’re the kind of fool who’d do exactly that, but that’s not what I meant.

—If that’s not it, then… don’t tell me—

I turned, eyes wide, and Jeok Cheongang nodded gravely.

—You’re going to hit him yourself, Old Master?

—……

—Good heavens, have you gone senile again? You can’t. If you lay a hand on the Emperor, it’s over for all of us. If he gets pissed off at us and takes a liking to Dark Heaven, we won’t have a Great Nation anymore. We’ll have the Dark Heaven Nation instead. With Hell thrown in.

I was still desperately trying to talk him out of it, like a missionary at Yeongdeungpo Station shouting that believers go to Heaven and unbelievers go to Hell, when Jeok Cheongang gave me a withering look and jerked his chin over my shoulder.

—Before I pluck those dog eyes out, look and see who’s waiting behind you.

I turned and saw a person standing in the distance, watching us with eyes that were calm and still.

*The Bow Saint.*

The moment our gazes met, the relief and joy that had wrapped around me seemed to wash away in an instant.

Along with an inexplicable chill seeping into my lungs.

—So it was you.

The question remained unresolved, and that voice lingered faintly in my ears like a breeze at dawn.

—The chosen one the Martial God spoke of.

What had that meant? What truth was hidden behind it?

My eyes trembled before I could stop them.

The Bow Saint gave me a slight nod, then quietly turned and began walking.

Toward somewhere beyond the eyes of the crowd.

Toward a secluded place where she could reveal the secret she’d kept hidden all this time.

* * *

I followed the Bow Saint without a word.

As if to prove that the battle in the grand banquet hall wasn’t the whole story, the clean, spacious grounds of the imperial palace were filled with blood and bodies that no one had yet managed to clear away.

Still, no one stopped me and the Bow Saint as we crossed the palace at an unhurried pace.

If anything, people hesitated, then bowed and stepped aside.

They recognized us.

They knew who we were.

And which side we had fought on—the Emperor’s or the Eastern Heaven Demon Lord’s.

But unlike them, I still didn’t know.

I didn’t know what the Bow Saint’s cryptic words meant. And I knew almost nothing about the one whose existence was shrouded in mystery.

*The Martial God.*

The peerless hero born of the Great Faction War, who had appeared one day and vanished just as suddenly.

No—he was the very sky that looked down upon all of Murim.

People used to say there had never been anyone like the Martial God, and there never would be again.

There were powerful figures known as the Three Saints and the Ten Kings, but the Martial God stood in a realm no one could reach.

That was why he was called the sky. That was why he was called a god.

But…the Martial God was gone now.

The symbol and center of Murim had vanished like a phantom shortly after disbanding the Murim Alliance.

As though he had never existed.

As though he’d been waiting for this to happen from the beginning.

When the Martial God disappeared in an instant and the years passed, all kinds of rumors sprang up like weeds.

Some said he died because the Internal Injury he sustained in his final life-and-death duel with the Heavenly Demon never healed. Others said he was spending the rest of his life in some remote mountain valley.

And that wasn’t all.

There were rumors that, after gaining enlightenment, he had finally become an immortal.

There were also plenty of outlandish rumors that the Martial God was, by nature, something like a divine beast protecting the Central Plains, and that he no longer appeared in human form.

The Martial God, surrounded by questions on all sides, had always made for fascinating stories.

The heroic tales about him were enough to feel like myths and legends.

Even to those who had seen and encountered the Martial God up close—and to me.

And yet…

*For the Martial God himself to come up so suddenly.*

I hadn’t even seen the Martial God’s little finger, but just hearing his title made every hair on my body stand on end.

Now that we’d reached our destination and stopped, I felt it more than ever.

*Rustle.*

Night had already given way to the early dawn.

The sound of wet grass brushing against us rang out with a chill. The Bow Saint slowly looked around, then spoke without turning.

“You’ve been here before, haven’t you?”

She looked like a young woman who had only just entered her early thirties, but the Bow Saint was an old master who had lived through an age beyond measure.

I answered with the respect she was due.

“Yes.”

“I remember you charging at me like you meant to kill me. It left quite an impression.”

The Bow Saint reached out and gave an unopened flower bud a light tap.

This place was filled with countless rare and beautiful plants. It was the same abandoned area where she and I had met a few days ago.

“Whenever I felt restless, I used to come here and walk. People treated it like a forbidden ground, so there wasn’t even an ant around.”

“Then that day, too…”

“That’s right. I had something on my mind. I couldn’t come to a conclusion, no matter how I looked at it, so I thought I’d walk around here and think it over.”

The Bow Saint turned around. Her crescent-shaped eyes, and the gaze hidden within them, were deeply still.

“You were the chosen one the Martial God spoke of, someone who was supposed to possess the supernatural powers to escape even death…so why are you in an irrecoverable state?”

“……!”
```
