<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0809.txt",
      "sha256": "e8fc47669b08faa1edde5402535557f60f56324f2832647b92cd15ea0d9240af",
      "bytes": 13765
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2aed220fb65b67d7537c8e62164492313224ba234ca92dd5ff45665c254e3a58",
      "bytes": 791
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1e8b8a33ae952423b359fb7c39a8c3a83fe8a43b894e38ef519681dd66dd55a7",
      "bytes": 225527
    },
    {
      "path": "characters/Michael.md",
      "sha256": "7aba5badf171ce2856f6d0470b6edcc6713b036d436462844e932a4eafdfc8b1",
      "bytes": 820
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "1dffb051932f7b167b6c087b1d4c10c1fa1207350e4a203211f7d3f503f165ee",
      "bytes": 707
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7c0e3ab3ab0cfe27e92a116960cc3f7a94573b671698596f3f385070423d776f",
      "bytes": 247922
    }
  ],
  "estimated_tokens": 8751
}
-->

# Durable State Update — Chapter 809

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 809. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 809. Profile updates may replace only one
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
  "chapter": 809,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 809,
    "continuity_sources": [809],
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
    "Jin is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate the Prophet within an unspecified time limit.",
    "The Prophet remains missing as the monster army in the Rub’ al Khali routs and the Hunters pursue it.",
    "Jin continues fighting despite mounting physical exhaustion.",
    "The Skeleton King and its undead are blocking the monsters’ retreat, and Magic Johnson is using large-scale magic on the battlefield."
  ],
  "continuity_sources": [
    807,
    808
  ],
  "open_questions": [
    "Where is the Prophet, and how is he directing the monster army?"
  ],
  "safe_through": 808,
  "temporary_decisions": [
    "Keep magical power distinct from mana."
  ],
  "version": 1
}
```

## Exact glossary matches

| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 초식     | **form**                                         | Numbered technique movement                           |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 도사      | **Daoist**                                                      |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 무닌 | **Muninn** | One of the two ravens associated with Odin in Norse mythology. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 만티코어 | **Manticore** | A-Rank Gate monster and original raid target. |
| 오크 | **Orc** | Monster species. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 근골 | **Muscles and Bones** | System attribute increased by 2 during the climb. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 암초 | **reef** | Reefs blocking the narrow water route. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 802
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 808
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a monster posing as the leader of the revived Hasasin, whose power includes stopping transport vehicles and absorbing blood and a pale mist from the dead.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

## Korean source

```text
＃809화



그것은 마치, 거대한 둑이 무너지는 것과 같은 광경이었다.

쿵. 쿵. 쿠웅!

흉포하기 그지없는 대형 몬스터들이 등을 돌려 도망친다.

수 미터에 이르는 거체가 걸음을 내디딜 때마다, 엄청난 무게에 짓밟힌 사체와 소형 몬스터들이 두부처럼 으스러졌다.

콰직! 콰드득!

- 끼이이잇!

- 캬륵!

사방에서 고통에 찬 단말마가 울려 퍼졌지만, 그중 헌터의 것은 어디에도 없었다. 적어도 오늘 이 전장에서 약자는 인간이 아닌 몬스터였으니.

약육강식(弱肉强食).

몬스터들은 탄생과 함께 각인된 본능을 따라 움직였다.

다만 흉포함에 사로잡혀 도시를 파괴하고 인간들을 학살했던 것과는 달리, 지금 이 순간 놈들을 움직이는 본능은 가장 원초적인 무언가였다.

‘두려움.’

감히 눈도 마주치지 못할 만큼 강한 S급 몬스터들이, 뒤이어 무리를 이끌던 우두머리 대부분이 몰살당했다.

실낱같은 지휘 체계는 무너졌고 열 배에 달하던 병력 차는 성큼 좁혀졌다.

아직 남아 있는 몬스터의 숫자만 어림잡아 수천을 헤아렸으나, 전의(戰意)를 상실한 맹수는 초식동물보다도 손쉬운 사냥감이나 다름없다.

그리고 힘겨운 악전고투를 치른 사냥꾼들은, 아직 이 사냥을 끝마칠 생각이 없었다.

