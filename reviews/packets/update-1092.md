<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1092.txt",
      "sha256": "8eaa540b548a6711fa91de926576acb9559c89ea63dd3246ce8b5427bc38eedb",
      "bytes": 11909
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e2aaadcde26bd79e264728e5221aa5e748c17952fb34a5c1516e55ca961db6fe",
      "bytes": 1767
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bee69e076364377f31e7856d6f9b353d3362d24e22138f2ec1d79723928adc10",
      "bytes": 243843
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "6a19ca496f3c32de6845c0b901a72372648622bf3e555a907bb1829567548ccf",
      "bytes": 916
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "2bfd7fd97d7ef5556cce81ad4348dc15879dc46ebaafadfdbea3f586f5684e58",
      "bytes": 760
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "4d19deaccca711aeff0599c06db05f627829b5bc45edd184d9fcf2c77820e2c8",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c0eb5e4e81662a3149e7d27bf0f558cbddbc7a88c759145d73ce3e3670f0deef",
      "bytes": 623
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "365b1f4c159472d85c3f763da0f4434bd756727b976c37d88a409afd3812009a",
      "bytes": 1084
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "c176ab8671e85d4501c7648b4a26928dc391132b44c98636cf568c9052c8daaf",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ebe79c16d6adf08cf85ebe92be4ce390014b7513b9c2f13e94caedd0cd180dd5",
      "bytes": 287086
    }
  ],
  "estimated_tokens": 10104
}
-->

# Durable State Update — Chapter 1092

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
1 and safe_through 1092. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1092. Profile updates may replace only one
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
  "chapter": 1092,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1092,
    "continuity_sources": [1092],
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
    "Dark Heaven’s army has arrived at Xining, with the Blood Lord at its head.",
    "The Blood Lord’s forces crossed Qinghai Lake using Blizzard, and the Grand Mage is with them.",
    "The Blood Lord released a Beggars’ Sect captive to carry his threat to destroy Xining; the messenger died upon arrival.",
    "Nearly thirty Beggars’ Sect disciples remained across Qinghai Lake; only the messenger returned to Xining.",
    "Jin Taekyung has chosen to remain in Xining and defend its civilians against the approaching forces.",
    "Jeok Cheongang supports Taekyung’s decision and intends to put his remaining strength to use.",
    "Most hidden magic formations retain one use; two or three used in the Shaolin attack may be spent.",
    "Mae Jonghak and the New Murim Alliance prepared an operation against Dark Heaven; Zhuge Feng has its intelligence and tasking to execute it.",
    "The Zhuge Clan left its ancestral home and fled to Mount Wudang.",
    "Jin Taekyung, Jeok Cheongang, and the Slaughter Saint left Xining’s wall to confront the Blood Lord; the fight has begun.",
    "Jeok Cheongang tells Taekyung that facing fear and caring about others’ pain are part of becoming a hero."
  ],
  "continuity_sources": [
    1090,
    1091
  ],
  "open_questions": [
    "What is the black-robed captive in Qinghai’s identity and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "What will happen in the confrontation with the Blood Lord?"
  ],
  "safe_through": 1091,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 매종학    | **Mae Jonghak**    |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 살성     | **Slaughter Saint**           | —              |
| 소림     | **Shaolin**                      |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 일격     | **One Strike**                         |
| 몬스터     | **monster**           |
| 귀가      | **your family**                                                 |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 여의주 | **dragon pearl** | Legendary treasure requested by Jang Taebo. |
| 이형환위 | **Shifting Form and Position** | Supreme Peak movement or evasion technique used by Jeok Cheongang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 잠룡 | **Hidden Dragon** | Epithet or metaphor for Jin Taekyung. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 수공 | **water arts** | Water-based martial arts; the Dongting Fisherman's specialty. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 매종학 | 혈주 | legendary_martial_master_to_enemy | you | cold and judgmental | After revealing himself, Mae Jonghak condemns the Blood Lord's accumulated sins and orders him to pay the price. |
| 혈주 | 매종학 | enemy_to_revealed_legendary_master | you | shocked and hostile | The Blood Lord addresses Mae Jonghak with 당신 immediately after recognizing him as the Sword Saint. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1091
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; strategically manipulates allies and adversaries, and conceals failures from the Lord of Heaven when he fears being discarded.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1088
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1091
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1091
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1087
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1090
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
1092화




