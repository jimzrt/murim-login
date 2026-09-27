<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1100.txt",
      "sha256": "80a4a066c9eaa4c968c113a246fbe4c3c385592e7ac2453642ccc8f75c5046c2",
      "bytes": 11460
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "71bc2c9d60cb001c228ad329a59efc63d0e1127182730eb53515b2865fd91a23",
      "bytes": 2491
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e58ae46a1bac772cc7720c130c81de8fb5906bb3ba1496eb8e7943cb290731fa",
      "bytes": 244132
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "629b3b2793501a8be548f1e1a949d928d26664336f5c762fcd847124dde7f1cd",
      "bytes": 907
    },
    {
      "path": "characters/Dalai Lama.md",
      "sha256": "1d063a9eaa7f50a108c3988e79c73e0c7318e7d7432a4ed24940d49708bc19d3",
      "bytes": 779
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b3c327ff3c903dcf5433da6c58ff00d454eaefb6477db9844a6cd6411527930e",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3ed0962346ad52fc79f8b6ed9f606fb00646464dfbe2d2c1841f243eb7c3f2b6",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "dade3db6f055f84c11c053ad8cfdec26e7a20f65bbe2169cc42ef1c61fbbf8fe",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "bd7b689a708e49bc8151965c6a76e59b8a98de77f0033e0d5a3c2b72a93b7e3f",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f15b6bb616e0bd10e582c2c20db1381f3647dfe2374b0b254aed2c21ef827565",
      "bytes": 287948
    }
  ],
  "estimated_tokens": 10196
}
-->

# Durable State Update — Chapter 1100

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
1 and safe_through 1100. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1100. Profile updates may replace only one
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
  "chapter": 1100,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1100,
    "continuity_sources": [1100],
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
    "Dark Heaven’s army surrounds Xining under the Blood Lord; the Potala Palace has joined its forces with elephants and the Twelve Secret Monks.",
    "Cheongheoja says he failed to teach one of his Disciples properly; Taekyung realizes a Dark Heaven agent is hidden deep within Xining’s defenders.",
    "Cheongheoja privately asks Taekyung a favor; its nature is not revealed before a day passes.",
    "A vast enemy force approaches Xining through torrential rain, and the battle begins with hundreds of ice spikes.",
    "The Blood Lord offered to spare everyone else if Taekyung leaves Xining alone within a day, severs the sinews and meridians in all four limbs, and surrenders; Jeok Cheongang believes the Blood Lord will break his promise.",
    "Taekyung believes the Lord of Heaven wants him more than anything, possibly more than the world; the reason remains unknown.",
    "The Potala Palace and Dark Heaven are allies, but the Palace has a deep, longstanding hatred of the Fire Gate Clan; the Dalai Lama accepts the alliance’s unequal terms.",
    "Namho fears Sichuan may be exposed to enemies from Tibet after the Nanman Beast Palace’s departure.",
    "The Fire Gate Clan’s leaders are unlikely to abandon Xining while their allies and civilians remain there.",
    "Mu Song disobeyed Pa Ryun’s order to kill captured imperial troops; Pa Ryun says the Eldest Senior Brother and Elders obeyed him without deviation.",
    "Mu Song claims the Eldest Senior Brother and Elders serve someone other than Pa Ryun, but loses consciousness before explaining.",
    "The Yangtze River Channel League fleet was preparing to meet thousands of new allies gathered near the river; their identity is unknown."
  ],
  "continuity_sources": [
    1098,
    1099
  ],
  "open_questions": [
    "Which of Cheongheoja’s Disciples is the hidden Dark Heaven agent, and what did Cheongheoja ask Taekyung to do?",
    "What will decide the battle for Xining, and will its defenders survive?",
    "Why does the Lord of Heaven want Taekyung, and what does he intend to do with him?",
    "Whom do the Eldest Senior Brother and Elders serve, and what was Mu Song about to reveal?",
    "Who were the new allies gathering near the river?"
  ],
  "safe_through": 1099,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
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
| 절정고수                | **Peak master** / **Peak martial artist** |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 일격     | **One Strike**                         |
| 마법사     | **mage**              |
| 노부      | **this old man / I**                                            |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 달뢰라마 | **Dalai Lama** | Traditional title of the Potala Palace’s leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
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
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 마법사 | rescuer assisting the operation | mage; otherwise you | polite emergency imperative | Taekyung orders the exhausted mage to request rescue under his name. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 혈주 | 달뢰라마 | allied leader to allied leader | Palace Lord | familiar, then threatening and insulting | Calls him 궁주, then warns him not to speak down to him. |
| 달뢰라마 | 혈주 | allied leader to allied leader | donor; you | formal, then angry and informal | Initially uses the Buddhist honorific 시주 before challenging the Blood Lord. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1098
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Cunning and controlling, he avoids costly risks while manipulating allies; beneath his devotion to the Lord of Heaven, he resents being treated as disposable and resents Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven but resents the Lord’s apparent special interest in Jin Taekyung, whom he resolves to kill even if it means defying the Lord’s command; he considers Taekyung and Cheongpung formidable adversaries.

