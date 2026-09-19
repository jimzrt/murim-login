<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0473.txt",
      "sha256": "417f48bfe1bec9b13dae20627a62a0292511529206041e7ecd269a5741e14dde",
      "bytes": 12916
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0ee88d7b170d67619d2689600c01570fe54ea9f7f3e2806e10d9fd08f448e475",
      "bytes": 3015
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "30e6ba49128079e0c23bac2c431896b8d8e15f9d946e31a02c7616bbd3f432ea",
      "bytes": 152895
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "bfe1e7f51435a327c5143d0752a876c8fdeafd5ed8f5d5b93a4cf3decdc80c84",
      "bytes": 553
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8a0be63db578cac44a78673a984d62314baccd26db8282146a3d64bc2e3cbbc6",
      "bytes": 147628
    }
  ],
  "estimated_tokens": 9048
}
-->

# Durable State Update — Chapter 473

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 473. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 473. Profile updates may replace only one
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
  "chapter": 473,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 473,
    "continuity_sources": [473],
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
    "The forced System Quest, Corrupted Spirit Beast, remains active for Taekyung, with Logout disabled until it ends and the Mutated Water God Dragon as its required target.",
    "The Mutated Water God Dragon was once a noble spirit beast awaiting ascension before an unknown power corrupted it into an evil beast.",
    "The battle against the dragon remains active; Cheongpung, Taekyung, Mungyeong, and Jeok Cheongang are engaged or supporting the engagement.",
    "Cheongpung remains highly resistant to the dragon's Fear and has returned to the frontline while using the Zaha Divine Technique.",
    "Mungyeong remains partially affected by Fear, reducing his martial ability, but continues fighting as the former Slaughter Saint.",
    "The dragon possesses extreme speed, immense physical durability, black scales, enormous whiskers, and energy accumulated over countless years that it can release as an anomalous martial art.",
    "Mungyeong believes the dragon caused the destruction at Donghu Stronghold and the death of Yangtze One Saber using its body and whiskers.",
    "Jeok Cheongang can withstand the dragon's direct tail attack without moving and considers it the strangest and most frightening monster he has encountered.",
    "Zhuge Feng has withdrawn under cover with the others and is protecting them rather than joining the current battle.",
    "The Dongting Fisherman remains alive and severely injured for interrogation about Dark Heaven.",
    "Honglan is recovering, while Ju Wongong remains unconscious under guard after surviving the most dangerous stage of his injuries.",
    "An unidentified figure is hanging from the dragon's head and tearing out its whiskers barehanded."
  ],
  "continuity_sources": [
    472,
    471
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Did the Mutated Water God Dragon destroy Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left?",
    "What unknown power corrupted the Water God Dragon, and what are its true origin and purpose?",
    "Who is the unidentified figure hanging from the dragon's head, and why can that figure tear out its whiskers barehanded?"
  ],
  "safe_through": 472,
  "temporary_decisions": [
    "Render 악물 as evil beast and distinguish the dragon's anomalous energy from Force and Sword Energy.",
    "Preserve Mungyeong's dry Slaughter Saint voice, Jeok Cheongang's gruff teasing, and Cheongpung's innocent but increasingly profane voice.",
    "Retain Cheongpung's deliberate Zhuge Pong misnaming as a comic address gag.",
    "Continue rendering 수염 as whiskers, 기암괴석 as bizarre boulder, and preserve jang and geun measurements."
  ],
  "version": 1
}
```

## Exact glossary matches

| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 검법     | **sword technique**                              |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 대한민국 | **Korea** | Country reference. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 흑목조간 | **black-wood fishing rod** | The Dongting Fisherman's distinctive weapon; the broken rod is his only known trace. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 472
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

## Korean source

```text
＃473화



푸푹!

변이된 수신룡.

놈의 거대한 눈깔에 백염의 창날을 쑤셔 넣은 순간, 나는 직감했다.

‘단단하고, 깊다.’

마치 끝이 보이지 않는 동굴에 손을 집어넣은 기분이다.

평범한 인간, 혹은 짐승이었다면 이 일격으로 눈은 물론이고 머리까지 흔적도 없이 녹아 버렸을 테지만, 놈은 아니었다.

‘뭐 이런……!’

대가리의 크기가 워낙 거대하다 보니 백염을 끝까지 찔러넣어도 창날에 서린 강기가 내부 깊숙한 곳까지 미치지 못한다.

