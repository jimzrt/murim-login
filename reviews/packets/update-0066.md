<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0066.txt",
      "sha256": "c059d37f94fac6fb30ebbe27185a4f4bf246e88da5a83c69cef8cc1d4f2aee55",
      "bytes": 12997
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "72d273d8c66781bf6b0ddf6d1499abbc603228858898c8d97980657ac085ddad",
      "bytes": 1211
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5ceb8c06453b57b24429a795ea41681d6acecb33449bdfbf7f12be2c08c4f8a8",
      "bytes": 1958
    },
    {
      "path": "characters/Gong Yacheong.md",
      "sha256": "c1d84555ab62f84967710ed54b319a54aa960a84fbaa6980b94a3ba976e6b540",
      "bytes": 2091
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "2c312975fd717b1edd3bae9803ab6527a1a5c1d79ea71c7412e1bc47461308a4",
      "bytes": 5010
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "32eef0b6746e32eaacd5f48de0cd9bc9f6a1a9796aff1c10da48339fb16a4ce6",
      "bytes": 1183
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a64c2fe283cb32e54d79e5dabdd572939300d3097bd09e6b8cb86f7b9c2fb1de",
      "bytes": 23754
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "2249038ea84d75c5163691534eb35ad067e2c316e53738503a4508deb5609012",
      "bytes": 8063
    },
    {
      "path": "characters/Socheon.md",
      "sha256": "a814390b93628773445cd4339f49a4b3344e74ab8e6b17dd663fb7712c6d6dfd",
      "bytes": 1629
    },
    {
      "path": "characters/Soyul.md",
      "sha256": "3905cb6701cc47eaa0fd71a65254dbdd91c4843a6ce60b52f55a70180db7b2cb",
      "bytes": 1524
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "f87bfe654bee07c92b46a7d961592fed5e31bb9fd011fe530c053b81d54431df",
      "bytes": 4516
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bdae616c899ebdcfb1105b2e93b0addab94bba58be071e5bbaee02bdd1b01178",
      "bytes": 1979
    }
  ],
  "estimated_tokens": 10436
}
-->

# Durable State Update — Chapter 66

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 66. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 66. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 66,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 66,
    "continuity_sources": [66],
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
    "Jin Mukyung recognizes Taekyung as a First Rate martial artist standing before the Peak realm and is astonished by his transformation over three years.",
    "Taekyung's spar with Mukyung ends with Mukyung's victory and the destruction of the pavilion; Taekyung survives and recovers in the Medicine King Hall.",
    "Hyuk Mujin is badly injured in the incident and is publicly credited with protecting Taekyung, with rumors that he will become the next Master of the Gatekeeper Pavilion.",
    "The Jin Family is pursuing an unidentified assassin believed possibly to be the Head Elder's hidden disciple."
  ],
  "continuity_sources": [
    65
  ],
  "open_questions": [
    "The identity of the assassin who attacked Taekyung and Hyuk Mujin remains unconfirmed.",
    "It remains unresolved whether Hyuk Mujin will actually become the next Master of the Gatekeeper Pavilion."
  ],
  "safe_through": 65,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun.",
    "Use junzi for 군자 with a cultural footnote.",
    "Retain Hyung-nim for 형님 in Taekyung's deferential speech."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 암천     | **Dark Heaven**                  |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 은인     | **Benefactor**                               |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 칭호               | **Title**                      |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 공야청 | **Gong Yacheong** |
| 소천 | **Socheon** |
| 소율 | **Soyul** |
| 삭주 | **Sakju** | Jin Family branch location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |

## Listed compact profiles

### Gong Yacheong.md

# Gong Yacheong (공야청)

- **Safe through:** Chapter 35
- **Aliases:** Uncle Gong
- **Role:** Guide and protector of the Sakju Branch survivors Socheon and Soyul
- **Personality:** Weary, responsible, and determined to keep the children alive despite the pursuit
- **Voice:** Protective and restrained
- **Relationships:** Longtime friend of Socheon’s father, the Sakju Branch Leader; guardian of Socheon and Soyul during their flight

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 65
- **Aliases:** None revealed
- **Role:** Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 65
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother; returns to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 65
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Son of a deceased father; supports his mother and younger sibling

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 65
- **Aliases:** None revealed
- **Role:** Thirty-five-year-old Lesser Family Head of the Jin Family of Taiyuan
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Socheon.md