### Dalai Lama.md

# Dalai Lama (달뢰라마)

- **Safe through:** Chapter 1097
- **Aliases:** Palace Lord
- **Role:** The Dalai Lama is the Potala Palace’s leader and ruler of Xizang, commanding its Twelve Secret Monks.
- **Personality:** Fiercely hostile to the Fire Gate Clan and committed to the Potala Palace’s interests; he trusts the Lord of Heaven but distrusts the Blood Lord.
- **Voice:** Uses Buddhist self-reference and addresses others as “donor”; his Han speech is described as halting.
- **Relationships:** He leads the Potala Palace in an unequal alliance with Dark Heaven, accepting its terms to pursue their shared goal of destroying the Fire Gate Clan and avenge the Palace’s longstanding grievance.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1099
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1099
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1099
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1099
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
1100화




누가 그랬다.

인간이 가장 큰 경이와 공포를 느끼는 순간은, 미지(未知)의 상황과 맞닥트렸을 때라고.

지금껏 단 한 번도 겪어 보지 못한 무언가와 직접 대면하고 그 실체를 마주했을 때, 모든 감정은 극을 향해 치닫는다고.

그리고 진태경은 그 말에 전적으로 동의했다.

인간은 학습의 동물이라는, 어느 철학자가 남긴 어록 역시도.

쐐애애액!

거대한 기운의 출렁임과 함께, 비의 장막을 관통하며 쏘아지는 수백여 개의 얼음송곳.

하지만 상당한 위력을 지닌 대범위 마법이 발현되었음에도, 진태경은 조금도 동요하지 않았다.

이미 예상했던 바였으니까.

“방(防)!”

진태경의 입술 사이로 심후한 공력이 담긴 외침이 터져 나온 그 순간.

쉬쉭! 촤라라락!

드높은 성벽 위를 빈틈없이 메운 아군들의 머리 위로 뒤덮이는 방패의 물결과 함께, 곳곳에서 솟구친 휘황한 빛줄기가 수백 개의 얼음송곳을 향해 쏘아졌다.

콰과광!

굉음과 함께 번뜩이는 섬광.

그와 함께 절정고수들이 흩뿌린 검기로 부서진 얼음송곳의 잔해가 빠른 속도로 성벽 위를 향해 튕겨 나갔지만, 단지 그뿐이었다.

터터텅!

겉면에 강철을 덧씌운 커다란 직각 방패는 제 역할을 톡톡히 해 냈다.

본래의 위력을 온전히 간직하고 있었다면 모를까, 앞서 한 차례 상쇄된 얼음송곳의 잔해는 단단하게 구축된 방패 벽을 뚫기에 역부족이었으니까.

“전원 무사합니다!”

곳곳에서 상기된 목소리로 전해져 오는 보고.

