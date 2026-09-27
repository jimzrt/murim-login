<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1087.txt",
      "sha256": "65326f7ef86a95d217b141d27881bbfb391bc031a024432d02b7944db8578567",
      "bytes": 12090
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ad16b834d28d17e7bc3366989fe97c32aa16bd4a25590b5ae68cc307085a3441",
      "bytes": 1031
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4ed8101452df2425b89e5c8364c1fe6dfdf6c2111129928b6ce5e8f121d10f80",
      "bytes": 243758
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "646a12a4ea1caa0d26d925a8cb72f34bbbfc0d4300f27200826f3391bbe39ff4",
      "bytes": 928
    },
    {
      "path": "characters/Hak Eui.md",
      "sha256": "f70550a69289af1dcf2f15c65a283415ee68dac2eda4337e99a0f00771c51861",
      "bytes": 554
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "17853032f1a26a6c7dfd334efc3544e1ea8730d67555f56ddc037ec8199f044f",
      "bytes": 1001
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "bb62371b30fa643c4babaf213644711ed67499356a3e223dc6a3964b5ccc02ed",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2f39070d3dee4fc71560e1d4d8ba3d013bc49e3dc94bc8547efc8c047dedbecc",
      "bytes": 623
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "8473b5149b06d0bec2708e7fedd81f4b9b9952a1ea8069ef624ec0620dedc236",
      "bytes": 1084
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "0c25dbc5459ba2aa04442385569daaabb24127b58a23d2088e905d30bc240462",
      "bytes": 650
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c4a0e6a83aedc85b5783bb09dd09c0203fec4ce272e8879854936f6a4d11be19",
      "bytes": 286755
    }
  ],
  "estimated_tokens": 10453
}
-->

# Durable State Update — Chapter 1087

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
1 and safe_through 1087. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1087. Profile updates may replace only one
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
  "chapter": 1087,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1087,
    "continuity_sources": [1087],
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
    "The Yangtze River Channel League and Green Forest Alliance are advancing west in a large combined force.",
    "Dark Heaven reinforcements are joining through Moving Formations; their locations remain unknown.",
    "Mae Jonghak and the New Murim Alliance have prepared an operation against Dark Heaven; Zhuge Feng has the intelligence and tasking to execute it.",
    "The Zhuge Clan is preparing to leave its current home immediately.",
    "Zhuge Feng urges Jin Taekyung to hold on in the west."
  ],
  "continuity_sources": [
    1086
  ],
  "open_questions": [
    "What is the black-robed captive in Qinghai’s identity and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "Who is the black-robed man beside Pa Ryun?"
  ],
  "safe_through": 1086,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 매종학    | **Mae Jonghak**    |
| 굉도     | **Hong Dao**       |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 장강수로맹  | **Yangtze River Channel League** |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 중원     | **Central Plains**                               |                                                       |
| 일격     | **One Strike**                         |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 방장      | **Abbot**                                                       |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 학의 | **Hak Eui** | Kunlun Sect First-Generation Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 녹옥불장 | **Green Jade Buddha Staff** | Ancient Shaolin sacred treasure carried by Hong Dao. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 불장 | **Buddhist Staff** | Generic term in Hong Dao's final words; the specific treasure is 녹옥불장. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 굉도 | 진태경 | senior_monk_to_guest_benefactor | Benefactor | formal-polite and probing | Hong Dao repeatedly addresses Taekyung as 시주 while identifying him as the Master of Morning Star. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 매종학 | 혈주 | legendary_martial_master_to_enemy | you | cold and judgmental | After revealing himself, Mae Jonghak condemns the Blood Lord's accumulated sins and orders him to pay the price. |
| 혈주 | 매종학 | enemy_to_revealed_legendary_master | you | shocked and hostile | The Blood Lord addresses Mae Jonghak with 당신 immediately after recognizing him as the Sword Saint. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 제갈풍 | 진태경 | senior strategist_to_younger_martial_artist | you | calm and familiar | Uses 자네 while inviting Taekyung to continue questioning the Hubei incident. |
| 진태경 | 제갈풍 | younger martial artist to senior clan head | Sir Zhuge | blunt and challenging | Uses 제갈 대협 while disputing Zhuge Feng's attempted ten-percent claim. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 매종학 | 제갈풍 | Alliance Leader to Zhuge Clan Family Head | Family Head Zhuge | formal and familiar | Mae Jonghak asks whether Zhuge Feng completed his assignment. |
| 천주 | 대술사 | master to servant | you | commanding and authoritative | Addresses her through mind-voice, ordering her to report, raise her head, and depart. |
| 대술사 | 천주 | servant to master | Lord of Heaven | extremely deferential | Uses reverent titles and self-abasing language while reporting and pleading. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 학의 | 진태경 | Kunlun Sect disciple to renowned martial artist | Great Hero Jin Taekyung | formal and deferential | Uses 진태경 대협 when introducing himself and greeting Taekyung. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1071
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Hak Eui.md

