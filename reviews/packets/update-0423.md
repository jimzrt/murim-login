<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0423.txt",
      "sha256": "d070b0e53641cd46ce22a923641c2020bdbd53759562d93e92e3920ef8c731c7",
      "bytes": 13426
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a273b04c33aaf4557b89d8cd77859118f99d0c6df00b40917604df1a26c758fe",
      "bytes": 2724
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "825830c5d5f8cb2bacbbe915414860467539c45a49c77a1cda4e551cb66a5898",
      "bytes": 139506
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "2ff2a104ac6c5120fa521e6f2a3e430c922b5f341dae23dbcd7daf4c901208b3",
      "bytes": 1182
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "49ceba78157d4e2797d238b8b08c5f3db8611ba99236482fae6096c5875127f7",
      "bytes": 129113
    }
  ],
  "estimated_tokens": 9051
}
-->

# Durable State Update — Chapter 423

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 423. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 423. Profile updates may replace only one
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
  "chapter": 423,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 423,
    "continuity_sources": [423],
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
    "Jin's Middle Dantian is open, raising all attributes by 20 and improving qi circulation, qi perception, and qi control; Muscles and Bones and Sinews and Meridians have also increased.",
    "Jin's level-up removed his Curse, fatigue, and other status ailments, restored his temporarily reduced attributes, and healed some injuries.",
    "Jin's new insight lets him perceive the center and mana flow of magic and sever or dispel the Arch Lich's spells.",
    "Jin's White Flame and Force, fueled by three jiazi of Scorching Yang Qi, pierced the Arch Lich's layered defenses before Great Bone Wall stopped the attack.",
    "Jin's Flame-Extinguishing Divine Fist destroyed Great Bone Wall and struck the Arch Lich's jaw; the battle remains unresolved.",
    "The Arch Lich commands powerful dark magic, including Sonic Buster, Gravity, and Great Bone Wall, and regards itself as superior to archmages.",
    "The Arch Lich believes Jin may be the Adversary, the king's eternal nemesis bound to the king by a god's machinations.",
    "The Arch Lich remembers an ancient human who killed it and the king and was the only human it ever feared.",
    "The Arch Lich can observe Jin through Familiars and protect itself from Qi Sense with an unidentified powerful force.",
    "Choi Minwoo trusts Jin deeply and leads the allied fighters against the monsters.",
    "The city's transformation into one enormous Gate remains an active threat, and the Skeleton Warlord remains intensely frightened by the Arch Lich.",
    "The Quest One Who Returned from Death remains active, keeping Login unavailable until the Quest ends."
  ],
  "continuity_sources": [
    422,
    421
  ],
  "open_questions": [
    "Is Jin truly the Adversary, and what are the god's machinations connecting him to the king?",
    "What is the full extent of the Arch Lich's power and its ability to observe or identify Jin?",
    "What is Asmodeus's current status and location?",
    "Why does the Skeleton Warlord react to the Arch Lich with such extreme fear?",
    "Can Jin and the allied Hunters stop the city's transformation into a Gate?"
  ],
  "safe_through": 422,
  "temporary_decisions": [
    "Render 중단전 as Middle Dantian and 단중혈 as Tanzhong acupoint.",
    "Render 소닉 바스터 as Sonic Buster and 그레이트 본 월 as Great Bone Wall.",
    "Render 멸염신권 as Flame-Extinguishing Divine Fist and 겁화 as hellfire.",
    "Render 대적자 as the Adversary and 왕의 대적자 as the king's Adversary.",
    "Preserve the Arch Lich's archaic, taunting register and Jin's profanity while retaining three jiazi, Scorching Yang Qi, Force, White Flame, and Gravity."
  ],
  "version": 1
}
```

## Exact glossary matches

| 이정룡    | **Lee Jungryong** |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 평화 | **Peace Guild** | Guild name. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 420
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

## Korean source

```text
＃423화



뻑!

둔중한 타격음과 함께 아크 리치가 지상으로 튕겨 나간 그 순간. 나는 공력을 끌어올려 허공을 박찼다.

파앙-!

압축된 공기가 터져나가는 소리와 함께, 나는 무시무시한 속도로 추락하는 놈의 신형을 향해 쏘아졌다.

스켈레톤 워로드가 비명인지 환호인지 모를 괴성을 내질렀다.

- 됐다, 인간! 어서 끝내 버려라!

끝내긴 뭘 끝내.