“놈들이 도망친다! 쓸어 버려!”

“한 놈도 살려 보내지 마라!”

“으아아아!”

붉게 충혈된 눈. 살점과 피가 끈적하게 묻어 있는 병장기.

치열했던 전투를 증명하듯, 핏물을 흠뻑 뒤집어쓴 헌터들은 혈인(血人)이나 다름없는 몰골로 사냥감을 좇았다.

자꾸만 손아귀에서 빠져나가려는 검 자루를 가죽끈으로 질끈 동여매고, 수없이 활시위를 당기느라 덜덜 떨리는 팔로 옆구리에 맨 화살통을 더듬었다.

피로하다. 끈적한 모래 위에 널브러져 잠들고 싶다.

그러나 멈출 수 없었다.

“네놈들 때문에 벤하민이, 벤하민이…… 이 개새끼들!”

누군가는 친구를.

“아, 안 돼! 엠마!”

누군가는 전우이자 연인을.

“Motherfucker. 네놈도 한 달 전 샌프란시스코에 있었나? 뭐? 빌어먹을. 알아듣지도 못할 소리는 그만 지껄이고 지옥에나 떨어져.”

또 다른 누군가는 그리 오래되지 않은 과거의 복수를 끝마쳐야 했으니까.

이 분노가 사라질 때까지 몬스터들을 죽이고, 또 죽여야 했으니까.

서걱, 푸푹!

- 컥!

사방에서 괴성과 함께 녹색 핏물이 솟구친다. 어디선가 날아든 화살이 오크의 머리통을 관통하며 트롤의 발목을 꿰뚫었다.

- 크륵.

주춤거리는 트롤을 에워싼 헌터들이 얼마 남지 않은 마나를 밑바닥까지 긁어모아 병장기에 실었다. 분노에 찬 수십 개의 날붙이가 괴물을 난도질했다.

퍼퍽! 콰드드득!

엄청난 수적 열세 속에서 치른 전투다. 헌터들도 상당한 희생을 치러야 했고 그들이 흘린 핏값은 몬스터의 것으로 환산해야 한다.

“죽어! 죽어엇!”

막대한 피로와 흥분으로 잔뜩 쉬어 버린 외침이 곳곳에서 울려 퍼졌다.

잘게 다진 고기처럼 조각난 트롤의 사체에 침을 뱉은 그들은 충혈된 눈으로 다음 사냥감을 찾아 움직였다.

펑, 퍼버버벙!

공격 마법이 비처럼 쏟아져 내렸다.

이런 와중에도 수천의 몬스터는 사체와 동족들을 무참히 짓밟으며 남쪽을 향해 물결처럼 나아갔고, 헌터들은 거대한 암초처럼 그 물결을 막아섰다.

그리고 그 중심에, 내가 있었다.

쉭!

비스듬히 내리그은 일격.

창날을 타고 쏘아진 예리한 바람이 도망치는 몬스터 무리를 스쳤다.

촤아악.

비명 대신 터져 나온 핏물이 모래 위를 적신다.

하지만 운 좋게 공격의 범위에서 벗어난 놈들은 내게서 더욱 거리를 벌리며 속도를 높였다.

처음부터 동족(同族)이라는 자각조차 없는 몬스터들이다.

전투가 아닌 회피를 최우선 목적으로 삼은 괴물들은 오직 생존을 위해 필사적으로 도망쳤고, 지금도 수많은 몬스터가 뿔뿔이 흩어져 포위망을 벗어나고 있었다.

‘놓쳐선 안 돼. 한 놈이라도 더 쓰러트려야 한다.’

전투는 이미 끝났다. 지금까지의 결과만으로도 두고두고 회자 될 대승(大勝)이고 역사에 기록될 것이다.

하지만 아직도 어림잡아 오천이 넘는 몬스터가 남아 있다.

그토록 죽이고, 또 죽였음에도 군단이라 칭하기에 부족함이 없는 대병력.

오늘 이 자리에서 놈들을 놓친다면 또 다른 재앙의 불씨를 남기는 셈이다.

‘그래도 당장 추격하는 건 무리야.’

