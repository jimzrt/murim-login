<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0966.txt",
      "sha256": "05780b7d0b00426ab71d3912d07119610adb971109e07d67b9fb2e14e4dec6df",
      "bytes": 14425
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4f84df9bb60ef3be797e1bd1b2cd50c78bcfae192d94189a5f94c835f84048d8",
      "bytes": 1869
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a9abc25b921cbdce05f090e91781cabe86a577757b8e253bfe7473b3c6a55ce2",
      "bytes": 235304
    },
    {
      "path": "characters/Hanga.md",
      "sha256": "103a04573a58d9fc0d17a48286e190ece836b17abd512ec005b2ecf539110036",
      "bytes": 568
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "ea14bfad2fcd23a59f00e2d006f3fdf1bf5082b7b1de0b3935ff86c8f0057b15",
      "bytes": 1389
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "5793c7c2c9d2d3fe76d6b8f1b3f71bbedadec09a4a1867becd9f09ebebe9991a",
      "bytes": 1116
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "ad3af9e7c78a33285b540476cb15c3f4cdcbd029f69c85c4734cd9040ff87f8e",
      "bytes": 707
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "37e19e0467234b45cbbaae5d189b109838afbd345811992a7e017233f86ec98d",
      "bytes": 269308
    }
  ],
  "estimated_tokens": 10603
}
-->

# Durable State Update — Chapter 966

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
1 and safe_through 966. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 966. Profile updates may replace only one
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
  "chapter": 966,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 966,
    "continuity_sources": [966],
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
    "The Shanxi battle continues; Peng Cheolhu and two thousand Hebei Peng Family fighters have arrived to aid Shanxi.",
    "Cheolhu interrupted Jamukha’s attack on exhausted, wounded Jin Mukyung; their confrontation remains unresolved.",
    "Jin Mukyung refused Jamukha’s offer to spare him and the others in exchange for submission.",
    "Someone anticipated the Hebei Peng Family’s arrival; that person’s identity is unknown.",
    "Jin Wikyung’s fate remains unknown.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment requiring him to die once remains unresolved.",
    "The improved Temporary Strength Pill’s source, effects, and distribution remain unknown; Jang Sam remains unconscious.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin.",
    "Taekyung resolved to trust his allies rather than bear every burden alone."
  ],
  "continuity_sources": [
    965,
    964
  ],
  "open_questions": [
    "Who is the person who anticipated the Hebei Peng Family’s arrival, and how will the battle and Jamukha’s confrontation with Mukyung unfold?",
    "What will become of Jin Wikyung?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?"
  ],
  "safe_through": 965,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 하북팽가   | **Hebei Peng Family**            |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 정마대전   | **Great Faction War**         |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 신병이기 | **divine weapon** | Jin's description of White Flame. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 케식 | **Keshik** | Elite warriors serving the Golden Clan. |
| 검귀 | **Sword Demon** | Title used for the kind of swordsman Mukyung is said to resemble. |
| 마조 | **Demon Bird** | Title given by the revealed impostor who wore Chinggen’s face. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진무경 | 마조 | hostile opponents | you | blunt and insulting | Mukyung directly insults the Demon Bird, refusing to call him Master. |
| 마조 | 진무경 | hostile opponents | you | familiar and blunt, with admiration | Calls him a young Sword Demon and speaks to him with growing respect. |
| 자무카 | 진무경 | hostile opponents | you | familiar, blunt, and patronizing | Jamukha uses 자네 while urging Mukyung to submit and become his hunting dog. |

## Listed compact profiles

### Hanga.md

# Hanga (항아)

- **Safe through:** Chapter 956
- **Aliases:** None
- **Role:** Local village girl, Jang-pal’s daughter, who lives near Jang Taebo and regularly visits him.
- **Personality:** Curious, energetic, observant, and already attentive to the value of information and food.
- **Voice:** Childlike, direct, and inquisitive, with an occasional surprisingly worldly remark.
- **Relationships:** Calls Jang Taebo Grandpa; Jang Taebo is his elderly neighbor and only conversational companion.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 965
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry, refusing to abandon what he believes is right.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, and Mukyung cherishes his promise to reunite with him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 964
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he commits firmly to his principles, even when doing so means remaining in a losing battle.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 965
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed; father of Peng Cheolyeong.