무림인에게 있어 기파(氣波)란 곧 힘의 발산이다.

그렇기에 진태경은 그 어느 때보다 선명하게 느낄 수 있었다.

혈주가, 눈앞의 적이 얼마나 무시무시한 무위를 지니고 있는지.

우우웅.

강력한 기파의 영향으로 쉽사리 가라앉지 못하는 공기.

그러나 사방에서 전해지는 그 잔 떨림과는 달리, 진태경의 마음은 되려 차분하게 가라앉았다.

차갑게 타오르는 혈주의 음성과 시선 앞에서도, 담담하게 대답할 수 있을 정도로.

“그때와 똑같군. 그 빌어먹을 혓바닥은.”

진태경은 입가에 맺혀 있던 미소를 지웠다. 동시에 자신이 백염(白炎)이라 이름 붙인 애병을 들어 혈주를 향해 겨누었다.

“그때와는 다를 거야. 그 외의 모든 것이.”

“다르다고? 푸핫.”

이번에는 혈주가 웃을 차례다. 그는 조소 어린 눈빛으로 진태경을 응시했다.

“잠룡에서 신룡이 되었다더니, 이제는 숫제 여의주라도 얻은 것처럼 구는군. 네놈이 아무리 발악을 해 봤자 아직 나한테는 안 돼. 스스로도 알 텐데?”

그리고 혈주의 예상과는 달리, 진태경은 순순히 고개를 끄덕이며 답했다.

“그래, 아마 그렇겠지.”

“뭐?”

“반응이 왜 그래? 이렇게 솔직하게 인정해 줬으면 조금은 기뻐해야 하는 거 아냐?”

“……너.”

착 가라앉은 혈주의 음성이 이어지려던 그때, 진태경이 한발 앞서 입을 열었다.

“보자마자 알겠더라고. 네 수준이 어느 정도인지 정확히 가늠할 수 없었으니까.”

길가에 굴러다니는 돌멩이도 그 크기와 형태가 제각각일진대, 구름에 닿은 태산이라고 한들 높낮이의 차이가 없을까.

더군다나 무림이라는 세상의 가장 밑바닥에서부터 초절정이라는 태산까지 도달한 진태경이었기에, 혈주를 대면한 그 순간 즉각 깨달을 수 있었다.

“넌 나보다 강해. 확실히.”

혈주와의 격차가 정확히 어느 정도인지는 모른다.

다만 그 격차가 설령 일초 반식이라 할지라도, 혈주가 더 강자라는 사실을 진태경은 인정하고 받아들였다.

그와 더불어 문득 떠올렸다.

절대적이라고 느껴질 만큼 강대한 힘 앞에 한낱 개미처럼 짓밟힐 수밖에 없었던, 그리 오래되지 않은 과거의 자신을.

마치 구름 위의 존재처럼 아득하게만 느껴졌던 혈주의 모습을.

“그런데, 그거 아냐?”

진태경은 나직한 물음과 함께 혈주를 응시했다.

그의 눈앞에서 과거와 현재가 겹쳐진다. 자신보다 혈주가 강하다는 사실과 함께 찾아온 또 하나의 깨달음이 전류처럼 등줄기를 타고 흐른다.

“그때는 아무리 죽을 힘을 다해도 네 털끝 하나 건드리지 못할 것 같았는데…….”

흐려지는 말꼬리와 함께, 진태경은 웃었다.

오늘에서야 비로소 알았다.

단지 마주하는 것만으로도 숨이 막혀왔던 기억 속의 혈주가, 더 이상 구름 위의 존재가 아니라는 것을.

“지금은 손만 뻗으면 닿을 것 같네.”

“……!”