그러나 이 모든 것을 사전에 예측하고 준비한 장본인인 진태경은 조금도 방심하지 않았다.

전투의 첫 단추를 잘 끼운 것은 사실이다.

이 세상에서는 귀신의 조화나 다름없는 마법을 훌륭하게 방어함으로써 아군의 사기도 올라갔으니 그 또한 큰 수확이다.

하지만 이는 어디까지나 시작에 불과하다는 것을, 진태경은 누구보다 잘 알고 있었다.

그리고 성벽 너머에서 이 광경을 지켜보고 있던 대술사와 혈주 역시도.

“발시(發矢)!”

힘찬 외침과 함께 성벽 위에서 명령을 전달하는 신호수들의 깃발이 춤추고, 방패벽 사이사이에 숨어 번뜩이던 화살촉이 마침내 팽팽하게 당겨진 시위를 떠났다.

솨아아악!

수천에 달하는 화살 비가 허공의 일부를 까맣게 물들이며 쏟아져 내린다.

그 아래에서 빠르게 진군해 오는 적들의, 잔인무도한 침략자들의 숨통을 끊기 위해서.

하지만 그들의 간절한 염원은, 저 멀리 면사 너머에 감춰진 붉은 입술이 달싹인 순간 물거품이 되어 사라졌다.

“보이지 않는 장막이여.”

사람의 말에는 알 수 없는 힘이 있다.

그리고 마법사의 언령(言令)은, 그 힘을 실체화한다.

파앗.

공간과 공간의 틈새를 비집고, 보이지 않는 벽이 허공을 갈랐다.

그것은 강철로 이루어진 화살촉 따위로는 결코 뚫을 수 없는, 강력한 보호 마법이었다.

콰드드득!

수천에 달하던 화살촉들이 단숨에 부러지거나 튕겨 나간다.

이 믿을 수 없는 광경을 두 눈으로 목격한 성벽 위의 사람들이 탄식을 토해 냈지만, 정작 그 놀라운 이적(異蹟)을 선보인 장본인은 평소와 다름없이 차분했다.

“나름대로 철저하게 준비해 놓은 것 같네. 대응 방법도 제법이고.”

대술사의 뇌까림에, 혈주가 나직한 목소리로 입을 열었다.

“그랬겠지. 온 힘을 다해 발악해야 하니까.”

“시간을 필요 이상으로 많이 줬다고는 생각하지 않아?”

“괜한 이야기를 하는군. 이 방법이 가장 확실하다는 건 네가 누구보다 잘 알고 있을 텐데. 그리고…….”

담담한 눈빛으로 대술사를 응시한 채, 혈주가 덧붙였다.

“너 역시, 그 덕분에 준비할 시간을 벌었고.”

피식 웃은 대술사가 고개를 끄덕였다.

하얗고 가느다란 그녀의 손끝은, 이미 하나의 수인(手印)을 그리고 있었다.

겉보기에는 더없이 부드러운 동작이지만, 그 안에는 끔찍한 파괴력이 담긴 또 다른 마법을.

우우웅.

어느덧 요동치는 공기 속, 대술사의 발아래에 각인되어 있던 기이한 문양들이 형형색색의 빛을 머금으며 타오르기 시작했다.

그 숫자만 자그마치 수십여 개.

그것은 대술사가 지난 이틀간, 오늘의 전투를 위해 준비해 두었던 마법진이었다.

“그래서, 뭘 원해?”

대술사의 물음에, 혈주는 문득 생각했다.

뭘 원하느냐고?

‘두말할 것도 없이, 진태경의 죽음이지.’

하지만 그는 목젖까지 차오른 그 한마디를 삼켜야만 했다.

저 멍청한 년은 결코 ‘그분’의 뜻을 거스르려 하지 않을 테니까.

만약 자신이 품고 있는 생각을 알게 된다면, 그녀가 어떤 반응을 보일지는 그로서도 미지수였으니까.

