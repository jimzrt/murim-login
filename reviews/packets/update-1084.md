<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1084.txt",
      "sha256": "f053cac45cd042d64ecda520298d91c7528332fd83b2e50524e9904eeb1f9889",
      "bytes": 12466
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ceba6fd16a5989d55410f6cbe4ad94a79a51daee6ce0cf8cbf0126883410539d",
      "bytes": 1082
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a89074e7ba35a8c4fba2a897c2d9206f156ca20277557ca35bc62c2180590e3b",
      "bytes": 243412
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "d07f4e528d34cbba9832719978ed3421da580fd8635f9e47b606cb82c8e32b0b",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ad8b96c6e72037db345bd400862ea4558d987b57923d01bcac183b767802f506",
      "bytes": 623
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "90e501f5a0a8dcffe35525ca0d0f00c4078b00c6b12be6390531f098a5aa52e5",
      "bytes": 1131
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "58a26ebc062bb2491d81493f3106d1710fa81b7f7ba862172b209911bfd6e6ec",
      "bytes": 286576
    }
  ],
  "estimated_tokens": 9741
}
-->

# Durable State Update — Chapter 1084

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
1 and safe_through 1084. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1084. Profile updates may replace only one
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
  "chapter": 1084,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1084,
    "continuity_sources": [1084],
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
    "Villagers suspect the Green Forest Alliance attacked the Blue Flower Escort Bureau and covered it up with a landslide; this remains unconfirmed.",
    "A Blue Flower Escort Bureau flag was recovered from the landslide that blocked the mountain road.",
    "Villagers report that the Murong Family joined forces with Dark Heaven.",
    "Pa Ryun leads hundreds of ships and thousands of men toward the Great Nation’s warships.",
    "Pa Ryun rejects the Son of Heaven’s claim to rule; imperial troops killed the old man who raised him when Pa Ryun was twelve."
  ],
  "continuity_sources": [
    1083
  ],
  "open_questions": [
    "Who is the black-robed captive in Qinghai, and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "Who is the black-robed man beside Pa Ryun?"
  ],
  "safe_through": 1083,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 파륜     | **Pa Ryun**        |
| 철수     | **Cheol Soo**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 정파     | **orthodox faction**                             |                                                       |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 상태               | **Status**                     |
| 대사      | **Master** for a senior Buddhist monk                           |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 평화 | **Peace Guild** | Guild name. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 철수신룡 | **Iron-Water Divine Dragon** | Title of Cheol Soo, a member of the Ten Dragons and Phoenixes. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 쾌조선 | **swift ship** | Fast vessel operated by the Yangtze River Channel League. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 군선 | **military vessel** | Vessel carrying the Hubei government troops and sailors. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 황하 | **Yellow River** | River along which civilization began. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 철수신룡 | rival_candidates | you; weakling | insulting-casual | Uses 너 and later insults him as 좆밥아 while provoking him. |
| 철수신룡 | 진태경 | rival_candidates | brat; you | condescending and taunting | Uses 애송아 and 네놈 while belittling Taekyung and the Fire Gate Clan. |
| 수하 | 채주 | subordinate_to_stronghold_lord | Stronghold Lord | deferential | The subordinate calls Mu Song 채주 while reporting the nearby vessel. |
| 진태경 | 무송 | junior_martial_artist_to_senior_martial_artist | Senior | formal-polite | Taekyung uses 선배님 after recognizing Mu Song as a senior martial artist and disciple of the Seafaring King. |
| 무송 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | familiar-teasing | Mu Song calls Taekyung 후배 and jokes about his supposed taste for men. |
| 진태경 | 미미 | rescuer to companion snake | Mimi or Mimi-chan | informal, pleading | Taekyung calls to Mimi while asking the snake to carry him and the survivors. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1082
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1082
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 836
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan, belongs to the Yangtze River Channel League's moderate faction, and is an exceptionally skilled ship captain.
- **Personality:** Ambitious, domineering, impatient with interruptions, strongly attached to life on the water, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** Mu Song belongs to the Yangtze River Channel League's moderate faction, regards Hwang Chung, his senior and Uncle Hwang, as family, must weigh whether the League will support the New Murim Alliance while the Seafaring King retains authority over major League decisions, and has instructed his subordinates to aid Jin Taekyung and the Jin Family of Taiyuan in repayment for past help.