거기에 더해 그 안의 뼈와 살은 어찌나 단단한지.

내 예상을 훌쩍 뛰어넘는 반발력에 당황한 찰나, 변이된 수신룡이 고통에 찬 괴성을 내질렀다.

- 크롸아아아아아!

회심의 일격으로 끝장을 보진 못했을 뿐, 아무런 타격도 주지 못한 것은 아니다.

창날에 실린 열양지기에 의해 놈의 한쪽 눈동자가 녹아내렸다.

끔찍한 고통에 거대한 동체는 몸부림쳤고, 그와 동시에 익숙한 시스템 알림이 귓가를 파고들었다.

띠링.



- [Lv.??? 변이된 수신룡]이 지금껏 경험해 보지 못한 고통과 분노에 휩싸였습니다!

- [광폭화] 상태에 돌입합니다!

- [광폭화]의 영향으로 대상의 모든 능력치가 증가합니다! 단, 순간적으로 이성을 상실했기에 전투에 관한 판단력이 흐려집니다!



“……어?”

시스템 알림을 듣는 순간 내가 이성을 상실할 뻔했다.

‘염병할. 광폭화는 뭔 놈의 광폭화야.’

일 똑바로 해라, 시스템. 안 그래도 괴물인데 여기서 더 강해지면 난 뭐 먹고 살라는 거냐.

하지만 이미 발동된 시스템이요, 엎질러진 물이었다.

하나밖에 남지 않은 수신룡의 눈동자가 온통 핏빛으로 물들며 본격적인 광폭화가 시작되었다.

- 캬우우우우우!

천지를 울리는 괴성과 함께 엄청난 바람이 전신을 후려쳤다.

눈 한번 깜빡이기도 전에 코앞까지 들이닥친 절벽을 바라본 나는 내심 중얼거렸다.

‘어, 좆 됐네.’

꽈앙!

하늘이 쪼개지는 듯한 굉음과 함께 전신을 덮쳐 오는 거대한 충격파. 순간 눈앞이 아득하게 흐려지고 눈의 초점이 흔들린다.

수만, 수십만 근의 힘을 실어 절벽에 대가리를 박은 수신룡은 거기에서 멈추지 않았다.

후우우웅!

수면 위로 드러난 몸통의 길이만 삼십여 장이다. 드러나지 않은 것까지 따진다면 현대의 항공 모함과도 비견될 만한 크기.

그런 거대한 괴물이 미친 듯이 날뛰기 시작하자 막을 수 있는 것은 아무것도 없었다.

꽈앙, 꽝! 콰과과광!

쉴 새 없이 절벽과 강물에 머리를 처박고, 꼬리를 휘두르며 때로는 낚싯바늘에 걸린 물고기처럼 몸뚱어리를 퍼덕인다.

움직임 한 번에 주위가 초토화되고 수많은 바위 조각과 풍압이 나를 덮쳤다.

바로 지금처럼.

뻐억!

“……흡!”

빌어먹을, 하필이면 뾰족하게 튀어나온 바위에 등이 찍혔다.

등줄기를 타고 흐르는 짜릿한 격통. 하지만 이를 악물고 신음을 참아냈다.

이건 나를 떨어트리려는 수신룡의 처절한 몸부림이다. 지금 떨어졌다가는 오히려 역공을 당할 수도 있다.

나는 놈의 눈깔 깊숙이 박아 넣은 백염을 쥔 손아귀에 힘을 더하며, 거대한 동체의 움직임에 따라 미친 듯이 요동치는 몸의 중심을 잡았다.

“이…… 개새끼가!”

고작 이 정도로 떨어져 나갈 줄 알았다면 큰 오산이다.

나는 한 손으로 창대를 단단히 말아쥐고, 다른 한 손으로는 보이지 않는 무언가를 움켜잡았다.

비록 지금은 공기밖에 없는 텅 빈 허공이겠지만, 이제부터는 달라질 거다.

오직 나만이 쓸 수 있는 마법의 주문이 있으니까.

‘인벤토리 오픈. 소환.’

스윽, 탁.

명령어와 동시에 예리한 소검의 검자루가 손아귀에 잡혔다.

지금껏 내가 배운 검법(劍法)이라고 해봤자 헌터 훈련소에서 배운 기초 검술이 전부.

하지만 이런 상황에서는 검법이고 뭐고 필요 없다.