모두가 길고 치열한 전투로 지쳐 있다. 지금 헌터들을 움직이는 것은 몬스터를 향한 분노와 복수심일 뿐, 그 이상도 이하도 아니었다.

그리고 이와 같은 생각을 떠올린 것은, 비단 나뿐만이 아니었다.

“인간!”

“진!”

후방을 막고 있던 스켈레톤 킹과, 몬스터들을 휩쓸며 이곳까지 도달한 매직 존슨이 내 양옆으로 다가왔다.

“최대한 빨리 대열을 수습한 뒤 놈들을 추격해야 해. 부대를 나누어서 이동하는 게 좋겠어.”

매직 존슨이 숨 가쁜 목소리로 말을 건넨다. 부상을 입고 뒤떨어진 오우거 한 마리를 베어 가른 스켈레톤 킹이 대답했다.

“동의한다. 마력이 거의 바닥나긴 했지만 이런 기회를 놓칠 수는 없지. 이미 그리핀 몇 마리를 언데드로 만들어 두었다. 시야를 확보하기에는 충분해.”

대답하려던 나는 문득 숨을 삼켰다. 거친 호흡을 가다듬으며 고개만 끄덕이는 내 모습에 스켈레톤 킹이 눈살을 찌푸렸다.

“인간, 괜찮나?”

“아무, 아무것도 아냐. 신경 쓰지 마.”

거짓말이다.

팔다리가 물에 젖은 것처럼 무겁다. 단전을 가득 채웠던 공력도 어느덧 바닥을 드러내는 중이었다.

무엇보다 전투 중간중간 신체 깊숙한 곳에서 느껴지는 아릿한 통증이 점점 커지고 있었다.

‘빌어먹을 디버프.’

나는 억지로 담담한 표정을 유지하며 얼마 전 보았던 시스템 메시지를 떠올렸다.

그것은 미카엘 실베르트를 쓰러트리고 긴 잠에서 깨어난 직후, 나를 기다리고 있던 알림 중 하나였다.



- 모든 일에는 그에 합당한 대가가 뒤따르는 법. 그러나 당신은 연이은 경고를 무시하고 한계를 뛰어넘는 힘을 다시 한번 사용했습니다.

- 특수 디버프, [망가진 신체]의 정보가 갱신됩니다.

- 특수 디버프, [부서진 신체]가 새롭게 부여됩니다.

- 디버프로 인한 기존의 능력치 하락 수치는 그대로 유지되며, 새로운 디버프 효과가 추가로 적용됩니다.

- [근골]이 약화 됩니다. 부상을 입을 확률이 상당량 증가합니다.

- [공력]의 소모가 심해집니다. 기의 수발이 전처럼 자유롭지 않습니다.



부서진 신체.

그것이 시스템의 경고를 무시한 대가였다.

일섬(一殲)이 지닌 미증유의 파괴력은 적의 생명뿐만 아니라 내 몸뚱어리를 갉아먹었고, 이는 레벨업을 포함한 어떤 방법으로도 치유할 수 없는 종류의 것이었다.

‘미카엘 실베르트를 상대로 일섬을 쓰지 말았어야 했나.’

입맛이 씁쓸했지만 어쩔 수 없는 일이었다. 당시의 내게는 일섬 외의 별다른 선택권이 주어지지 않았으니까.

나는 매직 존슨이 걱정스럽게 내민 포션을 밀어 내며 입을 열었다.

“이걸로는 무리예요. 지금 같은 상황에서 포션을 썼다간 더 지쳐 버릴 거고요.”

“하지만.”

“지금은 놈들을 추격하는 것이 우선입니다. 그중에서도 특히…….”

“그래, 선지자.”

스켈레톤 킹이 나직한 목소리로 뇌까린다. 곧이어 내 눈빛에 담긴 뜻을 이해한 녀석이 입맛을 다셨다.

“아직 발견하지 못했다. 분명 어딘가에서 놈이 지켜보고 있을 거라 생각했는데, 우리 짐작이 틀렸어.”

매직 존슨도 한 마디를 보탰다.

