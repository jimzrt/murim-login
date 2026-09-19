<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0425.txt",
      "sha256": "e7e957b196e5eb87ea2af0f12556aa9fd4416aca6b1fe037e4b68288fee1e707",
      "bytes": 12935
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9b65af46f8201b20f09d0dcaa7a1e403b4ad18e088105eb1978e77522288c86c",
      "bytes": 2135
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4ad052de6a1346999152919ed52db285ece8218aa2b22f0333147c5bdd9bff1a",
      "bytes": 140691
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "06622996891c0e61b360f2b8b27a64abe3743818759362e1abaeb5420c40e43a",
      "bytes": 533
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "f99fd9385fb9bceaf1f3a6fafff7f982c120763f424526b4fadf8e2430cc6500",
      "bytes": 667
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "a13e15d1b72f69c859f2dcdf486ad3e9ef5aafb179be7d14601f57a160b31e8d",
      "bytes": 1182
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "590303318fa0da6b60699da4fb376e0b4f4ad5d5ac3049feb3fa7299dc332dc3",
      "bytes": 129850
    }
  ],
  "estimated_tokens": 8655
}
-->

# Durable State Update — Chapter 425

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 425. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 425. Profile updates may replace only one
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
  "chapter": 425,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 425,
    "continuity_sources": [425],
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
    "Jin's Middle Dantian is open, allowing him to perceive the center and grain of magic and sever spells.",
    "Jin has Severe Injury, Excessive Bleeding, and Exhaustion; his Strength, Stamina, and Agility are temporarily greatly reduced.",
    "Endurance transformed into Will, and Indomitable is temporarily active, slightly raising all attributes and reducing fatigue.",
    "The Arch Lich survived One Annihilation with its left arm destroyed and remains weakened but active.",
    "The Arch Lich used Blood Explosion, took White Flame, and launched the spear back at Jin.",
    "The Skeleton Warlord sacrificed itself to save Jin and was destroyed by Bone Explosion; Hero's Soul remains embedded in the ground with its hand.",
    "The Arch Lich continues creating the enormous incomplete Gate in the ruined city.",
    "The Gate threatens Team Leader Choi, Xiao Shen, the Peace Guild members, and Jin's family.",
    "The Arch Lich continues to regard Jin as a possible Adversary.",
    "The Quest One Who Returned from Death remains active, keeping Login unavailable until the Quest ends."
  ],
  "continuity_sources": [
    424,
    423
  ],
  "open_questions": [
    "Is the Skeleton Warlord irreversibly erased, and can Jin recover Hero's Soul?",
    "Can Jin survive his catastrophic injuries and Exhaustion well enough to continue fighting?",
    "Can Jin defeat the Arch Lich and recover White Flame?",
    "Can Jin stop or disrupt the enormous incomplete Gate before it becomes a catastrophe?",
    "What is Asmodeus's current status and location?"
  ],
  "safe_through": 424,
  "temporary_decisions": [
    "Render 탈진 as Exhaustion, 의지 as Will, and 불굴 as Indomitable.",
    "Render 블러드 익스플로젼 as Blood Explosion and 본 익스플로젼 as Bone Explosion.",
    "Render 영웅의 혼 as Hero's Soul and 소멸 as Erasure.",
    "Render 중단전 as Middle Dantian and 단중혈 as Tanzhong acupoint.",
    "Preserve the Arch Lich's archaic, contemptuous register and Jin's profanity while retaining established wuxia and System terminology."
  ],
  "version": 1
}
```

## Exact glossary matches

| 이정룡    | **Lee Jungryong** |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 424
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 408
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 423
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

## Korean source

```text
＃425화



터텅!

목표를 잃은 백염이 지면을 나뒹굴었다.

“아.”

석상처럼 굳어 버린 나를 향해 아크 리치가 손가락을 튕겼다. 허공에서 생성된 한 쌍의 검은 손이 내 전신을 옥죄었다.

이제는 마법의 발현을 위한 주문조차 건너뛰는 무영창 마법.

저벅, 저벅.

아크 리치가 걸음을 내디딜 때마다 안개와도 같은 놈의 몸 곳곳에 스며들었다.