누구보다 빠르게, 남들보다 다르게. 색다르게 리듬을 타는 도마 위의 회 뜨기 명인이 되어야 하는 순간이다.

“앞으로 네 이름은 활어회다. 아니면 세꼬시.”

나는 엄숙하게 선언하며 청백색의 열양지기에 휩싸인 소검의 검날을 그대로 쑤셔 넣었다.

푹!

비록 검신의 길이가 짧아 깊숙하게 찌를 수는 없지만, 고통의 신호는 확실히 느꼈다.

단단하고 뽀얀 속살이 불에 타들어 가듯 갈라지며 검푸른 핏물이 터져 나온다.

“이 새끼 어울리지 않게 핑살이네.”

- 크르륵!

놈의 아가리에서 튀어나온 신음과 함께 순간 멈칫하는 동체. 나는 때를 놓치지 않고 재차 소검을 휘둘렀다.

서걱! 푸푹!

- 크르르륵!

푸푸푸푸푹!

- 크라아아아아아!

검법? 그딴 거 없다. 그저 손이 가는 대로, 눈에 보이는 대로 닥치고 베고 쑤셨다.

한차례 뼈와 살을 부수고 가른 검날이 다시 빠져나오고 재차 나아가는 속도는 섬광보다도 빨랐고, 그럴 때마다 놈의 괴성과 몸부림 역시 거세졌다.

‘아니, 이게 이럴 때 도움이 되네.’

초인이라 부를 수 있는 신체 능력도 한몫했겠지만, 인류의 보물이라 할 수 있는 USB를 통해 단련된 손목 스냅은 절정의 검수도 한 수 접을 정도다.

‘아아, 이것이 만류귀종(萬流歸宗)…….’

언제였던가. 현자가 된 직후 USB의 파손을 결심한 나를 만류하며 진호 형이 해 주었던 말이 뇌리를 스쳤다.



‘태경아, 옛 선조들께서 남기신 말을 기억해라. 치고 죽은 귀신이 때깔도 곱다. 치는 게 남는 거다.’

‘……선조 누구?’

‘그게 중요하니? 지금 네가 국보급 문화재를 파괴하려 한다는 게 문제지. 너 그거 지우면 내가 직접 문화재청에 신고 넣을 거야. 최소 가석방 없는 징역 25년 본다.’

‘미친놈인가.’



치긴 뭘 쳐. 때깔이 곱긴 뭐가 고와.

당시에는 한 대 칠 뻔했는데, 이제 와서 생각해 보니 대한민국 건국 이래 최고의 명언이 따로 없다.

나는 진호 형에게 깊이 감사하며 이제는 추억이 되어 버린 그녀들을 떠올렸다.

‘고맙습니다. 우에하라, 사랑합니다. 마파두부집 효녀.’

서걱! 푸푸푸푸푸푹!

- 그라아아아아!

아, 비명 스고이네.

감사의 마음을 담은 친일 검법이 뻥 뚫린 동공을 후벼 파며 점점 깊숙이 안으로 파고들자, 변이된 수신룡도 저 까마득한 지상에 있는 또 다른 적들에 대한 공격을 멈출 수밖에 없었다.

후우우웅, 꽝!

보이지 않지만 소리로 알 수 있었다.

고통으로 거대한 동체가 흔들림과 동시에 지상을 향해 내리 찍히던 꼬리가 엉뚱한 곳을 강타했다는 것을.

이어 솟구치는 흙과 물보라 속에서 표적을 바꾼 은색 빛줄기가 날아들었다.

취리리리릭!

밖에서 보면 괴이한 광경일 것이다. 괴물이 자신의 수염으로 녹아내린 눈동자를 후비고 있는 꼴이니까.

하지만 내 입장에서는 전혀 우습지 않았다.

‘빌어먹을.’

아무리 변이된 수신룡의 눈동자가 거대했다고 해도, 그 공간은 수십 줄기의 수염을 피하기에는 너무나도 비좁았다.

최대한 몸을 비틀었음에도 흑목조간의 그것처럼 교묘하게 움직인 빛줄기가 화룡갑을 피해 맨살을 베어 냈다.

푸확!

“큭!”

뿜어지는 붉은 핏물과 전신 곳곳에서 느껴지는 화끈한 통증.