그렇기에 혈주는 애써 침착한 목소리로 이렇게 답할 수밖에 없었다.

“성벽. 성벽을 노려. 단숨에 허물어질 정도로.”

그때, 순한 양처럼 묵묵히 두 사람이 주고받는 이야기를 듣고 있던 달뢰라마가 불쑥 입을 열었다.

“아직 후방이 완전히 봉쇄되지도 않았는데도 벌써 성벽이 무너진다면, 적들이 저항을 포기하고 도망치지 않겠소?”

언뜻 듣기에는 그럴듯한 의견이었지만, 그런 달뢰라마의 주장에도 혈주와 대술사는 조금도 개의치 않았다.

가장 먼저 성벽을 노려야 하는 이유는, 단지 그것을 무너트리기 위함만이 아니었으니까.

스아아아.

대술사는 천천히 손을 뻗었다. 머리 위 아득한 허공에서 끝없이 퍼부어지던 빗줄기가 그녀의 의지에 따라 정지하고, 이내 서로를 향해 뭉쳐 들기 시작했다.

그리고 그렇게 생성된 거대한 물의 구(球)가 수십에 달했을 무렵.

“쏘아져라.”

대술사의 나직한 한 마디와 함께, 저마다 각각 능히 일만 근의 무게와 힘을 지니게 된 물의 구들이 성벽을 향해 나아갔다.

그 어떤 방해도 용납하지 않겠다는 듯, 맹렬한 속도과 기세로.

콰아아아아!

바로 그 순간이었다.

성벽을 향해 가까워지는 적들을 향해 쉴 새 없이 화살을 퍼붓던 궁수들이 멍하니 입을 벌리고, 선두를 든든하게 지키던 방패수들이 자신도 모르게 방패를 내려놓았을 때.

마침내 ‘그들’이 나섰다.

슈확!

공간을 가로지르는 눈부신 섬광들.

어떤 것은 용암처럼 뜨겁고, 어떤 것은 목덜미가 서늘해질 만큼 은밀했으며, 또 다른 어떤 것은 벼락처럼 쾌속했다.

그리고 성벽 위의 무림인들과 관군들이 그 감각을 느꼈을 때는, 이미 모든 것이 이루어진 후였다.

화악, 퍼버버벙!

증발하고, 베어지고, 터져 나간다.

성벽이 아니라 산도 허물어트릴 것만 같았던 거대한 물의 구들이.

한낱 인간의 힘으로는 결코 막을 수 없는, 하나의 자연재해처럼 느껴졌던 그 무시무시한 재앙들이.

“……!”

“……!”

자신도 모르게 일순간 죽음을 직감했던 이들은 동시에 눈을 부릅떴다.

그와 동시에, 뒤늦게 잊고 있던 사실을 떠올렸다.

인간의 힘을 벗어난 존재는, 마법이라 불리는 저 끔찍한 사술(詐術)만이 아니라는 것을.

“시작부터 거칠게 나오는구먼.”

천하를 통틀어 단 열 명의 위대한 무인에게만 허락된 왕좌.

그중에서도 가장 높은 자리에 올라, 하늘의 별들과 어깨를 나란히 한다는 화왕(火王) 적천강이 가래를 탁 뱉으며 씩 웃었다.

“노부가 이런 거 좋아하는 건 또 어찌 알고.”

맹수가 으르렁거리는 듯한 그 목소리에, 사람들은 가슴 한구석이 뜨거워지는 것을 느꼈다.

그리고 다시 기지개를 켜기 시작한 희망의 불씨는, 뒤이어 모습을 드러낸 거인들을 목격함과 동시에 더욱더 크게 타오르기 시작했다.

“주축 고수들의 힘을 빼려는 속셈이군.”

청년보다는 소년에 가까운 모습.

하지만 이제는 모두가 안다.

아직 솜털도 채 가시지 않은 것 같은 저 소년이, 한때 모두의 경외를 한 몸에 받았던 살성(殺星)이라는 사실을.