“나로서도 마찬가지야. 진, 어쩌면 선지자는 처음부터 이곳에 없었을지도 몰라.”

“처음부터? 그럼 애초에 다른 것을 노린 함정이었다는 겁니까?”

“확신할 수는 없어. 하지만 가능성은 충분하지.”

잠시 생각하던 나는 고개를 저었다.

S급 몬스터만 네 마리에 만 오천이 넘는 몬스터 대군이다. 단순히 함정을 위한 미끼치고는 너무나도 과했다.

‘하지만 왜 나타나지 않은 거지?’

선지자는 예측불허의 강자다. 온갖 결계에 둘러싸인 대마도사, 지크프리트 바스만을 별다른 전투의 흔적도 남기지 않은 채 죽였으니 그 무위는 미카엘 실베르트와 대등하거나 이상일지도 모른다.

‘만약 놈이 가세했다면, 이 전투도 어찌 되었을지 모른다.’

제아무리 나라고 해도 만티코어 로드와 라이칸스로프 챔피언을 상대로 동시에 싸우는 것은 결코 쉽지 않았다.

그리고 그때야말로 선지자가 모습을 드러내기에 최적의 타이밍이었을 것이다.

‘그런데 끝끝내 나타나지 않았지.’

만약 이 전투가 함정이었고 선지자가 노리는 것이 본진이었다 해도 이해가 되지 않는 것은 매한가지였다.

스스로 말하기에는 낯부끄러운 말이지만, 세계 헌터 연맹의 중심이자 머리는 바로 나 자신이니까.

결국 내가 내린 결론은 하나였다.

“함정이 아닙니다.”

고민은 길었으나 그 시간은 짧았다.

나는 아직도 미친 듯이 몬스터를 추격하는 헌터들을 바라보며 말을 이었다.

하급 지휘관이라 할 수 있는 팀장들의 추격 정지 명령에도, 그들은 청력을 잃어버린 것처럼 몬스터를 쫓고, 또 쫓는 중이었다.

“선지자가 진정으로 원하는 게 무엇인지는 모르겠지만…… 바로 이 상황 역시 놈의 계산에 있었어요.”

“뭐?”

“지금 이대로 쉬지 않고 추격을 이어 가면 부대는 순식간에 와해 됩니다. 우선 최대한 빨리 흥분한 헌터들을 수습하세요.”

“이봐, 진.”

매직 존슨이 낮게 가라앉은 눈빛으로 나를 응시했다.

“부대를 수습해야 한다는 뜻에는 나 역시 같은 생각이긴 하지만…… 그럼 선지자는 무엇을 위해 저 많은 몬스터들을 이 사막으로 내몬 거지?”

“둘 중 하나예요. 이 정도만으로도 우리를 상대하기에 충분하다고 느꼈거나…….”

문득 말을 멈춘 나는, 이내 씹어뱉듯 말을 이었다.

“아니면 이미 이 정도 병력쯤은 소모되어도 상관없을 만큼, 막강한 전력을 구축했거나.”

“……!”

“……!”

그 순간, 주위의 공기가 차갑게 얼어붙었다.

나는 딱딱하게 굳은 두 사람의 얼굴을 바라보며 미처 입밖으로 꺼내지 못한 한 마디를 마음속으로 흘려 보냈다.

한 가지는 확실하다. 극한에 이른 직감은 예지처럼 나를 사로잡고 있었다.

‘선지자는, 나와 대면하길 원하고 있어.’

몬스터의 괴성이 멀어졌다. 그제야 하나둘씩 쓰러지는 사람들의 사이로 바람이 불었다.

짙은 혈향(血香)을 머금은 그것은 서늘한 밤공기를 타고 퍼져 나갔다.



* * *



백팔십오 명.

누구보다 용감하게 싸웠고, 그렇기에 두 번 다시 돌아올 수 없는 강을 건널 수밖에 없던 이들의 숫자다.

그러나 살아남은 자들은 계속해서 나아가야 했다.

우리가 이곳에 온 목적은 전투에서 승리하기 위해서가 아니라, 선지자를 처치하여 재앙을 뿌리 뽑는 것이었으니.

‘시간이 없어.’