회피와 동시에 공력을 일으켜 최대한 몸을 보호했기에 이 정도로 끝난 거지, 조금이라도 늦었다면 사지 중 하나는 잘려 나갔을지도 모른다.

취리리릭!

재차 날아드는 수십 개의 빛줄기. 나는 빠르게 번져 나가는 고통을 참으며 신형을 틀었다.

무시무시한 절삭력을 지닌 은빛 수염이 털끝 하나의 차이로 빗나가자 순간 등골이 서늘해졌다.

‘공간이 너무 좁아. 이대로면 꼼짝없이 당한다.’

위기감 때문이었을까. 내가 멈칫한 사이, 동아줄처럼 꼬여 창날과도 같은 형태를 취한 빛의 창이 얼굴을 향해 날아들었다.

쉬잉!

“……!”

실로 엄청난 속도.

느려진 세상 속, 나는 눈을 부릅뜬 채 날카로운 파공성과 함께 날아드는 빛줄기를 바라보았다.

머릿속에서는 수많은 경우의 수와 생각이 스쳐 지나가고 있었다.

‘당장 백염을 뽑아서 휘두른다면. 아니, 이미 늦었다. 그리고 그 전에 중심을 잃을지도 몰라.’

지금 이 순간까지도 놈의 대가리는 미친 듯이 흔들리고 있다. 만약 지지대나 다름없는 백염을 뽑는다면 나는 아주 잠깐 중심을 잃을 것이고, 그것으로 끝장이다.

‘더 좋은 방법이 있을 텐데. 분명 더 좋은 방법이…….’

하지만 내게 주어진 시간을 찰나에 불과했고, 황급히 휘두른 소검은 빛줄기와 부딪친 순간 속절없이 튕겨 나갔다.

아니, 수백 개의 파편으로 나뉘어 산산조각 났다.

콰창!

어쩌면 당연한 결과일지도 몰랐다.

저 한 가닥, 한 가닥의 수염에 실린 힘은 비록 강기에 미치지 못하지만 절정 고수의 검기를 상회하는 수준.

그런 기운이 한데 뭉쳤으니 USB를 통해 익힌 매국노 검법으로 막아설 수 있을 리 만무하다.

후웅!

이대로 당하는 건가?

공간을 지우며 눈앞까지 들이닥친 파괴적인 힘을 멍하니 바라보던 나를 움직인 것은, 말 그대로 본능에 가까웠다.

화륵, 콰드드득!

빛줄기가 가슴을 관통하려던 순간, 나는 어느덧 청백색의 화염이 깃든 손으로 빛줄기를 움켜잡았다.

그건 화염신장도, 멸염신권도 아니었다. 그저 전신의 모든 기운을 끌어올려 대항하는 무식한 힘겨루기였다.

그리고 이 격돌의 결과가 나오기까지는 그리 오랜 시간이 필요하지 않았다.

파지직, 푸확!

두 개의 강대한 기운이 부딪치며 눈부신 섬광이 눈앞을 가득 메운다.

그리고 그 화려한 빛무리 너머로, 걸레짝처럼 너덜거리는 손아귀와 미세하게 굵기가 줄어든 빛줄기가 보였다.

누가 우위에 있는지는 명백한 상황.

‘젠장. 품고 있는 기운의 크기가 달라.’

시스템을 이용한 초고속 성장으로 막대한 공력을 쌓은 나지만, 본래는 영물(靈物)로서 수백 년의 세월 동안 기를 축적한 놈에게 비할 바는 아니었다.

콰드드득!

이 벅찬 힘겨루기도 서서히 한계다.

나는 손아귀를 통해 전해지는 통증을 느끼며 이를 악물었다.

“이 활어회 새끼가!”

이대로 끝낼 수는 없다. 나는 젖먹던 힘까지 끌어 올려 신형을 비틂과 동시에, 업어치기 하듯 놈의 수염을 힘껏 잡아당겼다.

말도 안 되는 일이지만 이렇게라도……!

콰드드드득, 뽁!

“어?”

- 크륵?

나도 당황하고, 변이된 수신룡도 당황했다.

느려진 세상 속에서 뿌리째 뽑혀 나간 수십 가닥의 수염이 힘을 잃은 채 나풀나풀 추락한다.

‘뭐야, 시발. 이게 왜 뽑혀.’

순간 오만가지 생각이 머릿속을 스친다.