# Hak Eui (학의)

- **Safe through:** Chapter 1086
- **Aliases:** None
- **Role:** Hak Eui is a First-Generation Disciple of the Kunlun Sect.
- **Personality:** Composed, observant, and assertive; he investigates matters closely and uses his standing to bring consequential findings before the leaders.
- **Voice:** Calm and formal, with measured phrasing and dry, blunt statements of fact.
- **Relationships:** He has met Jin Taekyung and respectfully addresses him as a Great Hero.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 1013
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1086
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1086
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1086
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 1086
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
1087화




제갈풍이 간절한 바람을 담은 눈빛으로 서쪽을 바라보고 있던 그때, 서쪽 땅의 가장 높은 봉우리에서는 나직한 웃음소리가 흘러나오고 있었다.

“그래, 응당 이래야지. 이래야 하고말고.”

미소 띤 얼굴로 고개를 끄덕이는 혈주(血主)의 모습에, 이제 막 보고를 끝마친 전령은 내심 안도했다.

그가 충분히 흡족해할 만한 희소식을 가져왔음에.

이미 차례차례 싸늘한 시체가 된 동료들처럼, 눈앞의 난폭한 상관에게 죽임을 당하지 않아도 된다는 사실에.

하지만 아직 안심하기에는 일렀다.

이 시간은 아직 끝나지 않았으니까.

“해서, 죄다 눈치만 살살 보고 있다는 말이지?”

혈주의 물음에 더욱 자세를 낮추어 부복한 전령이 대답했다.

“그렇습니다. 구파일방과 오대세가도 사태를 주시하며 방비를 철저히 할 뿐, 그 이상의 움직임은 보이지 않고 있습니다.”

“평소에는 협의지사(俠義志士)라며 서로를 치켜세우더니, 막상 상황이 닥치니 겁을 잔뜩 집어먹었군.”

혈주의 미소가 더욱 짙어진 그때, 어디선가 낭랑한 목소리가 울려 퍼졌다.

“누구처럼 멍청한 것보다는 겁쟁이가 낫겠지. 안 그래?”

목소리의 주인을 확인한 혈주는 자신도 모르게 미간을 찌푸렸지만, 이내 여유로운 어조로 대꾸했다.

“백번 옳은 말이야. 멍청함은 곧 무능과 연결되니까. 그분께서 이번 계획을 내게 맡긴 것도 그런 이유에서겠지.”

“내 휘하의 술사들을 멋대로 데려가 일을 벌인 것도?”

“청해성에서의 일을 모두 일임받은 내가 패장(敗將) 따위와 상의해야 할 필요가 있을까?”

감숙에서의 실패를 지적당한 대술사가 싸늘하게 미소 지었다.

“확실히 언변이 늘긴 했네. 혹시 지난번에 잘린 게 팔이 아니라 머리였나? 조금 똑똑해진 건 칭찬해야겠어.”

일순간, 혈주의 입가에 맺혀있던 미소가 흐릿해졌다.

중원 무림이 소림혈사라 명명한 사건 당시, 검성 매종학의 일격에 한쪽 팔을 잃었던 것은 그에게 있어 건드려서는 안 될 역린(逆鱗)이 되어 버린 지 오래였다.