혈주가 눈을 부릅뜬 그 순간, 십여 장 밖에 우뚝 서 있던 진태경의 신형이 아지랑이처럼 일렁였다.

팟.

형태는 남았으나 실체가 없고, 기척조차 없으나 그 안의 살의(殺意)는 선명하다.

쏴아아악.

바람이 울부짖는 듯한 그 소름끼치는 소리를, 혈주는 똑똑히 들었다.

동시에 보았다.

거대한 압력에 의해 일그러지는 공간 속.

극의에 다다른 이형환위(移形換位)와 함께, 소리를 앞질러간 창날이 압축된 공기를 찢어발기는 광경을.

“진태경-!”

그리고 그 순간.

콰아아아!

혈주의 창노한 외침과 먹먹한 파공성이, 핏빛 섬광과 검푸른 파도가 맞닿고 뒤섞여 온 사방을 뒤덮었다.



* * *



일합(一合).

단 일 합으로 충분했다.

지금 이 순간, 혈주와 나의 격차를 깨닫기에는.

콰드드득!

벼락처럼 휘둘려진 혈주의 적도(赤刀)와 백염의 창날이 맞물리며 터져 나온 굉음은 이미 날붙이가 낼 수 있는 종류의 것이 아니었다.

그로 인한 충격파 역시도.

구구구궁!

단단한 지면이 거미줄처럼 갈라진다. 힘을 이기지 못하고 밀려 나가는 내 발끝을 따라 모든 것이 먼지처럼 바스라지고 있었다.

“감히, 고작 이 정도로 혀를 놀린 거냐.”

서로를 향해 교차된 병장기 너머, 분노로 들끓는 목소리와 함께 핏빛 안광이 번뜩인다.

손에 만져질 것만 같은 살기와 끔찍하리만치 거대한 기운.

‘강하다.’

새삼 놀라웠다. 동시에 또 다른 사실을 깨달았다.

길다면 길고, 짧다면 짧다고 할 수 있는 지난 일 년의 시간 동안 강해진 것은 혈주 역시 마찬가지였다는 것을.

‘나보다 최소 반 수. 아니, 한 수 위.’

초절정의 영역에서 한 수의 차이는 너무나도 크다. 

그러나 내가 새삼 놀랄 수밖에 없었던 이유는, 혈주의 강함이 비단 무공의 깨달음과 공력의 크기만으로 국한할 수 없기 때문이었다.

그그극.

서서히, 아니 그보다 빠르게 밀리기 시작하는 창날.

그 너머에는 핏빛 강기가 없이도 번뜩이는 붉은색의 도신과, 실핏줄이 한껏 도드라진 채 엄청난 근력을 쥐어 짜내는 근육질의 팔이 있었다.

‘이건……인간의 힘이 아니야.’

본능적으로 느낄 수 있었다. 

지난 수년 간 인간이 아닌 괴물들만을 상대해 왔던 나였기에, 더더욱 그럴 수밖에 없었다.

지금 이 순간, 혈주가 발산하는 신체 능력은 인간의 한계를 아득히 벗어났다.

아니, 그 이상이다.

충돌의 여파로 인해 찢어진 의복 사이로 보이는 놈의 살갗만 보아도, 지난 일 년간 무슨 짓을 벌였는지 충분히 짐작하고도 남음이었다.

“의수(義手)치고는 특이한데.”

시시각각 밀어붙여 오는 거대한 힘을 전력을 다해 막아 내며, 나는 침잠하게 가라앉은 눈빛으로 혈주를 응시했다.

정확히는, 비정상적으로 크게 부풀어 오른 놈의 팔과 마치 꿰맨 듯한 자국을.

그리고 그런 나를 향해, 혈주는 이빨을 드러내며 으르렁거렸다.

“모든 것이 그분의 은총 덕분이지.”

소림혈사 당시, 검성 매종학에 의해 한쪽 팔을 잃고 도주했던 혈주다. 

남은 일평생을 외팔이로 살아야 했을 놈이 두 팔을 달고 멀쩡히 나타났다는 것은, 동시에 이 정도의 힘을 발휘한다는 것은 한 가지 사실을 의미했다.