## Korean source

```text
＃966화



서로의 실력이 비등하다는 전제하에, 무인들 간의 생사결(生死決)에 있어 가장 결정적인 요소가 무엇이냐는 것은 강호의 호사가들에게 있어 오랜 화두였다.

그들 중 누군가는 상대보다 수준 높은 공력과 신공절학이라 했고, 다른 누군가는 신병이기의 존재를 첫손가락에 꼽았으며, 혹자는 흔들리지 않은 마음가짐과 뛰어난 신체 능력이라 주장하기도 했다.

그러나 그 모든 의견은 하나 같이 정답인 동시에, 오답이었다.

일정한 경지에 오른 고수들은 안다. 직접 피부로 체감한다.

목숨을 건 생사결에서는 아주 작은, 사소하게까지 느껴지는 차이점 하나가 승패를 가른다는 것을.

그렇기에 입을 모아 이렇게 말하고는 했다.

‘어떤 무공을 익혔는지는 그리 중요하지 않다. 가장 중요한 것은 상대의 움직임을 간파할 수 있는 눈과 감각이다.’

그리고 지금 이 순간, 협곡 안을 가득 메운 모든 이들은 마냥 멀게만 느껴졌던 그 말의 의미를 정확히 깨닫고 있었다.

쐐애애액! 콰앙!

보이지 않는다. 느껴지지도 않는다.

다만 눈앞의 적을 향해 날붙이를 휘두르는 것조차 잠시 잊은 채 멍하니 바라볼 뿐이다.

쉼 없이 터져 나오는 섬광과 굉음 너머, 보이지도 않는 속도로 서로를 향해 얽혀드는 세 인영을.

후웅!

무식하리만치 거대한 대도(大刀)가 공간을 가른다. 그 끝에 실린 막강한 강기가 바람과 함께 자무카의 신형을 찢어발겼다.

아니, 찢어발기는 듯했다.

쉭.

단 한 걸음.

일순간 흐릿해진 자무카의 신형이 일 장 밖에서 나타났다.

그리고 유령과도 같은 움직임을 선보이며 공격을 피해 낸 그가 벽력도왕을 향해 짓쳐 들려던 그때, 희미한 파공성이 보이지 않는 사각(死角) 너머에서 울려 퍼졌다.

솨악.

그 순간 자무카는 새삼 깨달았다.

오늘 이 자리에서 자신이 쓰러트려야 할 적은, 벽력도왕 한 사람뿐만이 아니라는 사실을.

스륵, 쾅!

신월도와 새하얀 검신이 맞닿았다.

협곡 내부를 떨어 울리는 충격파와 굉음 속, 생각지도 못한 충격에 한 걸음을 물러난 자무카의 입가에 미소가 맺혔다.

‘과연, 기대했던 것 이상이군.’

그의 시선은 깊은 고랑을 만들며 밀려난 진무경을 향하고 있었다.

만신창이가 된 몸뚱어리로도 생각지 못한 일격을 쏟아낸, 태원진가의 젊은 검귀를.

더불어 비로소 이해했다.

어떻게 이제 막 초절정의 벽을 넘어선 진무경이, 완숙한 경지에 다다라 있던 마조를 쓰러트릴 수 있었는지.

진무경이 펼치는 검에는 무공의 기본이라 할 수 있는 식(式)도, 형(形)도 없다.

오로지 일격.

상대의 숨통을 끊어 낼 수 있는 가장 빠르고 완벽한 길을 찾아내어 움직일 뿐이다.

그리고 필살(必殺)의 의지를 담은 그 일격은, 진무경 본연의 무위보다도 훨씬 강한 위력을 발휘하고 있었다.

초식 하나로 승부가 결정되는 초절정의 영역에서, 한 수 위의 고수인 마조를 쓰러트릴 만큼.

하지만…….

‘그것도 여기까지다.’

들리지 않을 한 마디와 함께, 자무카는 양팔을 떨쳤다.

그가 일평생 나고 자란 광활한 대초원을 닮은 녹색 강기가 각각 신월도와 비어 있던 한 손을 타고 솟구쳤다.

화아악!

아득하게 부풀어 오르는 섬광 너머, 두 줄기의 강기는 서로 다른 방향을 향해 나아갔다.

하나는 천하를 쪼갤 듯한 기세로 대도를 내리꽂는 벽력도왕을 향해.

또 다른 하나는 비틀거리며 핏물을 삼키고 있던 진무경을 향해.

그리고 그 결과는, 한 사람의 예상을 훌쩍 벗어난 것이었다.

콰드드득!

조금의 흔들림 없이 맞물린 두 개의 도신을 바라보며, 벽력도왕은 눈을 부릅떴다.

‘이 무슨!’

그는 뼛속까지 투사다. 정마대전이라는 거대한 전란 속에서 맹위를 떨치고 살아 있는 전설이 된 오늘날에도 결코 눈앞의 상대를 얕잡아 보지 않는.

한데, 전력을 다한 일격이 가로막혔다.

그것도 아주 손쉽게.

마치 자신이 펼친 무공의 초식과 그 흐름이 간파당한 것처럼.

“네놈이 어찌……!”

의문과 분노가 뒤섞인 음성이 입술을 비집고 흘러나온다.

서로의 몸에 닿지 못한 채 허공에서 맞물린 도신 사이로, 자무카는 담담한 눈빛으로 벽력도왕을 응시했다.

“실망이군. 차라리 까마득한 후배부터 구하지 그랬나, 벽력도왕.”

“……!”

부릅떠져 있던 벽력도왕의 눈동자가 일순간 흔들렸다.

자무카의 어깨너머, 강대한 장력의 힘을 이겨 내지 못하고 무릎을 꿇은 채 토혈하는 진무경의 모습이 뒤늦게 그의 눈에 비치고 있었다.

‘제기랄.’

실수다.

아니, 뼈아픈 오판이었다.

자무카는 그가 생각했던 것 이상으로 강하고, 훨씬 더 깊은 비밀을 품고 있는 강자였다.

쾅!

팽팽한 힘겨루기 끝에 마침내 떨어져 나간 도신이 굉음을 토해 낸다.

강렬한 충격을 흘려보낸 벽력도왕이 자무카를 향해 재차 대도를 내리그었다.

화아악!

타고난 신력(神力)과 수 갑자의 공력이 합쳐진 일격.

하북팽가의 삼남으로 태어난 그를 가주이자 벽력도왕으로 만들어준 가문의 신공절학, 혼원벽력도(混元霹靂刀)가 한 줄기의 벼락이 되어 떨어졌다.

눈앞의 적과 함께, 천하마저 반으로 갈라 버릴 듯한 기세로.

서걱! 콰과과광!

예리한 절삭음과 함께 뒤흔들리는 협곡.

그러나 십왕(十王)이라는 이름에 걸맞는 일격을 선보인 벽력도왕의 시선은, 깊게 가라앉은 채로 희뿌연 먼지구름이 치솟은 주위를 훑고 있었다.

‘어디냐.’

셀 수 없을 만큼 도를 휘둘렀고, 어림잡아 일천이 넘는 사람을 베었다.

그렇기에 누구보다 잘 안다.

조금 전의 일격으로 베어 낸 것은 바람과 땅이지, 한 인간의 살과 뼈가 아니라는 것을.

“놈!”

벽력도왕은 호랑이처럼 포효하며 대도를 휘둘렀다.

강맹한 압력에 산산이 흩어지는 먼지구름 너머, 마치 사냥을 준비하는 늑대처럼 기척을 죽인 채 웅크리고 있던 자무카가 그곳에 있었다.

훅.

누가 먼저랄 것도 없었다.

두 사람은 약속이라도 한 듯이 서로를 향해 신형을 내쏘았다.

하북팽가의 대호와 대초원의 늑대가 지닌 이빨과 발톱은, 이 자리의 그 누구도 볼 수 없을 만큼 빠르고 강했다.

쾅! 쾅! 콰아아앙!

두 자루의 도신이 맞부딪칠 때마다 포성(砲聲)과도 같은 굉음이 울려 퍼졌다.

협곡을 가로지르는 그 거대한 여파에 휩쓸린 이들이 토해 내는 비명이 그 위로 덧씌워졌다.

“크아아악!”

몸뚱어리에서 떨어져 나간 팔과 다리가, 피분수가 솟구친다.

자욱하게 맺힌 피 안개 너머로 쉴 새 없이 번뜩이는 섬광 앞에, 때아닌 재앙을 겪은 중심부의 유목민들은 죽을 힘을 다해 몸을 피했다.

누군가는 비교적 안전한 후미의 입구를 향해.

또 다른 누군가는 그 반대편에 위치한 출구를 향해.

그리고 불가피하게 후자를 선택할 수밖에 없었던 이들은, 어느덧 코앞까지 다가온 창칼의 숲과 마주해야 했다.

푸푸푹!

아직 건재한 토성(土城)에서 날아든 화살을 미처 피하지 못한 수십여 명의 유목민이 고슴도치가 되어 쓰러지고, 허물어지는 시신을 밟으며 전진한 산서인들의 손에 들린 날붙이가 번뜩였다.

서걱!

몸은 지쳤으나, 검신에 깃든 예기(銳氣)는 조금도 사그라지지 않았다.

신월도와 함께 그 주인마저 베어 버린 진위경은 거칠어진 호흡을 가다듬으며 나아갔다.

죽여도 죽여도 줄어들 것 같지 않았던, 하지만 이제는 파도처럼 휩쓸리고 있는 협곡 내부의 적들을 향해.

두 괴물이 격전을 벌이고 있는 협곡의 중심부를 향해.

위험?

상관없었다.

이미 활시위는 쏘아졌다. 물러선다면 두 번 다시 돌이킬 수 없는 패배만이 모두를 기다리고 있다.

‘한시라도 빨리 협곡을 점령하고 놈들을 몰아내야 승산이 있을 터.’

벽력도왕을 비롯한 하북팽가의 합류로 조금 전까지 암담하던 전황은 크게 회복되었지만, 진위경의 냉철한 이성은 현재 아군이 처한 상황을 빈틈없이 꿰뚫고 있었다.

‘지금의 흐름은 일시적일 뿐. 놈들이 평정심을 되찾는다면 다시 전세는 역전된다.’

하북팽가는 분명 강하다.

본거지인 하북을 넘어 모용세가와 함께 북부 전체를 아우르는 패자이며, 벽력도왕이라는 희대의 초절정 고수는 그 자체로도 일군(一群)을 상대하기에 모자람이 없었다.

하지만 강한 것은 상대 역시 마찬가지다.

자무카는 벽력도왕을 상대로도 한 치의 물러섬 없이 분투하는 중이고, 협곡 너머에는 아직도 물경 수만을 아우르는 초원의 군세가 하북팽가에 맞서 싸우고 있다.

사기가 꺾였다고는 하나 자그마치 열 배에 달하는, 아니 어쩌면 그 이상의 머릿수.

이미 수천이 넘는 적들이 이 비좁은 협곡에서 죽거나 전투 불능 상태에 빠진 상황에서도, 근본적인 전력 차이는 여전히 존재했다.

결국, 답은 하나뿐이다.

지금 같은 팽팽한 흐름의 전투에서 승리하기 위해서라면, 그저 죽을 힘을 다해 끝까지 나아가는 수밖에.

“나를 따르라!”

진위경은 목놓아 부르짖으며 달려 나갔다.

어느덧 피투성이가 된 몸을 이끌고, 허물어지는 적들의 전열(戰列)을 파고들어 미친 듯이 검을 휘둘렀다.

콰드드득!

그에게는 지켜야 할 것이 너무나도 많았다.

목숨을 바쳐 자신을 따르는 사람들.

그런 그들이 일평생을 나고 자란 이 땅.

마지막으로 저 멀리, 극심한 내상을 입은 상황에서도 비틀거리며 일어나는 아우까지.

그리고 진위경은 무엇하나 포기할 수 없었다.

단 하나도.



* * *



다른 모든 것을 떠나, 진위경의 판단은 정확했다.

협곡 밖, 항아리처럼 좁은 입구와는 달리 탁 트여 있는 너른 분지(盆地)에서는 한 치의 물러섬도 없는 팽팽한 전투가 이어지고 있었으니까.

푸푸푹!

서걱! 콰아아앙!

하북팽가와 유목민.

유목민과 하북팽가.

땅을 맞대고 있었던 만큼, 적지 않은 세월 동안 반목해 왔던 두 세력은 일생일대의 대적을 만난 것처럼 병장기를 휘두르며 목이 터지도록 외쳤다.

“나약한 오랑캐 놈들이다! 단숨에 짓밟아라!”

“대초원의 형제들이여! 고작 한 줌밖에 되지 않는 한족 따위를 상대로 물러설 셈인가!”

그리고 바람을 타고 서로를 향해 울려 퍼지는 그 외침은, 그들이 처한 현재의 상황을 정확히 대변하는 것이었다.

개개인의 무위는 하북팽가가 한 수 위였으나, 열 배가 넘는 압도적인 머릿수의 유목민들은 사방을 빽빽하게 둘러싼 채 쉴 새 없이 달려들고 있었으니까.

“쳐라! 물러서지 말고 포위하라!”

“돌파하라!”

날카로운 창과 거대한 방패의 대결.

만약 벽력도왕이 이 자리에 남아 있었다면 하북팽가가 우위를 점했겠지만, 한바탕 적진을 뒤흔든 그는 일부 정예와 함께 협곡으로 향했고 유목민들은 찢어진 포위망을 금세 매우며 반격을 가하고 있었다.

일말의 초조함을 마음 한구석에 품은 채.

‘지금 같은 흐름이 이어진다면…….’

‘좋지 않아, 결코.’

자무카의 명령으로 협곡 밖에 남은 케식 백인장들은 무거운 눈빛을 주고받았다.

갑작스러운 하북팽가의 등장은 산서인들의 사기를 하늘까지 끌어올리는 동시에, 유목민들의 기세를 무참히 꺾어 버렸다.

벽력도왕이라는 강자의 존재감.

더불어 유목민들로 하여금 감히 하북을 넘보지 못하게 만든 하북팽가의 위명까지.

이미 백인장 중 일부는 무의식적으로 품 안을 더듬고 있었다.

‘지금이라도 ‘그것’을 사용한다면 단숨에 이 전황을 뒤집을 수 있을 텐데.’

그러나 뇌리를 스친 그 생각은 금세 사그라들었다.

자무카.

초원의 절대자이자 자신들이 따르는 주군이 내린 명령을 떠올렸기 때문이었다.



‘누구도 내 명령 없이 사용하지 마라. 앞으로 우리가 치러야 할 전투는 이번뿐만이 아니니.’



그 단호한 명령에, 일말의 반박이나 의심 따위는 없었다.

단순히 군신 간의 관계라서가 아니라, 그 말을 한 것이 자무카이기 때문이었다.

자무카는 항상 냉철하고 확실한 사람이었다. 지금까지 그가 한 말은 언제나 옳았고, 이번에도 그럴 터였다.

설령 그 상대가 벽력도왕이라고 해도, 백인장들에게 있어 그 사실은 달라지지 않았다.

다만, 아주 작은 의문만이 있을 뿐.

‘도대체 무엇 때문에 이토록 확신하셨단 말인가.’

산서성에 다다르기 전, 자무카는 이미 예측한 바 있었다.

태원진가를 도와 자신들에게 맞설 또 다른 적들의 존재를.

더불어 흔들림 없는 목소리로 단언했다.



‘달라지는 것은 없다. 아무것도.’



며칠 전 들었던 그 한 마디를 떠올린 백인장들이 의문 어린 눈으로 전장을 바라보던 그 순간.

드드득.

수만에 달하는 적과 아군이 뒤얽힌 광활한 분지 너머, 어둠을 뚫고 불현듯이 나타난 일단의 무리가 일제히 활시위를 당겼다.

솨아아아악!

먹구름 아래, 바람을 가르며 내리꽂히는 수천 개의 화살촉이 번뜩였다.
```