아쉽게도 녀석의 판단은 틀렸다. 적어도 직접 아크 리치의 턱에 주먹을 꽂아 넣은 나는 그 사실을 잘 알고 있었다.

‘그 짧은 순간에 방어 마법을……!’

온 힘을 다한 멸염신권이 닿기 전, 놈은 본 쉴드(Bone Shild)를 얼굴에 덧씌워 스스로를 보호했다.

위력이 위력이니만큼 타격이 아예 없진 않겠지만, 이 정도로 쓰러질 놈이 아니다.

그리고 내 예상은 적중했다. 유성처럼 추락하던 아크 리치의 신형이 우뚝 멈추고, 강대한 마력이 대기를 타고 요동쳤다.

- 다크니스 홀드(Darkness Hold).

쏴아아악!

허공에서 튀어나온 한 쌍의 거대한 손. 얼핏 다크 핸드와 비슷해 보이지만, 다크니스 홀드는 주문에 담긴 뜻처럼 오로지 상대를 속박하는 것에 목적을 둔 마법이다.

나는 쾌속하게 날아드는 두 개의 손을 향해 창날을 내리그었다.

‘보여.’

모든 것에는 ‘결’이 있다. 생물에도, 바람에도, 그리고 보이지 않는 기운에도 존재한다.

중단전의 개방으로 나는 사물의 중심과 결을 느끼고 볼 수 있게 되었다.

바로 지금처럼.

서걱!

불꽃이 피어올랐고, 어둠이 갈라졌다. 고통스러운 듯이 꿈틀거리던 검은 손이 안개가 되어 흩어지는 광경에 아크 리치의 안광이 번뜩였다.

다음 순간, 거무튀튀한 뼈마디로 이루어진 놈의 손이 허공을 할퀴었다.

- 다크 클로우(Dark Claw)!

스아아아, 쉬익!

흩어지던 검은 안개가 맹수의 발톱이 되어 쏟아져 내렸다.

사방에서 각기 다른 궤적을 그리며 쇄도하는 수많은 공격들. 마음을 먹는다면 막아내는 건 어렵지 않겠지만, 그랬다가는 겨우 간격을 좁힌 아크 리치를 놓치고 말 것이다.

‘선택해야 한다.’

두 마리 토끼를 다 잡을 수는 없다. 상대가 토끼가 아니라 호랑이일 때는 더더욱.

짧은 순간 판단을 내린 나는 힘차게 백염을 쏘아 보냈다. 나를 둘러싼 마법이 아니라, 아크 리치를 향해.

콰아아아!

푸른 겁화로 타오르는 백염이 모든 것을 가르며 섬광처럼 쏘아졌다.

아크 리치의 입에서 그 어느 때보다 다급한 음성이 터져 나왔다.

- 본 쉴……!

이미 늦었다. 이 시벌놈아.

화아아아악!

푸른 겁화가 아크 리치의 신형을 집어삼켰다.

채 완성되지도 못한 뼈의 방패가 초고온의 열기 앞에서 잿더미로 화해 스러지고.

퍼걱!

백염의 창날이 아크 리치의 가슴을 관통했다. 꼬치처럼 꿰여 추락하는 아크 리치가 지금껏 들어 본 적 없는 괴성을 내질렀다.

그리고 그 순간, 나는 사방을 베어오는 오싹한 바람을 느꼈다.

- 인간, 위험……!

굳이 스켈레톤 워로드의 외침이 아니더라도 이미 알고 있었다.

알면서도 그렇게 했다. 뼈를 취하기 위해서는 살을 내주어야 하니까. 나 역시 온전하지 못하리라는 걸 알면서도 이 판단이 옳다고 믿었다.

나는 사방에서 쏟아져 내리는 마력의 발톱을 바라보며 내심 생각했다.

‘……그냥 막을 걸 그랬나.’

그러나 낙장불입(落張不入)이다.

쉬쉬쉬쉬쉭!

한 줄기의 돌풍이 내 전신을 휩쓸었다.

그건 본 스피어처럼 환영도 아니었고, 막을 수 있을 만큼 느리지도 않았다. 최대한 몸을 비틀며 공력을 끌어 올렸지만, 한계는 분명했다.

서걱, 서걱, 서걱! 촤아아악!

어깨, 옆구리, 허벅지, 팔…….