‘이 빌어먹을 년이.’

물론 맡은 바 목적은 충분히 이루었다.

가장 중요했던 녹옥불장(綠玉佛丈)을 탈취했고, 방장인 굉도를 비롯한 소림사의 무승들을 숱하게 죽여 엄청난 타격을 입혔으니까.

하지만 이런 성공적인 결과와는 달리, 그 과정에서 입은 자존심의 상처는 쉽게 회복될 기미가 보이지 않았다.

다시 떠올리는 것만으로도 마음 한구석이 서늘해지는, 그때의 자줏빛 검강(劍罡)이 베어 냈던 부위가 새로운 팔이 자리 잡은 지금까지도 욱신거릴 만큼.

그리고 조금도 자신을 두려워하지 않고 끝까지 맞섰던, 어느 하룻강아지에 대한 분노를 아직도 간직하고 있을 만큼.

“주둥이 닥쳐라. 그 자리에 있지도 않았던 네년 따위가 왈가왈부할 만한 일이 아니니까.”

침잠하게 가라앉은 혈주의 목소리에 대술사가 빙긋 웃었다.

“맞아. 그게 가장 아쉽더라고.”

“뭐?”

“만약 내가 그 자리에 있었다면, 검성과 수백 합을 겨룬 끝에 패배했다는 헛소리 따위는 처음부터 꺼내지도 못했을 테니까.”

“……!”

“솔직히 말해 봐. 화왕(火王), 그 난폭한 늙은이와 한바탕 생사결을 치르고도 검성과 수백 합을? 간도 크지. 감히 그분께 거짓을 고하다니.”

“망상이 지나치군. 난 항상 그분에게 진실만을 고했다.”

혈주는 애써 담담하게 대꾸했지만, 대술사의 말이 사실이라는 것은 그 자신이 누구보다 잘 알고 있었다.

맞다.

그는 매종학과의 마지막 일전에 대해 천주에게 거짓으로 보고했다.

난생처음이자 마지막으로.

그럴 수밖에 없었던 이유?

간단했다.

분했고, 또 한편으로는 두려웠다.

만약 자신이 처음부터 매종학의 정체를 알았다면, 그의 출현을 미리 대비하고 힘을 아꼈더라면 삼 합도 채 버티지 못하고 팔이 잘려 나가진 않았을 테니까.

그리고 이러한 사실을 한 치의 가감 없이 고한다면, 신처럼 믿고 따르는 주인에게 버려질 수도 있을 테니까.

‘하지만 그분께서는 나를 믿어 주셨다. 그것으로 된 거야.’

혈주는 조용히 마음을 가라앉혔다.

대술사가 눈앞에서 뭐라 지껄이건 상관없다.

진정으로 그를 믿었건, 혹은 알면서도 모른 척했건 간에 천주는 그 일을 문제 삼지 않았고 그것은 앞으로도 마찬가지일 테니.

“그쯤 해 둬. 자꾸 그러면 네년의 머리통을 날려 버리고 싶어지거든.”

완전히 평정심을 되찾은 혈주의 경고에 대술사가 어깨를 으쓱해 보였다.

“그럴 만한 능력이 있을지는 의문이지만, 관두자. 큰일을 앞두고 괜히 힘 빼긴 싫으니까.”

혈주는 말없이 고개를 끄덕였다.

전생에서부터 이어진 견원지간처럼 쉴 틈 없이 서로를 향해 으르렁거렸던 두 사람이었지만, 주인에게 받은 임무를 완수하는 것은 그 어떤 것보다 중요했다.

“네년도 짐작했겠지만, 현재로서는 중원(中原)도 청해성의 일에 관여할 수 없을 거다.”

녹림맹과 장강수로맹의 서진(西進)은 지금 이 순간에도 계속되고 있는 상황.

물론 중원의 힘을 한데 끌어모은 무림맹이 전력을 발휘한다면 단숨에 허물어지겠지만, 이동진(移動陳)이라는 족쇄를 채운 이상 무거운 발걸음을 떼기란 쉽지 않다.