추격자보다 도망자가 조급하다는 것은 전부 개소리다. 그 도망자가 전 세계를 집어삼킬 폭탄을 갖고 있다면 더더욱.

“전원, 재정비를 끝마쳤습니다.”

최 팀장의 보고를 들으며 눈을 떴다.

비록 한 시간도 안 되는 짧은 운기 조식이었지만, 전보다는 훨씬 호전된 몸 상태가 느껴졌다. 차분하게 가라앉은 마음도 함께.

‘도대체 뭘까. 선지자는.’

오랫동안 이어진 의문이다.

다섯 번째 무닌. 인간의 것이 아닌 마법을 사용하는, 몬스터로 추정되는 존재. 그리고 수많은 광신도를 이끄는 사막의 교황.

놈에 대해 알아 갈수록 늪에 빠지는 기분이다. 진정한 정체는 무엇인지, 목적은 무엇인지. 또 지금 어디에 있는지…….

만약 시스템이 실체화된 존재라면, 멱살이라도 붙잡고 묻고 싶은 심정이었다.

디버프든 뭐든 감당할 테니까, 자그마한 단서 하나라도 던져 달라고.

‘제기랄.’

나는 내심 욕설을 중얼거리며 어두워지는 하늘을 바라봤다.

사막의 낮은 짧았고, 마력 분포도의 영향 탓인지 하늘은 회색빛이었다.

마치 미카엘 실베르트처럼.

인간으로 태어나, 몬스터로 죽음을 맞이한 그 괴물처럼.

그리고 놈에 대한 모든 기억이 하나둘씩 떠오른 그 순간.

“……!”

섬광과도 같은 한 줄기 의문이, 뇌리를 관통했다.
```

## Final English reading copy

```markdown
# Chapter 809

It was like watching a massive dam collapse.

*Boom. Boom. KABOOM!*

The most ferocious of the large monsters turned and fled.

Every time their several-meter-tall bodies took a step, the enormous weight crushed corpses and smaller monsters underfoot like tofu.

*Crunch! Crack-crunch!*

—Kiiiiie!

—Kyargh!

Painful death cries rang out all around us, but not one of them belonged to a Hunter. At least on this battlefield today, the weak weren’t human. They were monsters.

The strong devour the weak.

Monsters moved according to the instincts stamped into them from the moment they were born.

But unlike when they’d been seized by ferocity and destroyed cities and slaughtered humans, the instinct driving them now was something far more primal.

*Fear.*

Even the S-rank monsters, so powerful no one had dared meet their eyes, had been wiped out. Most of the leaders who’d led the groups behind them had been massacred, too.

The threadbare chain of command had collapsed, and the ten-to-one difference in numbers was rapidly closing.

There were still several thousand monsters, by a rough count. But a beast that had lost the will to fight was an easier target than a herbivore.

And the Hunters, despite having endured a grueling, hard-fought battle, had no intention of calling this hunt over.

“They’re running! Wipe them out!”

“Don’t let a single one get away!”

“Aaaah!”

Bloodshot eyes. Weapons slick with flesh and blood.

Proof of how fierce the battle had been, the Hunters were soaked in blood from head to toe. Looking like people made of blood, they chased down their prey.

They cinched leather straps around sword hilts that kept slipping from their hands, then felt for the quivers at their sides with arms trembling from drawing the bowstring so many times.

They were exhausted. They wanted to collapse on the sticky sand and sleep.

But they couldn’t stop.

“Because of you bastards, Benjamin—Benjamin’s… You motherfuckers!”

Some had lost friends.

“N-no! Emma!”

Some had lost a comrade who was also a lover.

“Motherfucker. Were you in San Francisco a month ago, too? What? Damn it. Quit spewing shit I can’t understand and go to hell.”

And others had to finish avenging something that had happened not so long ago.

They had to kill monsters, again and again, until this anger finally went away.

*Shhk. Thud!*

Monstrous shrieks rang out as green blood spurted in every direction. An arrow flew from somewhere, piercing an Orc’s head and then a Troll’s ankle.

—Krrk.