무수히 많은 마력의 발톱이 내 전신을 베고 할퀴었다. 쩍 갈라진 살갗에서 핏물이 터지고 아득한 고통이 밀려들었다.

‘빌어먹을.’

아프다. 죽을 만큼. 그리고 죽고 싶을 정도로.

아무리 많이 겪어도 익숙해지기 힘든 것이 바로 고통이다.

눈앞이 흐려지고 나도 모르게 몸에서 힘이 풀렸다.

짧았지만 영원과도 같은 고통의 순간.

그 모든 것을 지나 눈을 떴을 때, 가장 먼저 시야에 들어온 것은 어느새 코앞에 들이닥친 거대한 콘크리트 더미였다.

- 정신 차려라, 인간!

“……!”

스켈레톤 워로드의 다급한 외침에 정신이 번쩍 들었다.

굳어 버린 몸에 억지로 공력을 불어넣자, 혈도가 찢어지는 고통과 함께 잠들어 있던 감각이 깨어난다.

‘지금!’

나는 한 치의 망설임 없이 신형을 뒤집었다.

쾅! 굉음과 함께 먼지구름이 피어올랐다. 콘크리트 더미 위로 거칠게 착지한 다리를 따라 격렬한 진동과 고통이 스멀스멀 기어 올라왔다.

“큭.”

고통을 참으려 이를 악문 내게, 스켈레톤 워로드가 말을 건넸다.

- 인간, 괜찮……아 보이지 않는군.

나는 거칠게 호흡하며 대답했다.

“훅. 알고 있으면, 후욱. 입 다물어. 머리 울려.”

그냥 하는 말이 아니라, 실제로 그랬다. 당장 귓가를 파고드는 시스템 알림만으로도 토악질이 나올 지경이다.

삐빅.



- 상태 이상, [중상]이 부여됩니다!

- 상태 이상, [과다출혈]이 부여됩니다!

- 심각한 부상으로 인해 신체적 능력치가 대폭 하락합니다!

- [근력], [민첩], [체력]이 200포인트씩 감소했습니다!

- 당신은 심각한 부상을 입었습니다! 당장이라도 빠른 치료가 필요합니다!



그래, 내 생각도 그런 것 같아.

피를 너무 많이 흘려서인지, 아니면 계속해서 전해지는 격통 때문인지 눈앞이 흐릿하고 사고가 제대로 작동하지 않는다.

하지만 그런 와중에도 잊을 수 없는 누군가의 존재가 있었다.

“아크 리치. 아크 리치는?”

내 갈라진 목소리에, 스켈레톤 워로드가 버럭 외쳤다.

- 이런 미친 인간을 보았나! 치료부터 해라!

“아직 처치 알림이 안 떴어. 놈이 살아 있…….”

- 처치 알림인지 뭔지 간에, 치료부터 하라고!

“흐읍.”

거, 소리 좀 지르지 말라니까.

나는 어지럼증과 함께 콘크리트 더미에 몸을 기댔다. 머리부터 발끝까지, 온통 핏물로 흠뻑 젖은 전신에서 핏방울이 흘러내리고 자의와는 상관없이 팔과 다리가 사시나무처럼 떨렸다.

‘제기랄.’

정말이지 된통 당했다.

그나마 한 가지 위안이 되는 점이라면, 아크 리치 역시 나보다 더했으면 더했지, 덜하진 않을 것이라는 사실이다.

- 이 멍청한 인간아!

안다. 알고 있다고.

나는 머릿속에서 쩌렁쩌렁 울리는 고함을 들으며 천천히 손바닥을 펼쳤다. 그리고 마음속으로 중얼거렸다.

‘인벤토리 오픈. 소환.’

팟!

생각과 동시에 모든 것이 이루어졌다.

본래는 이정룡이 소유하고 있던 아공간 포켓. 지금은 주인이 바뀐 그것에서 한 가지 물건을 꺼내 들었다.

‘최상급 포션.’

이정룡은 짐작이나 했을까? 만일을 대비해 가져온 최상급 포션 두 개가 모두 나를 위해 쓰일 거라는 사실을.

나는 잘게 떨리는 손으로 최상급 포션의 마개를 땄다. 그리고 생명수처럼 단숨에 들이켰다.

아니, 들이키려 한 그 순간이었다.

투둑, 촤아아아악!

“……어?”

그건 그야말로 한순간에 벌어진 일이었다.