일섬에 휘말려 사라졌던 왼팔이 천천히 재생되었고, 깨지고 금이 간 뼈는 전보다 더 어두운 빛을 띠며 견고하게 복구되었다.

게이트의 완성이 가까워질수록, 놈 역시 강해지고 있었다.

- 어쩐지 네게서 죽음의 냄새가 난다 했더니 그만한 이유가 있었군. 인간과 몬스터의 우정이라…… 아주 감동적이야.

우드득.

전신 곳곳에서 뼈가 어긋나는 소리가 들렸지만, 나는 멍하니 아크 리치의 어깨 너머를 바라보았다.

정확히는 지면을 파고든 한 자루의 검과 마지막까지 검 자루를 놓지 않은 누군가의 손을.

‘스켈레톤 워로드.’

몬스터와 인간은 신이 정한 숙적의 관계다.

나와 녀석도 마찬가지였다. 분명 처음에는 그랬다.

하지만…… 이제야 알겠다. 어느 순간부터인가 내게 있어 스켈레톤 워로드는 몬스터가 아니었음을.

‘몬스터라고 생각했다면, 내 손으로 그 녀석을 소멸시켰겠지.’

직접 스켈레톤 워로드를 처치했다면 레벨 업을 통해 마지막 희망을 얻을 수 있었을 것이다.

그러나 나는 망설였고, 결국 포기했다.

녀석이 내 목숨을 살려 주어서가 아니다. 마음속에서 이미 친구로 받아들였기 때문이었다.

허탈한 웃음이 흘러나왔다.

‘제기랄. 정을 붙이지 말았어야 했는데.’

그런 내 모습에 아크 리치의 안광이 가늘게 좁혀졌다.

- 웃어? 이런 상황에서?

“우리 엄마가 그러셨거든. 웃으면 복이 온다고.”

- 정신이 나갔군.

“내가 웃겠다는데 왜 지랄이야. 네가 내 맞선임이냐?”

나는 아크 리치의 얼굴을 향해 침을 뱉었다. 핏물인지 가래인지 구분이 되지 않는 걸쭉한 액체가 놈의 미간을 타고 주르륵 흘러내렸다.

동시에 눈이 있어야 할 자리에서 붉은 안광이 거세게 타올랐다.

- 대답, 잘 들었다.

“좆이나 까 잡숴.”

지나온 삶에 후회가 남지 않는다면 거짓말이지만 모두 부질없는 짓이다. 후회는 언제나 늦는 법이고 마지막까지 발버둥 쳤으니 할 만큼 했다.

마음을 내려놓자 모든 것들이 한바탕 꿈처럼 느껴졌다. 아크 리치의 안광에 편안히 미소짓는 내 얼굴이 비쳤다.

- 분명 말했었지. 네 육신은 갈기갈기 찢어질 것이며, 영혼은 죽음의 강을 영원히 떠돌게 될 것이라고.

나는 선선히 고개를 끄덕여 동의해 주었다.

“그렇겠지. 네가 충성하는 그 마왕 새끼처럼.”

- ……!

“만나게 되면 안부 전해 줄게. 주소 알려 줘 봐.”

- ……언제까지 그따위 헛소리를 지껄일 수 있는지 두고 보지.

아크 리치의 손짓에 따라, 나를 옥죄어오고 있던 거대한 마력의 손이 사지를 붙잡더니 이내 엄청난 힘으로 내 몸뚱어리를 양옆으로 끌어당기기 시작했다.

천천히, 그리고 조금씩.

우직, 우지지직.

내부에서 작은 파열음과 함께 잠시 잊고 있었던 통각(痛覺)이 깨어난다.

이제는 소리칠 힘조차 남아 있지 않다고 생각했는데, 나도 모르게 입술 사이로 비명이 뛰쳐나왔다.

“크읍, 크아아아악!”

- 듣기 좋군. 훨씬 나아졌어.

고통으로 눈앞이 새하얗게 물들었다. 나는 참았던 비명을 토해 내며 죽음이 다가오길 기다렸다.

하지만 고통마저 느껴지지 않을 무렵, 내게 찾아온 것은 죽음이 아닌 시스템 알림이었다.

띠링.



- [상급 포션]을 사용했습니다!