## Korean source

```text
1084화




끝없는 장강의 물결은 도도하게 흐른다(不尽长江滚滚来).

오랜 과거, 시성(詩聖)이라 불리며 당대를 풍미했던 어느 시인이 남긴 시구다.

그는 장강의 강물에 담긴 아득한 역사와 그 아름다운 자체를 깊이 경애했고, 그것은 눈을 감은 채 뱃머리에 앉아 있는 한 사내 역시 다르지 않았다.

아니, 당연하게도 그 이상이었다.

어릴 적부터 장강을 사랑하여 수적이 되었고, 선화아(船火兒)라는 별호는 어느덧 그 자신을 상징하는 것이 되었으니.

둥, 둥, 두웅!

마치 물결처럼 퍼져 나가는 북소리에 사내는, 해상왕의 두 번째 제자이자 수룡채의 채주인 선화아 무송은 감고 있던 눈을 떴다.

“채주. 마침내 명령이 떨어졌습니다.”

무송은 무겁게 고개를 끄덕였다. 설령 수하의 말을 듣지 않았더라도 저 북소리가 어디에서부터 비롯되었는지, 그는 이미 누구보다 잘 알고 있었다.

‘해룡선(海龍船).’

스승인 해상왕 파륜의 배다.

과거, 그들의 유일한 적수였던 황하수로맹(黃河水澇盟)과의 마지막 전투에서 홀로 수십여 척의 선박을 침몰시킨 최강의 함선.

현재에 이르러서는 그 누구도 감히 대적할 수 없는 바로 그 해룡선이, 장강 최고의 무인을 태운 채 돛을 활짝 편 채 물살을 가르고 있었다.

장강의 또 다른 주인.

아니, 실질적인 주인이나 다름없는 대국의 군선(軍船)을 향해.

‘하지만 오늘만큼은 다를 것이다.’

우리가, 장강수로맹이 진정한 장강의 지배자임을 보여 줄 때.

선화아 무송은 마음속으로 뇌까리며 주먹을 번쩍 치켜들었다. 터져 나오는 수하들의 함성과 함께 바람을 받은 돛이 한껏 부풀었다.

촤아아악!

힘차게 물살을 가르는 뱃머리.

광야를 달리는 말처럼 대국의 군선들을 향해 질주하던 그때, 비스듬히 측면으로 방향을 튼 군선들 사이로 거무튀튀한 무언가가 고개를 내밀었다.

“발포(發砲)하라!”

그 순간.

퍼버벙!

백여 문이 넘는 홍이포(紅夷砲)가 동시에 불을 뿜었다.

일개 수적 따위가 아닌, 대국의 수군이기에 지닐 수 있는 무기.

그러나 인간의 육신 따위는 단숨에 짓뭉갤 수 있는 쇳덩어리가 이백여 장의 허공을 가로질러 들이닥치는 그 무시무시한 광경 앞에서도, 무송의 눈동자는 조금도 흔들리지 않았다.

그는 일개 수적 따위가 아니었으니까.

팟.

일순간 흐릿해진 신형이 뱃머리를 박차며 쏘아진다. 

어느덧 그의 손에 들린 커다란 대도(大刀)가, 곡선을 그리며 날아드는 포탄을 향해 흉흉한 궤적을 그렸다.

콰아앙!

울려 퍼지는 굉음 속, 포탄을 튕겨낸 반동으로 뱃머리에 착지한 무송은 저릿해진 손아귀를 느끼며 외쳤다.

“돌격! 돌격하라!”

“와아아아!”

힘이 실린 함성과 함께, 장강수로맹이 자랑하는 쾌조선(快鳥船)들이 더욱더 빠르게 나아가기 시작했다.

오늘 이 자리에 모인 수적들은 하나같이 가려 뽑은 최정예들. 무공을 익힌 그들의 노질은 힘차면서도 쾌속했고, 선봉에 배치된 절정 고수들은 빗발치는 포탄으로부터 선박을 지키기 위해 온 힘을 다했다.

물론, 그럼에도 넘을 수 없는 한계는 있었지만.

콰과과광!

“크아아악!”

“배가, 배가 침몰한다!”

거대한 굉음이 비명을 집어삼킨다. 산산이 부서진 쾌조선들이 곳곳에서 침몰하기 시작한다.

수백여 척이나 되는 배가 결집해 있다는 것은, 그 자체로 거대한 과녁판과 같다는 뜻.

특성상 내구성보다 속도를 우선시한 덕분에 장강수로맹의 선박들은 그 선체의 폭이나 크기가 작고 유려했으나, 이는 곧 단 한 발의 포탄에도 침몰할 가능성이 크다는 것을 의미했다.

펑! 퍼어엉!

그럼에도 불구하고, 한참이나 선체를 빗나가 수면 위를 후려치는 포탄들을 본 무송이 눈매를 좁혔다.

‘역시, 화망(火網)이 제대로 갖춰져 있지 않군.’

조금 전에 쏘아진 포탄들은 신호에 맞춰 일거에 들이닥친 것이 아니었다.

아니, 정확히는 첫 발포 이후로 줄곧 그랬다.

쉼 없이 울려 퍼지는 요란한 굉음과는 달리, 막상 장강수로맹의 피해는 총 전력에 비하면 미미했고 되레 홍이포의 불발로 인해 침몰하는 군선마저 보였다.

그저 저마다의 시간차를 둔 채, 대장선의 명령을 기다리지 않고 무언가에 쫓기듯 준비가 되는 대로 쏘아 보내는 적들의 모습.

익히 알려진 화포의 위력에 내심 긴장하고 있던 수적들 또한 어느 순간 입가에 웃음을 띠기 시작했다.

“채주, 놈들이 당황한 모양입니다.”

“염병. 오줌 찔끔 지렸는데 괜히 머쓱해지네.”

화색을 띤 수하들의 말에, 무송이 고개를 끄덕였다.

“모두 스승님의 말씀대로다.”

“예? 총채주, 아니 맹주님께서요?”

“그래. 평화가 길었던 만큼, 저들 역시 무방비한 상태일 거라고 하셨지.”

무송의 생각 또한 스승과 다르지 않았다.

사냥이 끝난 맹수는 나태해지는 법.

이미 오래전부터 대륙이라는 큰 산을 오롯이 지배하게 된 대국과 맞설 적은 없었다. 장강수로맹은 수적들의 연합체로서 어느 정도 묵인되는 존재들에 지나지 않았고, 길었던 평화는 나약함을 부르곤 한다.

물론 만일의 상황을 대비해 훈련을 게을리하지 않은 정예 함대가 존재 하나, 그들이 있는 곳은 바다지 강이 아니다.

대륙을 일통한 이후부터, 대국이 경계해야 할 대상은 외적(外敵)뿐이었으니까.

‘이 전투는, 우리가 승리한다.’

확신에 찬 그 한마디를 마음속으로 작게 뇌까리던 그때, 시시덕거리던 수하 중 하나가 불쑥 입을 열었다.

“그나저나, 좀 거시기하구먼요.”

“무슨 소리냐?”

“이게 뭐랄까 그, 딱히 불만이 있는 건 아닌데.”

뒤통수를 긁적인 수하가 조심스럽게 덧붙였다.

“저희, 이래도 되는 겁니까?”

“뭐?”

“뭔가 아닌 것 같아서 말입니다. 지금까지도 그럭저럭 살 만했는데, 굳이 무림맹을 뒤통수치고 암천 그 썩을 것들이랑 손잡는다는 것이…….”

그가 떨떠름한 얼굴로 말꼬리를 흐리자, 다른 수하들도 눈치를 보며 슬쩍 한마디씩을 얹었다.

“하긴 뭐, 암천이 좀 구린내가 나긴하지. 정파 놈들이 뒤에서 우리 호박씨 까는 건 있어도 아주 질 나쁜 것들은 아니니까.”

“맞어, 맞어.”

“명령이 떨어진 이상 우리 같은 아랫놈들이야 따르는 게 맞지만, 사실 좀 그렇긴 혀.”

수군덕대던 수하들은 이내 딱딱하게 굳은 우두머리의 표정을 보고 입을 다물었지만, 정작 무송 역시도 마음이 편치 않았다.

‘이래도 되는 거냐고?’

앞서 들었던 말을 떠올릴수록 입맛이 씁쓸해졌다.

아니, 내심으로는 누구보다 그 이유를 잘 알고 있기에 더욱 쓰게 느껴지는지도 몰랐다.

‘제아무리 스승님의 명령이라지만…… 도무지 내키지 않는군.’

무송은 지금껏 단 한 번도 스스로를 결코 성인군자라고 여기지 않았다.

수적(水賊).

저 두 글자에 담긴 뜻 그대로 그는 도적이고, 그것이 엄연한 사실이다.

그러나 결코 정해진 선을 넘은 적은 없었다.

가난해 보이는 자의 재물은 빼앗지 않았고, 수하 중 누군가 살인을 저지르면 그 즉시 엄벌에 처했다.

‘하지만. 하지만 이건…….’

무송은 굉음과 혼란으로 뒤덮인 강 위를 바라보며 차오르는 뒷말을 삼켰다.

그리고 그와 동시에, 문득 한 사람의 얼굴을 떠올렸다.

‘열화신룡 진태경.’

몇 번이나 쾌조선을 빼앗듯이 빌려 가 종처럼 부린, 자신들보다 더한 도적이나 다름없는 놈이었지만 그래도 진태경은 협객이었다.

그 성질 무시무시한 화왕도, 심지어 살성도.

그들은 천하를 도탄에 빠트린 암천과 싸웠고, 불의(不義)에 맞섰다.

‘그러고 보면, 그들을 도왔던 나 역시 잠시 동안은 협객이었던 셈인가.’

불현듯 뇌리를 스친 그 말도 안 되는 생각에, 무송은 자신도 모르게 입술을 깨물었다.

괜한 생각이다.

여기까지 온 이상, 그 혼자만의 힘으로는 아무것도 되돌릴 수 없었다.

이미 이 문제에 대해서 사제인 철수신룡(鐵手神龍)과 함께 반대표를 던졌던 그였으나, 대사형을 비롯한 몇몇 핵심 장로들의 설득에 넘어간 스승의 의지는 굳건했다.



‘드디어 때가 왔다. 장강의 진정한 주인으로 거듭날 수 있는 절호의 기회가.’



그것으로 모든 것은 끝났다.

하늘 같은 스승이자 맹주인 해상왕 파륜의 명령이었으니까.

스승을 신처럼 믿고 따르는 제자에게 있어서는 더 이상의 반론이나 잡생각은 있을 수도, 있어서도 안 된다.

그는 수적이었고, 앞으로도 그럴 터였다.

“……단숨에 끝낸다. 다들 준비해라.”

슬금슬금 눈치를 살피는 수하들을 뒤로한 채, 무송은 손에 쥔 대도를 있는 힘껏 움켜쥐었다.

지금 이 순간에도 자욱하게 피어오르는 포연(砲煙)에 휩싸인 장강의 풍경은, 마치 처음 본 것처럼 낯설고 불편했다.

‘제기랄.’

혀끝에서 맴도는 욕설을 삼키며, 무송은 다시금 떠올렸다.

천자문도 제대로 못 뗀 주제에 입이 닳도록 외우고 다녔던, 어느 옛 시인이 남긴 한 줄의 시구를.

여느 때처럼 도도하게 흘러야 할 장강의 강물이, 어찌 이다지도 붉게 요동치는지를.

그리고 무송의 그 짧은 상념은, 마침내 코앞까지 다가온 군선의 그림자와 함께 끊어졌다.

구궁, 콰드드득!

강렬한 충돌.

쾌조선의 날카로운 충각(衝角)이 마침내 군선의 측면을 들이박은 그 순간.

팟!

뱃머리를 박차며 솟구친 무송은 힘차게 대도를 내리그었다.

갑판 위에서 전투를 대비하던 한 무리의 관군들을 향해.

그와 동시에, 또렷하게 보았다.

극도의 긴장과 공포에 젖은 그들의 눈동자를. 파르르 떨리는 창칼과 얼어붙은 몸뚱어리를.

“……빌어먹을.”

끝끝내 참지 못한 욕설을 토해 낸 무송은, 마지막 순간 온 힘을 다해 대도를 비틀었다.

올올히 맺혀 있던 도기(刀氣)가 연기처럼 사라지고, 시퍼렇게 날이 선 도신이 비스듬히 굽혀진다.

퍽! 털썩!

예리한 절삭음이 아닌, 둔탁한 타격음과 함께 힘없이 쓰러지는 군졸들.

“어?”

뒤이어 갑판으로 기어오른 수하들이 상황을 확인하고 눈을 동그랗게 떴지만, 그들이 뭐라 입을 열기도 전에 무송의 나지막한 음성이 울려 퍼졌다.

“죽이진 마라. 노 저을 놈들을 있어야 하니.”

서로를 멀뚱멀뚱 바라보던 수적들이, 이내 씩 웃으며 대답했다.

“다들 들었지? 채주께서 살려 두시란다.”

“암요. 누구 명이라고 거역할깝쇼.”

모두가 알았다.

이것이 얼마나 구차한 변명인지를.

하지만, 그들이 원하는 장강의 풍경은 결코 이런 것이 아니었다.

쿠구구궁! 퍼엉!

불길을 피워올리며 차례차례 침몰하는 군선들을, 사방에서 울려 퍼지는 처절한 비명을 보고 들으며 무송은 마음속으로 조용히 뇌까렸다.

저 멀리, 막아서는 모든 것을 침몰시키며 나아가는 해룡선에 있을 스승을 향해. 

‘이런 모습이었습니까? 당신께서 그토록 원하신 장강은.’

그날, 불과 두 시진 만에 수천의 관군을 실은 일백여 척의 군선을 수장(水葬)시킨 장강수로맹은 뱃머리의 방향을 틀었다.

서쪽 저 너머 어딘가로.

그리고 이 엄청난 소식은 천하를 발칵 뒤집어 놓기에 충분했다.
```

