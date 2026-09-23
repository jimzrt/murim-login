<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0753.txt",
      "sha256": "01b3db1474a7d28da4ba0f1b0e71f35e321ef0b7cf22acb5d4dc5333a5836338",
      "bytes": 12725
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ec320e1019cda1b0525504f12e9539c9e2f50279105bc8343e056615d4d24488",
      "bytes": 1451
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "72e3b8b0fe2336fc4fa4e232faecbef9df5f7eb854b9ada6de9c8470d2fb11bd",
      "bytes": 217894
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7728ca01e51a5fc97e36245fc69641635ec8ab94108e455c54491154b564250c",
      "bytes": 553
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "627d75f8b4f1b01fec1bed774af75505ae108ee571c87023cb22d00bea81a0ba",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6ebc580d01012225d667bce02764a88f40a1addea886efe0606e0b4703b0024c",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "fa27e076f6b55187c3202ae3bba6239a29483f7e676d100bc641bf0fad655d8a",
      "bytes": 622
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "adf2fc50e08355893bf9a9698541a75c115f4c2c5b6ebfc955d748a99c2f8b6a",
      "bytes": 746
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "762c8f86c3298808d54a583903bbbc3b2bb240cbf112a9a371958a211e10600b",
      "bytes": 231612
    }
  ],
  "estimated_tokens": 9687
}
-->