- 사용한 포션의 양이 너무 적습니다. 미약하게 부상이 치유되었습니다!

- 당신의 부상은 너무나도 심각합니다. 지금보다 더 많은, 양질의 치유가 필요합니다!



……뭐라고?

시원한 감각과 다시 깨어난 고통을 느끼며 눈을 부릅뜨자 비웃음이 맺힌 안광으로 나를 응시하는 아크 리치가 보였다.

놈의 손에 들려 있는 유리병도 함께.

‘저건.’

이정룡의 아공간 포켓에 들어 있던 포션 중 하나다. 이미 한참 앞서 아크 리치에게 빼앗겼던.

그리고 지금, 놈은 치유의 목적으로 만들어진 포션을 고통을 주기 위한 도구로 사용하고 있었다.

딱 죽음의 문턱 앞에서 멈출 수 있을 만큼의. 가장 큰 고통을 느낄 수 있을 만큼의 치유.

- 어리석은 인간이여. 이 몸이 그리 쉽고 편안한 죽음을 허락할 줄 알았더냐.

“……!”

- 계속해서 울부짖거라. 겁쟁이처럼 눈물 흘리고, 고통에 몸부림치며 네 어리석음을 깨달은 후에야 죽음의 강으로 향할 수 있으리라.

아크 리치는 비웃음이 가득한 음성과 함께 포션이 담긴 유리병을 흔들었다.

아직 십 분의 일도 채 비워지지 않은 포션은 내가 앞으로 느껴야 할 고통의 양과 같았다.

그리고 그 시간은 한없이 느리고, 억겁처럼 길게 흘러가겠지.

미약한 치유와 더불어 전신에 엄습해 오는 고통으로 숨이 가빠진다. 나는 애써 웃으며 아크 리치에게 물었다.

“마왕님 만세 삼창하면 빨리 끝내 주냐?”

- 글쎄, 열과 성을 다한다면 생각해 보지.

“안 해. 개새꺄.”

- 괜찮다. 어차피 시간은 넉넉할 테니. 천천히 생각해 보는 것도 나쁘지 않을…….

퍼걱!

아크 리치의 안광이 파르르 떨렸다. 그것은 나 역시 크게 다르지 않았다.

그건 나도, 놈도. 그 누구도 예상치 못했던 일이었으니까.

- ……이게 무슨.

아크 리치는 의혹 어린 음성과 함께 자신의 가슴을 내려다보았다.

빛. 그건 빛이었다. 온 세상을 밝힐 것처럼 휘황한 빛이 놈의 가슴을 뚫고 튀어나와 있었다.

‘아니, 빛이 아니야.’

나는 넋 나간 눈빛으로 그것을 바라보았다. 그건 어느 때보다 찬란한 빛을 내뿜고 있는 한 자루의 검이었다.

한없이 눈에 익은 그 검의 이름을, 나는 알고 있었다.

‘영웅의 혼.’

그리고 뼈로 이루어진 아크 리치의 가슴 너머로 보이는, 검 자루를 굳게 틀어쥔 손의 주인도.

“……!”

세상이 모든 움직임을 멈춘 듯했다.

나는 한없이 느려진 세상 속에서 수백, 수천 개의 뼛조각이 모여드는 것을 지켜보았다.

누군가가 남긴 마지막 흔적에 지나지 않던 그것들은 서로를 끌어당기고 저마다의 형태를 이루었다.

투둑, 툭!

뼈의 융합.

가장 처음으로 각각 두 개의 팔과 다리가 만들어지고, 가슴과 배가 생겨났다.

검은 광택이 흐르던 뼈들은 [영웅의 혼]이 흩뿌리는 빛에 씻겨져 나가 어느덧 은은한 금색을 띠었으며 더욱 길고 단단해졌다.

‘아.’

그건 경이로운 광경이었다.

무수히 많은 뼛조각이 모여 신체를 이루는 것은 시간을 역행(逆行)하는 듯했고, 검에서 흘러나온 빛이 뼈마디에 새겨진 어둠을 몰아내는 것은 새로운 존재의 탄생을 알리는 예고처럼 느껴졌다.

그리고 마침내 완성된 신체에 두개골이 내려앉은 그때.