또한, 그와 비견될 만한 전설을 써 내려간 이가 자신들의 곁에 있음을.

“뻔하지만, 확실한 방법이죠.”

빗방울보다도 투명한 목소리와 함께, 그와는 어울리지 않는 투박한 손가락이 시위를 당긴다.

쉬잉!

쏘아지는 빛줄기.

그리고, 파괴.

콰득!

적들의 머리 위 허공을 뒤덮은, 보이지 않는 보호의 장막을 단숨에 박살 낸 빛줄기가 굉음과 함께 폭발한다.

지면을 부수고, 적들의 생명을 관통하며.

콰아아아앙!

지면이 뒤흔들린다. 터져 나온 굉음이 비명을 집어삼킨다.

작은 동산처럼 움직이던 거구의 괴물들도, 그들을 방패 삼아 나아가던 암천의 교도들도 그 일격을 막기에는 역부족이었다.

궁성(弓星)이라는 위명이, 결코 허언이 아님을 알려주 듯이.

‘할 수 있다.’

일순간 뇌리를 스친 한 줄기의 희망과 함께, 성벽 위의 사람들은 격동에 사로잡혀 자신도 모르게 몸을 떨었다.

이토록 어두운 세상 속에서도 빛을 잃지 않은 저들의 광휘를 보며.

지금 이 순간에도 계속해서 성벽을 향해 짓쳐 드는 마법들을 가로막기 위해 나선 또 다른 초절정 고수들과 이런 위급한 상황 속에서도 조금도 동요하지 않는 진태경의 모습에.

그들은 감격했고, 동시에 전율했다.

살아 있는 전설들과 어깨를 나란히 하고 있었으니까.

그런 이들이 자신들을 살리기 위해 온 힘을 다하고 있었으니까.

쿵. 쿵쿵. 쿵쿵쿵!

어느덧 물결처럼 퍼져나가는 거대한 울림.

이제 그들 모두가 약속이라도 한 듯이 발을 굴렀다. 방패를 내리찍고, 창대를 두드리고, 검과 도를 부딪쳤다.

맹렬한 화염의 비가 쏟아져도.

번뜩이는 벼락이, 끔찍한 냉기를 간직한 얼음이, 정수리를 적셔야 할 빗줄기가 화살이 되어 날아들어도.

그들을 굴하지 않았다.

아니, 믿어 의심치 않았다.

설령 오늘 이 자리에서 어떤 최후를 맞이하더라도, 자신들 또한 전설의 일부가 되리라는 것을.

그리고 그들의 마음속 자그마한 불씨가 마침내 커다란 횃불이 되어 타오르기 시작했을 때.

드드드득!

끝없이 퍼부어지는 화살 비와 견제 속에서도 꿋꿋이 전진해 가던 거구의 괴물들이, 지진과도 같은 굉음을 일으키며 성벽을 향해 쇄도했다.

- 그아아아아!

모골이 송연해지는 듯한 포효.

그와 동시에 인간의 한계를 아득히 벗어난 힘과 속도로 쏘아진 몸뚱어리가, 온 힘을 다해 성벽을 들이받았다.

구구구구궁!
```

## Final English reading copy

```markdown
# Chapter 1100

Someone once said that people feel the greatest wonder and fear when they come face-to-face with the unknown.

When they encounter something they’ve never experienced before and see it for what it really is, every emotion races to its extreme.

And Jin Taekyung wholeheartedly agreed.

As he did with the saying left behind by a certain philosopher: Humans are creatures of learning.

*Whooosh!*

Hundreds of ice spikes shot through the curtain of rain amid a surging swell of enormous energy.

Yet even as a vast spell of considerable power took shape, Jin Taekyung didn’t flinch in the slightest.

He’d already expected it.

“Defend!”

The instant his shout, infused with deep reserves of internal energy, burst from between his lips—

*Shhk! Fwssh!*