콘크리트 더미 사이에서 솟구친 검은 가시넝쿨이 손목을 후려쳤고, 느려진 세상 속에서 튕겨 나간 최상급 포션이 희뿌연 안개 너머로 사라졌다.

허공에 점점이 흩뿌려진 몇 방울의 포션이 지면에 스며드는 광경을 멍하니 바라보던 나는 문득 입을 열었다.

“다크 바인(Dark Vine).”

더 없이 눈에 익은 누군가의 마법.

스켈레톤 워로드가 신음처럼 중얼거렸다.

- 놈이다.

나는 천천히 고개를 들었다. 짙은 안개 너머로 횃불과도 같은 붉은 안광이 가까워지고 있었다.

검은 광택을 띤 3m의 신체. 인간을 닮았지만, 인간이라 부를 수 없는 그것은 무거운 발걸음으로 안개를 헤치며 모습을 드러냈다.

- 너, 인간이여.

숨길 수 없는 분노가 깃든, 낮게 깔린 음성.

스켈레톤 워로드는 인벤토리 깊숙한 곳에서 몸을 떨었고, 나는 희미하게 웃었다.

“시벌 놈이. 먹던 걸 뺏네.”

- 발악은 여기까지다.

쉬릭, 팍!

손을 뻗을 틈조차 없었다, 아크 리치가 손가락을 튕기자, 평범한 가죽 주머니처럼 보이는 이정룡의 아공간 포켓이 다크 바인에 휩쓸려 보이지 않는 저 멀리로 내팽개쳐졌다.

- 더 이상의 얕은 수작은 통하지 않는다.

한 마디, 한 마디를 내뱉을 때마다 아크 리치를 둘러싼 마력이 반응했다.

하지만 내가 중상을 입었듯이, 녀석이 내뿜고 있는 기운 역시 예전만 못했다.

당장 가슴 한가운데를 관통한 백염이 바로 그 결정적인 원인이리라.

‘할 수 있다.’

나는 힘주어 몸을 일으켰다. 손을 뻗음과 동시에 인벤토리에서 소환한 창 한 자루가 잡혔다.

“가슴에 박힌 창, 예쁘네. 한 자루 더 심어 줘?”

- 네게 그럴 기회가 있을까.

“물론. 네 꼬라지 보면 충분히 가능할 것 같은데.”

- 인간은 늘 용기와 만용을 구분하지 못하지. 어리석구나. 참으로 어리석어.

소리 내어 웃은 아크 리치가 양팔을 펼쳤다.

앞서 당한 일격의 영향으로 잿더미가 된 로브 대신, 칠흑색 마력이 놈의 전신에서 흘러나와 하나의 형태를 이루었다.

‘저건…….’

보는 것만으로도 불길함이 느껴지는 마력의 소용돌이.

나는 본능적으로 아크 리치가 무엇을 하려는지 깨달았다.

‘게이트(Gate).’

금방이라도 폭발할 것처럼 불안정했지만, 그것은 분명 게이트의 형상을 갖추고 있었다.

그리고 다음 순간 이어진 아크 리치의 한마디는 내 짐작을 확신으로 바꿔 주었다.

- 아직 완전하지는 않지만…… 네놈만 쓰러트린다면 모든 것을 완성 시킬 수 있겠지.

동시에 하늘에서 들리는 듯한 낮은 음성이 공간을 떨어 울렸다.

- 이곳에 임하라. 게이트 오픈(Gate Open).

“……!”

어떻게든 막아야 했다. 하지만 고통은 몸을 더디게 만들었고, 변화는 시작되고 있었다.

나는 다음 순간 펼쳐진 광경을 눈을 부릅뜬 채 바라보았다.

콰아아아아아!

잿빛 하늘 사이로 희미하게 내리비추던 몇 줄기의 햇빛이 완전히 자취를 감췄다.

하늘이 갈라지는 굉음과 함께 폭풍이 사방을 휩쓸고, 그 빈자리에 들어선 짙은 어둠이 마치 태고의 거인처럼 몸을 일으켜 세웠다.

솨아아아아악!

일렁이는 어둠이 폐허가 된 도심지 한가운데에서 솟구쳤다.

고층 빌딩만큼이나 높고, 축구장보다 넓은 그것은 지금껏 봐 왔던 어떤 게이트보다 거대했으며 뼛속 깊숙이 스며드는 공포심을 불러일으켰다.

- 아, 아아.

언데드 몬스터인 스켈레톤 워로드조차 덜덜 떨게 만드는 광경.