파앗!

텅 비어 있던 동공에서 황금빛 안광이 터져 나왔다. 더없이 익숙하면서도 낯선 느낌.

다음 순간 이어진 목소리와 함께 멈췄던 시간이 흘러가기 시작했다.

- 도대체 왜, 라고 물었었지.

“……!”

번개에 관통당한 것처럼 몸이 떨렸다. 불과 한 시간도 지나지 않은 기억이 섬광처럼 뇌리를 스쳤다.



‘그럼, 도대체 왜?’



그래, 그때의 나는 분명 그렇게 물었었다. 왜 나를 구했느냐고. 어째서 소멸을 각오하면서까지 스스로 방패를 자처했느냐고.

그런 내 질문에 녀석은 모르겠다고 했다. 자신이 왜 이런 짓을 벌였는지, 검에 홀렸던 것일지도 모르겠다면서.

그리고 지금, 그때 듣지 못했던 대답이 귓가를 파고들었다.

- 넌 간악하지만, 썩 괜찮은 인간이니까. 단지 그뿐이었다.

썩 괜찮은 녀석.

언젠가 내가 누군가에게 해 주었던 말.

나는 아연한 시선으로 녀석을 바라보았다. 전보다 더욱 커지고 단단해진, 은은한 황금빛을 띤 전신. 두개골의 이마 부위에 아로새겨진 알 수 없는 은빛 문양은 왕관을 닮았다.

아니, 왕관임이 분명했다.



[Lv.160 스켈레톤 킹]



녀석의 머리 위에 뜬 시스템 창을 보자, 나도 모르게 헛웃음이 터져 나왔다.

“많이 컸네. 우리 골골이.”

- 어쩐지 전부터 줄곧 몸이 간지럽다 했었지.

검고 작았던 애벌레가 마침내 껍질을 벗고 날개를 폈다.

스켈레톤 워로드, 아니 스켈레톤 킹의 안광이 초승달처럼 휘었다. 녀석도, 나도 웃고 있었다.

그리고 유일하게 웃지 못하는 한 존재가 있었다.

- 크악! 크아아아아악!

아크 리치.

수십 만의 언데드 군단을 휘하에 거느리고, 마르지 않는 강대한 마력을 지닌 전대미문의 네임드 몬스터는 고통으로 몸부림쳤다.

정확히 가슴 한가운데를 관통한 한 자루의 검.

[영웅의 혼]에서 흘러나온 황금빛이 마력을 삼키고 신체를 녹이고 있었다.

어쩌면 놈의 영혼조차도.

- 인간.

스켈레톤 킹의 나직한 부름에, 나는 내가 해야 할 일을 깨달았다.

‘이제…… 끝내자.’

띠링.



- [영웅의 혼]이 당신에게 치유의 빛을 부여합니다!

- 모든 상태 이상이 해제되었습니다!

- 모든 부상과 능력치가 회복됩니다!

- 이 자리에 없는 누군가가 당신을 향해 미소 짓습니다.



화아아악!

[영웅의 혼]으로부터 뿜어져 나온 빛기둥이 몸을 감쌌다.

따스한 온기와 함께 으스러진 뼈가 붙고 살이 아물었다. 상처 입은 장기와 망가진 혈맥이 치유되었으며 금방이라도 터질 듯한 열기가 용암처럼 들끓었다.

‘할 수 있다.’

그건 나 자신도 놀랄 만큼 단호한 확신이었고, 실제로도 그러했다.

힘이 있으니 행하지 못할 것이 없다.

‘와라.’

쐐애애애액! 탁!

지면을 나뒹굴던 백염을 손아귀로 끌어당김과 동시에.

팟!

나는 허공에 붕 뜨는 감각과 함께 발을 뻗었다.

그 걸음의 끝에, 강대한 마력을 줄기줄기 내뿜으며 고통에 몸부림치는 아크 리치가 있었다.

- 도대체! 무슨 마법을 부린 것이냐!

나를 발견한 아크 리치가 발작하듯 외쳤다.

붉은 안광이 쉴 새 없이 흔들리고 크기를 부풀렸다.

그것만으로도 현재 놈이 느끼고 있을 고통이 어느 정도인지 알 만했다.