“그렇게라도 강해지고 싶었나? 괴물과 뒤섞이면서까지?”

“……!”

“하긴, 나는 몰라도 검성에게 복수하려면 뭐라도 떼서 붙여야 했겠지. 안 그래?”

“……너.”

내 한 마디에 정곡을 찔려서일까. 아니면 너무나도 쉽게 그 실체를 파악해서일까.

부릅떠진 눈으로 나를 노려보던 혈주가 이를 악물었다.

“기대되는군. 네놈이 죽어서도 그 혓바닥을 놀릴 수 있는지.”

그 순간.

콰득, 콰아앙!

고목나무의 몸통처럼 한층 크게 부풀어 오른 팔뚝이, 몬스터의 그것이 틀림없는 거대한 힘이 창날을 쳐올렸다.

텅!

세 자릿수에 접어든 지 오래인 내 근력 수치로도 감당할 수 없는 엄청난 힘과 공력이 창대를 허공으로 튕겨낸다. 

손아귀가 찢어진 채, 순식간에 적수공권(赤手空拳)이 되어 버린 나를 향해 혈주의 적도가 눈부신 궤적을 그렸다.

쐐애애액! 쾅!

투박하고 거칠지만, 그 무엇이든 부수고 조각낼 수 있는 일격이 벼락처럼 연이어 공간을 가른다.

쉼 없이 움직이는 내 발끝을 따라 휘둘러지고, 그 끝에 실린 핏빛 강기가 채찍처럼 휘어졌다.

쉬릭, 서걱!

일순간 전신의 솜털이 곤두선다. 아슬아슬하게 머리카락을 잘라내며 스쳐 지나간 강기가 지면을 강타했다.

콰앙! 드드드득!

강기에 실린 거대한 힘을 이기지 못하고, 지진이라도 일어난 것처럼 요동치는 대지.

그러나 반경 수십여 장을 뒤덮으며 자욱하게 일어난 먼지구름 따위로는, 혈주의 시야를 가릴 수 없었다.

“고작! 고작 이 정도로!”

슈확!

세찬 파공성과 함께 먼지 구름이 갈라진다. 태곳적 거인이 휘두른 도끼처럼 내리꽂히는 핏빛 강기를 피해, 나는 본능처럼 옆으로 몸을 날렸다.

서걱!

힘없이 반으로 쪼개진 땅이 칠흑처럼 새까만 아가리를 벌렸다. 

늦지 않게 몸을 날린 덕분에 앞서의 일격은 피했으나, 그 풍압(風壓)만으로도 피투성이가 된 나를 본 혈주의 입가에 조소가 맺혔다.

“나려타곤(懶驢打滾)이라. 못 본 새에 신룡이 되었다기에 기대했는데, 웬 게으른 당나귀 한 마리가 굴러다니는군.”

무림인들, 그중에서도 특히 긍지 높은 고수들에게 있어 나려타곤은 치욕 그 자체다.

천하에서 방귀 좀 뀐다는 사람치고, 흙투성이가 되어 굴러다니는 모습을 보이는 것이 썩 달가운 일은 아니니까.

하지만 나는 그런 것 따위는 조금도 신경 쓰지 않았다.

최하급 던전에서 코볼트 따위가 쏘아 대는 독침이 무서워서 축축한 동굴 바닥과 한 몸이 되고, 거리가 좁혀져 창을 쓸 수 없을 때는 눈 찌르기와 박치기도 서슴치 않았던 나다.

아직까지도 완결이 나지 않은 어느 해적 만화의 캐릭터는 등의 상처가 검사의 수치라고 말했지만, 나는 그 말에 조금도 동의하지 않는다.

“등의 상처는, 그냥 존나게 아픈 법이지. 수치는 살아 있을 때나 느낄 수 있는 거고.”

“뭐?”

불현듯 멈춘 발걸음.