A wave of shields covered the heads of his allies, who filled the lofty city wall without leaving a gap. At the same time, brilliant beams of light shot up from all around them, streaking toward the hundreds of ice spikes.

*Boom!*

A thunderous crash. A flash of light.

The ice spikes shattered by the Sword Energy scattered by the Peak masters ricocheted toward the city wall at high speed. But that was all.

*Clang! Clang!*

The massive rectangular shields, their outer surfaces clad in steel, did their job admirably.

Had the ice spikes retained their full strength, things might have been different. But after being weakened once, their shattered remnants weren’t enough to break through the firmly constructed wall of shields.

“Everyone’s safe!”

Reports came from all around, voices raised with excitement.

But Jin Taekyung—the one who’d predicted all this and made preparations beforehand—didn’t let his guard down for a moment.

They’d gotten the battle off to a good start. Successfully defending against magic, which in this world was little different from a supernatural miracle, had also lifted his allies’ morale. That was a major gain.

But Jin Taekyung knew better than anyone that this was only the beginning.

So did the Grand Mage and the Blood Lord, watching from beyond the city wall.

“Loose!”

At the forceful shout, the signalers on the wall waved their flags to pass along the command. Arrows that had gleamed from between the shields finally left their taut bowstrings.

*Whooosh!*

Thousands of arrows darkened part of the sky as they rained down.

They were meant to pierce the throats of the enemies advancing below—the merciless invaders.

But their desperate hopes vanished the moment the red lips concealed beyond a distant veil moved.

“O invisible veil.”

There’s an inexplicable power in human speech.

And a mage’s incantation gives that power substance.

*Fwoom.*

An invisible wall split the air, pressing through the space between one place and another.

It was a powerful protective spell, one that arrowheads of steel could never pierce.

*Crack!*

Thousands of arrowheads snapped or bounced away in an instant.

The people on the wall gasped as they witnessed the unbelievable sight. But the person who’d performed that astonishing miracle remained as calm as ever.

“They seem to have prepared quite thoroughly. Their countermeasures aren’t bad, either.”

At the Grand Mage’s murmur, the Blood Lord spoke in a quiet voice.

“Of course they have. They have to struggle with everything they’ve got.”

“Don’t you think we gave them more time than necessary?”

“You’re bringing that up now? You know better than anyone that this is the surest way. And besides…”

The Blood Lord gazed calmly at the Grand Mage as he added:

“You used that time to prepare, too.”

The Grand Mage gave a short laugh and nodded.

Her white, slender fingertips had already formed a hand seal.

The movement was soft and delicate, but it held another spell within it—one of terrible destructive power.

*Rumble.*

The air began to tremble. Strange patterns etched beneath the Grand Mage’s feet flared with multicolored light.

There were dozens of them.

They were magic circles she had prepared over the past two days for the battle.

“So, what do you want?” the Grand Mage asked.

The Blood Lord briefly considered the question.

*What do I want?*

*Without a doubt, Jin Taekyung’s death.*

But he had to swallow the words welling up in his throat.

That foolish woman would never defy *that person’s* will.

And he had no idea how she’d react if she learned what he was thinking.

So the Blood Lord forced himself to answer in a calm voice.

“The wall. Aim for the wall. Hit it hard enough to bring it down in one blow.”

The Dalai Lama, who’d been listening quietly to their conversation like a docile lamb, suddenly spoke.

“If the wall falls before the rear is completely sealed off, won’t the enemies give up resisting and flee?”

His suggestion sounded reasonable at first, but neither the Blood Lord nor the Grand Mage paid it the slightest mind.

There was a reason to target the wall first—and it wasn’t simply to bring it down.

*Fwoosh.*

The Grand Mage slowly extended a hand. Far above her, the rain that had poured endlessly through the air stopped at her will, then began to gather together.

By the time dozens of enormous spheres of water had formed—

“Fly.”

At the Grand Mage’s quiet command, the spheres hurtled toward the city wall. Each one now carried a weight and force of ten thousand geun.