- 빌어먹을, 빌어먹을 인간! 크아아악!

나는 대답 대신 천천히 백염을 들어 올렸다.

고통으로 인해 사지를 부들부들 떨고 있는 아크 리치와 놈의 뒤에 우뚝 선 거대한 게이트를 향해 투명한 창날을 겨누었다.

화륵.

단전에서 날개를 펴고 날아오른 화룡이 불덩이가 되어 사지 백해로 솟구친다. 손가락 끝을 타고 흘러, 백염의 창날 위로 푸른 화염을 피워올리고 겹겹이 덧씌웠다.

- 노옴! 감히 무슨 짓을!

아크 리치가 발광하듯 손발을 흩뿌렸지만, 놈이 쏘아 보낸 마법은 내게 닿기도 전에 방어막처럼 주위를 둘러싼 열기와 부딪쳐 사라졌다.

그러나 약화된 아크 리치와는 달리, 게이트를 둘러싼 어둠은 더욱 크게 휘몰아쳤다.

그리고 마침내, 나는 깨달았다.

‘지금!’

다리부터 허리, 어깨와 손목을 타고 흐른 회전력에 백염이 몸을 부르르 떨었다.

전신에서 끌어 올린 미증유의 기운이 어느 때보다 거대한 화염을 피워 올렸다.

그래, 바로 지금이다.

팟.

단 한 걸음. 아크 리치와 나를 가로막던 모든 공간이 사라지고 시간이 느려졌다.

천천히 달싹이는 놈의 입술이 주문을 끝맺기 전에, 나는 모든 의지와 힘이 담긴 일격을 쏘아 보냈다.

- 블링……!

일섬(一殲).

두 번의 실수는 없었다. 창날로부터 뛰쳐나간 푸른 화룡이 아크 리치와 게이트를 집어삼켰다.

콰아아아아아아!
```

## Final English reading copy

```markdown
# Chapter 425

*Thud!*

White Flame, having lost its target, rolled across the ground.

“Ah.”

The Arch Lich snapped its fingers at me, frozen stiff as a statue. A pair of black hands materialized in midair and squeezed my entire body.

A spell that no longer even needed an incantation to manifest.

*Step. Step.*

With every step the Arch Lich took, something seeped into various parts of its body, which was as hazy as mist.

The left arm that had vanished in One Annihilation slowly regenerated, while its shattered and cracked bones were restored even more solidly than before, taking on an even darker hue.

The closer the Gate came to completion, the stronger it became as well.

—So there was a reason I thought I smelled death on you. Human and monster, friends… How touching.

*Crack.*

I heard bones shifting out of place throughout my body, but I stared blankly over the Arch Lich’s shoulder.

More precisely, at the sword buried in the ground—and the hand of someone who had not let go of its hilt until the very end.

*The Skeleton Warlord.*

Monsters and humans were sworn enemies, as ordained by God.

The same had been true of me and it. It certainly had been at first.

But… I finally understood now. At some point, the Skeleton Warlord had stopped being a monster to me.

*If I had thought of it as a monster, I would have erased it with my own hands.*

If I had killed the Skeleton Warlord myself, I could have gained one last hope through a level-up.

But I had hesitated, and in the end, I had given up.

Not because it had saved my life. Because I had already accepted it as a friend in my heart.

A hollow laugh escaped me.

*Damn it. I never should have grown attached.*

At the sight of me, the Arch Lich’s eye-lights narrowed.

—Are you laughing? In a situation like this?

“My mother used to say that fortune comes to those who smile.”

—You have lost your mind.

“Why the fuck do you care if I laugh? What are you, my immediate senior in the army?”

I spat toward the Arch Lich’s face. A thick liquid, impossible to distinguish as blood or phlegm, trickled down between its brows.

At the same time, the red eye-lights in the places where its eyes should have been flared violently.

—I heard your answer clearly.

“Go eat a dick.”

It would be a lie to say I had no regrets about the life I had lived, but there was no point in any of it now. Regret always came too late, and I had struggled until the very end. I had done enough.

Once I let go of everything, it all felt like one long dream. My face, smiling peacefully at the Arch Lich’s eye-lights, was reflected in them.

