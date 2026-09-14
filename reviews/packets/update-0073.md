<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0073.txt",
      "sha256": "2543ff5731cced1e2e7a72d75ea40973564fb30ca752da1fa0d92daac52726c0",
      "bytes": 13487
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6101322a0aa9d035dc1353b5ffbd1647ce18cf940160d25694bfab4b9bf9ccfc",
      "bytes": 4789
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "30c56eb291b9b013bea1f10e4cf6a146279f2eda5c6280625abe2b5ad2abf2ac",
      "bytes": 3748
    },
    {
      "path": "characters/Childeuk.md",
      "sha256": "163138c6482510b0d3772510ef2132d0781a0bfa5d56b29ff64a97d08b4a3b44",
      "bytes": 666
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "c2f546269f15dfa6dbbc34beb570690e6d875d9642e3f5fc852275fdf635b5c0",
      "bytes": 1220
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "035aca4b54d844759ef456daf9ae613dea661582eeb922df8bb31f962e32d568",
      "bytes": 23807
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "b8ad09a032cf513744319b0ac7c68f4feefc0581b7cb0c60fcb57d779dfc7650",
      "bytes": 8153
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "38d7d69d2a9787b3ebc70ba432ce96dd430b4fd7180ecf842d47f39d8a581ce2",
      "bytes": 3262
    }
  ],
  "estimated_tokens": 12254
}
-->

# Durable State Update — Chapter 73

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 73. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 73. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 73,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 73,
    "continuity_sources": [73],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "Jin Mukyung recognizes Taekyung as a First Rate martial artist standing before the Peak realm, is astonished by his growth over three years, and now recognizes his genuine talent despite his incomplete and mixed martial arts.",
    "Taekyung's spar with Mukyung ends with Mukyung's victory and the destruction of Taekyung's pavilion; Taekyung survives and recovers in the Medicine King Hall.",
    "Hyuk Mujin is badly injured in the incident and remains under treatment after Taekyung is discharged.",
    "The Jin Family is pursuing an unidentified assassin believed possibly to be the Head Elder's hidden disciple.",
    "Jin Mukyung reunites with Jin Wikyung after three years but remains detached and prioritizes sword training.",
    "Jin Wikyung plans to summon every sect in Shanxi Province on New Year's Day and may seek to become Alliance Leader.",
    "Wipeng leads thirty elites south under the pretext of pursuing the nonexistent assassin, visits Song Sword Sect, and delivers Wikyung's summons as both summons and warning.",
    "Jin Wikyung searched the family's records for Dark Heaven but found no information.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months.",
    "Soyul is five years old and does not know that her parents are dead.",
    "Taekyung is Level 50 with fifty remaining points and fifteen years of internal energy after investing fifty points in Agility during the duel.",
    "Jin Wikyung arranged fifteen days of temporary cohabitation between Taekyung and Jin Mukyung while Taekyung's residence is rebuilt.",
    "Jin Wikyung publicly maintains a formal image but is openly recognized within the family as excessively devoted to Taekyung.",
    "Jin Wikyung stops Taekyung and Mukyung from fighting and requires both brothers to apologize and cooperate.",
    "Mukyung imposes rules of polite speech, silence, and obedience over the training hall during the cohabitation and has spent three years attempting to open the Ren and Du meridians.",
    "The Returnee title grants Taekyung All Stats +10 and activates the Login and Logout functions.",
    "Taekyung accepts that he is half-finished, asks Mukyung for help, and receives a System time limit of 9 days 20 hours 23 minutes.",
    "Mukyung trains Taekyung with continuous spear practice and sparring; Taekyung sleeps no more than two hours daily, uses fasting pills, and reaches mastery of the Jin Family's Spear Technique and Manoeuvre Technique.",
    "The System awards Master a First Rate Martial Art, generates Martial Arts Manual Creation, greatly raises all Stats, and grants Taekyung two Level Ups.",
    "Jin Wikyung is known as the Junzi Sword after the war; his servant Childeuk is removed from meal delivery after a misunderstanding."
  ],
  "continuity_sources": [
    72,
    71
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed.",
    "It remains unresolved whether Hyuk Mujin will actually become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung's summons.",
    "It remains unresolved whether Jin Wikyung will become Alliance Leader.",
    "It remains unresolved whether Song Sword Sect has any connection to the attack."
  ],
  "safe_through": 72,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung's deferential speech; use Three Questions Gorge for 삼문협.",
    "Use Alliance Leader for 맹주 and summon for 소집 to preserve the distinction from an invitation.",
    "Retain Great Hero for 대협 and Ghost Sword for 귀검.",
    "Use Sleep Mode for 수면 모드 and Medicine King Hall Master for 약왕당주.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, and Heart Demon for 심마; use Paralysis Acupoint for 마혈 and Mute Acupoint for 아혈.",
    "Use fist-and-kicking technique for 권각술 and recognition for 인정; render 낙류검 as Falling Flow Sword, 질풍십이권 as Twelve Gale Fists, 화염신장 as Flame Divine Palm, and 분근착골 as Tendon-Splitting and Bone-Twisting.",
    "Render 두 시진 as two hours and 아스모데우스 as Asmodeus; render 일문일살 as One Question, One Kill, 칠득이 as Childeuk, 천자문 as Thousand Character Classic, 벽곡단 as fasting pills, and 비급 제작 as Martial Arts Manual Creation while preserving the 남색 navy-blue and male-love pun."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 기녀     | **courtesan**                                    |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 큰형     | **eldest brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 시스템              | **System**                     |