아니, 쉽지 않은 것을 넘어 불가능에 가깝다.

청해성을 구원할 정도의 병력을 차출한다는 것은, 그만큼 중원이라는 단단한 벽에 금이 간다는 뜻이니까.

“청해성을 구하고자 한다면 중원의 방비가 허술해지고, 방비를 위해서는 청해성을 버려야 하는 상황이라.”

다시금 웃음을 되찾은 혈주가 말을 이었다.

“그간 중원의 도적놈들에게 공을 들인 보람이 있군. 이거야말로 완벽한 외통수지. 안 그래?”

하지만 그런 그와 달리, 면사 아래로 드러난 대술사의 입꼬리는 미동조차 하지 않았다.

“물론 알고 있어. 그래서 더 아쉬운 거고.”

“아쉬워야 할 이유가 있나? 머지않아 놈들이 집결해 있는 서녕(西寧)이 앞뒤로 포위당하는 건 시간문제일 텐데.”

“그게 전부야?”

“청해성을 완전히 손에 넣고, 추후 명령에 따라 가능하다면 진태경의 신병을 확보한다. 그게 그분의 지시 사항이 아니었나?”

혈주의 반문에 대술사가 헛웃음을 흘렸다.

“아까 했던 말, 취소해야겠네. 아직도 멍청한 건 똑같구나.”

“뭐?”

“아직도 모르겠어? 만약 이번에 무림맹이 움직였다면 우리는 중원 무림을, 아니 그분께서 원하시는 전부를 얻을 수도 있었다는 걸.”

촘촘한 면사 너머로 보이는 혈주를 똑바로 응시하며, 대술사는 나직이 덧붙였다.

“천하(天下)를.”

“……!”

“넌 결정을 내리기에 앞서 내게 상의해야 했어. 단 두 번밖에 쓸 수 없는 귀한 마법진(魔法陳)을 고작 그런 것에 쓰다니.”

우우웅.

서늘한 목소리를 따라 요동치는 기운.

지금 이 순간, 대술사는 진심으로 분노하고 있었다.

자신과 한 마디 논의조차 거치지 않고 병력을 대거 이동시킨 혈주의 어리석음에.

그로 인해 암천이 오랜 시간에 걸쳐 천하 곳곳에 설치해 두었던 수십여 개의 마법진을 허비하고, 천하를 손에 넣을 절호의 기회를 놓쳤음에.

하지만 분노하는 그녀의 모습에도, 혈주의 입가에 맺힌 미소는 사라지지 않았다.

아니, 오히려 더욱 짙어지기까지 했다.

‘뭐지?’

대술사가 뒤늦게 이상함을 느낀 순간, 혈주가 조소 어린 목소리로 툭 내뱉었다.

“네년이 방금 했던 말, 다시 한번 취소해야 할 것 같군. 내가 그 정도로 멍청해 보였나?”

“그게 무슨.”

“장강과 녹림. 그 비루먹은 도적놈들은 처음부터 미끼로 쓰기 위해 포섭한 것뿐. 그런 미끼 따위에 정성을 다할 생각 따위는 애초에 없었어.”

그 말에 담긴 의미를 알아챈 대술사의 눈이 크게 뜨였다.

“그렇다면 혹시…….”

“그래. 어디까지나 보여 주기 위함이었지. 동시에 한편으로는 설마 하는 마음도 있었어. 중원 놈들이 어지간히 병신이 아닌 이상 마법진의 존재는 예전부터 줄곧 경계하고 있었을 테니까.”

그렇기에 실험이 필요했다.

암천의 술사들이 천하 각지에 은밀히 설치해 놓은 수십여 개의 마법진이 아직 발각되지는 않았는지.

그렇다면 아직 제대로 작동하는지에 대한 실험이.

“그리고, 이번 기회를 통해 정확히 알 수 있었지.”

결과는 성공이었다.