They surged forward at a fierce speed, as if they would tolerate no interference.

*ROOOAR!*

It happened in an instant.

The archers who’d been firing nonstop at the enemies closing in on the wall stared with their mouths hanging open. The shield bearers who’d been firmly protecting the front line lowered their shields without realizing it.

At last, *they* stepped forward.

*Whoosh!*

Dazzling flashes cut across the air.

Some were as hot as lava. Others were so stealthy they sent a chill down the back of the neck. Still others were as swift as lightning.

By the time the martial artists and imperial troops atop the wall sensed them, it was already over.

*Fwoosh! Boom!*

The enormous spheres of water evaporated, were sliced apart, and burst.

The colossal spheres that looked powerful enough to flatten a mountain, not just the city wall.

The terrifying calamities that had seemed as impossible for humans to stop as a natural disaster.

“……!”

“……!”

Those who’d instinctively sensed their imminent deaths opened their eyes wide in unison.

And at the same time, they remembered what they’d momentarily forgotten:

Those terrifying dark arts called magic weren’t the only thing beyond human power.

“They’re coming in rough right from the start.”

A throne granted to only ten great martial artists across the entire world.

Jeok Cheongang, Fire King, who sat highest among them and stood shoulder to shoulder with the stars in the heavens, spat out some phlegm and grinned.

“How’d they know this old man likes this sort of thing?”

At his voice, like a beast’s growl, the people felt warmth rise in their chests.

The tiny spark of hope, beginning to stir again, blazed brighter still when the giants who appeared next came into view.

“They’re trying to wear down our key fighters.”

A figure closer to a boy than a young man.

But now, everyone knew.

That boy, who still looked as if he hadn’t even lost all his baby fuzz, was the Slaughter Saint, once revered by all.

And there was another living legend beside them, one who’d written a legend of his own to rival the boy’s.

“It’s an obvious move, but an effective one.”

With a voice clearer than raindrops, he drew the bowstring with a rough finger that seemed entirely at odds with it.

*Whoosh!*

A beam of light shot forth.

And then, destruction.

*Crack!*

The beam shattered the invisible protective veil over the enemy forces in an instant, then exploded with a thunderous roar.

It smashed into the ground, piercing the enemies’ lives.

*BOOM!*

The ground shook. The explosion swallowed the screams.

The hulking monsters that moved like little hills, and the Dark Heaven followers advancing behind them, were both powerless to stop that strike.

It proved that the title of Bow Saint was no empty boast.

*We can do this.*

A glimmer of hope flashed through the minds of the people atop the wall, and they trembled with excitement.

They saw the radiance of those people, who hadn’t lost their light even in a world this dark.

They saw the other Supreme Peak masters stepping forward to block the magic that kept crashing toward the wall, and Jin Taekyung, who remained completely unfazed even in this dire situation.

They were moved. And they shuddered.

Because they stood shoulder to shoulder with living legends.

Because those legends were giving everything they had to save them.

*Thud. Thud-thud. Thud-thud-thud!*

A massive rumble rippled outward like a wave.

As if they’d all agreed, the people began stomping their feet. They slammed their shields down, pounded their spear shafts, and struck their swords and sabers together.

Even as a rain of fierce flames poured down.

Even as flashing lightning, ice bearing a dreadful chill, and rain that should have soaked their heads came flying at them—the rain transformed into arrows.

They did not yield.

No—they had no doubt.

Even if they met their end here today, they would become part of a legend, too.

And just as the tiny sparks in their hearts began to flare into a great bonfire—

*Rumble!*

The hulking monsters, who’d steadily advanced despite the relentless rain of arrows and other attacks, charged toward the wall with a roar like an earthquake.

—*GRAAAAH!*

A roar that made their hair stand on end.

At the same time, a body propelled by strength and speed far beyond human limits hurtled toward the wall and slammed into it with all its might.

*RUMBLE!*
```