그저 멍하니 입을 벌린 채 게이트를 바라보던 나는, 문득 잊고 있던 사실을 깨달았다.

‘막아야 한다. 무슨 일이 있어도.’

비록 완전한 게이트가 아니라고는 하나, 이대로라면 걷잡을 수 없는 재앙이 시작되고야 만다.

수백만, 혹은 수천만이 죽을지도 모른다.

그리고…… 그중에는 내 사람들이 포함되어 있을 수도 있다.

전장에 있는 최 팀장, 짧지만 정이 들기에 충분했던 샤오 쉔.

만약 아크 리치가 중국을 넘어 반도로 간다면…… 평화 길드원들과 사랑하는 가족들까지 위험해질 것이다.

‘가야 해.’

고통과 경악으로 마비되어 있던 몸을, 의지가 움직였다.

젖먹던 힘을 다해 공력을 끌어올리자 내상을 입은 혈도가 고통을 호소하고, 전신 곳곳에서는 다시금 핏물이 터져 나왔다.

하지만 나는 멈추지 않았다. 단 한 번, 한 번의 기회를 위해.

‘염화일로(炎火一路).’

너덜거리는 다리가 지면을 밀었다. 부서지는 통증과 함께 불꽃의 길이 열린다.

그 끝에, 한 존재가 있었다.

이 모든 것을 시작한 존재. 동시에 끝낼 수 있는 존재.

‘죽어라.’

일섬(一殲).

느려진 세상 속, 나는 한껏 젖힌 창을 내질렀다.

모든 힘을 다해 쏘아 보낸 와류(渦流)가 놈에게 닿았다.

콰아아아아아!

그리고 세상을 가득 메운 푸른 화염 속에서, 놈의 웃음 섞인 한 마디가 내 귓가를 파고들었다.

- 블링크(Blink).
```

## Final English reading copy

```markdown
# Chapter 423

*Wham!*

At the very moment the Arch Lich was knocked back toward the ground by the heavy impact, I gathered my internal energy and kicked off the air.

*Bang!*

With the sound of compressed air bursting, I shot toward the Arch Lich’s rapidly falling body at terrifying speed.

The Skeleton Warlord let out a cry that could have been either a scream or a cheer.

—You did it, human! Finish it quickly!

*Finish what?*

Unfortunately, its judgment was wrong. At least, I knew that much from having driven my fist directly into the Arch Lich’s jaw.

*It cast a defensive spell in that split second…!*

Before my all-out Flame-Extinguishing Divine Fist could make contact, it had overlaid its face with Bone Shield to protect itself.

Given the power of the blow, it could not have escaped completely unharmed—but it was not an opponent who would fall from something like that.

And my prediction proved correct. The Arch Lich’s body, which had been plummeting like a meteor, came to an abrupt stop, and immense mana rippled through the air.

—Darkness Hold.

*Fwoooooosh!*

A pair of enormous hands burst out of thin air. At a glance, they looked similar to Dark Hand, but as its name implied, Darkness Hold was a spell designed solely to bind its target.

I slashed my spear down toward the two hands hurtling toward me.

*I can see it.*

Everything had a grain—a pattern running through it. Living creatures had one. So did the wind, and even invisible energy.

After opening my Middle Dantian, I had gained the ability to sense and see the center and grain of things.

Just like now.

*Shhk!*

Flames blossomed, and the darkness split apart. As the black hands writhed as if in pain before dispersing into mist, the Arch Lich’s eye-lights flashed.

The next moment, its hand—formed from dark, weathered bones—clawed through the air.

—Dark Claw!

*Fsssssh, shhk!*

The black mist that had been dispersing transformed into the claws of a beast and poured down.

Countless attacks rushed in from every direction, each following a different trajectory. If I made up my mind to stop them, it would not be difficult.

But if I did that, I would lose the Arch Lich after only just managing to close the distance.

*I have to choose.*

I could not catch two rabbits at once. Especially when my opponent was not a rabbit, but a tiger.

After making my decision in that brief instant, I sent White Flame flying with all my strength.

Not toward the magic surrounding me, but toward the Arch Lich.

*Fwoooooom!*

White Flame, blazing with blue hellfire, shot forward like a flash of light, cleaving through everything in its path.

The Arch Lich’s voice burst out, more urgent than ever.

—Bone Shi—

Too late, you son of a bitch.

*Fwoooooosh!*