도합 일만에 달하는 암천의 교도(敎道)들이 마법진으로 중원으로 넘어가 녹림맹과 장강수로맹에 합류했고, 혈주는 조금 전에서야 그 사실을 전해 들었다.

지금까지도 감히 고개를 들지 못하고 있는, 눈앞의 전령을 통해서.

“완벽해. 아쉽게도 소림을 칠 당시에 쓰였던 마법진 두어 개는 효력을 상실했겠지만, 대부분의 마법진은 아직 한 번의 기회가 남아 있지.”

어느샌가 입을 굳게 다문 채 이야기를 듣고 있던 대술사가 문득 중얼거렸다.

“충분해. 그 정도라면.”

현재 암천이 가진 전력을 모두 동원할 필요도 없다.

일거에 수만에 달하는 군세를 중원의 심장부에 떨어트려 주요 문파를 허물어트린다면, 단 한 번의 대전(大戰)만으로도 천하를 얻을 수 있을 테니.

그러나 이 정도만으로 모든 분노를 가라앉힐 수는 없다.

대술사는 꿰뚫어 보는 듯한 눈빛으로 혈주를 응시했다.

“이유도, 명분도 알겠어. 하지만 이것으로는 부족해.”

“어째서?”

“아직 마법진을 발동시킬 그 마지막 기회가 남았지만, 그로 인해 놈들은 우리를 더욱더 경계하고 있을 테니까.”

“아니, 그 반대겠지.”

“뭐?”

“도적놈들이 사방에서 날뛰기 시작하는데, 우리가 아무런 도움이나 수를 쓰지 않는다면 그게 오히려 더 이상한 게 아닐까?”

“……!”

“어차피 해야만 하는 일이었다. 언제 다시 마음을 바꿔먹을지도 모를 두 도적 떼들을 감시하기 위해서라도.”

한 번 배신할 수 있다는 것은, 두 번 세 번도 가능하다는 뜻.

앞서 보낸 암천의 교도 일만은 바로 그 배신을 막기 위한 억제제이기도 했다.

혹여 녹림맹과 장강수로맹이 다른 마음을 품을 수 없도록.

그럴 엄두조차 낼 수 없도록 만드는 또 다른 족쇄.

“어떻게 흘러가도 우리에게는 나쁠 것이 없지.”

혈주는 자리에서 일어나며 말을 이어 갔다.

“만약 죄책감을 이기지 못한 중원의 의협지사들께서 자리를 떨치고 일어난다면, 마법진이 빛을 발할 것이고.”

저벅. 저벅.

천천히 울려 퍼지는 발걸음 소리를 따라, 그의 목소리가 흩어졌다.

“설령 그대로 자리를 지킨다면, 청해성을 넘어 중원으로 향한다.”

그그긍.

혈주가 내뻗은 손을 따라, 육중한 철문이 열렸다.

그리고 그 아래, 새카맣게 산맥을 물들이는 수많은 군세가 있었다.

“군을 일으켜라. 서녕으로 간다.”
```

## Final English reading copy

```markdown
# Chapter 1087

While Zhuge Feng gazed west with an earnest wish in his eyes, a low laugh rang out from the highest peak in the western lands.

“Good. This is how it should be. It has to be.”

At the Blood Lord’s smiling nod, the messenger who had just finished his report felt a quiet sense of relief.

He had brought news good enough to satisfy his master.

And, unlike his comrades, who had already become cold corpses one after another, he wouldn’t be killed by the violent man in front of him.

But it was too soon to feel safe.

This hour wasn’t over yet.

“So they’re all just watching carefully and waiting to see what happens?”

At the Blood Lord’s question, the messenger lowered himself further, prostrating himself before he answered.

“That is correct. The Nine Sects and One Gang and the Five Great Families are watching the situation and strengthening their defenses, but they have made no further moves.”

“They used to praise one another as chivalrous heroes, but now that the moment has come, they’re scared stiff.”

The Blood Lord’s smile deepened. Then a clear voice rang out from somewhere.

“Better a coward than an idiot like you. Don’t you think?”