—I told you, did I not? Your flesh would be torn to pieces, and your soul would wander the River of Death forever.

I readily nodded in agreement.

“I suppose so. Just like that Demon King bastard you serve.”

—……!

“If we meet, I’ll pass on your regards. Give me the address.”

—……Let us see how long you can continue spouting such nonsense.

At the Arch Lich’s gesture, the enormous hands of mana squeezing me seized all four of my limbs. Then they began pulling my body apart with tremendous force.

Slowly, little by little.

*Crack. Craaack.*

Small ruptures sounded inside me, and the sensation of pain I had momentarily forgotten awakened.

I thought I no longer had enough strength even to scream, but a cry escaped between my lips before I realized it.

“Gnh, graaaaagh!”

—That sounds much better.

My vision was bleached white by the pain. I finally let out the screams I had been holding back and waited for death to approach.

But when even the pain began to fade, what came to me was not death, but a System notification.

*Beep.*

> **System**
>
> - **High-grade Potion** has been used!
>
> - The amount of potion used is too small. Your injuries have been healed slightly!
>
> - Your injuries are extremely severe. You require a greater amount of higher-quality healing than this!

…What?

As I felt a refreshing sensation and the pain awaken once more, I opened my eyes wide.

The Arch Lich was staring at me with mocking eye-lights.

And in its hand was a glass bottle.

*That’s…*

It was one of the potions that had been in Lee Jungryong’s subspace pocket—the one the Arch Lich had stolen long ago.

And now, it was using a potion made for healing as a tool to inflict pain.

Healing enough to stop me right at the threshold of death.

Healing enough to make me feel the greatest possible pain.

—Foolish human. Did you truly think this body would grant you such an easy and comfortable death?

“……!”

—Continue to howl. Weep tears like a coward and writhe in agony. Only after you realize your foolishness will you be permitted to travel to the River of Death.

The Arch Lich shook the glass bottle filled with potion, its voice thick with mockery.

The potion was not even one-tenth empty yet. That was equal to the amount of pain I still had to endure.

And that time would pass infinitely slowly, stretching on like countless eons.

Weak healing spread through my body, but so did pain that came crashing down over every inch of me. My breathing grew ragged. I forced a smile and asked the Arch Lich,

“If I give three cheers for the Demon King, will you end this sooner?”

—Perhaps, if you devote yourself to it with all your heart.

“I’m not doing that, you son of a bitch.”

—Very well. Time is plentiful, after all. There is no harm in taking your time to think about—

*Thwack!*

The Arch Lich’s eye-lights trembled.

I was just as shaken.

Neither of us—not a single person—had expected what happened next.

—……What is this?

With a doubtful voice, the Arch Lich looked down at its chest.

Light.

It was light. A dazzling radiance, bright enough to illuminate the entire world, had burst through its chest.

*No. It’s not light.*

I stared at it with vacant eyes.

It was a sword, emitting a radiance more brilliant than ever before.

I knew the name of that sword, which was so familiar to me.

*Hero’s Soul.*

And I knew the owner of the hand gripping its hilt tightly, visible beyond the Arch Lich’s skeletal chest.

“……!”

It was as if the entire world had stopped moving.

Within that world, slowed to an immeasurable crawl, I watched hundreds—thousands—of fragments of bone gather.

They were nothing more than the last traces someone had left behind, but they pulled toward one another and formed their own shapes.

*Pop. Pop!*

The fusion of bones.

Two arms and two legs formed first, followed by a chest and abdomen.

The bones that had gleamed black were washed clean by the radiance scattered from **Hero’s Soul**. Before long, they had taken on a soft golden hue and become longer and sturdier.

*Ah.*

It was a wondrous sight.

The countless fragments of bone gathering to form a body seemed to reverse the flow of time, while the light flowing from the sword drove the darkness engraved in each joint away, as if heralding the birth of a new being.

And finally, when a skull settled onto the completed body—

*Fwoosh!*

Golden eye-lights burst from its empty sockets.

The feeling was both utterly familiar and completely strange.

The next moment, a voice rang out, and the time that had stopped began to flow again.

—You asked me why, did you not?

“……!”