이게 이렇게 뽑혀도 되나. 혹시 얘가 모발에 비해 모근이 약한 건가. 아니 근데 그래도 이게 정말 되는 건가…….

그리고 마침내 한 가지 결론에 도달했다.

‘내 힘이, 정말 미친 듯이 세구나.’

생각해 보면 충분히 가능한 일이다. 강철로 반죽을 할 수 있을 정도의 근력인데 그깟 수염 뽑는 게 뭐라고.

제아무리 항공모함 크기의 괴물이라고 해도 한계가 있는 법.

엄청난 강도를 자랑하는 비늘, 뼈와는 달리 모근은 내 근력으로도 뽑아낼 수 있는 수준이었던 것이다.

‘이게 이렇게 되네.’

초인이라 부를 만한 근력을 지닌 나만이 가능한 일.

지금까지 피하고 벨 생각만 했지, 수염을 뜯어 버릴 생각을 못 했다. 나는 큰 깨달음과 함께 백염을 회수한 뒤 발을 내디뎠다.

쐐애애액!

동공을 빠져나오자 당황으로 굳어버린 놈의 거대한 몸뚱어리와 껌뻑이는 눈동자가 보였다.

“너 이 새끼…….”

나는 환하게 웃으며 놈의 수염을 잡아 뜯었다.

콰드드득!
```

## Final English reading copy

```markdown
# Chapter 473

*Puhuk!*

The Mutated Water God Dragon.

The instant I drove the tip of White Flame into its enormous eye, I realized something.

*Hard. And deep.*

It felt like plunging my hand into a cave with no visible end.

If it had been an ordinary human or beast, this single strike would have melted not only its eye but its entire head without a trace.

But this thing was different.

*What the…!*

Its head was so enormous that even after I drove White Flame in as far as it would go, the Force wrapped around the spearhead could not reach deep enough inside.

On top of that, the bones and flesh within were absurdly tough.

I was still reeling from the resistance that far exceeded my expectations when the Mutated Water God Dragon let out a scream of agony.

—Kraaaaaaaaaah!

I had failed to finish it with my decisive strike, but that did not mean I had failed to inflict any damage.

The Scorching Yang Qi carried by the spearhead had melted one of its eyes.

Its enormous body writhed in horrible pain. At the same time, a familiar System notification pierced my ears.

*Ding.*

> **System**
>
> - **Lv. ??? Mutated Water God Dragon** is overwhelmed by pain and rage it has never experienced before!
>
> - Enters **Berserk** Status!
>
> - Due to **Berserk**, all of the target’s stats increase! However, because it has momentarily lost its reason, its judgment in combat is clouded!

“... Huh?”

The moment I heard the System notification, I nearly lost my own reason.

*Damn it. What the hell is this Berserk bullshit?*

Do your damn job properly, System. It was already a monster. If it got even stronger, how was I supposed to make a living?

But the System had already activated, and the water was already spilled.

The Water God Dragon’s only remaining eye turned completely bloodred, and its Berserk Status began in earnest.

—Kyaaaaaaaaaow!

Along with a roar that shook heaven and earth, an enormous gust of wind slammed into my entire body.

Before I could even blink, I saw a cliff rush right up to my face.

*Oh. I’m fucked.*

*Kwaang!*

A tremendous shock wave crashed over my entire body with a roar that seemed to split the sky apart. My vision blurred, and my eyes lost focus.

The Water God Dragon slammed its head into the cliff with tens of thousands—perhaps hundreds of thousands—of *geun* of force, but it did not stop there.

*Whoooooosh!*

The length of its torso exposed above the surface of the water alone was more than thirty *jang*. If I counted the part hidden beneath the water, it was comparable in size to a modern aircraft carrier.

Once a monster that enormous began rampaging like a mad thing, nothing could stop it.

*Kwaang! Kwang! Kwagwagwagwang!*

It repeatedly smashed its head into the cliff and the river, lashed out with its tail, and sometimes flapped its entire body like a fish caught on a hook.

Every movement reduced the surrounding area to a wasteland, and countless fragments of rock and blasts of wind came crashing down on me.

Just like now.

*Ppeok!*

“... Hng!”

Damn it. Of all places, my back had slammed into a sharply jutting rock.

A searing pain raced up my spine. But I gritted my teeth and held back my groan.

This was the Water God Dragon’s desperate struggle to throw me off.

If I fell now, it might counterattack instead.