| 스킬               | **Skill**                      |
| 스킬창              | **Skill Window**               |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 칠득이 | **Childeuk** | Jin Family servant. |

## Listed compact profiles

### Childeuk.md

# Childeuk (칠득이)

- **Safe through:** Chapter 72
- **Aliases:** None
- **Role:** Illiterate servant of the Jin Family of Taiyuan, personally selected by Jin Wikyung to deliver meals to Jin Mukyung and Jin Taekyung
- **Personality:** Physically strong, diligent, gullible, and intensely excitable; readily interprets praise as recognition of exceptional talent
- **Voice:** Deferential, overeager, and breathless when speaking to Jin Wikyung
- **Relationships:** Servant under Jin Wikyung; assigned to serve Jin Mukyung and Jin Taekyung until removed from meal delivery after a misunderstanding

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 72
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 72
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 72
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

## Korean source

```text
＃73화



띠링. 띠링. 띠링.

밀려드는 시스템 알림에 귀가 아플 정도다. 나는 입을 딱 벌리고 눈앞을 가득 채운 메시지창을 지워 나갔다.

‘뭔 보상이 이렇게 많아?’

두 번의 레벨 업과 모든 능력치 상승, 거기에 더해 업적 달성으로 새로운 스킬이 주어졌다.

‘비급 제작?’

띠링.



스킬창



[비급 제작]

등급 : 無

경지 : 일 성

설명 : 대성한 무공에 한해 비급을 제작할 수 있다.

제작 가능한 비급 : 진가창법, 진가보법





설명을 읽어 보니 내가 짐작한 그대로다.

‘일단 스킬이니까 없는 것보다는 낫긴 한데…….’

지금으로써는 딱히 큰 효용이 없어 보인다. 이런 생산직 스킬도 주는구나, 하는 생각에 신기한 정도?

‘이럴 때는 확실히 게임 같단 말이지.’

이 세상에는 아직도 내가 겪어 보지 못한 것들이 너무 많다.

모든 것들이 생소하고 비현실적이다. 지금까지도 무림이 게임인지, 또 다른 현실인지 헷갈릴 정도로.

딱!

“아.”

얼얼한 뒤통수를 붙잡고 돌아섰다. 반 토막 난 목검을 든 진무경이 한심하다는 얼굴로 나를 바라보는 중이었다.

“집중 안 하지?”

“거, 진짜. 기분 나쁘게 자꾸 머리만 때리고 그래.”

“이 자식 또 자연스럽게 말 놓네.”

진무경은 눈을 가늘게 떴지만 이제는 별로 무섭지도 않다.

‘한두 번 맞아 보나.’

지옥 훈련이 시작된 지 오늘로 열흘째.

나는 시작과 동시에 중요한 사실 하나를 깨달았다.

‘존댓말 써도 맞는다!’

정말 오지게 맞았다. 겨우 이틀 차에 [맷집] 능력치가 생겼을 정도니 말 다 했다. 어차피 어떻게 하든 결과는 두들겨 맞을 텐데, 기왕이면 반말 쓰고 맞는 게 정신 승리에 도움이 된다.

따닥!

“이 정도야 간지럽지.”

괜히 맷집 능력치가 생긴 게 아니다.

꽃이 햇빛과 물을 받으며 자라는 것처럼, 내 능력치는 가혹한 폭력과 지옥 훈련으로 쑥쑥 성장했다.

빡!

“아, 잠깐만. 뼈 맞았어, 뼈.”

“비무 아직 안 끝났다.”

퍼버벅!

요령 있게 급소를 타격해 오는 목검을 맞아 가며, 나도 창을 휘둘렀다.

쉬쉬쉭! 타닥!

열흘간의 지옥 훈련.

마침내 대성에 이른 진가창법과 진가보법이 호흡처럼 자연스럽게 흘러나왔다.

띠링.



제한 시간 : 2시간 22분



띠링.



제한 시간 : 2시간 22분



“……?”

뭐야, 왜 두 번 울려.



* * *



쉬쉬쉭!

캉!

압박해 들어오는 창을 막아 내며 진무경은 새어 나오려는 헛웃음을 삼켰다.

‘이놈 봐라.’

열흘. 짧다면 짧고, 길다면 긴 시간이다. 그러나 그게 일류 무공을 대성하기까지 걸린 시간이라면 이야기가 달라진다.

‘뭐 이런 놈이 다 있지?’

지난 열흘간 수십 번도 넘게 든 생각이다. 진태경의 성장 속도는 문일지십(聞一知十)이라는 말로도 부족했다.

‘아는 것과 체득하는 것은 다르니까.’

무공을 대성(大成)했다는 말은 그 무공을 완벽히 이해하고 펼칠 수 있게 되었다는 말이다. 진태경은 일류 무공 두 개를 단 열흘 만에 고스란히 자신의 것으로 만들었다.

이미 어느 정도 경지에 올라 있었다는 사실을 감안해도 이건 엄청난 성과다.

‘이게 되네.’

진무경은 어이가 없었다. 처음 예상치가 어느 정도였더라?

확실한 건 처음 목표를 훨씬 초월했다는 것 정도다.

‘시도 때도 없이 손발 나가는 버릇 고치고, 기본기나 확실히 잡아 주려고 한 건데…….’

막상 시작해 보니 이야기가 달라졌다.

기본기? 진무경은 알 길이 없는 일이지만 진태경은 칠 년간 끊임없이 수련해 왔다. 강해지기 위한 수련, 살기 위한 발버둥이었다.

손바닥 가죽이 수십 번 찢어지고 아물수록 그의 창도 빠르고 강해졌다. 그 때문에 진태경의 기본기는 약간의 자세 교정을 제외하면 흠잡을 곳이 없다.

‘다른 부분들도 마찬가지고.’

마보(馬步) 수련 역시 시간 낭비에 불과했다.

근력, 체력, 민첩. 그의 모든 신체 능력은 동급의 무인들을 훌쩍 상회하고, 매우 균형감 있게 발달해 있었다.

‘지금까지 살아남은 게 마냥 운 때문만은 아니었군.’

껑충하게 큰 키와 길쭉한 팔다리. 날렵하고 옹골찬 근육을 보라. 삼 년 전, 기녀들한테 잘 보이겠다고 복근을 만들던 말라깽이가 맞나 싶을 정도다.

‘염병, 무슨 천무지체(天武肢體)도 아니고.’

진무경이 다시 한번 황당함을 느낀 그때였다.

쐐애애액!

강맹한 기세로 찔러 들어오는 창.

진무경은 보법을 밟으며 물러났지만 진태경은 끈질기게 따라붙으며 공격을 이어 나갔다.

쉭! 쉬쉬쉭!

같은 무공이라도 누가, 어떻게 펼치느냐에 따라 달라진다. 한 수, 한 수에 그가 가진 기질과 성향이 고스란히 묻어 나오는 것이다.

지금 펼쳐지는 진무경의 진가창법도 마찬가지였다.

‘진가창법이 이런 무공이었나?’

무인과 낭인. 어딘지 모르게 삐걱대고 불안하던 움직임이 서서히 조화를 이루기 시작했다.

‘벌써 제 것으로 만들었다, 이거지.’

열흘 전의 진태경은 반쪽짜리였지만…… 이미 변화는 시작됐다. 진무경은 아우의 성취가 기특하면서도 한편으로는 뱃속이 뜨거워졌다.

‘이건.’

과거, 다른 누군가를 상대로 한 번 느꼈던 감정이다. 그 대상이 진태경이 될 줄은 꿈에도 몰랐지만.

‘질투. 그리고 호승심.’

진무경은 그 자리에 우뚝 굳어 버렸다. 그 찰나의 빈틈을 향해 진가창법의 마지막 초식, 천관일이 쏘아졌다.

“합!”

콰아아아-!

창을 중심으로 휘몰아친 바람이 진태경의 기합을 집어삼켰다. 금방이라도 가슴이 꿰뚫릴 것 같은 그 순간, 진무경의 손이 검자루를 잡았다.

푸화악!

허리춤에서 솟구친 섬광이 바람을 갈랐다. 그 끝에, 진태경이 있었다.



* * *



쉭!

짧은 바람 소리와 함께 상반신이 시원해진다. 오른쪽 허리춤부터 시작해서 왼쪽 어깨까지. 깔끔하게 잘려 나간 무복 사이로 지하 연무장의 싸늘한 공기가 스며들었다.

상처가 없다는 걸 확인한 후에야 안도의 한숨이 흘러나왔다.

“후.”

그나저나 갑자기 검기라니. 심장이 목구멍 밖으로 튀어나올 뻔했다.

“미친. 검기는 안 쓴다더니.”

“……그걸 곧이곧대로 믿은 놈이 멍청한 거지.”

영 석연치 않은 얼굴로 대답한 진무경이 검을 집어넣었다.

“수련은 여기서 마친다.”

띠링.



- [진무경]이 수련 종료를 선언했습니다.

- 남아 있는 [제한 시간]이 소멸합니다.

- [진무경]의 평가에 따라 퀘스트 성공 여부가 결정됩니다.



성공? 아니면 실패?

내 기대감 어린 눈빛을 받으며, 그가 입을 열었다.

“한참 멀었어.”

“아.”

“열흘 동안 고작 이 정도밖에 못 따라오다니. 내 시간이 아깝…….”

진무경이 말하다 말고 떫은 표정을 지었다.

“그 표정은 뭐지?”

“응? 뭐가.”

“지금 짓고 있는 해괴망측한 표정 말이다!”

“아닌데? 무슨 말 하는 건지 모르겠는데?”

하지만 진무경의 말이 맞았다.

나는 자꾸만 솟구치는 입꼬리를 감추느라 무진 애를 써야 했다. 허공에 떠오른 시스템 메시지 때문이었다.

띠링.



- 퀘스트 성공 조건을 충족했습니다!

- [수련? 시련!] 퀘스트를 완료했습니다!

- 레벨 업!

- 퀘스트 완료 보상이 인벤토리로 이동합니다!

- 훌륭한 성과입니다. 추가 보상이 주어집니다!



“음. 부끄러움이 많은 아이로구나.”

정직한 청년. 진무경.

“이놈! 그게 무슨 소리냐!”

“아냐, 넘어가. 스물셋이면 한창 수줍을 때지.”

“이 새끼가?”

눈깔이 뒤집힌 진무경이 내게 달려들려던 그 순간이었다.

끼이익.

지상으로 통하는 문이 열림과 동시에 웬 하인 하나가 빼꼼 고개를 내밀었다.



[Lv.12 장칠득]



“저어, 공자님들?”

한 사흘인가? 그쯤 전에 꼬박꼬박 식사를 가져다주던 하인이다. 못 본 사이에 무슨 일이 있었는지 얼굴은 멍투성이고 이빨이 네댓 개 부러졌다.

그가 새어 나가는 발음으로 말을 이었다.

“소가주님께서 찾으십니다.”

“……젠장.”

나와 칠득이를 번갈아 보던 진무경이 아쉬운 얼굴로 주먹을 내렸다.



* * *



우리는 안내를 따라 이동했다. 진무경은 뭐가 그렇게 못마땅한지 뚱한 얼굴로 땅만 쳐다보며 걸었고, 칠득이는 걸을 때마다 통증이 올라오는지 자꾸 앓는 소리를 냈다.

“아야, 어이쿠. 으헉.”

“…….”

거 더럽게 신경 쓰이네.

“어쩌다가 다쳤어요?”

“그, 사소한 오해가 있었습니다.”

사소한 오해치고는 제법 중한 부상을 당한 것 같은데.

현실에서야 포션이 있으니 못 고칠 병이 없다지만 무림은 다르다. 나는 칠득이의 부러진 이빨을 보며 혀를 찼다.

“많이 아프시겠네.”

“괜찮습니다.”

칠득이가 의연하게 가슴을 쭉 폈다.

“태원진가의 무인이라면 이 정도는 견뎌야죠.”

“…….”

방금까지만 해도 아파 죽으려고 하더니.

그런데 이 사람, 하인 아니었나?

‘그러고 보니 옷이 바뀌었네.’

그는 태원진가 소속 무인들이 입는 짙은 남색의 무복을 입고 있었다. 이전에는 하인들이 입는 옷을 입었던 것 같은데.

내 시선을 알아차린 그가 수줍게 웃었다.

“아. 며칠 전에 정식으로 무인이 됐습니다.”

“무인?”

뒤에서 말없이 걷고 있던 진무경이 불쑥 입을 열었다.

“어디 소속인가?”

내가 근래 들어서 아무리 유명세를 떨치고 있다지만 진무경만큼은 아니다. 칠득이가 황송하다는 얼굴로 대답했다.

“소가주님 직속입니다.”

“큰형님 직속은 본가 내에서도 선별된 무인들만 들어갈 수 있는 곳인데.”

진무경이 칠득이를 위아래로 훑었다. 깔보는 눈빛이라기보다는 상대의 경지를 가늠하는 관찰에 가까웠다.

“근골은 제법이지만 딱히 무공을 배운 것 같지는 않은데?”

“예에. 사실 저도 얼떨떨합니다. 무공이라고는 일초 반식도 제대로 펼쳐 본 적이 없어서요.”

[기감]으로 파악한 칠득이의 레벨은 12. 음식이나 나르던 하인치고는 높지만 무인으로 치면 삼류다.

‘진위경 직속 일류 고수들은 최소 40레벨이 넘던데.’

뭐지? 배경이 빵빵한가?

진무경도 나와 비슷한 생각을 했는지 눈살을 찌푸렸다.

“뒷배가 좋나 보군. 춘부장께서 무슨 일을 하시나?”

칠득이가 송아지처럼 커다란 눈망울을 깜빡였다.

“십 년 전에 돌아가셨는데요.”

“…….”

“…….”

“유명한 약초꾼이셨는데, 호환(虎患)을 당하셔서 그만.”

순간 눈앞이 아득해졌다. 절정 고수답게 가장 먼저 평정심을 되찾은 진무경이 황급히 수습에 나섰다.

“후, 훌륭한 분이셨군.”

“지금 생각해도 참 순박한 분이셨습니다. 어머니와 금슬도 좋으셨고요.”

“그럼 어머니께서는, 혹시? 아니지?”

“잘 계십니다.”

우리가 안도의 한숨을 내쉬던 그때, 칠득이가 아련한 눈빛으로 먼 산을 응시했다.

“아버지 곁에 묻어 드렸으니 두 분 모두 잘 계실 겁니다.”

“…….”

“…….”

그 후는 죽음의 행진이었다. 당장 전력을 다해 도망치고 싶었지만 칠득이의 혼잣말을 듣고 포기했다.

“아, 저 꽃 오랜만에 보네요. 아버지를 따라 산에 가면 참 많이 보였는데.”

“…….”

“…….”

일각만 더 함께 걸었다면 진무경은 자살했을지도 모른다. 그러나 다섯 시간 같은 5분이 흐른 뒤, 우리는 다행히 목적지에 도착할 수 있었다.

“오, 왔느냐!”

전각 앞에서 기다리고 있던 진위경을 보자 눈물이 날 것 같다. 우리는 물기 어린 목소리로 부르짖었다.

“혀엉!”

“형님!”

칠득이는 어색하게 포권을 취했다.

“분부대로 공자님들을 모셔 왔습니다.”

나와 진무경을 향해 한걸음에 달려오던 진위경이 멈칫하더니 칠득이를 껴안았다.

“인의예지를 갖춘 장칠득! 우리 장 무인 왔는가!”

“옛! 소가주님.”

“아주 큰 임무를 완수했네! 이만 가서 쉬도록 하게.”

이게 도대체 무슨 상황이야. 나와 진무경이 얼빠진 얼굴로 그 광경을 지켜보던 그때, 귓가를 파고드는 전음이 있었다.

- 그, 내가 이 친구랑 사소한 오해가 좀 있어서…….

“…….”

어쩐지 칠득이의 뒷배를 알 것 같다.
```