My body trembled as if lightning had pierced through me. A memory from less than an hour ago flashed through my mind.

*Then why? Why, exactly?*

Yes. That was what I had asked back then.

Why had it saved me? Why had it chosen to become my shield even though it had been prepared to face Erasure?

In answer to my question, it had said it did not know. It had said it did not know why it had done such a thing. Perhaps it had been bewitched by the sword.

And now, the answer I had not heard then pierced my ears.

—You are a crafty human, but a pretty decent one. That was all.

*A pretty decent guy.*

Words I had once said to someone.

I stared at it in disbelief.

Its entire body was larger and sturdier than before, with a faint golden glow. An unknown silver pattern was engraved across the forehead of its skull, resembling a crown.

No. It was unmistakably a crown.

> **System**
>
> - **Lv. 160 Skeleton King**

The moment I saw the System window hovering above its head, a hollow laugh escaped me.

“Look how much you’ve grown, Bones.”

—No wonder I had felt itchy all over my body for so long.

The small black caterpillar had finally shed its skin and spread its wings.

The Skeleton Warlord—or rather, the Skeleton King’s eye-lights curved like crescent moons.

It was smiling.

So was I.

And there was one being who was unable to smile.

—Graaaagh! Graaaaaaaaaagh!

The Arch Lich.

The unprecedented named monster, which commanded hundreds of thousands of undead and possessed inexhaustible, tremendous mana, writhed in agony.

A single sword had pierced straight through the center of its chest.

The golden radiance flowing from **Hero’s Soul** devoured its mana and melted its body.

Perhaps even its soul.

—Human.

At the Skeleton King’s quiet call, I realized what I had to do.

*Now… let’s finish this.*

*Beep.*

> **System**
>
> - **Hero’s Soul** grants you the light of healing!
>
> - All status effects have been removed!
>
> - All injuries have been healed, and all attributes restored!
>
> - Someone who is not here smiles at you.

*Fwoooooosh!*

A pillar of light burst from **Hero’s Soul** and enveloped my body.

Along with a gentle warmth, my shattered bones joined together and my flesh healed. My injured organs and damaged meridians recovered, while a heat hot enough to burst boiled through me like lava.

*I can do this.*

It was a certainty so firm that even I was surprised by it.

And in reality, it was true.

If I had strength, there was nothing I could not do.

*Come.*

*Fwoooooosh! Clack!*

At the same time that I pulled White Flame, rolling across the ground, into my hand—

*Fwoosh!*

I thrust out my foot, feeling myself rise into the air.

At the end of that step stood the Arch Lich, streaming powerful mana as it writhed in agony.

—What in the world! What magic did you use?!

The Arch Lich spotted me and shouted as if in a fit.

Its red eye-lights shook without pause and swelled larger.

That alone told me how much pain it was suffering.

—Damn you, damn you, human! Graaaaagh!

Instead of answering, I slowly raised White Flame.

I aimed its transparent spearhead at the Arch Lich, trembling violently from the pain, and the enormous Gate standing behind it.

*Whoosh.*

The fire dragon spread its wings and soared from my dantian, transforming into a ball of flame as it surged through every limb and bone in my body. It flowed along my fingertips, kindling blue flames atop White Flame’s spearhead and layering them over and over.

—You cur! How dare you—

The Arch Lich flailed its arms and legs in a frenzy, but the magic it fired collided with the heat surrounding me like a barrier and vanished before it could even reach me.

Unlike the weakened Arch Lich, however, the darkness surrounding the Gate roiled even more violently.

And at last, I realized.

*Now!*

White Flame trembled as rotational force traveled up through my leg, waist, shoulder, and wrist.

The unprecedented surge of qi drawn from my entire body kindled flames larger than ever before.

Yes.

This was the moment.

*Fwoosh.*

One step.

All the space separating the Arch Lich and me disappeared, and time slowed.

Before the Arch Lich’s slowly moving lips could finish the incantation, I launched a single strike filled with every ounce of my will and strength.

—Blink…!

*One Annihilation.*

There would be no second mistake.

The blue fire dragon that sprang from White Flame’s spearhead swallowed both the Arch Lich and the Gate.

*Kwooooooooooong!*
```