I tightened my grip on White Flame, driven deep into the bastard’s eye, and steadied the center of my body as it bucked wildly with the enormous body’s movements.

“You… you fucking bastard!”

If it thought I would be thrown off by something this pathetic, it was gravely mistaken.

I wrapped one hand tightly around the spear shaft and grasped at something invisible with the other.

At the moment, my hand was clutching nothing but empty air.

But that was about to change.

I had a magical command that only I could use.

*Inventory Open. Summon.*

*Shhk. Tak.*

The instant I gave the command, the hilt of a sharp short sword appeared in my hand.

The only sword technique I had learned was the basic swordsmanship taught at the Hunter training center.

But in a situation like this, who cared about sword technique?

Faster than anyone else, different from everyone else. This was the moment to become a sashimi master riding a different rhythm on the cutting board.

“From now on, your name is live-fish sashimi. Or maybe bone-in sashimi.”[^1]

I made the solemn declaration and drove the blade of the short sword, wrapped in blue-white Scorching Yang Qi, straight into it.

*Puk!*

The sword was too short to stab very deeply, but I definitely felt the signal of pain.

Its firm, pale flesh split open as though it were burning, and dark-blue blood burst out.

“You’ve got pink flesh, of all things, you bastard.”

—Krrrk!

A groan burst from the creature’s maw, and its body stopped for a moment.

I did not miss the opening and swung the short sword again.

*Schk! Puhuk!*

—Krrrrrk!

*Puh-puh-puh-puh-puhuk!*

—Kraaaaaaaaaah!

Sword technique? There was no such thing.

I simply cut and stabbed wherever my hands moved and wherever my eyes saw.

The speed at which the blade emerged after crushing and splitting through bone and flesh, then shot forward again, was faster than a flash of light.

Each time it did, the creature’s screams and thrashing grew more violent.

*Huh. This is actually useful at a time like this.*

My physical abilities, which could be called superhuman, certainly played a part. But the wrist snap I had trained through the USB—a treasure of humanity—was enough to make even a Peak sword master yield a move.

*Ah. So this is All Streams Returning to the Source…*

When had it been?

Just after I became a Sage, Jin-ho hyung had tried to stop me when I decided to destroy the USB.

His words flashed through my mind.

*Taekyung, remember the words left behind by our ancient ancestors. A ghost that dies after getting one in has a beautiful complexion. It’s getting one in that counts.*

*…Which ancestor said that?*

*Does that matter? The problem is that you’re about to destroy a national-treasure-grade cultural artifact. If you erase that thing, I’ll report you directly to the Cultural Heritage Administration. You’re looking at a minimum of twenty-five years in prison with no chance of parole.*

*Is he insane?*

What did he mean, getting one in? And what did he mean, a beautiful complexion?

Back then, I had nearly hit him.

But looking back now, those words were without question the greatest saying since the founding of Korea.

I felt profound gratitude toward Jin-ho hyung and thought of the women who had now become memories.

*Thank you, Uehara. I love you, filial daughter of the mapo tofu restaurant.*

*Schk! Puh-puh-puh-puh-puhuk!*

—Graaaargh!

Ah, what a *sugoi* scream.

The pro-Japanese sword technique filled with my gratitude gouged into the gaping pupil and drove deeper and deeper inside.

The Mutated Water God Dragon had no choice but to stop attacking the other enemies far below on the ground.

*Whoooooosh—Kwaang!*

I could not see what had happened, but I could tell from the sound.

As the enormous body shook in pain, the tail that had been coming down toward the ground had struck somewhere completely different.

Then, amid the rising dirt and spray, a streak of silver light flew toward me after changing targets.

*Chiririririk!*

From the outside, it must have been a bizarre sight.

A monster was using its own whiskers to gouge at its melted eye.

But from my position, there was nothing funny about it.

*Damn it.*

No matter how enormous the Mutated Water God Dragon’s eye was, the space was far too narrow for me to avoid dozens of whiskers.

Even though I twisted my body as much as possible, the streaks of light moved with the same cunning subtlety as the black-wood fishing rod, slipping past my Fire Dragon Armor and slicing into my bare flesh.

*Puhwak!*

“Ghk!”

Red blood sprayed out, and searing pain spread through every part of my body.

I had managed to protect myself by circulating my internal energy at the same time as I dodged, so this was all that happened.

If I had been even slightly slower, one of my limbs might have been severed.