Blue hellfire swallowed the Arch Lich’s body.

The bone shield, not even fully formed, turned to ash and crumbled before the ultrahigh heat.

*Crunch!*

The spearhead of White Flame pierced through the Arch Lich’s chest. Impaled like meat on a skewer, the falling Arch Lich let out a scream unlike anything I had ever heard from it.

And at that moment, I felt a chill wind slicing in from every direction.

—Human, danger…!

I already knew. I did not need the Skeleton Warlord to shout a warning.

I knew, and I did it anyway. To take the bones, I had to give up flesh. Even knowing that I would not emerge unscathed, I believed this was the right decision.

As I watched the claws of mana raining down from all directions, I thought to myself,

*…Maybe I should have just blocked them.*

But there was no taking it back now.

*Shh-shh-shh-shh-shhk!*

A single gust of wind swept over my entire body.

It was not an illusion like Bone Spear, nor was it slow enough to block. I twisted my body as much as possible and gathered my internal energy, but there was a definite limit.

*Shhk! Shhk! Shhk! Fwoooooosh!*

My shoulder, side, thigh, arm…

Countless claws of mana slashed and raked across my body. Blood burst from my deeply split skin, and overwhelming pain surged through me.

*Damn it.*

It hurt. Enough to kill me.

Enough to make me want to die.

No matter how many times I experienced it, pain was something that was difficult to grow accustomed to.

My vision blurred, and the strength left my body before I even realized it.

It was a brief moment of pain, but it felt eternal.

When I opened my eyes after passing through it all, the first thing I saw was an enormous pile of concrete that had somehow rushed right up to my face.

—Get a hold of yourself, human!

“……!”

The Skeleton Warlord’s frantic shout snapped me back to my senses.

I forced internal energy into my stiffened body. Along with the tearing pain in my acupoints, the senses that had fallen asleep awakened.

*Now!*

Without the slightest hesitation, I flipped my body around.

*Crash!*

A thunderous roar rose with a cloud of dust. Violent vibrations and pain slowly crawled up the leg with which I landed roughly on the concrete pile.

“Urgh.”

I clenched my teeth against the pain, and the Skeleton Warlord spoke to me.

—Human, you do not… appear to be all right.

I answered while breathing harshly.

“Huff. If you know that, huff, then shut up. My head’s ringing.”

It was not just something I was saying. It really was.

The System notifications drilling into my ears alone were enough to make me feel like throwing up.

*Beep.*

> **System**
>
> - The status effect **Severe Injury** has been applied!
>
> - The status effect **Excessive Bleeding** has been applied!
>
> - Due to severe injuries, your physical attributes have been drastically reduced!
>
> - **Strength**, **Agility**, and **Stamina** have each decreased by 200 points!
>
> - You have suffered severe injuries! Immediate treatment is required!

Yeah. I thought so, too.

Whether it was because I had lost too much blood or because the excruciating pain kept coming, my vision was hazy and my thoughts were barely functioning.

But even in that state, there was someone whose existence I could not forget.

“The Arch Lich. Where is the Arch Lich?”

At the sound of my cracked voice, the Skeleton Warlord roared.

—Have you gone completely insane, human?! Treat yourself first!

“I haven’t gotten a kill notification yet. That means it’s still ali—”

—Who cares about a kill notification or whatever! Treat yourself first!

“Hngh.”

I said, don’t shout.

With my head spinning, I leaned against the concrete pile. Blood dripped from my entire body, which was soaked from head to toe, while my arms and legs trembled like aspen leaves beyond my control.

*Damn it.*

I had really taken a beating.

The one small consolation was that the Arch Lich had to be in even worse shape than I was—or at least no better.

—You stupid human!

*I know. I know.*

As I listened to the shout reverberating through my head, I slowly opened my palm. Then I muttered inwardly.

*Inventory open. Summon.*

*Pop!*

Everything happened at the same time as the thought.

The subspace pocket originally owned by Lee Jungryong—now belonging to me—yielded one item.

*Top-grade potion.*

Had Lee Jungryong ever imagined it? That both of the top-grade potions he had brought along just in case would be used for my sake.

With a finely trembling hand, I uncorked the top-grade potion. Then I drank it down in one gulp, like the elixir of life.

Or rather, I was just about to drink it.

*Tap—fwoooooosh!*

“……Huh?”

It all happened in an instant.

