<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1098.txt",
      "sha256": "4ac2d74cbb9f6290f3f4939cd1d96a5490b93c9e45f48036c4abb05df9947f2c",
      "bytes": 15311
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b21ff0a09af44624cce7e62bcee62fe70d6ca6e20abaafac84da3d052ec6d705",
      "bytes": 1920
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e58ae46a1bac772cc7720c130c81de8fb5906bb3ba1496eb8e7943cb290731fa",
      "bytes": 244132
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "a8bf02039b1061fe33f692fd76b5d6c9d5c66c86e884f3fc921a89ab88c0dd5d",
      "bytes": 907
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "4ca75d3848567c785581067b89a8fc61c60d9da45d3d393195cf8913f2e38d70",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "faca783b6902dfe8f4b058d37272bd14edcad81163d15f2ae5757c9fb92c01b3",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "28725fc974ef632a63ffba0961efb45ae7b43e6a8e7f6c4581d8c48d37cd16d1",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "551831dc0d38500a27ac28430869c6ded750cf26f4624ee347fa770311b9e4f0",
      "bytes": 623
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "ffa46f4a47a44f340cd4c50dc317af0e1ce4ae3cc029c5335057517b68f4571a",
      "bytes": 922
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "34333020496fb1076c32fa2b536366c4ae8a8a3a83548526b86c17e4abadb3e7",
      "bytes": 287451
    }
  ],
  "estimated_tokens": 12245
}
-->

# Durable State Update — Chapter 1098

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
1 and safe_through 1098. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1098. Profile updates may replace only one
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
  "chapter": 1098,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1098,
    "continuity_sources": [1098],
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
    "The Blood Lord expects thirty thousand reinforcements to reach Qinghai within one or two days.",
    "The Blood Lord wants Taekyung dead despite the Lord of Heaven’s apparent special interest in him; he plans to attack when a hidden agent inside the defenders’ ranks signals.",
    "The Potala Palace and Dark Heaven are allies, but the Palace has a deep, longstanding hatred of the Fire Gate Clan; the Dalai Lama accepts the alliance’s unequal terms.",
    "Namho fears Sichuan may be exposed to enemies from Tibet after the Nanman Beast Palace’s departure.",
    "The Fire Gate Clan’s leaders are unlikely to abandon Xining while their allies and civilians remain there.",
    "A nighttime strike against the enemy leadership has only a one-in-ten chance of success, or one in five if the heavens help; Taekyung rejects it because of Dark Heaven’s magic.",
    "Jeok Cheongang is pressing Taekyung to reveal the Blood Lord’s final words; Taekyung has not disclosed them."
  ],
  "continuity_sources": [
    1096,
    1097
  ],
  "open_questions": [
    "Will the expected reinforcements reach Xining in time to decide the battle?",
    "Why does the Lord of Heaven appear to want Taekyung above all else?",
    "Who is the hidden Dark Heaven agent inside the defenders’ ranks, and when will they signal?",
    "What did the Blood Lord say at the last moment, and will Taekyung tell Jeok Cheongang?",
    "Will the Blood Lord’s plan to kill Taekyung bring him into conflict with the Lord of Heaven?"
  ],
  "safe_through": 1097,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 파륜     | **Pa Ryun**        |
| 살성     | **Slaughter Saint**           | —              |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 소림     | **Shaolin**                      |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 태원     | **Taiyuan**            |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 대사      | **Master** for a senior Buddhist monk                           |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 화주 | **strong liquor** | Liquor stored and consumed by the dark-path swordsmen. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 황하 | **Yellow River** | River along which civilization began. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 역천 | **defying heaven** | Supernatural power that regenerates the masked man's body. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 수하 | 채주 | subordinate_to_stronghold_lord | Stronghold Lord | deferential | The subordinate calls Mu Song 채주 while reporting the nearby vessel. |
| 진태경 | 무송 | junior_martial_artist_to_senior_martial_artist | Senior | formal-polite | Taekyung uses 선배님 after recognizing Mu Song as a senior martial artist and disciple of the Seafaring King. |
| 무송 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | familiar-teasing | Mu Song calls Taekyung 후배 and jokes about his supposed taste for men. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |
| 적천강 | 무송 | legendary martial master to stronghold lord | you | gruff, coercive, and dismissive | Uses 자네 while ordering Mu Song to take the group only as far as Sichuan and leave the fast ship. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 노호검객 | 적천강 | senior_martial_artist_to_legendary_elder | Senior Jeok | deferential and cautious | Addresses Jeok as 노 선배 while explaining his actions. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1097
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Cunning and controlling, he avoids costly risks while manipulating allies; beneath his devotion to the Lord of Heaven, he resents being treated as disposable and resents Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven but resents the Lord’s apparent special interest in Jin Taekyung, whom he resolves to kill even if it means defying the Lord’s command; he considers Taekyung and Cheongpung formidable adversaries.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1096
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1097
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1097
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1097
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 1084
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan, belongs to the Yangtze River Channel League's moderate faction, and is an exceptionally skilled ship captain.
- **Personality:** Ambitious, domineering, impatient with interruptions, strongly attached to life on the water, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song is Pa Ryun’s second Disciple and the Water Dragon Stronghold Lord; he opposed Pa Ryun’s alliance with Dark Heaven but continues to follow his Master’s command.