이게 무슨 뜬금없는 헛소리냐고 묻는 듯한 혈주의 표정에, 나는 뻐근한 몸을 일으켜 세우며 말을 이었다.

“헛소리 맞으니까 자꾸 눈 크게 뜨지 마라. 귀여워서 깨물어 죽여 버리고 싶네.”

“이런 개……!”

“그리고 시발아. 내가 용이든 당나귀든 뭔 상관이야? 어디서 뭔 듣도 보도 못한 괴물 팔다리나 뜯어 와서 붙인 새끼가.”

“……!”

묵직한 팩트리어트 미사일이 가장 아픈 법.

으득.

어금니가 부서지도록 이를 악문 혈주가 다시금 걸음을 뗐다.

아니, 떼려고 했다.

더욱 짙어진 살기가 실린 적도와 핏빛 강기가 꿈틀거리던 그때, 줄곧 마비되어 있던 놈의 이성을 일깨우는 거대한 폭음(爆音)이 들려오지 않았다면 분명 그러했을 것이다.

꽈아아앙!

온 사방을 떨어 울리는 폭음의 진원지는 놈의 등 뒤였다.

그리고 일백여 장이나 나를 뒤쫓으며 공격을 쏟아부은 혈주의 공백을 채운 것은, 다름 아닌 화왕과 살성이라는 두 거인이었다.

콰드득, 퍼엉!

곳곳에서 불길이 솟구치고, 피 분수가 쉴 틈 없이 뿜어져 나온다.

그제야 돌아가는 상황을 눈치챈 혈주가 나를 향해 핏빛 안광을 쏘아 보냈지만, 나는 아랑곳하지 않고 어깨를 으쓱해 보였다.

“격장지계야. 뻔하디뻔한.”

“놈……!”

“아, 전적으로 내가 한 말은 아니고. 조금 전에 누가 비슷한 말을 했었지.”

그 순간.

쉬이이잉!

어느덧 가까워진 성벽 위에서, 한 줄기 벼락과도 같은 섬광이 희뿌연 먼지구름을 관통하며 내리꽂혔다.

콰아아앙!
```

## Final English reading copy

```markdown
# Chapter 1092

To a martial artist, a wave of qi was the outward release of power.

That was why Jin Taekyung could feel it more clearly than ever.

Just how terrifyingly skilled the Blood Lord—his enemy standing right before him—was.

Rumble.

The air refused to settle under the influence of that powerful wave of qi.

But unlike the faint tremors reaching him from every direction, Jin Taekyung’s heart sank into an even calmer stillness.

Calm enough to answer evenly, even beneath the Blood Lord’s cold, burning voice and gaze.

“You’re just the same as before. That damned mouth of yours.”

Jin Taekyung’s smile faded. At the same time, he raised his beloved spear, which he had named White Flame, and pointed it at the Blood Lord.

“This time will be different. Everything else will be.”

“Different? Puhaha.”

This time, it was the Blood Lord’s turn to laugh. He stared at Jin Taekyung with a mocking gaze.

“I heard you went from Hidden Dragon to Divine Dragon, but now you act like you’ve gotten your hands on a dragon pearl, too. No matter how hard you struggle, you’re still no match for me. You know that yourself, don’t you?”

Contrary to the Blood Lord’s expectations, Jin Taekyung answered with an easy nod.

“Yeah. Probably.”

“What?”

“Why the reaction? Shouldn’t you be a little happy I admitted it so honestly?”

“……You.”

The Blood Lord’s voice was sinking into a low growl when Jin Taekyung spoke first.

“I knew as soon as I saw you. I couldn’t get an exact measure of your strength.”

Even stones rolling along the roadside came in all shapes and sizes. So why should a towering mountain reaching the clouds have no difference in height?

And because Jin Taekyung had climbed from the very bottom of the Murim to the peak of Supreme Peak, he’d understood the instant he stood face-to-face with the Blood Lord.

“You’re stronger than me. No question.”

He didn’t know exactly how wide the gap between them was.

But even if the gap was only one move—or half a move, Jin Taekyung accepted that the Blood Lord was the stronger one.