A black thorny vine shot up from between the concrete piles and lashed my wrist. In the slowed world, the top-grade potion went flying and disappeared beyond the pale haze.

I stared blankly at the few drops of potion scattered through the air as they soaked into the ground. Then I suddenly spoke.

“Dark Vine.”

Someone’s all-too-familiar magic.

The Skeleton Warlord muttered like it was groaning.

—It is him.

I slowly raised my head. Beyond the thick fog, a pair of red eye-lights like torches was drawing closer.

A three-meter-tall body with a black sheen. It resembled a human, but it was something that could not be called human. It emerged through the fog with heavy footsteps.

—You, human.

Its low voice carried unmistakable fury.

Deep inside my inventory, the Skeleton Warlord trembled. I smiled faintly.

“You son of a bitch. You stole the food right out of my mouth.”

—Your futile struggle ends here.

*Shhk! Pop!*

I did not even have time to reach out. The moment the Arch Lich snapped its fingers, Lee Jungryong’s subspace pocket, which looked like an ordinary leather pouch, was swept up by Dark Vine and flung far out of sight.

—No more cheap tricks will work.

With every word the Arch Lich spoke, the mana surrounding it reacted.

But just as I had suffered a severe injury, the power it emitted was also weaker than before.

The White Flame piercing the center of its chest had to be the decisive cause.

*I can do this.*

I forced myself to stand. As I reached out, a spear summoned from my inventory landed in my hand.

“The spear sticking out of your chest looks nice. Want me to plant another one?”

—Will you have the opportunity to do so?

“Of course. Looking at the state you’re in, I think it’ll be more than possible.”

—Humans never know the difference between courage and recklessness. How foolish. Truly, how foolish.

The Arch Lich laughed aloud and spread both arms.

The robe that had been reduced to ash by the earlier attack was gone. In its place, pitch-black mana flowed from the Arch Lich’s entire body and took shape.

*That’s…*

A vortex of mana that felt ominous merely to look at.

I instinctively realized what the Arch Lich was about to do.

*Gate.*

It was unstable, as though it might explode at any moment, but it had unmistakably taken the shape of a Gate.

And the Arch Lich’s next words transformed my guess into certainty.

—It is not yet complete, but… if I can merely bring you down, I should be able to complete everything.

At the same time, a low voice that seemed to come from the heavens reverberated through the space.

—Descend upon this place. Gate Open.

“……!”

I had to stop it somehow. But the pain slowed my body, and the transformation had already begun.

I stared wide-eyed at the sight that unfolded the next moment.

*Kwaaaaaaaaaaang!*

The few rays of sunlight faintly shining through the ash-gray sky disappeared completely.

With a thunderous roar, the sky split open. A storm swept across everything, and in the empty space left behind, a thick darkness rose like an ancient giant standing up.

*Fwoooooosh!*

The rippling darkness surged up from the center of the ruined city.

As tall as a high-rise building and wider than a soccer stadium, it was larger than any Gate I had ever seen. It inspired a fear that seeped deep into my bones.

—Ah… ahh.

Even the Skeleton Warlord, an undead monster, trembled at the sight.

I stood there with my mouth hanging open, staring blankly at the Gate. Then I suddenly realized something I had forgotten.

*I have to stop it. No matter what.*

Even if it was not yet a complete Gate, if things continued like this, an uncontrollable disaster would begin.

Millions, perhaps tens of millions, could die.

And among them…

Some might be my people.

Team Leader Choi, who was on the battlefield, and Xiao Shen, whom I had grown attached to despite our short time together.

If the Arch Lich crossed from China to the Korean Peninsula… the members of the Peace Guild and even my beloved family would be in danger.

*I have to go.*

My will moved the body that had been paralyzed by pain and shock.

I gathered my internal energy with every last ounce of strength I had. The acupoints suffering from internal injuries cried out in pain, and blood burst once more from various places across my body.

But I did not stop.

For one opportunity. Just one.

*Flamefire Path.*

My battered leg pushed against the ground. Along with shattering pain, a path of flames opened.

At its end stood one being.

The being that had started all of this.

The being that could end it all at the same time.

*Die.*

*One Annihilation.*

In the slowed world, I drew back my spear as far as I could and thrust it forward.

The vortex I sent flying with all my strength reached the Arch Lich.

*Kwaaaaaaaaaaang!*

And amid the blue flames filling the world, a single laughter-laced word from the Arch Lich pierced my ears.

—Blink.
```