## Final English reading copy

```markdown
# Chapter 1084

The endless waves of the Yangtze roll on.

A line from a poem left behind by a poet who flourished in his time, long ago, and was called the Poet Sage.

He had revered the Yangtze’s waters—their distant history and their beauty in itself. A man sitting at the bow with his eyes closed felt much the same.

No. Naturally, he felt it even more deeply.

He had loved the Yangtze since childhood, become a river pirate, and in time made Ship-Fire Boy a name that symbolized him.

Boom. Boom. Booooom!

At the sound of drums spreading like ripples, the man opened his eyes. Mu Song—the Seafaring King’s second Disciple and Stronghold Lord of Water Dragon Stronghold—had been sitting with them closed.

“Stronghold Lord. The order has finally come.”

Mu Song nodded gravely. Even if he hadn’t heard his subordinate, he would have known better than anyone where that drumbeat came from.

*The Sea Dragon Ship.*

His Master, the Seafaring King Pa Ryun’s vessel.

In the final battle against the Yellow River Channel League, once their only rival, it had sunk dozens of ships all by itself. It was the mightiest vessel on the river.

And now, the Sea Dragon Ship—against which no one dared stand—was cutting through the current with the greatest martial artist on the Yangtze aboard.

It was headed for the Great Nation’s military vessels, the Yangtze’s other master.

No—the Yangtze’s master in all but name.

*But today will be different.*

Today, we’ll show them that we—the Yangtze River Channel League—are the Yangtze’s true rulers.

Mu Song muttered the words to himself and thrust his fist into the air. His subordinates roared, and the wind filled the sails.

*Whoooosh!*

The ship’s bow cut forcefully through the water.

Just as they charged toward the Great Nation’s vessels like horses across an open plain, something dark and grayish emerged between the vessels that had turned obliquely to face them.

“Fire!”

At that instant—

*Boom! Boom!*

More than a hundred Hongyi cannons[^1] roared at once.

A weapon only the Great Nation’s navy could possess—not some band of river pirates.

But even as lumps of iron capable of crushing a human body in an instant came hurtling through the air from two hundred *zhang* away, Mu Song’s eyes didn’t waver.

Because he was no ordinary river pirate.

*Whoosh.*

His form blurred for an instant. He kicked off the bow and shot forward.

The great saber in his hand traced a vicious arc toward the cannonball flying at him in a curve.

*Kaboom!*

Amid the thunderous blast, the recoil from deflecting the cannonball sent Mu Song back onto the bow. His grip tingled, and he shouted:

“Charge! Charge!”

“Waaaah!”

Fueled by the roar, the swift ships the Yangtze River Channel League was so proud of began to surge forward even faster.

Every river pirate gathered here today was a handpicked elite. Their oarsmen, all trained in martial arts, rowed with strength and speed, while the Peak masters stationed at the vanguard did everything they could to shield the ships from the hail of cannonballs.

Of course, there were limits they couldn’t overcome.

*Rumble!*

“Arrrgh!”

“The ship—the ship’s sinking!”

A tremendous boom swallowed their screams. Swift ships, shattered to pieces, began to sink all around them.

Hundreds of ships gathered together made one enormous target.

The League’s ships had been built for speed rather than durability, so their hulls were small and sleek. That also meant a single cannonball could easily send one to the bottom.

*Boom! Boom!*

Even so, Mu Song narrowed his eyes as cannonballs missed the hulls by a wide margin and slammed into the water.

*As I thought, they haven’t set up a proper barrage.*

The cannonballs just fired hadn’t all come at once on a signal.

No. They hadn’t done that even once since the first volley.

Despite the constant, deafening blasts, the League’s losses were minor compared with its full strength. He could even see military vessels sinking because their own cannons had misfired.

The enemy ships were firing at their own pace, not waiting for orders from the flagship. They looked as if something were chasing them, shooting as soon as they could get ready.

The river pirates had been tense, knowing full well the power of cannons. Now, some of them were beginning to smile.

“Stronghold Lord, they look flustered.”

“Shit. I nearly pissed myself, and now I just feel embarrassed.”

At his subordinates’ cheerful remarks, Mu Song nodded.

“Just as my Master said.”

“Pardon? The Chief Stronghold Lord—no, the Alliance Leader?”

“That’s right. He said they’d be caught unprepared, with peace having lasted so long.”

Mu Song thought the same as his Master.

A predator grew lazy once the hunt was over.

For a long time now, no one had risen to challenge the Great Nation, which ruled the continent like a mountain. The Yangtze River Channel League was only an alliance of river pirates, tolerated to a certain extent. And a long stretch of peace had a way of making people weak.

Of course, the Great Nation had an elite fleet that never neglected its training in case of emergency. But that fleet was on the sea, not the river.

Ever since the Great Nation unified the continent, the only enemies it had to watch for were foreign ones.

*We’ll win this battle.*

Just as Mu Song quietly repeated the words to himself, sure of victory, one of the chuckling subordinates suddenly spoke up.

“Still, there’s something that feels a little off.”

“What do you mean?”

“It’s not that I’m complaining, exactly, but…”

The subordinate scratched the back of his head, then added hesitantly:

“Are we really supposed to be doing this?”

“What?”

“It just doesn’t feel right. We’ve managed well enough up to now, so why stab the Murim Alliance in the back and join hands with those rotten bastards in Dark Heaven…?”

As he trailed off, looking uneasy, the other subordinates exchanged glances and chimed in.

“Well, Dark Heaven does stink to high heaven. The orthodox faction may talk shit about us behind our backs, but they’re not that kind of rotten.”

“Yeah, yeah.”

“Orders are orders, so it’s right for underlings like us to follow them. But still, it doesn’t sit right.”

The subordinates had been murmuring among themselves, but when they saw their leader’s expression stiffen, they fell silent. The truth was, Mu Song wasn’t at ease either.

*Are we really supposed to be doing this?*

The more he thought about what he’d just heard, the more bitter his mouth felt.

No—perhaps it felt all the more bitter because deep down, he knew better than anyone why they were doing it.

*Even if it’s my Master’s order… this doesn’t sit right with me at all.*

Mu Song had never once thought of himself as a *junzi*.

A river pirate.

Just as those two words implied, he was a thief. That was an undeniable fact.

But he had never crossed a certain line.

He never took from anyone who looked poor, and if one of his subordinates committed murder, Mu Song punished him severely on the spot.

*But this. This is…*

Mu Song looked out over the river, cloaked in thunder and chaos, and swallowed the words rising in his throat.

At the same time, a face suddenly came to mind.

*Blazing Flame Divine Dragon Jin Taekyung.*

He’d borrowed their swift ships so many times it was practically theft, then bossed them around like servants. He was a thief worse than they were, if anything. But Jin Taekyung was still a chivalrous hero.

The fearsome Fire King—and even the Slaughter Saint.

They had fought Dark Heaven, which had plunged the world into misery, and stood against injustice.

*Come to think of it, since I helped them, was I a chivalrous hero for a little while too?*

At the absurd thought that flashed through his mind, Mu Song bit his lip without realizing it.

It was a pointless thought.

Now that they’d come this far, there was nothing he could turn back by himself.

He and his Junior Brother, the Iron-Water Divine Dragon, had already voted against this. But their Master’s resolve had held firm after the First Disciple and several key Elders persuaded him.

*At last, the time has come. This is our one chance to become the Yangtze’s true rulers.*

That had settled everything.

It was an order from his Master and Alliance Leader, the Seafaring King Pa Ryun, a man as exalted as the heavens.

For a Disciple who trusted and followed his Master as if he were a god, there could be no further objections or idle thoughts. There couldn’t be, and there shouldn’t be.

He was a river pirate, and that was what he would remain.

“…We’ll finish this quickly. Everyone, get ready.”

Leaving his subordinates to watch him anxiously, Mu Song gripped the great saber in his hand with all his might.

The Yangtze, shrouded in thick cannon smoke rising even now, looked strange and unsettling, as if he were seeing it for the first time.

*Damn it.*

Swallowing the curse on the tip of his tongue, Mu Song recalled the line from an old poet’s verse—the one he’d repeated until he was hoarse, despite never even finishing the Thousand Character Classic.

Why were the waters of the Yangtze, which should have flowed so steadily as always, churning so violently and red?

His brief reverie ended as the shadow of a military vessel drew close.

*Rumble—crash!*

A tremendous impact.

The moment the swift ship’s sharp ram slammed into the side of the military vessel—

*Whoosh!*

Mu Song kicked off the bow and leaped up, bringing his great saber down in a powerful slash.

He was aiming at a group of government troops on deck, readying themselves for battle.

At the same time, he saw them clearly.

Their eyes, brimming with terror and tension. Their spears and blades trembling, their bodies frozen in place.

“…Damn it.”

Mu Song finally let the curse escape. At the last moment, he twisted the saber with all his strength.

The blade energy coiling along its edge vanished like smoke, and the keen blade tilted to the side.

*Thud! Thump!*

The soldiers crumpled limply with dull blows instead of sharp cuts.

“Huh?”

The subordinates who climbed onto the deck behind him stared at the scene, eyes wide. But before they could say a word, Mu Song’s quiet voice rang out.

“Don’t kill them. We’ll need men to row.”

The river pirates looked at one another blankly, then grinned.

“You all hear that? The Stronghold Lord says to leave them alive.”

“Of course. Who’d dare disobey an order like that?”

Everyone knew how flimsy an excuse this was.

But the Yangtze they wanted to see was nothing like this.

*Rumble! Boom!*

As the military vessels sank one after another in flames, as cries of agony rang out from every direction, Mu Song murmured silently to himself—toward his Master aboard the Sea Dragon Ship, far away, sinking everything in its path as it advanced.

*Is this what the Yangtze you wanted so badly is supposed to look like?*

That day, in just two *shichen*, the Yangtze River Channel League sank more than a hundred military vessels carrying thousands of government troops, then turned its ships west.

Somewhere far beyond the horizon.

And the astonishing news was enough to turn the world upside down.

[^1]: Hongyi cannons were large, European-style cannons adopted by China.
```