## Final English reading copy

```markdown
# Chapter 73

Ding. Ding. Ding.

The flood of System notifications was enough to make my ears hurt. I opened my mouth wide and dismissed the message windows filling my vision one by one.

*Why are there so many rewards?*

Two Level Ups, an increase to all my Stats, and a new Skill for completing an achievement.

*Martial Arts Manual Creation?*

Ding.

> **System**
>
> **Skill Window**
>
> **Martial Arts Manual Creation**
>
> **Grade:** None
>
> **Realm:** First Stage
>
> **Description:** Can create martial arts manuals for martial arts that have reached mastery.
>
> **Martial Arts Manuals Available:** Jin Family’s Spear Technique, Jin Family’s Manoeuvre Technique

After reading the description, I realized it was exactly what I had guessed.

*It’s a Skill, so it’s better than nothing, I suppose…*

For now, though, it did not seem particularly useful. I was mostly fascinated that the System would give me a Skill for some kind of production job.

*This really does feel like a game sometimes.*

There were still far too many things in this world that I had never experienced.

Everything was unfamiliar and unreal. Even now, I was still unsure whether Murim was a game or another reality altogether.

Smack!

“Ah.”

I turned around, clutching the back of my stinging head. Jin Mukyung was looking at me with a contemptuous expression, a wooden sword broken in half in his hand.

“Not concentrating?”

“Seriously. Why do you keep hitting me in the head? It’s annoying.”

“This bastard is slipping back into informal speech again.”

Jin Mukyung narrowed his eyes, but he was not very frightening anymore.

*It’s not like this is the first or second time I’ve been hit.*

Today marked the tenth day since the hellish training began.

I had realized one important fact right from the start.

*I get hit even when I use polite speech!*

I had been beaten black and blue. I had even gained the **Toughness** Stat on only the second day, which said everything that needed to be said. No matter what I did, I was going to get beaten anyway. If so, using informal speech while getting beaten at least let me claim a moral victory.

Smack!

“This much is just a tickle.”

The Toughness Stat had not appeared for no reason.

Just as flowers grew with sunlight and water, my Stats had flourished under merciless violence and hellish training.

Whack!

“Hey, wait. You hit bone. Bone.”

“The spar isn’t over.”

Thud-thud-thud!

While taking hits from the wooden sword as it struck my vital points with practiced precision, I swung my spear as well.

Sshh-shh-shhk! Crack!

Ten days of hellish training.

At last, the Jin Family’s Spear Technique and Jin Family’s Manoeuvre Technique flowed out as naturally as breathing, having reached mastery.

Ding.

> **System**
>
> **Time Limit:** 2 hours 22 minutes

Ding.

> **System**
>
> **Time Limit:** 2 hours 22 minutes

“…?”

What the hell? Why did it ring twice?

* * *

Sshh-shh-shhk!

Clang!

Blocking the spear pressing in on him, Jin Mukyung swallowed a laugh that was about to escape.

*Look at this bastard.*

Ten days. It was a short time if you thought of it one way, and a long time if you thought of it another. But if that was how long it took to achieve mastery of a First Rate martial art, the matter was entirely different.

*What kind of person is this?*

He had thought the same thing dozens of times over the past ten days. Jin Taekyung’s rate of growth was beyond even the saying “hear one, know ten.”

*Knowing something and making it your own are different.*

To achieve mastery of a martial art meant that one understood it perfectly and could wield it as such. Jin Taekyung had made two First Rate martial arts completely his own in only ten days.

Even taking into account the fact that he had already reached a certain level, this was an astonishing achievement.

*So it really is possible.*

Jin Mukyung was dumbfounded. What had his initial estimate been again?

One thing was certain: Taekyung had far surpassed his original goal.

*I was only trying to cure his habit of throwing out his hands and feet whenever he felt like it and make sure his fundamentals were solid…*

But once training began, things had changed.

Fundamentals? Jin Mukyung could not have known it, but Jin Taekyung had trained relentlessly for seven years. Training to become stronger. Struggling desperately to survive.

His palms split open and healed dozens of times, and with each cycle, his spear became faster and stronger. Because of that, there was nothing to criticize in Jin Taekyung’s fundamentals except for a few issues with his posture.

*The same goes for everything else.*

Horse-stance training would have been nothing more than a waste of time.

Strength, Stamina, Agility—every one of his physical abilities far surpassed those of martial artists at the same level, and they had developed with remarkable balance.

*So surviving until now wasn’t simply a matter of luck.*

Look at his tall, lanky frame and long limbs. At his lean, solid muscles. Was this really the same skinny brat who had built abdominal muscles three years ago to impress courtesans?

*Damn, was he some kind of heavenly martial physique?*

Jin Mukyung was feeling dumbfounded all over again when it happened.

Swoooosh!

A spear thrust forward with powerful momentum.

Jin Mukyung stepped back using his footwork, but Jin Taekyung tenaciously followed and continued his attack.

Sshk! Sshh-shh-shhk!

Even the same martial art changed depending on who wielded it and how they wielded it. Every move carried the wielder’s temperament and disposition.

The Jin Family’s Spear Technique Jin Mukyung was using now was no different.

*Was this what the Jin Family’s Spear Technique was supposed to be?*

Martial artist and wandering martial artist. Movements that had been awkward and uneasy in some indefinable way were gradually beginning to harmonize.

*He’s already made it his own.*

Ten days ago, Jin Taekyung had been half-finished, but the change had already begun. Jin Mukyung was proud of his younger brother’s achievement. At the same time, heat began to build in his stomach.

*This feeling…*

It was an emotion he had felt once before, toward someone else. He had never imagined that Jin Taekyung would become its object.

*Jealousy. And fighting spirit.*

Jin Mukyung froze in place.

Toward that momentary opening, the final form of the Jin Family’s Spear Technique, Sky-Piercing Strike, shot forward.

“Haap!”

Whoooosh!

The wind spiraling around the spear swallowed Jin Taekyung’s shout. At the moment when it seemed the spear was about to pierce straight through his chest, Jin Mukyung’s hand seized his sword hilt.

Fwoosh!

A flash erupted from his waist and cleaved through the wind.

At its end stood Jin Taekyung.

* * *

Sshk!

With a short rush of wind, my upper body suddenly felt breezy. Starting from my right waist and ending at my left shoulder, my martial arts uniform had been sliced cleanly apart, and the chilly air of the underground training hall seeped through the gap.

Only after confirming that I had not been injured did I let out a relieved sigh.

“Whew.”

A Sword Energy attack out of nowhere? My heart had nearly jumped out of my throat.

“Crazy. You said you weren’t going to use Sword Energy.”

“……Only an idiot would take that at face value.”

Jin Mukyung answered with a distinctly uneasy expression and sheathed his sword.

“Training ends here.”

Ding.

> **System**
>
> - **Jin Mukyung** has declared the training complete.
>
> - The remaining **Time Limit** has vanished.
>
> - Quest success will be determined according to **Jin Mukyung’s** evaluation.

Success? Or failure?

With my eyes shining expectantly, he opened his mouth.

“You’re nowhere near good enough.”

“Ah.”

“To think this is all you managed to keep up with me after ten days. What a waste of my ti—”

Jin Mukyung stopped speaking and made a sour face.

“What’s with that expression?”

“Huh? What expression?”

“That bizarre expression you’re making right now!”

“I’m not making one. I have no idea what you’re talking about.”

But Jin Mukyung was right.

I had to make a tremendous effort to hide the corners of my mouth, which kept trying to rise. The reason was the System message floating in the air.

Ding.

> **System**
>
> - You have fulfilled the conditions for quest success!
>
> - Quest **Training? Trial!** has been completed!
>
> - Level Up!
>
> - The Quest completion Reward has been moved to your Inventory!
>
> - Excellent work. An additional Reward will be granted!

“Hm. You’re a shy child, aren’t you?”

Jin Mukyung. An honest young man.

“You bastard! What the hell is that supposed to mean?”

“No, forget it. At twenty-three, you’re still at the age when you get embarrassed easily.”

“You little—”

Jin Mukyung’s eyes went wild, and he was just about to charge at me.

At that moment—

Creak.

The door leading to the surface opened, and a servant cautiously poked his head inside.

> **System**
>
> **Level 12: Jang Childeuk**

“Um, Young Masters?”

He was the servant who had brought us meals regularly until about three days ago. Something had clearly happened while we had not seen him. His face was covered in bruises, and four or five of his teeth were broken.

He continued speaking through his damaged mouth.

“The Lesser Family Head is looking for you.”

“……Damn it.”

Jin Mukyung looked back and forth between Childeuk and me, then reluctantly lowered his fist.

* * *

We moved according to Childeuk’s directions. Jin Mukyung walked along with a sour expression, staring only at the ground as if everything offended him. Childeuk kept groaning whenever pain shot through him with each step.

“Ow. Good grief. Urgh.”

“……”

What a pain in the ass.

“How did you get hurt?”

“There was a small misunderstanding.”

That seemed like a fairly serious injury for a small misunderstanding.

In the modern world, there were potions, so there was no ailment they couldn’t cure. Murim was different. I clicked my tongue as I looked at Childeuk’s broken teeth.

“That must hurt.”

“It’s all right.”

Childeuk puffed out his chest with stoic resolve.

“A martial artist of the Jin Family of Taiyuan must be able to endure this much.”

“……”

He had been acting like he was about to die from the pain just moments ago.

But wasn’t this man a servant?

*Come to think of it, his clothes have changed.*

He was wearing the dark navy martial arts uniform worn by martial artists of the Jin Family. I thought he had been wearing a servant’s clothes before.

Noticing my gaze, he smiled shyly.

“Oh. I officially became a martial artist a few days ago.”

“A martial artist?”

Jin Mukyung, who had been walking silently behind us, suddenly spoke.

“Under whose command?”

I might have made a name for myself lately, but I was still nowhere near as famous as Jin Mukyung. Childeuk answered with an awestruck expression.

“I’m directly under the Lesser Family Head.”

“Only specially selected martial artists within our family can serve directly under our eldest brother.”

Jin Mukyung looked Childeuk up and down. His gaze was not contemptuous so much as observant, as though he were estimating Childeuk’s level.

“Your physique is decent, but you don’t seem to have learned any martial arts.”

“Yes. I’m still bewildered myself. I’ve never properly performed even a single form of martial arts.”

Childeuk’s Level, as determined through **Sense**, was twelve. That was high for a servant who had done nothing but carry food, but he was Third Rate by martial-artist standards.

*The First Rate masters directly under Jin Wikyung are at least Level 40.*

What was going on? Did he have powerful backing?

Jin Mukyung seemed to have reached the same conclusion. His brow furrowed.

“You must have good connections. What does your father do?”

Childeuk blinked his large, calf-like eyes.

“He died ten years ago.”

“……”

“……”

“He was a famous herbalist, but he was killed by a tiger.”

For a moment, my vision went hazy. As befitted a Peak master, Jin Mukyung was the first to regain his composure and hurriedly tried to smooth things over.

“Whew. He sounds like he was an excellent man.”

“Even now, I remember him as such an innocent man. He and my mother were very loving, too.”

“Then your mother, perhaps? No, never mind.”

“She’s doing well.”

Just as we let out sighs of relief, Childeuk gazed wistfully at a distant mountain.

“I buried her beside my father, so I’m sure they’re both doing well.”

“……”

“……”

What followed was a march of death. I wanted to run away at full speed, but I gave up after hearing Childeuk muttering to himself.

“Oh, I haven’t seen those flowers in a long time. I used to see them everywhere when I went into the mountains with my father.”

“……”

“……”

If we had walked together for another fifteen minutes, Jin Mukyung might have killed himself. Fortunately, after five minutes that felt like five hours, we reached our destination.

“Oh, you’re here!”

Seeing Jin Wikyung waiting in front of the pavilion nearly brought tears to my eyes. We cried out in voices thick with emotion.

“Hyuung!”

“Hyung-nim!”

Childeuk awkwardly clasped his hands in a formal salute.

“As ordered, I have escorted the Young Masters here.”

Jin Wikyung, who had been hurrying toward Jin Mukyung and me, suddenly stopped and embraced Childeuk.

“Jang Childeuk, a man of benevolence, righteousness, propriety, and wisdom! Is that you, Martial Artist Jang?”

“Yes, sir, Lesser Family Head!”

“You’ve completed a very important mission! Go and rest now.”

What on earth was happening? Jin Mukyung and I stared blankly at the scene.

Then a voice reached my ear through Sound Transmission.

*There was, uh, a minor misunderstanding between me and this fellow…*

“……”

Somehow, I thought I knew who was backing Childeuk.
```