# Socheon (소천)

- **Safe through:** Chapter 65
- **Aliases:** None revealed
- **Role:** Fourteen-year-old survivor of the Sakju Branch; older brother and protector of Soyul
- **Personality:** Watchful, frightened, and determined to survive and protect his sister after witnessing the massacre of his home
- **Voice:** A guarded child’s voice that becomes resolute under pressure
- **Relationships:** Son of the Sakju Branch Leader; older brother of Soyul; protected by Gong Yacheong

### Soyul.md

# Soyul (소율)

- **Safe through:** Chapter 65
- **Aliases:** None revealed
- **Role:** Young survivor of the Sakju Branch; Socheon's younger sister
- **Personality:** Exhausted, frightened, and dependent on her brother during the flight from the massacre
- **Voice:** A young child’s voice
- **Relationships:** Younger sister of Socheon; daughter of the Sakju Branch Leader; protected by Gong Yacheong

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 64
- **Aliases:** None revealed
- **Role:** Jin Wikyung’s personal guard
- **Personality:** Loyal, observant, teasing, and resigned to his master’s impulsive departures
- **Voice:** Weary and knowing; jokes with Jin Wikyung and uses Sound Transmission
- **Relationships:** Trusted guard and retainer of Jin Wikyung

## Korean source

```text
＃66화



저벅저벅.

청년이 발걸음을 옮길 때마다 사람들이 분분히 물러섰다.

조각처럼 수려한 외모도 외모지만, 그에게서 흘러나오는 강렬한 분위기에 압도된 탓이었다.

그는 멀리서도 단연 눈에 띄는 존재였다.

“와아, 잘생겼다.”

작년에 들어온 시녀의 철없는 말에 늙은 하인이 피식 웃었다.

“꿈 깨라.”

“누가 뭐래요? 그냥 처음 보는 얼굴이니까 그렇지.”

“아까 못 봤어? 삼공자님 전각 무너졌을 때.”

“그 난리 통에 본 사람이 한둘인가. 그래도 저 남자는 전쟁 통에 봤어도 못 잊을 것 같은데, 헤헤.”

“하긴, 그때는 행색이 말이 아니었으니까.”

곰곰이 생각하던 시녀가 눈을 동그랗게 떴다.

“아, 설마?”

“그래. 바로 그 이공자님이시다. 그러니까 헛꿈 꾸지 말고 가서 일이나 해.”

진무경은 주위의 수군거림을 무심한 얼굴로 흘려보내며 걸음을 옮겼다.

고풍스러운 전각에 도착하자 입구를 지키던 무인들이 문을 열어 주었다. 경외 어린 시선은 덤이다.

“소가주님께서 기다리고 계십니다.”

“고맙네.”

소가주 집무실에 들어선 그를 반긴 것은 짙은 다향(茶香)과 쿵쿵, 커다란 소리를 내며 달려오는 형, 진위경이었다.

“아우야!”

활짝 벌린 두 팔이 진무경을 꽉 끌어안았다.

순간 피할까 생각도 해 봤지만 그랬다가는 저 덩치가 어린애처럼 칭얼대는 꼴을 봐야 한다.

“숨 막힙니다.”

목각 인형처럼 딱딱한 말투였다.

“그게 삼 년 만에 만난 형한테 할 말이냐?”

진무경이 단호하게 대답했다.

“삼십 년 만에 만나도 마찬가집니다.”

“차가워졌구나. 많이 변했어.”

“예, 저는 피도 눈물도 없는 냉혈한이니까요.”

“괜찮아. 난 체질상 몸에 열이 많아.”

“……놓으십시오.”

잠시 후, 마주 앉은 두 사람이 대화를 시작했다.

“위 대협이 안 보이는군요.”

소가주의 곁에 늘 그림자처럼 붙어 있어야 할 위팽의 모습이 보이지 않는다.

차를 한 모금 마신 진위경이 대답했다.

“추격대 맡겨서 보냈다. 삼문협(三問峽)까지 다녀오려면 보름은 걸리겠지.”

“그렇게 멀리 말입니까?”

가문이 위치한 태원이 산서의 중심이라면 삼문협은 초입이자 끝자락이나 마찬가지다. 섬서(陝西)와 하남(河南)으로 이어지는 길목이기도 했으니 보름이라는 시간도 빡빡했다.

“어차피 요식 행위인데 너무 고생시키는 거 아닙니까?”

“왜, 미안해서?”

“일이 이렇게 커질 줄 몰랐죠.”

“나도 몰랐다. 네가 오자마자 그런 사고를 칠 줄은.”

“그건!”

“무경아.”

지금까지와는 달리 가벼운 질책이 담긴 눈빛에 진무경이 한숨을 내쉬었다.

“그렇게까지 할 생각은 없었습니다. 처음에는 단순히 몇 수 겨뤄 보려고 했을 뿐이에요.”

“그런데?”

“제법이더군요. 열이 받아서 힘이 과해졌습니다.”

“그랬겠지. 네가 알던 막내가 아니었을 테니까.”

진무경이 떨떠름한 표정으로 고개를 끄덕였다.

불과 한두 시진 전에 직접 손을 섞어 보기까지 했으니 이젠 인정하지 않을 수 없었다.

“말이 나왔으니 말인데, 도대체 무슨 일이 있었던 겁니까?”

“막내?”

“전부 다. 제가 받은 서신에는 항산검문 놈들이 쳐들어온다고만 적혀 있었습니다.”

항산검문이 선전포고를 한 직후 전서응을 날렸으니 그로서는 자세한 내막을 알 방법이 없었다.

기껏해야 태원진가로 오는 도중에 들었던 소문이 전부다.

“대장로가 배신했다는 말, 사실입니까?”

“그래. 말하자면 길다.”

“어느 정도로요?”

“사십 년 전, 정마대전까지 거슬러 올라가지.”

진위경이 굳은 표정으로 입을 연 순간이었다.

“그럼 됐습니다.”

“당시 대장로가…… 뭐라고?”

“어차피 끝난 얘기, 제가 들어 봤자 뭐 하겠습니까.”

대수롭지 않게 찻물을 한입에 털어 넣는 동생의 모습에 진위경의 얼굴이 황당함으로 물들었다.

“야, 인마!”

명색이 가문의 비사(秘史) 아닌가. 평소에도 무공밖에 모르는 녀석이긴 했지만 이 정도일 줄은 몰랐다.

“넌 알아야지! 본가의 직계…….”

“대장로가 배신했다. 그리고 죽었다. 그 과정에서 항산검문도 박살 났다. 태원진가가 최종 승자다. 제가 이해한 게 틀립니까?”

“아니, 맞긴 한데…….”

이제는 누가 비정상인지 헷갈린다. 혼란스러워하던 그는 불현듯 한 가지 사실을 떠올렸다.

“네가 전부 말해 달라며!”

“아, 그거 취소하겠습니다. 태어나기도 전에 있었던 일까지 듣는다면 이 자리에서 늙어 죽을 테니까요. 그 시간에 검이나 한 번 더 휘두르는 게 낫습니다.”

“…….”

“그럼 갑니다.”

“간다고? 어딜?”

“당연히 수련이죠.”

“수, 수련? 지금?”

“오랜만에 위 대협하고 비무나 하려고 온 건데, 없으니 혼자서라도 해야 하지 않겠습니까.”

진위경은 말문이 막혔다. 저게 삼 년 만에 형을 만난 동생의 태도란 말인가. 배신감에 가슴이 미어졌다.

“무경아!”

절절한 음성에 진무경이 차갑게 대꾸했다.

“차 잘 마셨습니다.”

뒤도 돌아보지 않고 집무실을 떠나는 둘째 동생의 뒷모습에, 진위경은 충격에 휩싸였다.

‘내가 널 어떻게 키웠는데.’

둘째도, 막내도 너무 훌쩍 커 버렸다. 각기 훌륭하게 장성한 동생들이 기특하면서도 가끔은 이렇게 서운하다.

‘그래, 이게 순리겠지.’

진위경은 땅이 꺼져라 한숨을 내쉬고는 집무용 탁자 앞에 앉았다. 그리고 아까 찢긴 비운의 걸작, ‘영웅의 탄생’을 신중하게 이어 붙이기 시작했다.



* * *



“흔적을 찾을 수 없습니다.”

“목격자도, 족적도 남기지 않았습니다. 신출귀몰한 놈입니다.”

수하의 말에 위팽은 쓴웃음을 삼켰다. 살수는 애초부터 없었으니 발견될 흔적도 없는 게 당연하다.

‘팔자에도 없는 연기를 해야 한다니.’

위팽의 머릿속에 한 시진 전, 진위경과 나눴던 대화가 스쳤다.



‘살수라니. 일을 너무 키우신 것 아닙니까?’

‘기회가 왔으니 이용해야지.’

‘그 기회가 삼공자 전각을 더 화려하게 새로 지을 기회는 아니겠지요.’

‘오, 그거 좋네. 추진해 봐.’

‘주공!’

‘장난일세, 장난.’

‘그럼 도대체 어떤 기회를 말씀하시는 겁니까?’



주군의 얼굴에서 웃음기가 사라진 것도 그때였다.



‘본가가 산서성 전역을 아우를 기회.’

‘……!’

‘지난 닷새 동안 가문의 모든 기록을 뒤져 봤네. 찾아야 하는 이름이 있었거든. 그게 무엇인지는 자네도 알겠지.’

‘암천(暗天).’

‘그 결과가 궁금하지 않나?’

‘못 찾으셨군요.’

‘구름이 몰려오고 있네. 지금까지 모습을 드러낸 적 없는 구름이. 그 전에 대비해야 해.’

‘하명하십시오.’

‘정예 서른을 붙여 줄 테니 곧장 남하하게. 공식적인 목표는 살수의 생포, 혹은 처단이지만 진짜 임무는 따로 있네.’



위팽은 저도 모르게 가슴을 더듬었다. 진위경에게 건네받았던 두툼한 종이 뭉치가 만져졌다.



‘이것은?’

‘곧 다가오는 새해 원단(元旦)에 산서성의 모든 문파를 본가로 소집할 생각이네.’



초청도, 초대도 아니다. 소집이다.

위팽은 그 뜻을 모를 정도로 멍청하지 않았다.



‘맹주(盟主)가 되려 하십니까?’

‘필요하다면.’



불과 얼마 전까지 세인들의 눈에 비친 산서 무림은 태원진가와 항산검문이라는 양대 산맥으로 나뉘어 있었다.

그러나 실상은 달랐다. 산서 무림은 세 발 달린 솥과 같은 형국이었다.

‘태원진가, 항산검문. 그리고 중소 문파.’

태원진가는 중부, 항산검문은 북부. 그리고 남부는 이십여 개 중소 문파들의 영역이었다. 이번 전쟁으로 사라진 산서오문은 그중에서도 특히 강성했던 다섯 개 문파를 칭하는 이름이었을 뿐이다.



‘그들의 연대는 끈끈합니다. 응하지 않을 수도 있습니다.’

‘전쟁이 일어나기 전이었다면 그랬겠지.’



세 발 달린 솥이 기울기 시작했다. 그리고 태원진가는 산서 무림이라는 솥을 홀로 지탱할 만한 힘과 명분이 있었다.



‘할 수 있겠나?’



대답은 정해져 있었다. 위팽은 작은 목소리로 중얼거렸다.

“받들겠습니다.”



그 시각, 진위경은 ‘영웅의 탄생’을 이어 붙이며 위팽을 욕하고 있었다.



* * *



상태창



[Lv.50 진태경]

직업 : 일류 무인

명성 : 1180 (+150)

칭호 : 4개 (칭호 효과 적용 중)

- 산서잠룡 (모든 능력치 +10, 명성 +100)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 초보 수련자 (수련 속도 +10%)

- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)

근력 : 135 (+15)체력 : 142(+15)

민첩 : 180 (+15)지력 : 25(+15)

매력 : 25(+15)공력 : 15년

잔여 포인트 : 50

- 잔여 포인트를 분배하십시오.





나는 상태창을 보며 후회했다.

‘젠장. 포인트를 너무 많이 썼어.’

진무경을 상대하면서 자그마치 50포인트나 민첩에 꼴아박았다. 애써 유지해 온 능력치 균형이 무너졌으니 나로서는 속이 쓰릴 수밖에 없다.

‘기껏해야 2, 30포인트면 충분할 거라고 생각했는데.’

절정 고수의 벽은 높았다. 아니, 어쩌면 진무경이 생각 이상으로 강한 것인지도 모르겠다. 천재라는 꼬리표가 쉽게 붙는 게 아니니까.

“내가 오십 합을 버티자 살수도 낭패한 기색이 역력하더군. 얼마 전까지 수련에만 매진한 나는 아직 산서에 알려지지 않은 미지의 고수…….”

빡!

“컥!”

뒤통수를 얻어맞은 혁무진이 비명을 질렀다.

“뭡니까!”

“애들한테 헛소리 좀 그만해. 뒤지기 싫으면.”

하지만 소천은 반짝거리는 눈으로 뒷이야기를 기다리는 중이었다.

“전 괜찮습니다.”

“뒤지는 게 모야? 소율이도 뒤질래!”

“……넌 아직 한참 남았어.”

나는 소매를 잡아당기며 보채는 소율의 머리를 쓰다듬었다.

이 꼬마 남매와의 인연도 제법 깊다. 가만히 보고 있으니 문득 생각나는 사람이 있었다.

“공 대협은 요즘 어떠시냐?”

공야청. 소천과 소율이 숙부라고 부르는 중년인.

여전히 무림의 용어가 어색한 나도 공야청을 부를 때는 꼬박꼬박 대협을 붙인다. 그는 그럴 만한 자격이 있는 사람이니까.

“순조롭게 회복 중이십니다. 아직 거동이 불편하시긴 하지만요.”

“그래? 다행이네.”

“안 그래도 떠나기 전에 한번 뵈었으면 하시더군요.”

무심코 고개를 끄덕이려다가 멈칫했다.

“떠난다고?”

“예, 이번에 재건되는 삭주지부를 맡게 되실 겁니다.”

“그럼…….”

“저희도 따라가기로 했습니다.”

전쟁은 많은 것들을 앗아 간다. 소천과 소율은 항산검문의 습격으로 터전과 부모를 모두 잃었다. 지나간 시간을 되돌릴 수는 없겠지만 모든 것이 정리되었으니 이젠 소중한 추억이 서린 곳으로 돌아갈 것이다.

“감사했습니다, 은인.”

진심이 느껴지는 인사에 가슴 한구석이 간질거렸다. 어린 남매가 감당하기에는 너무 잔인한 현실이 아직 남아 있었다.

더군다나 소율은 아직 부모의 죽음조차 모른다.

‘다섯 살이라…….’

현재를 인지하고 받아들이기에는 너무나도 어린 나이다.

문득 22년 전의 기억을 떠올려 봤다. 흐릿하다.

“……너도 그랬으면 좋겠구나.”

소율이는 뜻을 모를 말에도 배시시 웃었다.

나는 소천을 향해 고개를 돌렸다.

“종종 보러 가도 되냐?”

내 말에 소천이 기다렸다는 듯 환하게 웃었다.

“은인이라면 언제나 환영입니다.”

우리 사이에 훈훈하게 흐르는 공기를 뚫고 가만히 듣고 있던 혁무진이 끼어들었다.

“그럼 언제쯤 떠나는 거야?”

“반년 후요.”

“…….”

내 감동. 아껴 둘걸.
```