And with that, something suddenly came back to him.

His not-so-distant past, when he’d been no better than an ant, helpless beneath a power so immense it felt absolute.

The Blood Lord, who had seemed impossibly far away, like someone living above the clouds.

“But you know what?”

Jin Taekyung gazed at the Blood Lord as he asked quietly.

The past and present overlapped before his eyes. Along with the knowledge that the Blood Lord was stronger than him, another realization coursed down his spine like an electric current.

“Back then, no matter how hard I fought, I thought I wouldn’t even be able to touch a hair on your head…”

His voice trailed off, and Jin Taekyung smiled.

Only today had he finally realized it.

The Blood Lord in his memory, whose mere presence had left him short of breath, was no longer someone who lived above the clouds.

“Now it feels like I could reach you just by stretching out my hand.”

“……!”

The instant the Blood Lord’s eyes widened, Jin Taekyung’s figure, standing tall over thirty meters away, wavered like a mirage.

Fshh.

His shape remained, but his body was gone. There wasn’t even a trace of his presence, yet the killing intent within it was unmistakable.

Whooosh!

The Blood Lord heard the eerie sound as clearly as if the wind itself were howling.

And at the same time, he saw it.

In the space warped by immense pressure, a spearhead that had outpaced its own sound tore through the compressed air, propelled by Shifting Form and Position at its pinnacle.

“Jin Taekyung!”

And then—

KWA-A-A!

The Blood Lord’s furious shout and the muffled boom of a sonic blast rang out as a blood-red flash clashed with a dark-blue wave, swallowing the world around them.

* * *

One exchange.

A single exchange was enough.

Enough to realize the gap between the Blood Lord and me at that very moment.

KRRRACK!

The Blood Lord’s red saber swung like lightning and locked against White Flame’s spearhead. The resulting boom wasn’t the kind of sound weapons could make.

Neither was the shock wave that followed.

Rumble!

The hard ground cracked like a spiderweb. Everything crumbled to dust beneath my feet as they slid backward, unable to withstand the force.

“Dare to wag that tongue at me when this is all you’ve got?”

Beyond our crossed weapons, blood-red light flashed in his eyes as his voice seethed with fury.

Killing intent I could almost touch. A terrifyingly vast force.

*Strong.*

It was astonishing. At the same time, I realized something else.

The Blood Lord had grown stronger, too, over the past year—which could feel long or short, depending on how you looked at it.

*At least half a move above me. No—a full move.*

At the Supreme Peak level, a single move made an enormous difference.

But the reason I couldn’t help being surprised was that the Blood Lord’s strength couldn’t be measured by his martial enlightenment and internal energy alone.

Grnnnk.

The spearhead began to give way. Slowly—no, faster than that.

Beyond it was a red blade that flashed without any blood-red Force, and a muscular arm, bulging with veins as he squeezed out every ounce of strength.

*This is… not human strength.*

I could feel it by instinct.

I’d spent the past few years fighting monsters rather than humans. How could I not?

At that moment, the physical ability the Blood Lord was unleashing had gone far beyond human limits.

No—beyond even that.

Just looking at the skin exposed through the rips in his clothes was enough to guess what he’d been up to over the past year.

“Unusual, for a prosthetic arm.”

I put everything I had into holding back the immense force pressing in on me, and stared steadily at the Blood Lord.

More precisely, at his arm, swollen to an abnormal size, and the marks on it that looked as if it had been sewn together.

The Blood Lord bared his teeth and growled at me.

“Everything is thanks to his grace.”

During the Shaolin Bloodshed, the Blood Lord had lost an arm to the Sword Saint, Mae Jonghak, and fled.

The fact that he’d shown up in one piece with both arms, when he should have spent the rest of his life one-armed—and that he could wield this kind of strength—meant only one thing.

“Did you want to get stronger that badly? Enough to splice yourself together with a monster?”

“……!”

“Well, forget about me. To get revenge on the Sword Saint, you’d have had to tear something off and stick it on. Right?”

“……You.”