## Korean source

```text
1098화




사람의 신체에는 상상하는 것 이상으로 수많은 정보가 담겨 있다.

그리고 오감(五感)의 극한에 도달한 초절정 고수들은 상대의 미세한 표정 변화와 움직임만으로도 그에 담긴 뜻을 읽고 해석해 낸다.

바로 지금 이 순간처럼.

- 그래서, 네 녀석은 끝까지 말하지 않을 셈이냐?

나직한 전음과 끝을 짐작할 수 없을 만큼 깊게 가라앉은 눈빛.

그것만으로도 충분했다.

나는 찰나의 동요를 완전히 감추지 못했고, 그 흔들린 눈빛은 곧 자백이나 다름없었다.

- 마지막 순간, 혈주 그놈이 무슨 헛소리를 지껄였는지.

씹어 뱉는 듯한 전음과 함께 모든 것을 꿰뚫어 보는 듯한 적천강의 심유한 눈빛에, 나는 문득 깨달았다.

설령 그가 천하에서 손꼽히는 초절정 고수가 아니었더라도, 내가 동요를 내비치지 않았더라도 달라지는 것은 아무것도 없었을 것이라고.

한 뿌리에서 자라난 나무의 가지들이 뻗은 방향이 다를지언정 서로 연결되어 있듯, 늙은 스승은 이미 제자의 마음을 훤히 들여다보고 있었을 것이라고.

그렇기에, 내가 할 수 있는 대답은 하나뿐이었다.

- 회춘하셔서 그런가, 귀가 더 밝아지셨네요.

이런 상황을 조금도 예측하지 못했다면, 그건 거짓말이다.

적천강은 과거 태원진가로 쳐들어와 나를 겁박했던 노호검객(怒號劍客)의 전음을 엿듣고 그를 묵사발 낸 전적이 있으니까.

하지만 혈주는 노호검객과 비교하는 것이 민망할 정도로 고강한 무위를 지닌 자.

소림혈사 때보다도 더욱 진일보한 놈의 전음을 읽어 내는 것은 적천강으로서도 무리라고 여겼고, 성안으로 돌아온 후부터 지금껏 별다른 내색을 하지 않는 그의 모습에 내심 안도했었다.

물론, 이제 와 다시 생각해 보면 결국 잘 쳐줘야 절반짜리 답안지에 불과했지만.

“대답하거라. 어서.”

불현듯 적천강의 입술을 비집고 흘러나온 육성.

그로 인해 단번에 집중된 수십 쌍의 시선을 느끼며, 나는 크게 심호흡했다.

그리고 마침내 그가 원하는 진실을 털어놓았다.

“예상하신 바가 맞습니다. 혈주, 그놈이 제게 제안하더군요.”

“무엇을 말이냐.”

“지금부터 하루의 말미를 줄 테니, 홀로 성을 빠져나와 스스로 사지 근맥을 끊고 투항하라고요.”

“……!”

“……!”

일순간, 보이지 않는 파동이 주위의 공기를 찌르르 울렸다.

이제야 상황을 알아차린 사람들로부터 흘러나오는 침음 속, 적천강이 석고상처럼 딱딱하게 굳은 표정으로 입을 열었다.

“그래서, 네 녀석의 목숨줄을 쥐는 대가로 다른 이들의 안위를 약속했더냐?”

역시.

나는 쓴웃음을 지으며 고개를 끄덕였다.

“예.”

“왜…… 처음부터 말하지 않았지?”

“고민했으니까요. 그리고 이런 상황이 오지 않았다면, 계속해서 고민했을 테니까요.”

“고민? 그따위 터무니없는 헛소리를 말이냐?”

“다른 누구도 아닌 바로 그 혈주가, 천주의 이름을 걸고 맹세했습니다. 약속대로 이루어진다면 한 사람의 목숨값으로는 충분히 남는 장사죠. 아닙니까?”

조금 전 자신이 했던 말을 그대로 돌려받은 살성이, 내 시선과 마주치자 눈살을 찌푸렸다.

“그래, 그럴지도 모르지. 하지만 지금의 넌 가장 중요한 걸 놓치고 있다.”

“그게 뭡니까?”

“신뢰. 거래를 주고받는 상대에 대한 신뢰성이다.”

망설임 없이 대답한 살성이 말을 이었다.

“놈들은 결코 약속을 지키지 않을 것이다. 조금 전의 내가 스스로의 실력을 믿고 도박을 하는 거라면, 너는 애당초 믿을 수 없는 대상을 상대로 거래를 하려 하고 있지.”

나는 조용히 입술을 깨물었다.

솔직히, 모르겠다.

아니, 마음 한구석으로는 이미 알고 있었는지도 모른다.

적천강이, 살성이 하는 모든 말들이 사실이라는 것을.

마지막 제안을 하기 이전에 혈주가 내게 내비쳤던 그 진득한 살기(殺氣)와 반드시 죽이겠다는 다짐이, 결코 허언이 아니리라는 것을.

하지만, 이 말도 안 되는 거래를 두고 고민할 수밖에 없던 이유 또한 명백했다.

“지금 천주의 목표는, 오직 저뿐입니다.”

돌이켜 보면 천주는 늘 나를 원해 왔다.

그것도 아주 오래전부터.

그렇지 않았다면 괄목상대(刮目相對)라는 말조차 무색하게 만들 정도로 하루가 다르게 강해지는 나를, 천하의 지배자가 되고자 하는 자신의 앞길을 번번이 막아서는 가장 큰 걸림돌을 지금껏 내버려 두지는 않았을 것이다.

천주가 나를 원하는 정확한 이유?

모른다.

그러나 어느 한 가지 사실만큼은 어렴풋이 알 것 같았다.

“놈에게 있어, 지금의 저는 그 무엇보다 중요한 존재입니다. 어쩌면…….”

나는 문득 말꼬리를 흐렸다.

동시에 전신의 털이 곤두서는 듯한 감각을 느끼며, 참았던 숨을 토해 냈다.

“이 천하보다도 더.”

“……!”

“……!”

더는 감출 수 없을 만큼 선명하게 드러난 진실은, 소름이 끼치도록 차갑고 어두웠다.

일순간 얼어붙어 버린 주위의 공기처럼.

그리고 나를 고민에 휩싸일 수밖에 없게 만들었던 또 다른 이유처럼.

솨아아아아.

침묵 가운데 온 사방을 두드리는 요란한 빗줄기를 뒤로한 채, 나는 머나먼 동쪽 어딘가를 향해 고개를 돌렸다.

지금 이 순간에도 귓가를 파고드는 저 빗소리가, 마치 뱃머리를 따라 갈라지는 물살의 그것과 닮았다는 생각과 함께.

‘놈들이 오고 있다.’

보이지 않는다. 

그러나 느껴진다.

이미 확연히 기울어져 버린 이 전장의 저울추를 완전히 부러트릴, 서녕의 마지막 한 사람까지 휩쓸어 버릴 최후의 파도가.



* * *



종종 그럴 때가 있다.

새와 벌레, 물고기조차 잠들고 오직 달만이 휘영청 떠 있을 때가.

장강(長江)의 어부들은 그런 날을 좋아했다.

굳이 물고기를 그물질하지 않더라도, 혹은 어부가 아니더라도 그날만큼은 모두가 강가로 나가 멱을 감고 배를 띄워 싸구려 화주(火酒)나마 술잔 가득 기울이곤 했다.

자신들에게 많은 것을 선물해 준 이 광활한 강줄기에 감사하며, 수면에 비친 달을 저으며 노래를 부르고 그들만의 시간을 즐겼었다.

분명.

그랬던 때가 있었다.

촤아아아악!

깊은 밤, 칠흑 같은 강물이 갈라진다.

먹구름 사이로 모습을 드러낸 달이 수면에 제 얼굴을 비춰 보기도 전, 수백에 달하는 뱃머리가 그 위를 뒤덮으며 나아갔다.

맹렬하면서도 끝없이.

그 광경은 마치 하나의 도시가 움직이는 것과 같았고, 거침없는 파도나 다름없었다.

이제는 세상 모든 만물의 어버이이자 지배자인 천자(天子)조차 막을 수 없는, 하늘의 이치를 거슬러 역천(逆天)을 꿈꾸는 거대한 물결.

그리고 한껏 부풀어 오른 돛을 따라 휘날리는 무수한 깃발들은, 그 존재만으로도 공포의 대상이 되어 버린 지 오래였다.

“무슨 용무더냐.”

뱃머리에 몸을 기댄 채, 위풍당당한 필체로 깃발을 장식한 장강수로맹(長江水澇盟)이라는 다섯 글자를 말없이 올려다보던 노인이 천천히 돌아서며 덧붙였다.

“그것도, 기별도 없이 혼자서.”

노인, 해상왕(海上王) 파륜의 나직한 음성에 때아닌 불청객을 데려온 수하가 굳은 얼굴로 고개를 숙였다.

“송구합니다. 맹주. 그것이…….”

“되었다.”

단칼에 수하의 입을 다물게 만든 파륜은, 돛대가 드리운 그림자 속에 서 있는 불청객을 향해 말을 이었다.

“목적지에 다다르기 전까지 임무에 소홀히 하는 자는 엄벌로 다스리겠다 했거늘, 벌써 잊었느냐?”

불청객이 고개를 저었다.

“아닙니다.”

“하면, 제자만큼은 예외일 것이라 생각했느냐?”

“그 또한 아닙니다.”

“하면?”

저벅.

무거운 발걸음과 함께, 그림자 속에서 모습을 드러낸 선화아(船火兒) 무송이 대답했다.

“스승님과 함께 달구경이나 할까 하여 왔습니다.”

달구경이라.

자신도 모르게 먹구름이 가득한 하늘을 바라본 파륜이 무뚝뚝한 음성으로 대꾸했다.

“본 맹의 규율에 따라, 날이 밝는 대로 갑판에서 태형(笞刑) 서른 대를 집행하겠다.”

순간 멈칫한 무송이 곧장 반문했다.

“스무 대 아니었습니까?”

“명령을 어긴 데다가 헛소리까지 지껄였으니, 그 정도는 각오했겠지. 서른 대.”

“그건.”

“마흔.”

말문이 막힌 무송이 침묵한 그때, 파륜이 아직까지도 자리에 남아 있던 수하를 향해 덧붙였다.

“본연의 임무에 소홀했던 것은 네놈 역시 마찬가지. 태형 열 대다.”

“매, 맹주.”

“이만 물러나거라. 이 일은 불문(不問)에 부치고.”

장강수로맹의 그것은 일반적인 태형이 아니다. 

단단한 박달나무로 만들어진 노에 물을 흠뻑 묻혀, 계율을 담당하는 절정 고수가 집행하니까.

비록 공력을 사용하지는 않지만, 열 대만 맞아도 엉덩이 살이 짓무르고 뼈가 몇 군데 부러지는 건 기본이니 두어 달은 앓아누워야 한다.

하지만 해상왕 파륜의 엄격함은, 자신의 제자나 삼십여 년을 따른 수하일지라도 예외일 수는 없는 법.

결국 별다른 말 없이 물러난 수하의 인기척이 완전히 사라질 때쯤, 갈라지는 강물을 바라보던 파륜이 불쑥 입을 열었다.

“아무래도, 오십 대로 해야겠군.”

“예?”

“누구의 잘못인지는 명백하니, 십 년이라도 더 젊고 팔팔한 네 녀석이 대신 맞거라.”

그런 스승을 멍하니 바라보던 무송이 이내 쓴웃음을 지으며 고개를 끄덕였다.

“그러겠습니다. 그 정도면 저도 석 달은 옴짝달싹 못 할 테니, 오히려 이게 더 나을 수도 있겠군요.”

“말에 뼈가 있구나.”

“그렇다면 제대로 들으신 겁니다.”

크게 심호흡한 무송이 돌연 무릎을 꿇었다.

쿵.

“부디, 부디 단 한 번이라도 결정을 재고해 주십시오.”

그리고 그 울림이 가라앉기도 전에, 바닥에 머리를 박으며 덧붙였다.

“아무리 생각해도 이건…… 옳지 않습니다.”

하지만 제자의 갑작스러운 오체투지(五體投地)에도 불구하고, 스승의 눈은 여전히 장강을 향하고 있었다.

“옳지 않다, 라.”

“가당치 않은 소리라는 것은 압니다. 저 역시 코흘리개 시절부터 수적으로 살아왔으니 말입니다.”

약탈이 업이었다.

이립의 나이로 수룡채를 맡게 된 이후부터는, 많은 식구를 거느린 채주로서 남의 것을 빼앗고 그것을 수하들과 함께 누려 왔다.

그러나…… 이런 것을 바란 적은, 단 한 번도 없었다.

“장강이 피로 물들고 있습니다. 앞으로도 계속해서 그럴 겁니다. 제가, 아니 우리 모두가 사랑하는 저 넓고 푸른 강물이 말입니다.”

어느샌가 파르르 떨려오는 무송의 목소리에, 파륜이 불현듯 입을 열었다.

“그래서였느냐? 지난번 전투 때, 누구보다 앞장서서 그 많은 관군들을 포로로 잡은 이유가.”

“알고…… 계셨습니까.”

“이 장강에서 벌어지는 일 가운데, 노부가 모르는 것이 있을 것 같으냐?”

“……!”

“너뿐만이 아니다. 셋째도, 적지 않은 숫자의 중진들도 엇비슷한 수작을 부렸더군. 아니, 항명(抗命)이라고 해야 하나?”

“스승님, 이건 결코 항명이 아닙니다. 저희는 단지……!”

“감히, 누구의 안전에서 목소리를 높이느냐.”

고개를 돌린 파륜이 착 가라앉은 눈빛으로 무송을 내려다보았다.

“노부는 죽이라 명했고, 너희는 죽였어야 했다. 그 관군들은 그래도 되는 이들이었으니.”

“아닙니다. 그들은 구태여 죽일 필요도 없는 이들이었습니다.”

차라리 강자였다면 사정을 봐주지 않았을지도 모른다.

무송으로서도 스스로를, 수하들을 지켜야 했으니까.

하지만 그날 그가 마주한 관군들은 너무나도 약했다. 피를 보는 것이 무서워질 만큼.

“그건, 그건 전투가 아니었습니다. 학살이었습니다.”

“그래. 노부는 그걸 원했느니라.”

“……!”

“하지만 결국 한 치의 오차 없이 명령을 수행한 것은 네 사형과 장로(長老)들뿐이었지.”

스아아아.

무송은 자신도 모르게 몸을 떨었다.

멈춰야 한다.

스승의 분노를 생각한다면 멈추는 것이 옳았다. 

지금 당장이라도.

하지만 머리 위로 쏟아지는 그 압도적인 기파(氣波)에도, 무송은 이를 악물며 버텨 냈다.

지금 이 순간 눈앞을 스치는 누군가를 떠올리며.

무공은 개같이 강한 데다 성격은 지랄 맞아서 온갖 고욕을 치러야 했지만, 자신 같은 수적 따위도 협(俠)을 좇을 수 있다는 사실을 일깨워 준 그.

진태경을.

“아, 아직도 모르시겠습니까?”

전신을 짓누르는 강대한 기파 속, 무송은 숨을 헐떡이며 힘겹게 말을 이어 갔다.

“대사형도, 그리고 그 빌어먹을 장로들도. 스승님을 따른 것이 아닙니다.”

“뭐라?”

“그들이 충성하는 대상은 따로 있습니다. 어쩌면 이미 오래전부터 마, 말입니…….”

쿵.

거기까지였다.

그가 십왕(十王)의 일인인 파륜의 기세를 감당할 수 있었던 것은.

그리고 말을 채 잇지 못하고 의식을 잃은 제자를 심유한 눈빛으로 내려보던 스승은, 이내 다시 강물을 향해 고개를 돌리며 뇌까렸다.

정확히는 어느덧 황톳빛을 띠기 시작한, 황하의 지류를.

“그래. 차라리 그대로 있거라. 이제 와 네가 나선다 한들 달라지는 것은 아무것도 없고, 오직 끝을 향해 달려갈 뿐이니.”

그때, 먹구름 사이로 다시 고개를 내민 달빛이 지상으로 쏟아졌다.

그와 동시에 강가와 그리 멀리 떨어지지 않은 곳에 위치한 풀숲 사이로, 헤아릴 수 없이 많은 인영이 몰려들기 시작했다.

수천, 아니 수만에 달하는 그림자들이.

“다시 보니, 달구경 하기에 썩 괜찮은 날이로군.”

달빛처럼 흐릿한 웃음을 머금은 목소리와 함께, 장강수로맹의 깃발을 단 수백여 척의 함선이 새로운 아군을 맞이할 준비를 시작했다.
```