## Final English reading copy

```markdown
# Chapter 966

Assuming two martial artists were evenly matched, what was the most decisive factor in a life-and-death duel? For ages, that question had been a favorite topic among the gossips of the martial world.

Some said it was superior internal energy and peerless martial arts. Others named the presence of a divine weapon as the most important factor. Still others insisted it was an unshakable mindset and outstanding physical ability.

Yet every one of those opinions was both right and wrong.

Masters who had reached a certain realm knew. They had felt it firsthand.

In a life-and-death duel, a single difference—however small, however trivial it might seem—could decide the outcome.

That was why they often all agreed on this:

*It doesn’t matter all that much what martial art you’ve learned. What matters most is having the eyes and instincts to see through your opponent’s movements.*

And in that moment, everyone filling the gorge understood exactly what those words meant—words that had once seemed so far removed from them.

*Whoosh! Kaboom!*

They couldn’t see it. They couldn’t sense it, either.

They simply stared, dazed, for a moment forgetting even to swing their blades at the enemies in front of them.

Beyond the endless flashes and thunderous booms, three figures were locked together, moving too fast to see.

*Whoom!*

An absurdly massive saber cleaved through the air. The mighty Force along its edge tore through Jamukha’s body with the wind.

Or seemed to.

*Shhk.*

A single step.

Jamukha’s form blurred for an instant, then reappeared about ten feet away.

He had dodged the attack with a ghostly movement. Just as he surged toward the Thunderbolt Saber King, a faint whistle sounded from beyond his blind spot.

*Shwaa!*

In that instant, Jamukha realized anew:

The enemy he had to defeat here today wasn’t just the Thunderbolt Saber King.

*Shk—KABOOM!*

The crescent saber met a gleaming white blade.

Amid the shock wave and deafening boom that reverberated through the gorge, Jamukha took a step back, caught off guard. A smile formed at the corner of his mouth.

*Impressive. Even better than I expected.*

His gaze fell on Jin Mukyung, who had been driven back, carving a deep furrow through the ground.

The young Sword Demon of the Jin Family of Taiyuan had delivered an unexpected strike with a body battered from head to toe.

And at last, Jamukha understood.

How Jin Mukyung, who had only just broken through the Supreme Peak barrier, had defeated the Demon Bird, a master who had reached full mastery of his realm.

There was neither form nor pattern to the sword Mukyung wielded—nothing that could be called the fundamentals of martial arts.

Only One Strike.

He simply found the fastest, most perfect path to end his opponent’s life, then moved along it.

And that strike, imbued with an intent to kill, had far greater power than Mukyung’s own martial prowess should have allowed.

Powerful enough to defeat the Demon Bird, a superior master, in the realm of Supreme Peak, where a single form could decide the fight.

But…

*This is as far as it goes.*

Without a word anyone could hear, Jamukha shook out both arms.

Green Force, like the vast grasslands where he had been born and raised, surged along his crescent saber and his empty hand.

*Fwoosh!*

Beyond the blinding flash swelling to an immense size, the two streams of Force shot in different directions.

One toward the Thunderbolt Saber King, who was bringing his great saber down with enough force to cleave the world in two.

The other toward Jin Mukyung, who was staggering and swallowing blood.

The result was far beyond what one man had expected.

*Craaaack!*

The Thunderbolt Saber King’s eyes widened as he stared at the two blades locked together without the slightest give.

*What in the—!*

He was a warrior to the bone. Even now, a living legend who had made his name in the great upheaval of the Great Faction War, he never underestimated an opponent standing before him.

And yet his full-powered strike had been blocked.

With astonishing ease.

As if his opponent had seen through the form—and the flow—of the martial art he had just used.

“How could you…!”

A voice thick with confusion and anger slipped through his lips.

The two blades remained locked in midair, their wielders’ bodies still apart. Jamukha looked at the Thunderbolt Saber King with calm eyes.

“I’m disappointed. Shouldn’t you have saved your much younger junior first, Thunderbolt Saber King?”

“……!”

The Thunderbolt Saber King’s wide eyes wavered for an instant.

Over Jamukha’s shoulder, he belatedly saw Jin Mukyung on his knees, vomiting blood, unable to withstand the might of the palm strike.

*Damn it.*

It was a mistake.

No—a devastating misjudgment.

Jamukha was stronger than he had thought, and he was a far more formidable master, with deeper secrets.

*BOOM!*

After their strength had been locked in a fierce contest, the sabers finally tore apart with a deafening boom.

The Thunderbolt Saber King let the force of the impact roll through him, then brought his great saber down at Jamukha again.

*Fwoosh!*

A strike combining his innate divine strength with several jiazi of internal energy.

Born the third son of the Hebei Peng Family, he had become its Family Head and the Thunderbolt Saber King through the family’s peerless martial art, the Primordial Thunderbolt Saber. Now it fell like a bolt of lightning.

With enough force to split the world in two along with the enemy before him.

*Shing! KRAAAASH!*

A keen slicing sound rang out as the gorge shook.

But the Thunderbolt Saber King, whose strike had lived up to the name of one of the Ten Kings, swept his deep-set gaze across the area as a hazy cloud of dust billowed into the air.

*Where is he?*

He had swung his saber countless times and cut down more than a thousand people, by his estimate.

So he knew better than anyone:

The strike he had just delivered had cut through wind and earth—not a man’s flesh and bone.

“You bastard!”

The Thunderbolt Saber King roared like a tiger and swung his great saber.

Beyond the dust cloud scattering under the force of his blow, Jamukha was there, crouched and silent, like a wolf preparing to hunt.

*Hup.*

Neither waited for the other.

As if on cue, both men shot toward each other.

No one there could see the teeth and claws of the great tiger from the Hebei Peng Family or the wolf of the Great Steppe—so fast and so powerful were they.

*BOOM! BOOM! KRAAA-BOOM!*

Every time the two sabers collided, a boom like cannon fire rang out.

The screams of those swept up in the tremendous shock waves surging across the gorge piled over the noise.

“Gwaaaah!”

Arms and legs tore from bodies. Fountains of blood shot into the air.

Beyond a thick haze of blood, flashes of light kept sparking without pause. The nomads caught at the heart of the calamity fled for their lives.

Some ran toward the entrance at the rear, where it was relatively safe.

Others ran toward the exit on the opposite side.

But those with no choice but to take the latter route found themselves face-to-face with a forest of spears and blades, now almost upon them.

*Thud-thud-thud!*

Dozens of nomads, unable to dodge the arrows raining down from the still-standing earthen rampart, fell like pincushions. The blades in the hands of Shanxi fighters flashed as they pressed forward, trampling the crumbling bodies.

*Shhk!*

His body was exhausted, but his sword had lost none of its sharpness.

Jin Wikyung, who had cut through a crescent saber and its wielder, steadied his ragged breathing and moved forward.

Toward the enemies inside the gorge, who had seemed endless no matter how many they killed, but were now being swept away like a wave.

Toward the heart of the gorge, where two monsters were locked in a fierce battle.

Danger?

It didn’t matter.

The arrow had already been loosed. If they retreated now, only a defeat they could never undo awaited them all.

*We have to seize the gorge and drive them out as soon as possible. That’s our only chance.*

The arrival of the Hebei Peng Family, led by the Thunderbolt Saber King, had greatly improved the desperate battle situation. But Jin Wikyung’s cool head saw every detail of the position his side was in.

*This momentum is only temporary. If the enemy regains their composure, the tide will turn again.*

The Hebei Peng Family was undoubtedly strong.

Beyond its home province of Hebei, it was a power that ruled the entire north alongside the Murong Family. And the Thunderbolt Saber King, a peerless Supreme Peak master, was a force who could take on an army all by himself.

But their enemy was just as strong.

Jamukha was fighting the Thunderbolt Saber King without giving up an inch, and beyond the gorge, tens of thousands of steppe warriors were still fighting the Hebei Peng Family.

Their morale had been broken, but they still outnumbered the enemy ten to one—perhaps more.

Even after thousands of their soldiers had been killed or put out of action in the narrow gorge, the fundamental gap in their forces remained.

There was only one answer.

To win a battle that was still so evenly matched, they had to keep advancing with everything they had until the very end.

“Follow me!”

Jin Wikyung shouted at the top of his lungs and charged.

Dragging along his now blood-soaked body, he plunged into the collapsing enemy line and swung his sword like a madman.

*Craaaack!*

He had too much to protect.

The people who followed him, ready to give their lives.

The land where they had been born and raised.

And finally, his little brother, staggering back to his feet in the distance despite his grievous internal injuries.

Jin Wikyung couldn’t give up a single thing.

Not one.

* * *

Apart from everything else, Jin Wikyung’s judgment had been right.

Outside the gorge, where the terrain opened into a broad basin instead of narrowing like a jar at its entrance, the battle was continuing without either side giving an inch.

*Thud-thud-thud!*

*Shhk! KRAAA-BOOM!*

The Hebei Peng Family and the nomads.

The nomads and the Hebei Peng Family.

The two forces had shared a border and spent many years at odds. Now they swung their weapons and screamed at each other as if they’d met their sworn enemy in the fight of their lives.

“They’re weak barbarians! Crush them in one blow!”

“Brothers of the Great Steppe! Are you going to retreat before a handful of Han Chinese?”

Those cries, carried on the wind as they rang out against each other, perfectly reflected the situation they were in.

Each individual martial artist of the Hebei Peng Family was a cut above the nomads. But outnumbering them more than ten to one, the nomads pressed in without pause, surrounding them on all sides.

“Attack! Don’t fall back—surround them!”

“Break through!”

The clash of sharp spears and enormous shields.

If the Thunderbolt Saber King had stayed here, the Hebei Peng Family would have held the advantage. But after shaking the enemy ranks in a fierce assault, he had headed into the gorge with a portion of his elite. The nomads had quickly closed the breach in their encirclement and launched a counterattack.

A trace of unease lingered in their hearts.

*If this keeps up…*

*This is bad. Very bad.*

The Keshik centurions Jamukha had left outside the gorge exchanged grim looks.

The Hebei Peng Family’s sudden arrival had sent the morale of the Shanxi fighters soaring, while brutally crushing the nomads’ momentum.

The imposing presence of a master like the Thunderbolt Saber King.

And the fame of the Hebei Peng Family, which had kept the nomads from daring to encroach on Hebei.

Some of the centurions were already unconsciously reaching inside their robes.

*If we use that now, we could turn this battle around in an instant.*

But the thought that had crossed their minds quickly faded.

They remembered Jamukha’s order—the command of the absolute ruler of the Great Steppe, the lord they served.

*“No one uses it without my order. This won’t be the last battle we have to fight.”*

There wasn’t the slightest hint of objection or doubt.

Not simply because of the relationship between lord and subject, but because it was Jamukha who had said it.

Jamukha was always coolheaded and decisive. Everything he had said so far had been right, and he would be right this time, too.

That wouldn’t change even if the opponent was the Thunderbolt Saber King.

There was only one small question.

*What made him so certain?*

Before they reached Shanxi Province, Jamukha had already predicted that other enemies would help the Jin Family of Taiyuan oppose them.

And he had declared with an unwavering voice:

*“Nothing will change. Nothing at all.”*

The centurions, recalling those words from several days ago, watched the battlefield with questioning eyes.

*Rrrrattle.*

Beyond the vast basin, where tens of thousands of enemies and allies were tangled together, a group suddenly emerged from the darkness. All at once, they drew their bows.

*Shwaaaaa!*

Beneath the storm clouds, thousands of arrowheads flashed as they sliced through the wind and plunged down.
```