# Durable State Update — Chapter 753

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 753. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 753. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 753,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 753,
    "continuity_sources": [753],
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
    "Public opinion is shifting away from Jin Taekyung's critics and toward blaming Japan's Defense Ministry for Leviathan's escape.",
    "Michael and Huginn are preparing to leave after a press conference for another undisclosed operation connected to Odin Guild's larger plan.",
    "Michael wants Jin Taekyung and Leviathan to kill each other and regards Jin's death as the ideal outcome.",
    "Michael feels growing impatience and anxiety toward Jin, which recalls his former humiliation beneath Cheon Taemin.",
    "Leviathan is severely wounded, hiding in the deep sea, and hungry for magical power after absorbing S-rank Magic Gems and marine life.",
    "Leviathan has recognized a small boat carrying immense magical power as a probable human trap but is moving toward it because of its hunger."
  ],
  "continuity_sources": [
    752
  ],
  "open_questions": [
    "What is Odin Guild's next destination and operation after the Japanese press conference?",
    "Will Leviathan reach the bait vessel and trigger the humans' planned trap?",
    "What are the full conditions of Michael's prepared plan against Jin Taekyung?"
  ],
  "safe_through": 752,
  "temporary_decisions": [
    "Render 마력 as magical power, distinct from mana.",
    "Render 마정석 and 마정 as Magic Gem when referring to monster power sources.",
    "Render 심해 as the deep sea and 생기 as vital energy."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 낭인     | **wandering martial artist**                     |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 대성 | **Great Completion** | Completion stage of a martial technique. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 귀식대법 | **Turtle Breath Technique** | Cheongpung’s joking description of breath-holding and suspended bodily functions. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 선미 | **stern** | The rear of the swift ship. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 일본 | **Japan** | Country requesting emergency assistance and under Leviathan's attack. |
| 마정 | **Magic Gem** | Monster power source; Leviathan seeks an untouched one. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 752
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 752
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 752
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 752
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 752
- **Aliases:** None
- **Role:** Leviathan is an ancient S-rank sea monster and ruler of the sea that remains severely wounded in the deep sea after Jin Taekyung's attack, has absorbed S-rank Magic Gems and marine life, and is now moving toward a human trap drawn by its immense magical power.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus, its master, and withdrew into the deep sea after Asmodeus fell.

## Korean source

```text
＃753화



남자는 주위를 바라보며 생각했다.

참 좋은 날씨였다. 20여 시간 전만 하더라도 미친 듯이 요동치던 바다는 잠잠했고, 맑아진 하늘 위에는 갈매기가 무리 지어 날아가고 있었다.

‘아름답군. 이것이 자연인가?’

남자가 지내던 장소는 이렇지 않았다. 멀고도 먼 어딘가에 있는 그곳은 언제나 밤처럼 어두컴컴했고 끔찍한 악취가 풍겼다. 물론 개인적인 사정으로 악취 따위는 맡아 본 적도 없지만, 틀림없이 그랬을 것이다.

여하튼 남자는 이 세상이 좋았다.

지금껏 볼 수 없던 아름다운 풍경을 볼 수 있다는 점에서, 그리고 썩 괜찮은 사람들과 함께하고 있다는 점에서 더더욱.

“…….”

다시 생각해 보니 그중에서 한 놈. 아니, 두 놈은 빼야 할 것 같다.

남자, 스켈레톤 킹은 문득 몇 시간 전 누군가와 나누었던 대화를 떠올렸다.



‘무엇이든?’

‘어?’

‘뭐든 한다고 했다, 맞지?’

‘어어?’

‘세상에, 이토록 숭고한 희생정신이라니. 본 대대장은 진심으로 감동했다.’

‘희생정신? 무슨 희생정신?’

‘쉿. 그만. 알아. 네 마음 다 아니까 더 이상은 시치미 떼지 마.’

‘Holy Shit……?’



쎄했다.

뭔가 일이 이상하게 흘러가고 있었다.

간절히 도움을 청하는 눈빛으로 다른 인간을 바라봤지만, 그나마 멀쩡하다고 생각했던 그놈도 한통속인 건 마찬가지였다.



‘저기, 잘생기고 똑똑한 인간아…….’

‘말 걸지 마십시오. 지금은 가슴이 벅차올라 대답하기 어렵습니다.’

‘이 개 같은 인간아…….’

‘다시 봤습니다, 미스터 킹. 대의를 위해 스스로를 희생하다니.’

‘아니, 희생한다는 말은 안 했는데 왜 아까부터 자꾸…….’

‘우리 모두 이 희생을 영원히 잊지 않겠습니다. 당신이야말로 진정한 영웅입니다.’

‘멈춰! 왜 다가오는 것이냐!’



이상함을 넘어 위기감을 느꼈을 때는 이미 늦었다.

어느새 문을 가로막은 진태경이 한 뭉텅이의 밧줄을 들고 슬금슬금 다가오고 있었으니까.



‘조심스럽게 얘기할래요. 용기 내 볼래요.’

‘이상한 노래 부르지 마! 손에 든 밧줄 내려 놔!’

‘나 오늘부터 그대를 미끼 삼고 싶어요.’

‘세상에 그딴 가사를 가진 노래가 어디 있어! 개사하지 마!’

‘최 팀장님, 안 붙잡고 뭐 합니까. 나만 나쁜 놈이에요?’

‘아, 죄송합니다. 눈물을 닦느라 잠시.’

‘썩 꺼져어어엇!’



촤아아악! 투두둑!

저 멀리서 몰려온 파도가 작은 통통배의 선미에 부딪힌다.

얼굴에 시원하게 끼얹어진 바닷물로 인해 상념에서 깨어난 스켈레톤 킹이 중얼거렸다.

“……빌어먹을.”

당연하게도 반항은 무의미했다.

믿고 있던 인간 놈들은 그를 앞뒤로 에워쌌고, 만악의 근원이나 다름없는 진태경은 재판관처럼 엄숙하게 선언했다.



‘괜한 소란 피우지 마. 순순히 미끼가 된다면 유골사태는 일어나지 않는다.’

‘유혈사태 아닙니까?’

‘쟤는 피가 없잖아요.’

‘아.’

‘그래서, 어쩔래?’



어쩌긴 뭘 어쩌겠나.

이미 주사위는 던져졌고 그건 타짜들에 의해 조작된 주사위였다.

레비아탄보다 먼저 함정에 빠진 것을 깨달은 스켈레톤 킹은 유골사태를 피하고 순순히 통통배에 올랐다.

사전에 일본 정부에서 제공한 S급 마정석 두 개와 함께.



‘이 거추장스러운 건 치워라. 어차피 나 혼자만으로도 놈이 군침을 흘릴 테니까.’

‘아니지. 넌 삼겹살 먹을 때 쌈장이랑 파채도 없이 먹냐?’

‘……이 몸이 레비아탄에게 먹히는 건 벌써 확정된 거냐?’

‘걱정하지 마. 쌈장에 찍을 때쯤에 구해 줄게.’

‘만약 한입에 삼키면?’

‘와, 진짜 맛있겠다.’

‘……구해 주는 거 맞지?’

‘갑자기 소주 땡기네. 안 그래요, 최 팀장님?’

‘저는 와인이 취향이긴 한데, 확실히 삼겹살에는 소주가 맞습니다.’

‘구해 주는 거…… 정말 확실하지?’



그게 마지막이었다.

한 명의 S급 몬스터와 두 개의 S급 마정석을 실은 통통배는 대답을 듣기도 전에 출발했고, 사전에 입력된 GPS를 따라 수백 킬로미터 밖에 떨어진 무인도 인근을 배회하기 시작했다.

한 시간 전부터 지금까지 쭉.

깊은 바닷물 속 어딘가에 숨어 있을 대물(大物)이 미끼를 물기를 기다리며.

“이 개 같은 인간 놈들.”

푸른 하늘을 바라보며 한탄한 스켈레톤 킹은 있지도 않은 심장이 쿵쿵 뛰는 것을 느꼈다.

‘진짜로 놈이 나타나면 어떡하지?’

스켈레톤 킹은 레비아탄과의 힘의 격차를 똑똑히 인지하고 있었다.

이성(理性)조차 없었던 과거의 자신과 달리, 상대는 첫 탄생부터 강대한 마력을 부여받은 포식자. 소위 말해 근본부터가 달랐다.

마계에서는 이른바 ‘72군단장’이라 칭해지는 S급 몬스터 중에서도 열 손가락 안에 꼽히던 존재가 바로 레비아탄이었으니까.

비록 과거의 위명에 비해 그 힘이 약해졌다고는 해도, 한번 마음에 내려앉은 두려움은 쉽게 사라지지 않았다.

‘오지 마라. 오지 마라. 제발 오지 마라…….’

스켈레톤 킹은 이 세상이 마음에 들었다.

이미 죽어 있는 자신과는 반대로 생기(生氣)를 머금은 자연. 화려하면서도 신기한 문물로 가득한 도시과 눈부신 미모의 인간 여자들.

간혹 어떤 인간들이 보이는 모습들에 환멸이 날 때도 있었지만 대부분은 괜찮았고, 처음에는 낯설었던 친구라는 단어에 조금씩 익숙해지고 있었다.

하지만 그런 그에게 있어서도 레비아탄에게 먹혀 영양분이 되는 건 사양이었다.

스켈레톤 킹은 한 끼 든든한 삼겹살 정식이 되어버린 자신의 모습에 눈물이 날 것 같았다.

‘이 빌어먹을 인간 놈들아, 제발 같이 좀 살자!’

레비아탄이 나타날까 봐 크게 소리 내어 외칠 수도 없는 현실에 더 서글퍼졌지만, 돌이키기에는 이미 너무 늦었다.

스켈레톤 킹은 목에 건 쌈장과 파채. 아니, S급 마정석 두 개를 매만지며 바다를 노려봤다.

‘그래, 한번 죽지 두 번 죽냐.’

인간들이 자주 쓰는 말을 마음속으로 뇌까리자, 어디 숨어 있었는지 모를 용기가 솟구쳤다.

심지어 인간들과 달리 자신은 진짜 죽기까지 했다. 남은 건 뼈밖에 없으니 몇 번 씹힌다고 해도 어찌어찌 살 수 있을지 모른다. 이빨에 끼기라도 하면 더 좋고.

“와라, 이 괴물아! 이 몸이 상대해 주마!”

그리고 스켈레톤 킹이 용맹한 외침을 토해 낸 바로 그 순간.

찌지지직. 철퍽.

허공에서 떨어져 내린 무언가가 그의 정수리와 어깨를 뒤덮었다.

어리둥절한 얼굴로 끈적하면서도 새하얀 그것을 문지른 스켈레톤 킹이 인상을 구겼다.

똥.

그것도 따끈따끈한 새똥이었다.

“깃털을 죄다 뽑아 버릴 놈들 같으니.”

작게 으르렁거린 스켈레톤 킹은 고개를 쳐들었다.

아니나 다를까. 언제부턴가 인간을 무료 급식소로 생각하고 통통배를 쫓아다니던 갈매기 무리가 그의 머리 위를 배회하는 중이었다.

정확히는 똥오줌을 흩뿌리며 저 멀리 어딘가를 향해 날아가는 중이라고 해야 옳았겠지만.

“눈치 하나는 더럽게 빠르…….”

문득 말꼬리를 흐린 스켈레톤 킹의 동공이 흔들렸다.

어느새 크게 뜨인 그의 눈동자에, 반대편 하늘을 까맣게 물들이며 날아오는 날짐승들이 보였다.

‘새라고? 저게 전부?’

스켈레톤 킹이 멍하니 입을 벌린 사이, 조류 학자도 구분하기 어려울 만큼 다양한 종이 뒤섞인 수천수만 마리의 새들은 그의 머리를 지나 이미 저 멀리 날아가는 갈매기 무리의 뒤를 쫓았다.

아니, 아니다.

저건…….

‘도망.’

순간 스켈레톤 킹의 뇌리를 가득 채운 그 두 글자와 함께. 고요하던 바다가 요동치기 시작했다.

구구구궁!

해저(海底) 깊숙한 곳에서 시작된 울림.

그리고.

촤아아악!

세상을 집어삼킬 듯이 솟구친 삼각파도와 그 안에서 일렁이는 거대한 그림자.

- 그아아아아아!

흉포한 괴성이 필리핀해를 떨어 울린다.

길이만 삼백여 미터에 달하는 신화 속 괴물이, 자그마한 통통배에 차려진 만찬을 향해 아가리를 벌린 그 순간.

“23시간 만이다. 이 시벌 새끼야.”

누구도 예상치 못했던 한 사람의 목소리와 함께, 세찬 화염이 수분을 증발시키며 쏘아졌다.

퍼걱!



* * *



무림에는 귀식대법(龜息大法)이라는 무공이 있다.

정확히 말하자면, 사실 무공보다는 수법에 가깝다.

하지만 중요한 것은 바로 이 귀식대법으로 호흡과 심장박동을 최대한 억제하고, 체온마저 하강시킬 수 있다는 점이다.

한 마디로 일정 시간 동안 생기(生氣)를 지우는, 괴이한 수법인 데다 뛰어난 공력과 무위를 필요로 하기 때문에 무림에서도 귀식대법을 익히는 이는 드물었다.

사실 무림인이라는 별종들에 대해 조금이라도 안다면 당연한 일이었다.

당장 목숨이 왔다 갔다 하는 와중에도 초식 이름까지 외치며 싸우는 겉멋충들이 득실거리는 마당에 시체 코스프레라니.

그러니 땅이라도 나뒹구는 날에는 나려타곤(懶驢打滾)을 대성했다면서 수치 플레이를 당하는 그 바닥에서, 귀식대법을 익히는 부류는 극히 한정될 수밖에 없었다.

사파. 낭인.

그리고…….

‘살수(殺手).’

앞서 나열한 두 직업군과 달리 살수라는 놈들은 살면서 한번 보기도 힘든 희귀종이다.

옷깃까지 스쳤다고 해도 살수인 걸 눈치채지 못하고, 만약 눈앞의 상대가 살수인 걸 알아차린다면 이미 어느 정도 좆 된 거다.

그러나 살수를 만나도 도움이 될 때가 있다.

특히 그 살수의 별호가 살성(殺星)일 경우에는 더더욱.



‘네놈에게 뭘 가르쳐야 할지 잘 모르겠군. 그렇다고 화왕의 후인씩이나 되는 녀석에게 귀식대법 같은 것을 가르쳐 줄 순 없는 노릇…….’

‘와, 귀식대법!’

‘……?’

‘가르쳐 주세요! 살고 싶어요!’

‘……네놈, 정파 아니냐?’

‘정파는 칼 맞아도 안 뒈집니까?’

‘아니, 그래도 무공을 더 발전시키는 것이…….’

‘귀식대법! 귀식대법! 생존! 태경그릴스!’

‘알았으니 제발 진정해라. 자꾸 이상한 헛소리 좀 하지 말고.’



한 마디로 운이 좋았다.

살수계의 리빙 레전드는 대치동 1타 강사 뺨치는 강의 실력을 지니고 있었고, 몸으로 하는 거라면 뭐든지 잘하는 나는 스펀지처럼 그의 가르침을 흡수했으니까.

물론 그때 배운 귀식대법을 무림이 아닌 현대에서 먼저 쓰게 될 줄은 꿈에도 몰랐지만, 적어도 효과 하나는 확실했다.

퍼걱!

청백색의 화염을 머금은 한 자루의 창이 컴컴한 괴수의 아가리로 빨려 들어간다.

아니, 어느새 다시 자라난 놈의 이빨을 부수고 입천장에 틀어박혔다.

- 크아아아아!

콰드드득!

괴성과 함께 몸부림치는 거대한 동체에 통통배가 수수깡처럼 으스러졌다.

나는 눈을 부릅뜬 채 이쪽을 바라보는 스켈레톤 킹의 뒷덜미를 붙잡고, 침몰 직전의 배를 박차며 솟구쳤다.

쾅!

등 뒤에서 터져나간 파편이 어깨를 스쳤다. 거센 바람이 전신을 스친다. 나는 보이지 않는 계단을 밟고, 허공에 우뚝 섰다.

크르르륵.

거친 숨소리. 악어를 닮은 레비아탄의 거대한 눈동자가 세로로 길게 찢어진다.

- 네놈. 네놈이 어떻게…….

“아, 그거. 말하자면 길지.”

나는 씩 웃으며 말을 이었다.

“말해 줄 생각도 없고.”

인벤토리 오픈. 소환.

말과 동시에 이루어진 생각과 함께, 나는 손에 들린 창을 쏘아 보냈다.

콰아아아!
```

## Final English reading copy

```markdown
# Chapter 753

The man looked around and thought,

*What wonderful weather.*

Only a little over twenty hours ago, the sea had been bucking like mad. Now it was calm, and gulls flew in flocks across the clear sky.

*Beautiful. Is this nature?*

The place where the man had lived was nothing like this. That distant, distant place was always dim and dark as night, with a terrible stench hanging in the air. Of course, for personal reasons, he had never smelled a stench in his life, but there was no doubt the place had reeked.

In any case, the man liked this world.

He liked it even more because he could see beautiful scenery he had never witnessed before, and because he was surrounded by some pretty decent people.

“……”

Thinking it over again, though, he supposed he had to exclude one of them.

No, two.

The man—the Skeleton King—suddenly remembered a conversation he had shared with someone a few hours earlier.



“Anything?”

“Huh?”

“You said you’d do anything, right?”

“Huh?”

“My goodness, such a noble spirit of sacrifice. As battalion commander, I am genuinely moved.”

“A spirit of sacrifice? What are you talking about?”

“Shh. Enough. I know. I know all about your heart, so stop pretending.”

*Holy shit…?*



Something felt off.

Things were taking a strange turn.

He looked toward another human with an expression that desperately pleaded for help, but even the man he had thought was at least somewhat sane turned out to be in on it.



“Hey, handsome and intelligent human…”

“Please don’t speak to me. My heart is too full right now to answer.”

“You son of a bitch…”

“I see you in a new light, Mr. King. To sacrifice yourself for the greater good…”

“I never said anything about sacrificing myself, so why do you keep saying that…?”

“We will never forget this sacrifice. You are a true hero.”

“Stop! Why are you coming closer?”



By the time he sensed that this was more than just strange—that he was in danger—it was already too late.

Jin Taekyung was blocking the door and creeping toward him with a bundle of rope in his hands.



“I’ll talk to you carefully. I’ll try to find my courage.”

“Don’t sing some weird song! Put down the rope!”

“From today on, I want to use you as bait.”

“What song has lyrics like that? Don’t rewrite it!”

“Team Leader Choi, what are you doing just standing there? Am I the only bad guy?”

“Ah, my apologies. I was wiping away my tears.”

“Get the hell out of here!”



*Whooosh! Rattle!*

A wave that had rolled in from far away crashed against the stern of the little motorboat.

The seawater splashed refreshingly across his face, jolting the Skeleton King out of his thoughts. He muttered,

“……Damn it.”

Naturally, resisting had been pointless.

The humans he had trusted had boxed him in from the front and rear, while Jin Taekyung—the root of all evil—solemnly declared, like a judge delivering a verdict:



“Don’t make a needless fuss. If you willingly become bait, there won’t be a boneshed.”

“Isn’t it supposed to be bloodshed?”

“He doesn’t have any blood.”

“Oh.”

“So, what’ll it be?”



What else could he do?

The die had already been cast—and it was a loaded die controlled by hustlers.

Realizing that he had fallen into the trap before Leviathan, the Skeleton King chose to avoid a boneshed and obediently boarded the little boat.

Along with the two S-rank Magic Gems provided in advance by the Japanese government.



“Get rid of these cumbersome things. The monster will drool over me even if I’m alone.”

“No, no. Do you eat samgyeopsal without ssamjang and scallion salad?”[^1]

“……Has it already been decided that this body will be eaten by Leviathan?”

“Don’t worry. We’ll save you when it’s time to dip you in the ssamjang.”

“What if it swallows me in one bite?”

“Wow, that sounds delicious.”

“……You are going to save me, right?”

“I suddenly feel like having some soju. Don’t you think so, Team Leader Choi?”

“I do prefer wine, but soju definitely goes with samgyeopsal.”

“You’re definitely going to save me… right?”



That was the last thing he heard.

The little boat, carrying one S-rank monster and two S-rank Magic Gems, set off before he even received an answer. Following the GPS coordinates entered beforehand, it began circling near an uninhabited island several hundred kilometers away.

It had been doing so for the past hour.

Waiting for the big one hiding somewhere in the deep sea to take the bait.

“You damn humans.”

The Skeleton King looked up at the blue sky and lamented. He could feel a nonexistent heart pounding in his chest.

*What if the monster really shows up?*

The Skeleton King was fully aware of the difference in strength between himself and Leviathan.

Unlike his former self, who had not even possessed reason, Leviathan was a predator endowed with immense magical power from the moment of its birth. In other words, they were fundamentally different.

Leviathan had ranked among the top ten even among the S-rank monsters known in the Demon Realm as the “Seventy-Two Legion Commanders.”

Even if its strength had declined compared to its former reputation, fear that had once settled in his heart did not disappear easily.

*Don’t come. Don’t come. Please don’t come…*

The Skeleton King liked this world.

Unlike himself, who was already dead, nature was filled with vital energy. The cities were packed with dazzling, wondrous things, and there were human women of blinding beauty.

Sometimes, the sight of certain humans disgusted him, but most of them were decent enough. He was even gradually getting used to the word *friend*, which had felt so unfamiliar at first.

But even for him, becoming nourishment for Leviathan was out of the question.

The Skeleton King felt as though he might cry when he imagined himself turned into a hearty samgyeopsal set meal.

*You damn humans, please let me live too!*

He was even more miserable because he could not shout aloud for fear of attracting Leviathan’s attention, but it was already far too late to turn back.

The Skeleton King touched the ssamjang and scallion salad hanging around his neck.

No—the two S-rank Magic Gems.

He glared at the sea.

*Right. You only die once, not twice.*

As he repeated a phrase humans often used, courage he did not know he possessed welled up inside him.

Besides, unlike humans, he had actually died before. There was nothing left but bones, so maybe he could somehow survive being chewed a few times.

It would be even better if he got stuck between the monster’s teeth.

“Come on, you monster! I’ll take you on!”

And at the very moment the Skeleton King released that brave shout—

*ZZZT. Splat.*

Something fell from the sky and covered the crown of his head and one shoulder.

The Skeleton King rubbed the sticky, glaringly white substance with a bewildered expression, then scowled.

Shit.

Fresh bird shit, too.

“I ought to pluck every last feather off those bastards.”

Growling under his breath, the Skeleton King lifted his head.

As expected, a flock of gulls had been circling above him for some time. They had apparently decided that humans were free cafeterias and had been following the little boat.

More precisely, they were flying somewhere far away while scattering their droppings and urine.

“They’ve got one hell of a sense of—”

The Skeleton King suddenly let his voice trail off, and his pupils began to tremble.

His eyes widened.

Across the opposite sky, a mass of flying creatures was approaching, blackening the heavens.

*Birds? All of those?*

As the Skeleton King stared blankly with his mouth hanging open, tens of thousands of birds of countless different species—so mixed together that even an ornithologist would have struggled to distinguish them—flew over his head and chased after the gulls already disappearing into the distance.

No.

That wasn’t it.

That was…

*They were fleeing.*

Together with those two words filling the Skeleton King’s mind, the calm sea began to heave.

*Rumble, rumble, rumble!*

A vibration rising from deep beneath the seafloor.

And then—

*Whooosh!*

A triangular wave surged upward as though it intended to swallow the world, a massive shadow undulating within it.

“GRAAAAAAAH!”

A savage roar shook the Philippine Sea.

The moment the three-hundred-meter-long monster of myth opened its jaws toward the feast laid out on the tiny boat—

“It’s been twenty-three hours. You piece of shit.”

Along with the unexpected voice of one man, a fierce flame shot forward, evaporating the moisture in its path.

*Thud!*



* * *



There is a martial art in the Murim called the Turtle Breath Technique.

To be precise, it is closer to a method than a martial art.

But what matters is that the Turtle Breath Technique can suppress breathing and heartbeat as much as possible, even lowering the body’s temperature.

In short, it is a strange method that erases a person’s vital energy for a certain amount of time. Since it also requires excellent internal energy and martial prowess, few people in the Murim learned it.

In fact, that was only natural if you knew anything at all about the strange species known as martial artists.

Even with their lives hanging in the balance, the Murim was crawling with show-offs who shouted the names of their forms as they fought. And you expected them to play dead?

In that world, where even rolling around on the ground could earn you a humiliating performance as people claimed you had achieved Great Completion in Narye tagon, the people who learned the Turtle Breath Technique were bound to be extremely limited.

The unorthodox faction.

Wandering martial artists.

And…

*Assassins.*

Unlike the two occupations listed above, assassins were such rare creatures that it was difficult to see one even once in your lifetime.

Even if an assassin brushed past your sleeve, you would not realize what they were.

And if you did recognize that the person standing before you was an assassin, you were already pretty damn screwed.

Still, meeting an assassin could sometimes be helpful.

Especially if that assassin’s epithet was the Slaughter Saint.



“I’m not sure what I should teach you. But I can’t exactly teach something like the Turtle Breath Technique to the Fire King’s successor…”

“Wow, the Turtle Breath Technique!”

“……?”

“Teach me! I want to live!”

“……Aren’t you from the orthodox faction?”

“Do orthodox martial artists not die even when they get stabbed?”

“No, but it would be better to further develop your martial arts…”

“Turtle Breath Technique! Turtle Breath Technique! Survival! Taekyung Grylls!”

“I understand, so please calm down. Stop spouting weird nonsense.”



In short, I had been lucky.

The living legend of the assassin world had teaching skills that could put even Daechi-dong’s top cram-school instructor[^2] to shame, and I was good at anything that involved using my body, so I absorbed his teachings like a sponge.

[^2]: Daechi-dong is a Seoul neighborhood famous for its intensely competitive private academies.

Of course, I had never dreamed that I would use the Turtle Breath Technique in the modern world before using it in the Murim.

But at least its effectiveness was unquestionable.

*Thud!*

A spear wreathed in blue-white flames was sucked into the dark monster’s maw.

No—it shattered the teeth that had already grown back and embedded itself in the roof of its mouth.

“GRAAAAAAAH!”

*Crack-crack-crack!*

As the enormous body thrashed with a roar, the little motorboat crumpled like a stalk of dried grass.

I grabbed the Skeleton King by the back of his neck as he stared at me with wide eyes, then kicked off from the sinking boat and shot upward.

*Boom!*

Fragments exploding behind me grazed my shoulder. Strong wind whipped across my entire body.

I stepped on an invisible staircase and came to a stop in midair.

*Grrrrr.*

Ragged breathing.

The pupils of Leviathan’s enormous crocodilian eyes narrowed into long vertical slits.

“You. How could you…”

“Ah, that? It’s a long story.”

I continued with a grin.

“And I have no intention of telling you.”

Inventory open. Summon.

Along with the thought that accompanied the words, I hurled the spear in my hand.

*Whoooooom!*

[^1]: Samgyeopsal is grilled pork belly, traditionally eaten with ssamjang, a savory dipping paste, and pa-chae, a shredded scallion salad.
```