Had I hit a nerve with a single remark? Or had I just figured out what he was so easily?

The Blood Lord glared at me, eyes wide, then clenched his teeth.

“I look forward to seeing whether that mouth of yours can still run after you’re dead.”

At that moment—

Crack—KWA-AANG!

His arm swelled even larger, like the trunk of an old tree. With an immense force that could only belong to a monster, it knocked the spearhead skyward.

Clang!

Even my Strength stat, which had been in triple digits for a long time, couldn’t handle that force and internal energy. They sent the shaft spinning into the air.

My palm split open. In an instant, I was left empty-handed—and the Blood Lord’s red saber drew a dazzling arc toward me.

Whoosh! KWAANG!

Crude and brutal, but capable of breaking and shattering anything, the strike tore through the air like lightning, followed by another.

His saber swung after my feet as they moved without pause, the blood-red Force at its edge bending like a whip.

Whish—slice!

Every hair on my body stood on end. The Force skimmed past, slicing off a few strands of hair before slamming into the ground.

KWAANG! Rrrumble!

The earth shook like an earthquake, unable to withstand the tremendous force carried by the Force.

But even a thick cloud of dust spreading across a radius of hundreds of feet couldn’t block the Blood Lord’s view.

“That’s all! That’s all you’ve got!”

Whoosh!

The dust cloud split beneath a fierce sonic boom. I threw myself to the side on instinct, dodging the blood-red Force plunging down like an axe swung by some ancient giant.

Slice!

The ground split cleanly in two and opened a pitch-black maw.

I’d dodged the strike just in time, but even its backwash had left me covered in blood. The Blood Lord smirked when he saw me.

“Narye tagon.[^1] I’d heard you’d become the Divine Dragon while I was away, so I expected more. Instead, here’s a lazy donkey rolling around on the ground.”

Among martial artists—especially masters with pride to spare—Narye tagon was the height of humiliation.

After all, nobody who thought they were somebody in the martial world wanted to be seen rolling around covered in dirt.

But I didn’t care about any of that.

In low-level dungeons, I’d pressed myself against the damp cave floor because I was afraid of the poison darts fired by kobolds. When an enemy got too close for me to use my spear, I hadn’t hesitated to go for the eyes or head-butt them.

A character in some pirate manga that still hasn’t reached its ending once said that a scar on your back was a swordsman’s shame. I’ve never agreed with that for even a second.

“A wound on your back just fucking hurts. Shame’s something you can only feel while you’re alive.”

“What?”

My feet came to an abrupt stop.

The Blood Lord’s face seemed to ask what the hell I was going on about. I stood up, my body aching, and continued.

“I am talking nonsense, so stop staring at me like that. You’re so cute I want to bite you to death.”

“You little—!”

“And what the fuck does it matter whether I’m a dragon or a donkey? You’re the one who ripped off some monster’s limbs and stuck them onto yourself.”

“……!”

A heavy Patriot missile of a fact was what hurt the most.

Grind.

The Blood Lord clenched his teeth so hard they seemed about to break and started forward again.

Or tried to.

The killing intent thickened, and the blood-red Force stirred around his saber. Then a tremendous explosion rang out, jolting his long-paralyzed reason back to life.

KWA-AANG!

The source of the deafening boom that shook the world around us was behind him.

And the ones who filled the opening left by the Blood Lord, who had chased me for over three hundred meters while unleashing attack after attack, were none other than the two giants—the Fire King and the Slaughter Saint.

Crack—pboom!

Flames shot up all around us, and blood sprayed without pause.

Only then did the Blood Lord grasp what was happening. He shot me a blood-red glare, but I only shrugged.

“A goading strategy. Obvious as can be.”

“You—!”

“Oh, I’m not taking all the credit. Someone said something pretty similar a little while ago.”

At that moment—

Whoooosh!

From the city wall, now much closer, a streak of lightning plunged through the hazy cloud of dust.

KWA-A-AANG!

[^1]: Narye tagon is a humiliating martial arts term for rolling on the ground like a lazy donkey to evade an attack.
```