## Final English reading copy

```markdown
# Chapter 1098

The human body held more information than anyone could imagine.

And masters who had reached the limits of their five senses could read and interpret what that information meant from the slightest change in an opponent’s expression or movement.

Just like right now.

—So, you’re planning to keep quiet until the very end?

A low Sound Transmission. Eyes sunk so deep I couldn’t guess what lay beneath them.

That alone was enough.

I hadn’t managed to completely hide my momentary agitation, and the shift in my eyes was practically a confession.

—At the last moment, what kind of nonsense did that bastard the Blood Lord spout?

As Jeok Cheongang’s deep gaze seemed to see through everything, his Sound Transmission coming as if he were spitting out the words, I suddenly realized something.

Even if he hadn’t been one of the world’s foremost Supreme Peak masters, even if I hadn’t let my agitation show, nothing would have changed.

Like the branches of a tree grown from the same root, connected even when they spread in different directions, my old Master had already seen straight through his Disciple’s heart.

So there was only one answer I could give.

—Maybe your hearing got better because you got younger.

I’d be lying if I said I hadn’t anticipated this situation at all.

Jeok Cheongang had once overheard the Sound Transmission of the Roaring Fury Swordsman, who’d come to the Jin Family of Taiyuan and threatened me, then beaten him to a pulp.

But the Blood Lord’s martial prowess was so formidable that comparing him to the Roaring Fury Swordsman was almost embarrassing.

I’d assumed that even Jeok Cheongang couldn’t read the Sound Transmission of someone who’d grown even stronger since the Shaolin Bloodshed. And I’d secretly felt relieved that, ever since we returned inside the city, Jeok Cheongang hadn’t let on that anything was wrong.

Of course, looking back now, that answer had been half-right at best.

“Answer me. Now.”

Jeok Cheongang’s voice suddenly slipped past his lips.

Feeling dozens of pairs of eyes turn toward me at once, I took a deep breath.

And at last, I told him the truth he wanted to hear.

“You were right. The Blood Lord made me an offer.”

“What offer?”

“He said I had one day, starting now, to leave the city alone, sever the sinews and meridians in all four of my limbs myself, and surrender.”

“……!”

“……!”

An invisible ripple shivered through the air.

As murmurs rose from the people who were only now grasping the situation, Jeok Cheongang spoke with a face gone stiff as a stone statue.

“So, he promised everyone else’s safety in exchange for your life?”

As expected.

I nodded with a bitter smile.

“Yes.”

“Why… didn’t you tell me sooner?”

“Because I was thinking it over. And if things hadn’t come to this, I would’ve kept thinking about it.”

“Thinking it over? You mean that ridiculous load of crap?”

“The Blood Lord himself swore on the Lord of Heaven’s name. If he kept his word, it’d be a bargain more than fair for one life. Wouldn’t you agree?”

The Slaughter Saint, who’d just had his own words thrown back at him, frowned when he met my gaze.

“Yes, perhaps. But you’re overlooking the most important thing.”

“What’s that?”

“Trust. Whether you can trust the person you’re making a deal with.”

The Slaughter Saint answered without hesitation, then continued:

“They’ll never keep their promise. If the gamble I proposed earlier rests on confidence in my own skill, you’re trying to make a deal with someone you can’t trust in the first place.”

I bit my lip in silence.

Honestly, I didn’t know.

No—I might have known already, somewhere in the back of my mind.

That Jeok Cheongang, that the Slaughter Saint, was right about everything.

That the Blood Lord’s thick killing intent before he made his final offer, and his vow that he would kill me, had never been empty words.

But there was another reason I couldn’t help considering this absurd deal.

“The Lord of Heaven’s goal right now is me. And me alone.”

Looking back, the Lord of Heaven had always wanted me.

And for a very long time.

Otherwise, he wouldn’t have left me alone all this time as I grew stronger by the day—so quickly that the saying “treat someone with new eyes” couldn’t keep up—even though I kept standing in the way of his path to ruling the world.

Why the Lord of Heaven wanted me, exactly?

I didn’t know.

But there was one thing I thought I could make out, however dimly.

“To him, I’m more important than anything else right now. Maybe…”

My voice trailed off.

At the same time, I felt the hairs all over my body stand on end and let out the breath I’d been holding.

“Even more than this entire world.”

“……!”

“……!”

The truth, too clear now to hide, was chillingly cold and dark.

Like the air around us, frozen in an instant.

And like the other reason I couldn’t help agonizing over this.

Whoooosh.

With the racket of rain pounding all around us, I turned my head toward somewhere far to the east.

The rain still burrowing into my ears sounded, for some reason, like water parting around the prow of a ship.

*They’re coming.*

I couldn’t see them.

But I could feel them.

The final wave, ready to snap the scales of this already-lopsided battlefield—and sweep away every last person in Xining.



* * *



Sometimes, there are nights like that.

When the birds, insects, and even fish are asleep, and only the moon shines bright in the sky.

The fishermen of the Yangtze liked nights like those.

Whether they cast their nets or not, whether they were fishermen or not, on those nights everyone went down to the river. They’d swim and set out in boats, filling their cups with cheap strong liquor and drinking their fill.

Grateful for the vast river that had given them so much, they’d row across the moon’s reflection on the water, singing and enjoying a little time for themselves.

There was a time.

There really was.

*Splash!*

Deep in the night, the pitch-black river split open.

Before the moon emerged from between the dark clouds and could even see its face reflected on the water, hundreds of prows covered the river and forged ahead.

Fiercely. Without end.

It was like watching a city move, a wave that nothing could stop.

A mighty current that defied the order of heaven and dreamed of defying Heaven itself, one not even the Son of Heaven—the father and ruler of all under it—could stop.

And the countless flags fluttering from the swollen sails had long since become objects of fear in their own right.

“What brings you here?”

The old man, leaning against the prow, had silently looked up at the five characters inscribed on the flag in bold, imposing strokes: Yangtze River Channel League. Now he slowly turned and added:

“And alone, without even sending word.”

At the Seafaring King Pa Ryun’s quiet voice, the subordinate who’d brought the unexpected visitor lowered his head, face stiff.

“My apologies, Alliance Leader. It’s just—”

“Enough.”

Pa Ryun cut him off with a single word, then addressed the uninvited guest standing in the shadow of the mast.

“I said I’d punish anyone who neglected their duties before we reached our destination. Have you already forgotten?”

The visitor shook his head.

“No.”

“Then did you think my Disciple would be an exception?”

“No.”

“Then?”

Thud.

With a heavy step, Ship-Fire Boy Mu Song emerged from the shadows and answered:

“I came to watch the moon with you, Master.”

Watch the moon.

Pa Ryun found himself glancing up at the cloud-filled sky. His voice remained gruff.

“By the rules of the League, you’ll receive thirty strokes with the rod on deck at dawn.”

Mu Song hesitated, then immediately objected.

“Wasn’t it twenty?”

“You disobeyed an order and spouted nonsense on top of it. You knew what you were getting into. Thirty.”

“But—”

“Forty.”

Mu Song fell silent. Then Pa Ryun turned to the subordinate, who was still standing there, and added:

“You neglected your duty, too. Ten strokes.”

“B-But, Alliance Leader—”

“Leave us. This matter will go unpunished.”

The Yangtze River Channel League’s corporal punishment was no ordinary beating.

The strokes were delivered with an oar made of hard birchwood and soaked in water—by a Peak master in charge of discipline.

The master didn’t use internal energy, but even ten strokes were enough to leave your backside raw and break several bones. You’d be bedridden for a couple of months.

But Seafaring King Pa Ryun’s strictness made no exceptions—not for his own Disciple, and not for a subordinate who’d followed him for over thirty years.

In the end, the subordinate left without another word. By the time his presence had completely faded, Pa Ryun, still watching the river split around the ships, spoke abruptly.

“Perhaps it ought to be fifty.”

“What?”

“It’s obvious whose fault this is. You’re ten years younger and in better shape, so take the extra strokes for him.”

Mu Song stared blankly at his Master, then nodded with a bitter smile.

“I will. If it’s that many, I won’t be able to move for three months. Maybe that’s for the best.”

“There’s a barb in your words.”

“Then you heard me right.”

Mu Song took a deep breath and suddenly dropped to his knees.

*Thump.*

“Please—please reconsider your decision, just this once.”

Before the echo had even faded, he struck his forehead against the deck and added:

“No matter how I look at it… this isn’t right.”

But even as his Disciple suddenly prostrated himself, the Master kept his eyes on the Yangtze.

“Not right, you say.”

“I know it sounds absurd. I’ve been a bandit since I was a snot-nosed kid, too.”

Pillaging had been his trade.

Ever since he’d taken charge of Water Dragon Stronghold at thirty, he’d led a large family of followers, taking what belonged to others and sharing it with them.

But… he’d never once wanted something like this.

“The Yangtze is being stained with blood. And it’ll keep happening. I mean that vast, blue river we all love.”

Mu Song’s voice had begun to tremble. Pa Ryun suddenly spoke.

“Is that why, in the last battle, you were the first to capture so many imperial troops?”

“You knew…?”

“Do you think there’s anything that happens on the Yangtze that this old man doesn’t know about?”

“……!”

“It wasn’t only you. The Third Disciple and quite a few of the senior members pulled similar tricks. Should I call it insubordination?”

“Master, this isn’t insubordination. We only—”

“How dare you raise your voice in whose presence?”

Pa Ryun turned his head and looked down at Mu Song, his eyes gone cold.

“This old man ordered them killed, and you should have killed them. They were people it was all right to kill.”

“No. There was no need to kill them.”

If they’d been strong, Mu Song might not have shown them mercy.

He had to protect himself and his followers, too.

But the imperial troops he’d faced that day had been so weak. Weak enough to make him afraid to see blood.

“That—that wasn’t a battle. It was a massacre.”

“Yes. That’s what this old man wanted.”

“……!”

“But in the end, the only ones who carried out my orders without the slightest deviation were your Senior Brother and the Elders.”

Hiss.

Mu Song shuddered without meaning to.

He had to stop.

Given his Master’s anger, the right thing to do was stop.

Right now.

But even with that overwhelming aura bearing down on him, Mu Song clenched his teeth and endured it.

Thinking of someone who flashed through his mind at that very moment.

A man whose martial arts were insanely strong and whose personality was a total bastard—he’d put Mu Song through all kinds of hell. But he’d also shown him that even a bandit like himself could pursue chivalry.

Jin Taekyung.

“D-Do you still not understand?”

Under the weight of his Master’s mighty aura, Mu Song gasped for breath and struggled to continue.

“Eldest Senior Brother—and those damn Elders, too. They weren’t following you.”

“What?”

“The people they’re loyal to are someone else. Maybe they have been for a long time, M-Master…”

*Thump.*

That was as far as he got.

As far as he could withstand the force of Pa Ryun, one of the Ten Kings.

His Disciple had lost consciousness before he could finish speaking. Pa Ryun looked down at him with a deep gaze, then turned back to the river and muttered.

Or, more precisely, to the tributary of the Yellow River, whose waters had begun to turn the color of brown earth.

“Yes. Better stay just as you are. Even if you stepped in now, nothing would change. It would only rush toward its end.”

Just then, moonlight poured down to the ground as the moon reappeared between the clouds.

At the same time, countless figures began gathering in the grass not far from the riverbank.

Thousands—no, tens of thousands of shadows.

A voice, its laugh as faint as moonlight, spoke.

“It seems the moon’s looking rather fine tonight after all.”

Hundreds of ships bearing the Yangtze River Channel League’s flags began preparing to welcome their new allies.
```