## Final English reading copy

```markdown
# Chapter 66

Step. Step.

Each time the young man took a step, people hurriedly moved aside.

His sculpted, handsome features were part of it, but more than that, they were overwhelmed by the intense presence radiating from him.

He stood out even from a distance.

“Wow, he’s handsome.”

At the thoughtless remark from a maid who had joined the household the previous year, an old servant gave a quiet laugh.

“Wake up from your dream.”

“Who said anything? It’s just because I’ve never seen his face before.”

“Didn’t you see him earlier? When the Third Young Master’s pavilion collapsed?”

“With all that chaos, do you think I only saw one or two people? Still, I don’t think I’d ever forget that man, even if I’d seen him in the middle of a war. Hehe.”

“True enough. His appearance was a complete disaster back then.”

The maid thought about it for a moment, then her eyes went round.

“Oh, no way?”

“That’s right. He’s the Second Young Master. So stop dreaming nonsense and go do your work.”

Jin Mukyung ignored the whispers around him with an indifferent expression and continued walking.

When he reached the stately, traditional pavilion, the martial artists guarding the entrance opened the doors for him. The looks of awe came free of charge.

“The Lesser Family Head is waiting for you.”

“Thank you.”

The moment Jin Mukyung entered the Lesser Family Head’s office, he was greeted by the rich scent of tea—and by his older brother, Jin Wikyung, charging toward him with heavy, pounding footsteps.

“Little brother!”

Jin Wikyung spread his arms wide and pulled Jin Mukyung into a tight embrace.

For a moment, Mukyung considered dodging, but if he did, he would have to watch that hulking body whine like a child.

“I can’t breathe.”

His tone was as stiff as a wooden puppet’s.

“Is that what you say to your brother after not seeing him for three years?”

“Even if we had not seen each other for thirty years, my answer would be the same.”

“You’ve grown cold. You’ve changed so much.”

“Yes. I’m a cold-blooded man without blood or tears.”

“That’s all right. I naturally run hot.”

“……Let go.”

A short while later, the two brothers sat across from each other and began to talk.

“Sir Wipeng is nowhere to be seen.”

Wipeng, who was supposed to remain at the Lesser Family Head’s side like a shadow, was absent.

After taking a sip of tea, Jin Wikyung answered.

“I put him in charge of a pursuit team and sent him out. It’ll take at least half a month to go all the way to Three Questions Gorge and back.”

“That far?”

If Taiyuan, where the family was located, was the center of Shanxi, Three Questions Gorge was practically at its entrance and far edge. It was also a crossroads leading to Shaanxi and Henan, so even fifteen days was a tight schedule.

“It’s only a formality anyway. Aren’t you making him work too hard?”

“Why? Feeling sorry for him?”

“I didn’t expect things to get this big.”

“Neither did I. I didn’t expect you to cause such an incident the moment you arrived.”

“That’s not—”

“Mukyung.”

Unlike before, Jin Wikyung’s eyes held a light reproach. Jin Mukyung sighed.

“I didn’t intend to take it that far. At first, I only meant to exchange a few moves.”

“And then?”

“He was pretty good. I got heated and used too much force.”

“Of course you did. He wasn’t the youngest brother you remembered.”

Jin Mukyung nodded reluctantly.

He had personally exchanged blows with Jin Taekyung only an hour or two earlier. By now, he could no longer refuse to acknowledge the truth.

“Since we’re on the subject, what on earth happened?”

“The youngest?”

“Everything. The letter I received only said that the Mount Heng Sword Sect bastards were invading.”

A carrier hawk had been sent immediately after the Mount Heng Sword Sect declared war, so there had been no way for him to learn the details.

The rumors he had heard on the way to the Jin Family of Taiyuan were all he knew.

“Is it true that the Head Elder betrayed us?”

“Yes. It’s a long story.”

“How long?”

“It goes all the way back to the Great Faction War forty years ago.”

Jin Wikyung’s expression hardened as he began to speak.

“Then never mind.”

“Back then, the Head Elder… Wait, what did you say?”

“Never mind. It’s already over. What good would hearing about it do me?”

Jin Mukyung emptied his teacup in one gulp, and Jin Wikyung’s face filled with disbelief.

“You little bastard!”

It was, after all, the hidden history of the family. Jin Mukyung had always been a man who cared about nothing but martial arts, but Jin Wikyung had never imagined he could be this bad.

“You need to know! The direct line of our family—”

“The Head Elder betrayed us. Then he died. The Mount Heng Sword Sect was destroyed in the process. The Jin Family of Taiyuan was the final victor. Did I misunderstand anything?”

“No, that’s right, but…”

Jin Wikyung began to wonder which of them was the abnormal one.

Then he suddenly remembered something.

“You were the one who said you wanted to hear everything!”

“Ah, I take that back. If I listen to things that happened before I was even born, I’ll grow old and die right here. I’d rather spend that time swinging my sword one more time.”

“……”

“Then I’ll be going.”

“You’re leaving? Where?”

“To train, obviously.”

“Training? Right now?”

“I came to spar with Sir Wipeng after so long, but he’s gone. Shouldn’t I train by myself, at least?”

Jin Wikyung was speechless.

*Is that how a younger brother is supposed to act after seeing his older brother for the first time in three years?*

His heart ached with betrayal.

“Mukyung!”

Jin Mukyung answered the heartfelt call coldly.

“The tea was good. Thank you.”

He left the office without even looking back.

Jin Wikyung stared at the back of his departing younger brother, stunned.

*After everything I did to raise you…*

Both his second and youngest brothers had grown up so much. He was proud of how wonderfully they had each matured, but sometimes, moments like this still hurt.

*Yes. This is the natural order of things.*

Jin Wikyung let out a sigh that seemed to drain the earth itself, then sat down in front of his worktable.

He carefully began piecing together the unfortunate masterpiece that had been torn apart earlier: *The Birth of a Hero*.

* * *

“We haven’t found a single trace.”

“He left behind no witnesses or footprints. He’s an elusive bastard.”

At his subordinate’s report, Wipeng swallowed a bitter smile.

There had never been an assassin in the first place. Naturally, there would be no traces to find.

*I have to put on an act I was never meant to perform.*

A conversation he had shared with Jin Wikyung an hour earlier flashed through Wipeng’s mind.



*An assassin? Haven’t you made this affair too big?*

*An opportunity has presented itself. We have to use it.*

*You don’t mean the opportunity to rebuild the Third Young Master’s pavilion even more lavishly, do you?*

*Oh, that’s a good idea. Make it happen.*

*My lord!*

*I’m joking. Just joking.*

*Then what opportunity are you talking about?*



That was when the smile disappeared from his lord’s face.

*An opportunity for our family to encompass all of Shanxi Province.*

*……!*

*I spent the past five days searching through every record in the family. There was a name I needed to find. You know what it is, don’t you?*

*Dark Heaven.*

*Don’t you want to know what I found?*

*You didn’t find it.*

*Clouds are gathering. Clouds that have never shown themselves before. We need to prepare before they appear.*

*Give me your orders.*

*I’ll assign thirty elites to you. Head south immediately. The official objective is to capture or kill the assassin, but your true mission is something else.*



Wipeng unconsciously touched his chest. His fingers brushed against the thick bundle of papers Jin Wikyung had handed him.

*What is this?*

*On the coming New Year’s Day, I intend to summon every sect in Shanxi Province to our family.*



This was no invitation. It was a summons.

Wipeng was not foolish enough to misunderstand what that meant.

*Are you trying to become the Alliance Leader?*

*If necessary.*



Until recently, Shanxi Murim had appeared to the outside world as two towering peaks: the Jin Family of Taiyuan and the Mount Heng Sword Sect.

But the reality was different. Shanxi Murim was shaped like a three-legged cauldron.

*The Jin Family of Taiyuan, the Mount Heng Sword Sect, and the smaller sects.*

The Jin Family of Taiyuan held the central region, and the Mount Heng Sword Sect held the north. The south belonged to more than twenty mid-sized and small sects.

The Five Gates of Shanxi, which had vanished in the recent war, was merely the name given to the five especially powerful sects among them.

*Their alliance is strong. They may refuse to comply.*

*They might have, if this had been before the war.*



The three-legged cauldron had begun to tip.

And the Jin Family of Taiyuan had both the strength and the justification to support Shanxi Murim’s cauldron alone.

*Can you do it?*



The answer had already been decided.

Wipeng muttered in a low voice.

“I shall obey.”



At that same moment, Jin Wikyung was piecing together *The Birth of a Hero* and cursing Wipeng.

* * *

> **System**
>
> **Status Window**
>
> **Lv.50 Jin Taekyung**
>
> **Job:** First Rate martial artist
>
> **Fame:** 1,180 (+150)
>
> **Titles:** 4 (Title effects active)
>
> - **Sleeping Dragon of Shanxi** (All Stats +10, Fame +100)
>
> - **Scion of a Prestigious Family** (All Stats +5, Fame +50)
>
> - **Novice Trainee** (Training speed +10%)
>
> - **Gambler** (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 135 (+15)  
> **Stamina:** 142 (+15)  
> **Agility:** 180 (+15)  
> **Intelligence:** 25 (+15)  
> **Charm:** 25 (+15)  
> **Internal Energy:** 15 years
>
> **Remaining Points:** 50
>
> - Distribute your remaining points.

I stared at the Status Window and regretted it.

*Damn it. I spent too many points.*

While fighting Jin Mukyung, I had dumped no fewer than fifty points into Agility. The balance between my stats, which I had worked so hard to maintain, had collapsed. Naturally, it left a bitter taste in my mouth.

*I thought twenty or thirty points at most would be enough.*

The wall posed by a Peak master was high.

No—perhaps Jin Mukyung was simply stronger than I had expected. The title of genius was not something people handed out easily.

“When I lasted fifty exchanges, even the assassin looked visibly flustered. I had devoted myself to training until recently, so I was an unknown master in Shanxi—”

Smack!

“Ghk!”

Hyuk Mujin, who had been struck on the back of the head, let out a scream.

“What was that for?”

“Stop filling the kids’ heads with nonsense. Unless you want to croak.”

But Socheon was waiting for the rest of the story with shining eyes.

“I’m fine.”

“What does ‘croak’ mean? Soyul wants to croak too!”

“……You’ve still got a long time before that.”

I stroked Soyul’s head as she tugged on my sleeve and pestered me.

My connection with these little siblings had grown fairly deep. As I watched them quietly, someone suddenly came to mind.

“How is Great Hero Gong these days?”

Gong Yacheong—the middle-aged man Socheon and Soyul called their uncle.

Even now, Murim terminology felt awkward to me, but whenever I addressed Gong Yacheong, I always called him Great Hero. He was someone who deserved it.

“He’s recovering smoothly. He still has trouble moving around, though.”

“Really? That’s good to hear.”

“He said he wanted to see you before he left.”

I was about to nod without thinking when I stopped.

“Before he leaves?”

“Yes. He’ll be put in charge of the Sakju Branch, which is being rebuilt this time.”

“Then…”

“We’ve decided to go with him.”

War took many things away.

Socheon and Soyul had lost both their home and their parents in the Mount Heng Sword Sect’s attack. They could not turn back the years that had passed, but now that everything had been settled, they would return to the place steeped in precious memories.

“Thank you for everything, Benefactor.”

The sincerity in his farewell made something tickle in a corner of my chest. There was still a reality far too cruel for these young siblings to bear.

What was worse, Soyul did not even know that her parents were dead.

*She’s five…*

She was far too young to recognize and accept the present for what it was.

I suddenly recalled a memory from twenty-two years ago.

It was hazy.

“……I hope it will be that way for you, too.”

Soyul only smiled shyly at the words she did not understand.

I turned toward Socheon.

“Would it be all right if I came to see you from time to time?”

Socheon beamed as if he had been waiting for me to ask.

“You’re always welcome, Benefactor.”

Hyuk Mujin, who had been listening quietly, broke through the warm atmosphere between us.

“Then when are you leaving?”

“Half a year from now.”

“……”

*There went my touching moment. I should’ve saved it.*
```
