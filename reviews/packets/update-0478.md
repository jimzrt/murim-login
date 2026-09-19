<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0478.txt",
      "sha256": "6c88c08c1e3ac5801cd8fe559ee040ba11c72bd988ee2d363fc95ce680ad83dc",
      "bytes": 14704
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3f2a20760fc59449af1b6b0dbf25180ef58582568c5d3632215154a86f8c29e9",
      "bytes": 2730
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "834c94431f8255d969947faa6a53e2198fe6725fbec90a6ae680418f289aee3a",
      "bytes": 153332
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3e8adee1069fb2de7e79066ef1cbd3f714efd9280d34de54dddfcae2f5192f9d",
      "bytes": 553
    },
    {
      "path": "characters/Honglan.md",
      "sha256": "086f7467d54e928b241397da32b381e7f124737bb17b511e3b805fccb378c1fb",
      "bytes": 799
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bb882cf37f97b20509363dde65c544ab530ac7be2754709b99da838a8410a1ae",
      "bytes": 147867
    }
  ],
  "estimated_tokens": 9629
}
-->

# Durable State Update — Chapter 478

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 478. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 478. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 478,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 478,
    "continuity_sources": [478],
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
    "Taekyung's forced System Quest, Corrupted Spirit Beast, remains active with Logout disabled and the Mutated Water God Dragon as its target.",
    "The Water God Dragon was once a noble spirit beast awaiting ascension before an unknown power corrupted it into an evil beast.",
    "Taekyung has pinned the dragon's tail with White Flame and summoned spears, recovered White Flame through Seizing an Object Through Empty Space, and commands Jeok Cheongang, Mungyeong, and Cheongpung in a coordinated raid.",
    "Mungyeong, Cheongpung, Jeok Cheongang, and Taekyung have severely wounded the dragon through relentless attacks from every direction.",
    "The dragon's Berserk Status increases its abilities but clouds its judgment; its enormous size has become a weakness against the surrounding raid team.",
    "The dragon's reinforced scales, flesh, and bones have been shattered or cut apart by the team's Force and sword attacks.",
    "The dragon's storms, lightning, and violent winds are subsiding as its life wanes.",
    "The dragon remains alive and was beginning to form a final Water Breath when Taekyung vanished from its sight.",
    "Taekyung's final attack and the dragon's fate remain unresolved.",
    "The unidentified figure hanging from the dragon's head remains unresolved."
  ],
  "continuity_sources": [
    477,
    476
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Did the Mutated Water God Dragon destroy Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left?",
    "What unknown power corrupted the Water God Dragon, and is it related to the black pupils and sudden increase in power?",
    "Who is the unidentified figure hanging from the dragon's head, and why can that figure tear out its whiskers barehanded?"
  ],
  "safe_through": 477,
  "temporary_decisions": [
    "Render 광폭화 as Berserk and preserve the System Status distinction.",
    "Preserve Taekyung's raid-game terminology, profane improvisational combat humor, and exaggerated comparisons.",
    "Render 장수 돌침대 as Jangsu stone bed and 효자손 as hyojason, each with an explanatory footnote when used.",
    "Continue rendering 수염 as whiskers and distinguish Force, Sword Energy, Hellfire, and Water Breath.",
    "Retain established jang and geun measurements, along with established renderings of live-fish sashimi and bone-in sashimi."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 암천     | **Dark Heaven**                  |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 습득               | **Acquired**                   |
| 게이트     | **Gate**              |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍란 | **Honglan** | Stage name of Ju Wongong's Lower District Sect singing courtesan; her real name is concealed. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 브레스 | **Breath** | Dragonkin power used by the Wyverns. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 이각수 | **Two-Horned Beast** | Legendary local name for the creature regarded as Dongting Lake's divine spirit. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 477
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Honglan.md

# Honglan (홍란)

- **Safe through:** Chapter 467
- **Aliases:** None
- **Role:** Honglan is a Lower District Sect courtesan who uses a stage name while serving as Ju Wongong's singing courtesan.
- **Personality:** Discreet about her real identity and professionally alluring.
- **Voice:** Clear, pure, and alluring, with humble formal speech toward honored guests.
- **Relationships:** Honglan is kept at Ju Wongong's side as a singing courtesan, belongs to the Lower District Sect, lost her clan and parents overnight as a child, can respond to Taekyung through Sound Transmission, and is the sole surviving eyewitness to the Dongting Lake attack who knows several possible locations of the Dongting Fisherman's hidden refuges.

## Korean source

```text
＃478화



처음부터 그곳을 노렸던 것은 아니다. 아니, 몰랐다.

이건 울창한 숲속에 숨어 있는 다람쥐를 쉽게 찾지 못하는 것과 같은 이치다.

그곳을 발견하기에는 변이된 수신룡의 동체는 실로 거대했고, 놈이 전투 도중에도 철저히 보호했던 부위에 그런 빈틈이 있을 거라고는 생각하지 못했다.

하지만…….

‘저건.’

있었다. 이 거대한 괴물의 질긴 숨통을 끊을 만한 약점이.

그리고 나는 이 싸움을 끝낼 절호의 기회를 놓치지 않았다.

푹!

- 크륵……!

생물이란 참으로 신기하다. 주위 환경에 맞춰 끊임없이 자신의 약점을 보완하며 진화하니까.

이제 고작 평균 수명 100년을 바라보는 인간도 그럴진대, 수백 년을 살아온 이 지고한 존재라고 다를 리 없다.

‘우연인가? 아니면 운명?’

둘 중 어느 것이든 상관없다.

지금 이 순간 무엇보다 중요한 사실은 가장 단단한 비늘로 둘러싸여 있던 놈의 목덜미 부위에 딱 비늘 한 장만큼의 공간이 비어 있었다는 것과, 내가 그 틈을 놓치지 않았다는 것이다.

“고생했다.”

마지막으로 건네는 덕담은 오직 승자만이 누릴 수 있는 권리.

목 아랫부분, 인간이었다면 목젖이 있어야 할 그 부위에 정확히 창날을 꽂아 넣은 나는, 창대를 쥔 손아귀에 힘을 더하며 그대로 깊숙이 밀어 넣었다.

푸욱-!

크르륵. 헛숨을 들이키는 듯한 짧은 신음과 함께 비늘에 뒤덮인 턱이 파르르 떨렸다.

이어 칠흑색 동공이 흔들리고, 한껏 벌린 아가리의 끝에서 완성을 코앞에 둔 물의 구가 서서히 흩어지기 시작했다.

촤아아악.

완성되지 못한 워터 브레스는 단순한 물에 불과한 것.

나는 정수리를 향해 쏟아지는 물벼락을 피하지 않고 고스란히 맞았다.

유난히도 서늘한 동정호의 강물이 전신을 흠뻑 적시자 마음이 차분하게 가라앉았다.

‘이겼다.’

동시에 짜릿한 감각이 등골을 타고 솟구쳤다.

길고 치열했던 전투의 끝.

나는 다시 한번 살아남았고 강적의 목에 창날을 박아 넣었다. 그리고 언제나 그렇듯, 목숨을 건 싸움의 끝은 오직 두 단어로 귀결된다.

수직과 수평.

우뚝 선 승자와 쓰러지는 패자.

비록 아득한 세월을 살아온 악물(惡物)이라 할지라도, 이 절대적인 약육강식의 법칙에서 예외일 수는 없었다.

후우우웅. 촤악!

한때 누구보다 단단하고 강대한 힘을 품었던 동체가 허물어지고, 이내 동정호의 강물 위로 쓰러진다.

높게 솟구치는 물보라 사이로 천천히 깜빡이는 눈동자와 잘게 떨리는 주둥이가 보였다.

아니.

들렸다.

- 그대로군.

“……!”

머릿속에서 울려 퍼지는 누군가의 목소리를 듣는 순간, 완전히 숨통을 끊기 위해 재차 창을 밀어 넣으려던 손에 힘이 풀렸다.

뭔가에 홀린 듯 변이된 수신룡의 거대한 눈동자를 바라본 나는, 그대로 몸이 덜컥 굳는 것을 느꼈다.

‘이게 무슨.’

온통 칠흑빛으로 번들거리던, 흉성(凶星)을 띤 괴물의 모습은 이제 어디에서도 찾아볼 수 없었다.

마치 한바탕 비바람을 쏟아 낸 어느 날의 먹구름이 걷힌 것처럼, 푸른 하늘을 닮은 맑고 깊은 눈동자가 그곳에 있었다.

- 놀랄 것 없네. 오백 년쯤 살다 보면 자연스럽게 얻게 되는 능력이니까.

“……전음(傳音)?”

- 글쎄, 그보다는 의념(疑念)이라 부르는 게 맞겠지.

변이된 수신룡, 아니 동정호의 이각수라는 또 다른 이름을 지닌 신령스러운 존재는 담담하게 자신의 의념을 흘려보냈다.

- 그대는 나를 모르지만, 나는 그대를 알지. 아주 오래전 꿈속에서 보았던 모습 그대로야. 단순한 미몽(迷夢)이라 여겨 잊고 있었건만……. 그래, 이 또한 순리겠지.

꿈? 순리?

빌어먹을, 이게 도대체 어떻게 돌아가는 상황인지 모르겠다.

“이게, 이게 그러니까.”

- 허.

할 말을 찾지 못해 머뭇거리는 내 모습이 퍽 우스웠던 모양이다. 피로 흠뻑 젖은 수신룡의 입가에서 그르릉거리는 웃음소리가 흘러나왔다.

- 이해할 수도 없고, 이해하려 하지도 말게. 수행이 부족하여 승천(昇天)하지 못한 늙은 이무기의 푸념일 뿐이니까. 다만 한 가지 애석한 점이 있다면, 내게 더 이상 남은 시간이 없다는 것일세.

수신룡의 말은 사실이었다. 이미 한계에 다다른 육신은 죽음을 앞두고 있었고, 깊은 눈동자에서는 서서히 빛이 사라지고 있었다.

‘제기랄.’

후회해도 이미 엎질러진 물.

나는 지그시 입술을 깨물었다.

수신룡의 죽음에 대해 안타깝기도 했고, 냉정하게 말하자면 아쉽기도 했다.

죽음을 코앞에 두고 정신을 차린 이 영험한 존재는 수수께끼를 풀 수 있는 중요한 열쇠니까.

‘암천(暗天).’

신령스럽고도 지혜로운 이무기가 아무런 이유도 없이 인간들을 살육하는 미친 악물이 되었을 리는 없다.

분명 누군가의 개입이 있었을 테고, 그렇다면 현재 무림에서 벌어지는 모든 사건의 용의 선상에서 가장 윗줄을 차지하는 암천을 빼놓을 수 없다.

“누가, 어떻게 한 겁니까.”

짧지만 모든 것이 담긴 질문.

그러나 곧이어 머릿속에 울려 퍼진 수신룡의 의념은 내 예상을 뛰어넘는 것이었다.

- 직접 보도록 하게.

“예?”

내 반문에 수신룡은 눈을 깜빡이는 것으로 답을 대신했다.

스륵.

커다란 눈동자에 가득 고인 푸른 액체. 모두가 눈물이라 부르는 그것이 천천히 비늘 위를 미끄러져 내 몸에 닿은 순간, 나는 앞서 수신룡이 했던 말의 의미를 깨달을 수 있었다.

띠링.



- [수신룡]이 당신에게 자신의 기억 중 일부를 전하고자 합니다.

- [기억의 파편]을 습득했습니다.

- [기억의 파편]에 서린 힘이 당신을 수신룡의 기억으로 이끕니다.



귓가에 울려 퍼지는 시스템 알림과 함께, 수신룡의 눈물이 장막처럼 펼쳐져 내 눈앞에 드리워졌다.

솨아아아.

시원한 물의 감촉과 함께, 세상이 멈췄다.



* * *



그건 말 그대로 기억의 파편이었다.

수신룡이 간직한 오백 년의 세월이 고스란히 담긴, 하지만 변이의 영향 때문인지 부분부분 깨져 나가 어떤 부분은 흐릿하고 어느 부분은 또렷한 기억의 파편.

그리고 그 모든 것의 시작은 탄생이었다.

- 꾸룩?

동정호의 깊은 물 속 어딘가, 갓 태어난 작은 생명체가 어리둥절하게 주위를 둘러본다.

마치 춤을 추듯 넘실거리는 수초(水草)와 헤아릴 수 없을 만큼 많은 수중 생물들이 모인 자리.

신령스러운 존재의 탄생을 알아차린 백성들이 기뻐하며 물살을 가르며 헤엄친다.

그날은 동정호의 새로운 주인이 탄생한 경사스러운 날이었고, 성대한 즉위식이 열린 날이었다.

- 구룩? 꾹!

강아지처럼 호기심 넘치는 표정으로 고개를 갸웃거린 새로운 강의 주인은 이내 자그마한 몸으로 헤엄치기 시작했다.

탄생과 동시에 눈부신 지혜와 힘을 부여받은 존재가 움직이자, 수많은 생물이 그의 뒤를 따르고 강물마저 길을 비켰다.

촤아아아악!

유연하면서도 힘차게 동정호의 강물을 가르던 몸집이 서서히 크기를 부풀렸다.

작고 부드럽던 분홍색 몸통에는 은빛 비늘이 돋아났고, 콧잔등 아래에는 위엄이 서린 수염이 제법 길게 자라났다.

아마 그때부터였을 것이다.

수십 년, 혹은 더욱 긴 시간 동안 한 번씩 모습을 드러내는 이 신령스러운 존재를 목격한 사람들은 경의를 담아 새로운 이름을 지어주었다.

나 역시 알고 있는 그 이름을.

‘수신룡(水神龍).’

이마에 난 두 개의 뿔 덕분인지 이각수(二角獸)라고도 불렸지만, 대부분은 이 아름답고도 신비한 존재를 짐승이라 부르기를 꺼렸고, 동정호의 신령으로 떠받들었다.

그리고 인간들로부터 새로운 이름을 얻은 이무기는 종종, 정말로 신령 같은 일들을 해내고는 했다.

익사 직전의 상태에 빠진 뱃사람들을 구해 내어 인적 드문 뭍에 데려다 놓기도 하고, 타고난 능력을 이용해 난폭한 물살을 잠재우는 일도 부지기수였다.

뿐인가. 한때 장강을 피로 물들였던 악물(惡物)을 쓰러트린 것도 바로 수신룡이었다.

거북이의 형태를 한 악물을 치열한 싸움 끝에 쓰러트린 수신룡은 동정호와 장강을 지배하게 되었다.

세월은 유수(流水)와도 같은 법.

그렇게 장장 오백여 년의 세월이 흐르자, 수신룡은 처음과 비교할 수 없을 만큼 성장했다.

그는 강대한 힘과 깊은 지혜를 지닌 선한 이무기였고, 백성을 생각할 줄 아는 훌륭한 지배자였다.

그러나 그런 수신룡에게도 한 가지 고민이 있었다.

- 허어, 하계(下界)에서는 싸움이 끊이질 않는구나.

긴 세월 수신룡이 목격한 참상은 그야말로 끔찍했다.

인간들은 끊임없이 반목하며 싸웠고, 그럴 때마다 무수한 피와 시체가 강물에 흩뿌려졌다.

두 개의 제국이 몰락하고 전란이 이어지자 수신룡은 근심했고, 지쳐 갔다.

- 이미 아득히 긴 세월을 하계에서 보냈건만, 도대체 나는 언제쯤 승천할 수 있단 말인가.

사람들이 동정호의 신령이요, 용이라며 떠받들어도 결국 수신룡의 본질은 아직 용이 되지 못한 이무기.

그런 수신룡에게 승천이라는 목표는 탄생과 함께 정해진 것이나 다름없었다.

하지만 하늘이 원망스러울 만큼 수행은 더뎠고, 깨달음은 도통 찾아오지 않았다.

그러던 중 어느 물고기 무리가 전해 준 소식은 지쳐 있던 수신룡의 호기심을 자극하기에 충분했다.

- 인간이 나타났다는 말인가? 하지만 그곳은 지난 수십 년간 아무도 찾지 않았던 곳인데.

동정호에서도 가장 깊고 은밀한, 오랫동안 사람의 발길이 닿지 않았던 험지(險地)를 찾은 불청객.

문득 호기심이 동한 수신룡은 한때 자신의 거처로 사용하기도 했던 그곳을 찾아갔고, 도착과 동시에 무언가 잘못되었음을 깨달았다.

- 이 무슨……!

경악하는 것은 과거의 수신룡뿐만이 아니었다.

지금 이 순간 기억의 파편을 통해 그 광경을 바라보고 있는 나 역시도 마찬가지였다.

‘저건 설마.’

끈적하고 불쾌한 무언가가 등골을 타고 천천히 기어오른다.

불신, 의문, 그리고 뒤통수를 한 대 얻어맞은 듯한 충격에 사로잡혀 있던 나는 멍하니 뇌까렸다.

‘……게이트.’

틀림없다. 적어도 지금까지 수백, 수천 번도 넘게 게이트를 통과했던 나는 확신할 수 있었다.

커다란 바위 틈새로 줄기줄기 쏟아지는 검은 기운은 분명 마력(魔力)이다.

‘이런 미친……!’

순간 눈앞이 아찔해지며 온갖 욕설이 마음속에서 울려 퍼졌다.

아마 지금 내가 수신룡의 기억 속이 아니었다면, 마음껏 소리 내어 말할 수 있고 움직일 수 있었다면 주위에 있는 모든 것을 부쉈을 것이다. 목이 터질 때까지 고함을 질렀을 것이다.

‘씨발, 게이트라니. 마력이라니!’

수많은 생각으로 머리가 터질 것 같다. 토해 내지 못한 외침이 혀끝에서 흩어진다.

나는 경악과 분노로 눈을 부릅뜬 채, 눈앞에서 벌어지는 광경을 망연히 응시했다.

- 멈추어라! 멈추란 말이다!

강의 주인은 자신을 향해 달려드는 수많은 백성을 온몸으로 막아 내고 있었다.

마기에 노출된 물고기들의 이빨은 톱니보다 예리했고, 비늘은 온통 칠흑빛으로 물들어 있었다.

- 제발 그만두어 다오!

그러나 필사적인 의념은 이미 마기로 변이된 물고기들에게 닿지 않았고, 수신룡은 실로 어려운 결정을 내려야 했다.

기이할 정도로 강하고 난폭해진 물고기들이 이곳을 빠져나간다면 동정호와 장강 전체가 피로 물들 터.

대의를 위한 희생이 필요했다.

- ……미안하구나.

동정호의 가장 깊은 물 속에서 벌어진 전투는 당연하게도 수신룡의 승리로 끝났다.

하지만 수신룡에게는 비탄에 젖어 있을 틈조차 주어지지 않았다.

수백 년간 살아온 이 지혜로운 이무기는 자신이 해야 할 일을 깨달았고, 끊임없이 불길한 기운을 뿜어내는 거대한 틈새를 직접 몸으로 막아섰다.

- 네가 무엇인지는 모르나, 뜻대로 되지는 않을 것이다.

쿠구구구궁!

그건 수신룡이 살아온 모든 세월 중에서도 가장 길고 치열한 싸움이었다.

힘이 팽팽히 대치한 칠 주야 동안 동정호와 장강의 강물은 난폭하게 요동쳤고, 육지의 사람들은 신령이 노했다며 두려워했다.

그리고 이 싸움의 결과를, 나는 이미 알고 있었다.

- 크르르륵.

눈부신 지성을 잃고 악물로 타락한 수신룡이 낮은 울음소리를 흘렸다.

마기를 대부분 흡수함으로써 자신의 영역과 백성을 지켰지만, 그 힘을 모두 감당할 수는 없었다.

츠츠츠츠.

서서히 붉게 물드는 한 쌍의 눈동자.

그러나 마지막 남은 한 톨의 이성이, 수신룡으로 하여금 물 위로 솟구치게 했다.

그건 이와 같은 끔찍한 만행을 벌인 범인을 찾고자 했던 늙은 이무기의 의지였다.

촤아아아악!

어두운 밤, 검게 물든 강물이 갈라졌다.

마치 용이 승천하듯 솟아오른 수신룡의 붉은 동공에, 이끼 낀 바위에 앉아 물장구를 치고 있던 한 사람이 비쳤다.

“기운이 좋네. 먼 곳까지 온 보람이 있어.”

맑고 나긋한 목소리, 눈이 부시도록 새하얀 목선.

그리고 긴 흑발을 틀어 올려 고정한 은빛 비녀.

‘……홍란(紅蘭).’

머릿속에 떠오른 한 사람의 이름과 함께, 나를 둘러싼 모든 세상이 산산이 부서졌다.
```

## Final English reading copy

```markdown
# Chapter 478

I hadn’t been aiming for that spot from the beginning.

No. I hadn’t even known it was there.

It was like trying to find a squirrel hiding in a dense forest. You simply couldn’t spot it easily.

The Mutated Water God Dragon’s body was truly enormous, and I had never imagined that a weakness could exist in a part of its body that it had protected so thoroughly throughout the battle.

But…

*That.*

There it was.

A weakness capable of severing the windpipe of this gigantic monster.

And I did not let the perfect opportunity to end this fight slip away.

*Thk!*

—Krrk…!

Living creatures were truly strange. They constantly evolved, compensating for their weaknesses to suit the environments around them.

If even humans, with their life expectancy of barely a hundred years, did that, then surely this sublime being, which had lived for hundreds of years, would be no different.

*Was it coincidence? Or fate?*

Either way, it didn’t matter.

The most important fact at this moment was that there had been exactly enough space for one scale to be missing at the back of the monster’s neck, which was covered in its strongest scales.

And I hadn’t missed that gap.

“You’ve worked hard.”

Those final words of encouragement were a privilege only the victor could enjoy.

I had driven my spearhead precisely into the area beneath its neck—where a human’s Adam’s apple would have been—and tightened my grip around the shaft as I shoved it deeper.

*Thk—!*

The dragon’s scaled jaw trembled, accompanied by a short groan like it was sucking in a breath that would never come.

Then its jet-black pupil shook, and the sphere of water that had nearly finished forming at the back of its wide-open maw began to scatter.

*Shhhhhhh!*

The incomplete Water Breath was nothing more than ordinary water.

I did not dodge the deluge pouring down toward the crown of my head. I took it all head-on.

The unusually cold waters of Dongting Lake soaked me from head to toe, and my mind settled into calm.

*I won.*

At the same time, a thrilling sensation surged up my spine.

The end of a long and fierce battle.

I had survived once again and driven a spearhead into the neck of a powerful foe. And as always, the end of a life-or-death battle could be reduced to two words.

Vertical and horizontal.

The victor standing tall and the loser collapsing.

Even an evil beast that had lived for an immeasurably long time could not be exempt from this absolute law of the jungle.

*Whoooooosh. Splash!*

The body that had once held unparalleled resilience and power gave way, then fell onto the waters of Dongting Lake.

Through the spray rising high into the air, I saw an eye blinking slowly and a snout trembling faintly.

No.

I heard it.

—You’re exactly the same.

“……!”

The moment I heard someone’s voice echo inside my head, the strength left my hand, which had been about to drive the spear in once more and finish severing the dragon’s windpipe.

As I stared at the enormous eye of the Mutated Water God Dragon as though bewitched, I felt my body suddenly stiffen.

*What the hell…?*

The monster’s appearance, gleaming entirely in jet black and carrying an ominous murderous aura, could no longer be found anywhere.

Like storm clouds clearing after a day of pouring rain, clear and deep eyes resembling the blue sky were now looking at me.

—There is no need to be surprised. After living for around five hundred years, one naturally acquires abilities like this.

“Sound Transmission?”

—Perhaps it would be more accurate to call it mental intent.

The Mutated Water God Dragon—or rather, this divine being also known by another name, the Two-Horned Beast of Dongting Lake—calmly sent its thoughts to me.

—You do not know me, but I know you. You look exactly as you did when I saw you in a dream long ago. I had forgotten it, thinking it was nothing more than a confused dream… Yes. This, too, must be the natural order.

A dream? The natural order?

*Damn it, what the hell is going on?*

“This is… I mean…”

—Huh.

My hesitation, as I searched for something to say, must have looked rather amusing. A growling laugh escaped the blood-soaked corner of the Water God Dragon’s mouth.

—You can neither understand it nor should you try. It is nothing more than the grumbling of an old imugi that failed to ascend because its cultivation was lacking. If there is one thing I regret, it is that I have no time left.

The Water God Dragon’s words were true. Its body had already reached its limit and stood on the verge of death, while the light was gradually fading from its deep eyes.

*Damn it.*

Even if I regretted it now, the water had already been spilled.

I bit down on my lip.

I felt sorry about the Water God Dragon’s death. And to be perfectly honest, I also felt disappointed.

This mystical being had regained its senses moments before death. It was an important key to solving the mystery.

*Dark Heaven.*

There was no way that a divine and wise imugi had become a mad evil beast that slaughtered humans for no reason.

Someone must have intervened. And if so, Dark Heaven—at the very top of the list of suspects behind every incident currently taking place in the Murim—could not be excluded.

“Who did this, and how?”

It was a short question, but it contained everything.

Yet the Water God Dragon’s mental reply that immediately followed went beyond anything I had expected.

—See for yourself.

“Excuse me?”

In answer to my question, the Water God Dragon simply blinked.

*Slither.*

Blue liquid filled its enormous eye. The thing everyone called tears slowly slid down its scales. The moment it touched my body, I understood what the Water God Dragon had meant.

*Ding.*

> **System**
>
> **Water God Dragon** wishes to convey a portion of its memories to you.
>
> **Memory Fragment** **Acquired**.
>
> The power contained within **Memory Fragment** is leading you into the Water God Dragon’s memories.

Along with the System notification ringing in my ears, the Water God Dragon’s tear spread out like a curtain before my eyes.

*Shhhhhhh.*

Along with the cool sensation of water, the world came to a stop.

* * *

It was exactly what its name suggested: a fragment of memory.

The Water God Dragon’s five hundred years were contained within it in their entirety. But perhaps because of the effects of its mutation, some parts had broken away. Some memories were blurred, while others remained clear.

And the beginning of it all was its birth.

—Guruk?

Somewhere deep beneath the waters of Dongting Lake, a tiny newborn creature looked around in confusion.

It was surrounded by swaying aquatic plants that moved as though dancing and an uncountable number of underwater creatures.

The subjects who sensed the birth of a divine being swam joyfully through the currents.

That day was a joyous one—the day a new master of Dongting Lake was born, and the day a grand enthronement ceremony was held.

—Guruk? Guk!

The new master of the river tilted its head with a curious expression like a puppy, then began swimming with its tiny body.

The moment a being born with dazzling wisdom and power began to move, countless creatures followed behind it, and even the river parted to make way.

*Shhhhhhh!*

Its body, slicing through the waters of Dongting Lake with both flexibility and vigor, gradually grew larger.

Silver scales sprouted across its once-small, soft pink body, and imposing whiskers grew quite long beneath its snout.

It was probably around then.

People who witnessed the divine being appear once every few decades—or perhaps even longer—gave it a new name out of reverence.

A name I knew as well.

*Water God Dragon.*

Perhaps because of the two horns on its forehead, it was also called the Two-Horned Beast. But most people were reluctant to call this beautiful and mysterious being a beast, instead worshiping it as the divine spirit of Dongting Lake.

And the imugi, having received a new name from humans, would occasionally perform acts that truly seemed divine.

It would rescue sailors who had nearly drowned and carry them to remote shores untouched by people. It would also use its innate abilities to calm violent currents.

And that wasn’t all. The one that defeated the evil beast that had once stained the Yangtze with blood was the Water God Dragon.

After defeating the turtle-shaped evil beast in a fierce battle, the Water God Dragon came to rule Dongting Lake and the Yangtze.

Time flowed like water.

After more than five hundred long years had passed, the Water God Dragon had grown beyond comparison with its former self.

It was a benevolent imugi with tremendous strength and profound wisdom, as well as an excellent ruler who knew how to care for its people.

Yet even the Water God Dragon had one concern.

—Huh. Fighting never ends in the Lower Realm.

The devastation it had witnessed throughout its long life was truly horrific.

Humans constantly fought among themselves, and whenever they did, countless rivers of blood and corpses were scattered across the waters.

As two empires fell and wars continued, the Water God Dragon grew worried and weary.

—I have already spent an immeasurably long time in the Lower Realm. When, exactly, will I be able to ascend?

Even when people worshiped it as the divine spirit of Dongting Lake and called it a dragon, the Water God Dragon’s true nature was still that of an imugi that had yet to become a dragon.

For the Water God Dragon, ascension was practically a goal set from the moment of its birth.

But its cultivation progressed so slowly that it came to resent the heavens, and enlightenment never seemed to arrive.

Then, news brought by a school of fish was enough to stir the curiosity of the weary Water God Dragon.

—You say a human has appeared? But no one has visited that place for the past several decades.

An uninvited visitor had entered the deepest, most secret, and most perilous region of Dongting Lake, a place no human had set foot in for a very long time.

Suddenly curious, the Water God Dragon went to the place it had once used as its dwelling. The moment it arrived, it realized that something had gone terribly wrong.

—What is this…!

The Water God Dragon of the past was not the only one to be shocked.

I was the same, staring at the scene through the fragment of memory.

*That couldn’t be…*

Something sticky and unpleasant slowly crawled up my spine.

Overcome by disbelief, doubt, and the shock of being struck in the back of the head, I muttered blankly.

*…A Gate.*

There was no doubt.

Having passed through Gates hundreds, no, thousands of times by then, I was certain.

The black energy pouring in steady streams through the cracks between the enormous rocks was unmistakably mana.

*What the fucking hell…!*

My vision went dizzy, and every kind of profanity echoed inside my head.

If I had not been inside the Water God Dragon’s memories—if I had been able to speak aloud and move freely—I would have smashed everything around me. I would have screamed until my throat split open.

*Fuck, a Gate. Mana!*

My head felt as though it would burst from the countless thoughts racing through it. The shout I could not release scattered at the tip of my tongue.

Eyes wide with shock and fury, I stared blankly at what was unfolding before me.

—Stop! I said stop!

The master of the lake used its entire body to block the countless subjects charging toward it.

The teeth of the fish exposed to demonic qi were sharper than saw blades, and their scales had been dyed completely jet black.

—Please, stop!

But the desperate mental plea could not reach the fish already mutated by demonic qi, and the Water God Dragon was forced to make an extremely difficult decision.

If those strangely powerful and violent fish escaped this place, all of Dongting Lake and the Yangtze would be stained with blood.

A sacrifice was necessary for the greater good.

—…I am sorry.

The battle that took place in the deepest waters of Dongting Lake ended, naturally, with the Water God Dragon’s victory.

But the Water God Dragon was not even given time to grieve.

This wise imugi, which had lived for hundreds of years, understood what it had to do and used its own body to block the enormous rift that constantly poured out ominous energy.

—I do not know what you are, but things will not go as you wish.

*Rumble, rumble, rumble!*

It was the longest and fiercest battle of the Water God Dragon’s entire life.

For seven days and nights, while their strength remained evenly matched, the waters of Dongting Lake and the Yangtze roiled violently, and the people on land grew afraid, believing that the divine spirit had grown angry.

And I already knew the outcome of that battle.

—Krrr…

The Water God Dragon had lost its dazzling intelligence and fallen into an evil beast. It let out a low growl.

It had protected its territory and subjects by absorbing most of the demonic qi, but it could not withstand all that power.

*Hissss.*

Both its eyes slowly turned red.

Yet the last grain of reason remaining inside it caused the Water God Dragon to surge out of the water.

It was the will of an old imugi that wanted to find the culprit behind this terrible atrocity.

*Shhhhhhh!*

On a dark night, the blackened waters parted.

The Water God Dragon rose as though ascending to heaven, and its red pupil reflected a person sitting on a moss-covered rock and splashing their feet in the water.

“The energy here is nice. Coming all this way was worth it.”

A clear, gentle voice.

A dazzlingly white nape.

And a silver hairpin securing long black hair twisted up.

*…Honglan.*

Along with the name of one person surfacing in my mind, the entire world surrounding me shattered into pieces.
```