The Blood Lord frowned without meaning to when he saw who had spoken, but soon answered in a leisurely tone.

“Couldn’t agree more. Stupidity leads straight to incompetence. That must be why he entrusted this plan to me.”

“And what about taking the sorcerers under my command and starting this without my permission?”

“Since I was entrusted with everything happening in Qinghai, why would I need to consult a mere defeated general?”

The Grand Mage smiled coldly at the reminder of her failure in Gansu.

“Your eloquence has certainly improved. Last time, was it your head that got cut off instead of your arm? I suppose I should praise you for getting a little smarter.”

For an instant, the smile on the Blood Lord’s lips faded.

Ever since Sword Saint Mae Jonghak’s strike had taken one of his arms during the incident the Central Plains Murim called the Shaolin Bloodshed, it had become a sore point he could not bear to have touched.

*That damned woman.*

Of course, he had accomplished his mission well enough.

He had stolen the Green Jade Buddha Staff, the most important prize, and killed countless Shaolin Temple martial monks, including the Abbot, Hong Dao, dealing the temple a devastating blow.

But despite the success, the wound to his pride from how it had all happened showed no sign of healing.

Even remembering that violet Sword Force sent a chill through him. The place it had severed still throbbed, even now that a new arm was in place.

And he still carried his anger toward one reckless young pup who had stood against him to the very end, without the slightest fear.

“Shut your mouth, bitch. You weren’t even there, so you’ve got no right to run your mouth about it.”

The Blood Lord’s voice sank low. The Grand Mage gave him a faint smile.

“Right. That’s what I regret most.”

“What?”

“If I’d been there, you never could’ve come out with that nonsense about losing after fighting the Sword Saint for hundreds of exchanges.”

“……!”

“Be honest. After a life-and-death duel with the Fire King—that violent old man—you fought the Sword Saint for hundreds of exchanges? Quite a nerve you have. How dare you lie to him?”

“You’re imagining things. I’ve always told him the truth.”

The Blood Lord replied as calmly as he could, but he knew better than anyone that the Grand Mage was right.

It was true.

He had lied to the Lord of Heaven about his final fight with Mae Jonghak.

The first time he had ever lied—and the last.

Why?

It was simple.

He had been furious, and afraid.

If he had known Mae Jonghak’s identity from the start, and had conserved his strength in preparation for his arrival, he wouldn’t have lost his arm before he could even last three exchanges.

And if he had reported everything without leaving out a single detail, the master he trusted and worshiped like a god might have cast him aside.

*But he believed in me. That’s enough.*

The Blood Lord quietly settled his thoughts.

It didn’t matter what the Grand Mage said to his face.

Whether the Lord of Heaven truly believed him or had simply pretended not to know, he had made no issue of it—and he never would.

“Enough. Keep this up and I’ll want to blow your head off.”

At the Blood Lord’s warning, his composure now restored, the Grand Mage shrugged.

“I doubt you could, but let’s leave it there. We have important work ahead. I don’t want to waste my strength.”

The Blood Lord nodded without a word.

The two of them had snarled at each other without pause, like sworn enemies from a past life. But carrying out the mission their master had given them mattered more than anything else.

“As you’ve probably guessed, the Central Plains won’t be able to interfere in Qinghai’s affairs for now.”

The Green Forest Alliance and the Yangtze River Channel League were still pushing west even as they spoke.

Of course, if the Murim Alliance brought all the Central Plains’ strength together and committed its full forces, it could crush them in an instant. But now that the Moving Formations had shackled them, taking that heavy first step would be difficult.

No—not just difficult. It was close to impossible.

Sending enough troops to save Qinghai would mean cracking the solid wall of the Central Plains.

“So if they want to save Qinghai, the Central Plains’ defenses will be left exposed. And if they want to protect the Central Plains, they have to abandon Qinghai.”

The Blood Lord’s smile returned as he continued.

“Looks like all that effort we put into those Central Plains bandits has paid off. A perfect checkmate, wouldn’t you say?”

Unlike him, the Grand Mage’s lips did not move beneath her veil.