*Chiriririk!*

Dozens of streaks of light flew toward me again.

I endured the rapidly spreading pain and twisted my body.

When the silver whiskers, which possessed terrifying cutting power, missed by less than the width of a hair, a chill ran down my spine.

*The space is too narrow. I’ll be cut to pieces if this continues.*

Perhaps it was because of that sense of crisis.

While I hesitated, a spear of light, twisted together like a rope into the shape of a spearhead, flew toward my face.

*Shwing!*

“...!”

It was unbelievably fast.

In the slowed-down world, I stared wide-eyed at the streak of light flying toward me with a sharp sound as it tore through the air.

Countless possibilities and thoughts flashed through my mind.

*If I pull out White Flame right now and swing it… No. It’s already too late. And I might lose my balance before then.*

Even now, the bastard’s head was shaking like mad.

If I pulled out White Flame, which was practically acting as a support, I would lose my balance for just an instant.

That would be the end.

*There has to be a better way. There has to be some better way…*

But the time I had been given amounted to no more than a fleeting instant, and the short sword I swung in haste was helplessly knocked away the moment it collided with the streak of light.

No—it shattered into hundreds of fragments.

*Kwa-chang!*

Perhaps it was only natural.

The power contained in each individual whisker did not reach the level of Force, but it surpassed the Sword Energy of a Peak master.

With that much energy gathered together, there was no way the traitorous sword technique I had learned through the USB could stand against it.

*Whoom!*

*Am I going to get hit like this?*

I stared blankly at the destructive force erasing the space between us and rushing toward my face.

What moved me was something close to instinct itself.

*Fwoosh—Kwaddeudeuk!*

Just as the streak of light was about to pierce through my chest, I found myself gripping it with a hand wreathed in blue-white flames.

It was neither Flame Divine Palm nor Flame-Extinguishing Divine Fist.

It was nothing more than a crude contest of strength, in which I dragged up every ounce of energy in my entire body and forced it against the attack.

The result of that clash did not take long to reveal itself.

*Pajik—Puhwak!*

Two powerful energies collided, filling my vision with a blinding flash.

And beyond that dazzling radiance, I could see my hand hanging in tatters like a rag and the streak of light, its thickness reduced ever so slightly.

There was no question who held the advantage.

*Damn it. The amount of energy we possess is on completely different levels.*

I had accumulated a tremendous amount of internal energy through the System’s accelerated growth.

But I could not compare with the bastard, which had accumulated qi for hundreds of years as a spirit beast.

*Kwa-deu-deuk!*

Even this grueling contest of strength was slowly reaching its limit.

I gritted my teeth as pain traveled through my hand.

“You live-fish-sashimi bastard!”

I could not end things here.

I summoned every last ounce of strength I possessed, twisted my body, and yanked hard on the creature’s whiskers as though executing a shoulder throw.

It was impossible.

But even if it was, I had to try—

*Kwadeudeudeudeuk—Ppok!*

“... Huh?”

—Krrk?

I was stunned.

The Mutated Water God Dragon was stunned too.

In the slowed-down world, dozens of whiskers had been torn out by the roots and were fluttering helplessly toward the ground.

*What the fuck? Why did those pull out?*

Countless thoughts flashed through my mind.

Was it really okay for them to come out this easily? Were its roots weaker than its hair? No, but even so, could this really happen…?

At last, I reached one conclusion.

*My strength is really fucking insane.*

When I thought about it, this was entirely possible.

I had enough muscle to knead steel like dough. What was pulling out a few whiskers compared to that?

No matter how enormous a monster the size of an aircraft carrier was, everything had its limits.

Unlike its scales and bones, which boasted tremendous durability, its hair roots were apparently weak enough for my Strength to pull out.

*So this is how it works.*

This was something only I could do, with my strength worthy of being called superhuman.

Until now, I had only thought about dodging and cutting.

It had never occurred to me to tear the whiskers out.

With that great enlightenment, I retrieved White Flame and stepped forward.

*Shwaaaaaaaaaak!*

When I emerged from the pupil, I saw the creature’s enormous body frozen stiff in confusion and its eye blinking rapidly.

“You bastard…”

I smiled brightly and tore out its whiskers.

*Kwadeudeuk!*

[^1]: *Hwal-eo-hoe* is sashimi prepared from live fish, while *sekkosi* is thinly sliced raw fish served with the bones left in.
```