The Hunters surrounded the staggering Troll and scraped together every last bit of their mana, pouring it into their weapons. Dozens of blades, brimming with rage, hacked the monster to pieces.

*Thump! Crack-crack-crack!*

We’d fought against overwhelming numbers. The Hunters had suffered heavy losses, and the price they’d paid in blood had to be repaid in monsters.

“Die! Die!”

Hoarse shouts rang out here and there, voices raw from exhaustion and excitement.

After spitting on the Troll’s corpse, chopped up like ground meat, the Hunters moved on to find their next prey, their eyes bloodshot.

*Boom! Boom-boom-boom!*

Attack spells rained down.

Even now, thousands of monsters were tramping mercilessly over corpses and their own kind as they surged south like a wave. The Hunters stood in its path like an enormous reef.

And I was right at the center of it.

*Whoosh!*

A slanted downward slash.

A razor-sharp gust shot along the spearhead and swept past the fleeing monsters.

*Shraaaak.*

Blood burst out instead of a scream, soaking into the sand.

But the monsters lucky enough to escape the attack’s range widened the distance between us and picked up speed.

They were monsters who hadn’t even recognized their own kind as kin from the start.

With evasion now their sole priority instead of fighting, they fled desperately for their lives. Even now, countless monsters were scattering in every direction and escaping the encirclement.

*I can’t let them get away. I have to take down as many as I can.*

The battle was already over. The result so far was a great victory that would be talked about for generations and recorded in history.

But there were still roughly five thousand monsters left.

We’d killed so many, and yet there were still enough to make up a full army.

If we let them go here today, we’d be leaving behind the seeds of another disaster.

*Still, chasing them right now would be impossible.*

Everyone was exhausted from a long and brutal battle. Right now, the only things driving the Hunters were their anger and desire for revenge against the monsters. Nothing more, nothing less.

And I wasn’t the only one thinking this.

“Human!”

“Jin!”

The Skeleton King, who had been holding the rear, and Magic Johnson, who had fought his way through the monsters to reach us, came up on either side of me.

“We need to regroup as quickly as possible, then pursue them. It would be best to split the troops into separate units.”

Magic Johnson spoke in a breathless voice. The Skeleton King, who had just cut down an injured ogre that had fallen behind, answered him.

“I agree. My magical power is nearly depleted, but we can’t let this opportunity pass. I’ve already turned several Griffins into undead. They’ll be enough to give us a view of the area.”

I started to answer, then suddenly caught my breath. I struggled to steady my ragged breathing and only managed to nod. The Skeleton King frowned.

“Human, are you all right?”

“It’s… it’s nothing. Don’t worry about it.”

It was a lie.

My arms and legs felt as heavy as if they’d been soaked in water. The internal energy that had filled my dantian was already running low.

More than anything, the dull ache I’d felt deep inside my body on and off throughout the battle was growing worse.

*Damn debuff.*

I forced myself to keep a calm expression as I recalled the System message I’d seen a while ago.

It was one of the notifications that had greeted me just after I defeated Michael Silbert and woke from a long sleep.

> **System**
>
> All things come with a price. But you have once again ignored repeated warnings and used power that surpasses your limits.
>
> Information for the special debuff **Damaged Body** has been updated.
>
> The special debuff **Broken Body** has been newly applied.
>
> The existing stat penalties caused by debuffs remain unchanged, and the effects of the new debuff will also apply.
>
> **Muscles and Bones** have weakened. The chance of injury has increased considerably.
>
> **Internal energy** is consumed more rapidly. Your control over qi is no longer as free as before.

Broken Body.

That was the price I’d paid for ignoring the System’s warning.

The unprecedented destructive power of One Annihilation had eaten away not only at my enemy’s life, but at my own body as well. It wasn’t the kind of damage that could be healed by any method—not even leveling up.

*Should I not have used One Annihilation against Michael Silbert?*

The thought left a bitter taste in my mouth, but there was nothing I could do about it. Back then, I hadn’t had much choice beyond One Annihilation.

I pushed aside the potion Magic Johnson held out to me with a worried look and spoke.

“That won’t be enough. If I use a potion in a situation like this, I’ll only get more exhausted.”