“Of course I know. That’s why I regret it even more.”

“Why regret it? It’s only a matter of time before Xining, where they’ve gathered, is surrounded from both sides.”

“Is that all?”

“Take complete control of Qinghai, then, if possible, secure Jin Taekyung according to further orders. Wasn’t that what he instructed?”

The Grand Mage let out a hollow laugh at the Blood Lord’s question.

“I take back what I said earlier. You’re still just as stupid.”

“What?”

“Don’t you understand? If the Murim Alliance had moved this time, we could have taken the Central Plains Murim—or even everything he wants.”

The Grand Mage stared straight at the Blood Lord through her fine veil and added quietly,

“The whole world.”

“……!”

“You should have consulted me before making your decision. To waste those precious magic formations, each usable only twice, on something like this…”

A low hum.

Qi surged in time with her cold voice.

At that moment, the Grand Mage was truly furious.

Furious that the Blood Lord had moved so many troops without so much as a word of discussion with her.

That he had wasted the dozens of magic formations Dark Heaven had planted throughout the world over a long period—and missed a golden opportunity to take the world.

Yet even as she seethed, the smile on the Blood Lord’s lips did not disappear.

If anything, it grew even broader.

*What?*

The Grand Mage only realized something was wrong a moment too late. The Blood Lord tossed out a scornful reply.

“I think you need to take back what you just said. Did you really think I was that stupid?”

“What are you talking about?”

“The Yangtze and the Green Forest. Those mangy bandits were recruited as bait from the very beginning. I never intended to waste real effort on bait like that.”

The Grand Mage’s eyes widened as she grasped what he meant.

“Then perhaps…”

“That’s right. It was all for show. At the same time, I thought there was a chance it might work. The people of the Central Plains must have been keeping a close watch for magic formations for a long time, unless they were complete idiots.”

That was why they needed to test them.

Had the dozens of magic formations Dark Heaven’s sorcerers secretly set up throughout the world been discovered?

And if not, were they still working properly?

“And now we know for certain.”

The test had succeeded.

A total of ten thousand Dark Heaven faithful had crossed into the Central Plains through the magic formations and joined the Green Forest Alliance and the Yangtze River Channel League. The Blood Lord had only just received the news.

From the messenger still unable to raise his head in front of them.

“Perfect. Unfortunately, two or three of the magic formations used when we attacked Shaolin may have lost their power, but most still have one use left.”

The Grand Mage had fallen silent and was listening closely. Now she murmured,

“That’s enough. With that much…”

They wouldn’t need to bring all of Dark Heaven’s forces into play.

They could drop tens of thousands of troops into the heart of the Central Plains all at once and bring down its major sects. A single great war would be enough to conquer the world.

But that alone could not quell all her anger.

The Grand Mage looked at the Blood Lord with a piercing gaze.

“I understand your reasons. I understand the justification. But it’s not enough.”

“Why not?”

“We still have that final chance to activate a magic formation. But now they’ll be even more wary of us because of it.”

“No. It’s the other way around.”

“What?”

“When bandits start rampaging all around them, wouldn’t it be stranger if we did nothing to help or intervene?”

“……!”

“It was something we had to do anyway. We need to keep watch over those two bandit gangs, in case they change their minds again.”

If they could betray them once, they could do it twice or three times.

The ten thousand Dark Heaven faithful sent ahead were also a deterrent against that betrayal.

Another shackle, to keep the Green Forest Alliance and the Yangtze River Channel League from entertaining other ideas.

To make sure they wouldn’t even dare.

“No matter what happens, it won’t hurt us.”

The Blood Lord rose to his feet and continued,

“If the Central Plains’ chivalrous heroes can’t bear their guilt and rise from their seats, the magic formations will come into play.”

Step. Step.

His voice scattered as his footsteps rang out slowly.

“And if they stay where they are, we’ll pass through Qinghai and head into the Central Plains.”

Rumble.

At the Blood Lord’s gesture, the massive iron doors swung open.

Below them lay countless troops, blackening the mountain range.

“Raise the army. We march on Xining.”
```