“But—”

“Right now, pursuing them is the priority. Especially…”

“Yes. The Prophet.”

The Skeleton King murmured in a low voice. He understood what I meant from my expression and clicked his tongue.

“We haven’t found him yet. I thought he was watching from somewhere, but we were wrong.”

Magic Johnson added, “It’s the same for me. Jin, perhaps The Prophet was never here in the first place.”

“Never here? Then was it a trap aimed at something else from the start?”

“I can’t be certain. But it’s certainly possible.”

I thought for a moment, then shook my head.

Four S-rank monsters and an army of more than fifteen thousand monsters. That was far too much to use as bait for a mere trap.

*But why hasn’t he shown himself?*

The Prophet was an unpredictable powerhouse. He had killed Siegfried Bassman, the Grand Mage surrounded by all kinds of barriers, without leaving behind any obvious signs of a fight. His might might be on par with Michael Silbert’s—or even greater.

*If he’d joined the battle, who knows how things would have turned out.*

Even for me, fighting the Manticore Lord and the Lycanthrope Champion at the same time would have been anything but easy.

And that would have been the perfect moment for The Prophet to show himself.

*But he never did.*

Even if this battle had been a trap, and The Prophet’s real target had been our main camp, it still didn’t make sense.

It might sound embarrassing to say it myself, but I was the heart and head of the World Hunter Federation.

In the end, I reached one conclusion.

“It’s not a trap.”

I’d thought about it for a long time, but the time it took was short.

I looked at the Hunters, still chasing after the monsters like mad, and continued.

Even though the Team Leaders—the lower-ranking officers—were ordering them to stop the pursuit, they kept chasing, as if they’d gone deaf.

“I don’t know what The Prophet truly wants, but… this situation is part of his calculations, too.”

“What?”

“If we keep pursuing them without rest, the units will fall apart in no time. First, get the worked-up Hunters back under control as quickly as you can.”

“Jin.”

Magic Johnson looked at me, his eyes dark and serious.

“I agree that we need to regroup the troops… But then what did The Prophet drive all those monsters into this desert for?”

“Either he thought this much would be enough to deal with us…”

I stopped for a moment, then continued as if spitting the words out.

“Or he’s already built up a force so powerful that losing an army this size wouldn’t matter.”

“……”

“……”

The air around us went cold.

I looked at their stiff faces and let a thought I hadn’t been able to say aloud drift through my mind.

One thing was certain. My instincts, sharpened to their limit, had taken hold of me like a premonition.

*The Prophet wants to face me.*

The monsters’ cries faded into the distance. Only then did the wind blow among the people collapsing one after another.

Heavy with the stench of blood, it spread through the cool night air.

* * *

One hundred and eighty-five.

That was how many people had fought more bravely than anyone else—and, because of that, had crossed a river they could never come back over.

But those who survived had to keep moving forward.

We hadn’t come here to win a battle. We’d come to kill The Prophet and uproot the disaster he’d set in motion.

*There’s no time.*

The idea that the one being chased is more desperate than the pursuer is complete bullshit. Especially if the one being chased is carrying a bomb capable of swallowing the whole world.

“Everyone has completed their preparations.”

I opened my eyes as I listened to Team Leader Choi’s report.

Though I’d only spent a little under an hour circulating my energy, my body felt much better than before. My mind had settled, too.

*What the hell is The Prophet?*

It was a question I’d been asking for a long time.

The fifth Muninn. A being believed to be a monster, using magic that wasn’t human. And the desert’s pope, leading countless fanatics.

The more I learned about him, the deeper I felt myself sinking into a swamp. What was his true identity? What was his goal? And where was he now?

If the System were a physical being, I felt like grabbing it by the collar and demanding answers.

I’d take any debuff it threw at me. Just give me one tiny clue.

*Damn it.*

I cursed to myself and gazed up at the darkening sky.

Daylight in the desert was brief, and the sky was gray, perhaps due to the distribution of magical power.

Just like Michael Silbert.

That monster who had been born human and met his death as a monster.

And just as all my memories of him came back to me one by one—

“……!”

A question like a flash of light pierced my mind.
```
