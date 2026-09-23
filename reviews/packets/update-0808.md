<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0808.txt",
      "sha256": "b3f15d8d9919f3ddfab09d51ca76a2995a1c52a07ea9d16fcb2fc796a26c5d3a",
      "bytes": 13614
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1d17363459160a336fa289e0139182d0fb8424af7242f5cbe08b3f9e245900f7",
      "bytes": 1293
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1e8b8a33ae952423b359fb7c39a8c3a83fe8a43b894e38ef519681dd66dd55a7",
      "bytes": 225527
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "7879bd6f9e0f03723db25030f56235d66f14b9a24522bf95a02193f393c0f80d",
      "bytes": 752
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e0b2bd17fc629ed2b699a0d2e22e9a779e924fcc68a571c508daf62ec8e1029e",
      "bytes": 553
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "cd010db6a37db1a80ff8c9041b25bed83bba0704dff5f2c7512b9f762eac1b39",
      "bytes": 707
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "50c86696a90d0b181ea15b9b447f966ee2a43b087c919b9a8afa94dc3c9bf82e",
      "bytes": 574
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7c0e3ab3ab0cfe27e92a116960cc3f7a94573b671698596f3f385070423d776f",
      "bytes": 247922
    }
  ],
  "estimated_tokens": 9250
}
-->

# Durable State Update — Chapter 808

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 808. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 808. Profile updates may replace only one
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
  "chapter": 808,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 808,
    "continuity_sources": [808],
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
    "Jin leads roughly one thousand Hunters against a monster force exceeding ten thousand in the Rub’ al Khali; the Prophet’s location and means of directing the army remain unknown.",
    "Jin’s Poisoned and Convulsions status abnormalities were cured by the Myriad-Poison Ring absorbing the Manticore Lord’s venom; he remains physically worn down with depleted internal energy.",
    "Yamamoto Genji killed the Lycanthrope Champion, taking the last hit Jin had expected to earn a level-up from.",
    "The Skeleton King killed the Death Knight and absorbed its departing soul.",
    "A Grand Mage used Reverse Gravity to bring down the Griffin leader and the other flying monsters; Jin’s forces advanced after the monster army’s formation collapsed."
  ],
  "continuity_sources": [
    806,
    807
  ],
  "open_questions": [
    "Where is the Prophet, and how is he directing the monster army?"
  ],
  "safe_through": 807,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Render 리버스 그래비티 as Reverse Gravity."
  ],
  "version": 1
}
```

## Exact glossary matches

| 천태민    | **Cheon Taemin**  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 경험치              | **EXP**                        |
| 지능               | **Intelligence**               |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 힐러      | **healer**            |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 청해     | **Qinghai**            |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 오크 | **Orc** | Monster species. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 위압 | **Intimidation** | System attribute strengthened by the achievement reward. |
| 일기당천 | **One Against a Thousand** | Title that temporarily increases Taekyung’s attributes and Intimidation when facing many enemies. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 804
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 806
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 805
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a monster posing as the leader of the revived Hasasin, whose power includes stopping transport vehicles and absorbing blood and a pale mist from the dead.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 807
- **Aliases:** None
- **Role:** Yamamoto Genji is a Japanese S-rank Hunter and J1’s sole survivor.
- **Personality:** Prideful and easily offended, prone to self-aggrandizement and self-serving assumptions, and cowardly under mortal threat.
- **Voice:** Not established.
- **Relationships:** Jin Taekyung sent Yamamoto on the J1 mission and treated him after the attack, though Jin resents Yamamoto for arriving late during the Leviathan crisis.

## Korean source

```text
＃808화



대격변은 인류의 역사를 뒤바꾼 거대한 사건이다.

당연하게도 그에 관한 수많은 분석과 연구가 이루어졌고, 전 세계의 석학들은 인류가 승리할 수 있었던 결정적인 이유를 총 세 가지로 꼽았다.

첫째. 천태민의 존재.

둘째. 헌터라 불리게 될 각성자들의 등장.

그리고 마지막 셋째.

‘인간이라는 생물체가 지닌 지성과 의지.’

맞는 말이다.

천태민의 존재나 각성자들의 등장이 예상치 못한 구원이었다면, 인간의 지성과 의지는 어떠한 위기도 헤쳐 나갈 수 있는 근원이었다.

바로 그것이야말로 인류가 승리할 수 있었던 이유이자, 몬스터가 패배한 원인이기도 했다.

수십여 년 전에도.

그리고…… 지금 이 순간에도.

콰드드드득!

거대한 함성과 함께 천여 명의 헌터들이 물결처럼 나아간다.

사방에서 끊임없이 몰려드는 몬스터들을 막느라 모든 기력을 소진한 탱커들의 머리 위로 힐러들의 축복이 쏟아지고, 일대를 휘감고 있던 방어 마법을 해제한 거구의 대마도사는 자신의 진정한 힘을 드러냈다.

“마음껏 불태우고 가로질러라.”

끓어오르는 듯한 음성과 함께 막대한 마나가 요동친다.

어지간한 마법사라면 몇 분에 걸쳐 준비해야 했을 대규모 마법.

그러나 매직 존슨이 내저은 스태프를 따라 허공에 떠오른 마법진은 짧은 주문과 함께 발현을 끝마쳤다.

“파이어 월(Fire Wall).”

화륵, 콰아아아!

끔찍한 열기를 머금은 불꽃이 사방으로 내달렸다. 두꺼운 비늘을 불태우고, 살과 뼈를 녹이며 몬스터 군단의 대열을 좌우로 쪼갰다.

- 끄아아아아!

고통에 찬 괴성과 함께 매캐한 악취가 사방에서 피어오른다.

밀집된 대형을 그대로 찢어발기는 범위 마법.

그 극심한 혼란 속에서, 제법 높은 지능을 가진 것으로 보이는 상위 몬스터 하나가 황급히 무너진 대형을 수습했다.

아니, 수습하려고 했다.

- 알루. 카르쉬……!

퍼걱!

어느덧 놈의 머리 위로 떨어져 내린 내가, 공력을 실은 일권(一拳)으로 그 단단한 머리통을 터트리기 전까지는.

띠링.



- [Lv.101 미노타우로스 대전사]를 처치하셨습니다!

- 소량의 경험치를 획득했습니다!



스륵. 쿵.

시스템 알림과 함께 비틀거리던 몸뚱어리가 썩은 통나무처럼 쓰러진다.

사체 위로 가래를 탁 뱉은 나는 백염을 고쳐 잡으며 뇌까렸다.

“이 씹새끼가. 어디서 초를 쳐.”

혜성처럼 허공에서 뚝 떨어진 내 모습에, 주위의 몬스터들이 눈을 깜빡였다. 마치 개울가에 모인 초식동물처럼 순박한 눈빛.

하지만 나는 이미 알고 있다.

온순하게만 느껴지는 저 눈빛은 너무나도 멍청해서 보일 수 있는 것이고, 그 안에 숨겨진 본능은 세상의 어떤 생명체보다 흉포하고 잔인하다는 것을.

- 크륵?

“만나서 반가웠고, 잘 가라.”

처음이자 마지막이 될 인사와 함께, 나는 몸을 회전시키며 창날을 휘둘렀다.

콰드드득!

뼈와 살이 분리되고 피 안개가 자욱하게 맺힌다. 일격에 수십이 쓰러지고, 한 걸음 나아가며 휘두른 이격에 주위가 텅 비었다.

철벅.

피에 젖은 모래를 밟으며 다가가자 주위의 공기가 찌르르 울렸다.

열양지기가 불러일으킨 열기는 뜨거웠지만, 나를 바라보는 몬스터들의 눈동자는 차갑게 얼어붙은 지 오래였다.

일기당천(一騎當千).

내게서 흘러나오는 압도적인 무위와 기세.

손을 뻗으면 만져질 것 같은 [위압]이 놈들의 몸뚱어리를 옥죄인다. 흉포함을 지워 낸 두려움이 본능을 잠식했다.

그리고 끈기 있게 때를 기다려온 헌터들은, 이 순간을 놓치지 않았다.

퍼걱!

“돌격! 모조리 쓸어 버려라!”

“죽어, 이 개새끼들아!”

차차창, 서걱!

거대한 함성과 함께 번쩍이는 강철의 파도가 몬스터들을 덮쳤다.

비교적 짧은 시간이었지만 그들은 열 배가 넘는 대병력을 상대로 큰 피해 없이 버텨 낸 정예들.

끊임없이 몰려드는 괴물들을 상대로 참고 참았던 헌터들은, 때를 놓치지 않고 앞서 매직 존슨의 범위 마법으로 와해 된 대열을 파고들어 닥치는 대로 찌르고 베었다.

서걱, 푸푸푹!

“God damm it! Motherfucker!”

- 그아아아아!

욕설과 비명이 뒤섞이고 오러와 마력이, 빛과 어둠이 사방에서 격돌한다.

그리고 그 격돌의 저울추는, 시시각각 빛을 향해 기울고 있었다.

“3팀. 두 시 방향 주시! 우회하여 돌파한다!”

“원거리 부대 준비, 발사!”

“Fire!”

쉬쉬쉬쉭, 퍼엉!

바람을 가로지르는 날카로운 파공성과 함께 쏟아지는 궁수들의 화살 비. 마법사들의 범위 마법이 전장을 휩쓸었다.

살아있는 유기체와 같은 각 팀의 움직임. 체계적이면서도 적의 빈틈을 찌르는 전술.

마력 분포도의 증가로 전보다 강력하게 거듭난 몬스터 군단.

그러나 탄생과 함께 주어진 우월한 신체 능력과 마력만으로 모든 전투에서 승리할 수 있었다면 이 세상은 이미 놈들이 차지했을 것이다.

“덤벼, 개자식들아.”

나는 서늘한 목소리와 함께 신형을 내쏘았다. 목표를 정한 순간 움직인 몸뚱어리는 이미 공간을 지우며 다음 행동에 나서고 있었다.

서걱, 펑!

마법을 준비하려는 고블린 주술사의 목을 가르고, 곁에 있던 오크 족장의 가슴을 후려친다.

순식간에 우두머리를 잃고 우왕좌왕하는 오크들의 머리 위로 화살 비가 쏟아져 내렸다.

쉬쉭, 퍼버버벅!

오러가 맺힌 화살촉들이 두꺼운 가죽을 뚫고 머리와 가슴을 관통한다.

가까워진 내 모습에 유독 거대한 몸집을 한 트롤이 황급히 물러나던 그때, 놈의 등 뒤에서 두 줄기의 섬광이 휘어지듯 쏘아졌다.

푸푹, 서걱!

첫 번째 검은 가슴을 꿰뚫었고, 두 번째 검은 목을 쳐 날렸다.

한 치의 망설임도, 군더더기도 없는 약속된 움직임.

이내 치명상을 입고도 살아남아 꿈틀거리는 트롤을 수십 조각으로 쪼개 버린 검의 주인들이 나를 발견하고 희미하게 웃었다.

‘샤오 쉔. 그리고 최 팀장.’

혼잡한 전장 속에서 서로 간에 주고받을 말은 없다.

굳이 말하지 않아도 뜻이 통하는 상대라면 더더욱.

나를 향해 가볍게 눈인사를 건넨 두 사람은 또 다른 목표를 향해 달려들었다. 그들이 노리는 것은 각 무리를 통제할 만큼의 지능을 지닌 상위 몬스터였다.

‘옳은 선택이야.’

대부분의 사람들은 생명체, 특히 자신과 같은 사람을 죽이는 것을 본능적으로 거부한다.

그것이 오랜 역사 속에서 각인된 본능인지, 아니면 문명인으로서의 학습인지는 모르겠지만 틀림없는 사실이다.

하지만 몬스터들은 시작점부터 다르다. 탄생과 함께 투쟁의 운명을 부여받은 놈들에게는 동족(同族)이라는 개념조차 희미하다.

‘이런 상황에서 명령을 내릴 우두머리 격 몬스터들을 제거한다면, 그때부터 진정한 혼란의 시작이지.’

아니, 혼란은 이미 시작되었다.

가장 강력한 개체인 만티코아 로드를 비롯한 네 마리의 S급 몬스터가 쓰러졌으며, 내 명령에 따라 오직 수비에 집중하던 매직 존슨과 헌터들은 괴물들의 중심부를 파고들어 그야말로 갈아 버리는 중이다.

하급 지휘관이라 할 수 있는 각 무리의 우두머리들은 최 팀장과 샤오 쉔을 필두로 한 A급 헌터들에 의해 지금 이 순간에도 전장 곳곳에서 쓰러지고 있었고, 야마모토 겐지 역시 눈에 띄는 활약을 펼쳤다.

“흐읍. 질풍참(疾風斬)!”

한껏 가라앉은 목소리로 토해 내는 기술명은 열도의 허세 그 자체지만, 그 일검에 실린 위력은 허세가 아니다.

슈확, 서걱!

섬광처럼 가로지르는 섬광과 함께 수십여 마리의 괴물들이 피를 뿌리며 쓰러진다.

일순간 텅 비어 버린 공간을 놓치지 않고 달려온 헌터들이 닥치는 대로 몬스터들을 베어 넘겼다.

퍼걱! 푸화아아악!

서서히 무너지는 대형과 뒤로 밀려나는 전열.

그러나 조금씩 뒷걸음질치는 몬스터 군단을 기다리고 있던 것은, 후방을 틀어막은 스켈레톤 킹과 일천의 스켈레톤들이었다.

“놈들을 에워싸라! 이가 없으면 뼈로 버텨라!”

따닥, 따다닥!

- 크워어어어!

콰직!

수 미터에 달하는 대형 몬스터가 휘두른 메이스에 십여 마리의 스켈레톤이 산산이 부서진다.

동시에 그 틈을 타 달라붙거나 기어오른 수십의 해골들이 녹슨 검과 이빨을 괴물의 거체에 박아넣었다.

푹. 콰득!

- 그어어어어!

분노에 찬 괴성은 고통에 물든 비명으로 변하고, 이내 끔찍한 죽음을 맞이한 대형 몬스터의 눈동자에 시퍼런 안광이 맺혔다.

- 그. 아. 아. 아.

언데드로 부활한 대형 몬스터가 육중한 몸뚱어리를 이끌고 달려 나간다.

그 광경에 흠칫하던 헌터들이 이내 스켈레톤 킹의 모습을 발견하고 아무렇지 않게 전투를 계속해 갔다.

“쳐! 무너진다!”

“놈들의 대형이 흐트러졌다! 물러서지 말고 밀어붙여!”

불과 한 시간도 되지 않는 짧은 시간.

그러나 이미 승기(勝機)는 인간들을 향해 기울었다.

벌써 수천에 달하는 몬스터들이 녹아내렸고, 처음 열 배에 달하던 병력 차이는 이제 다섯 배로. 그 이하로 시시각각 좁혀지고 있었다.

우지직! 쿵!

4m가 넘는 오우거 대전사가 비명도 지르지 못한 채 쓰러진다.

가슴이 뻥 뚫린 채 기울어지는 놈의 어깨를 밟고 허공으로 솟구친 나는, 짧은 순간 눈에 들어온 전장의 상황을 시야에 담았다.

‘끝났어. 조금만 더 밀어붙인다면, 전투는 승리한다.’

헌터들을 포위한 채 끊임없이 공격을 가하던 초반의 기세는 지금의 몬스터들에게서 더 이상 찾아볼 수 없었다.

네 마리의 S급 몬스터를 비롯하여 하급 지휘관급 우두머리를 잃은 몬스터들은 극심한 혼란에 빠졌고, 전방에서 펼쳐지는 대마도사의 범위 마법과 후방에서 몰아붙이는 스켈레톤 킹의 언데드 병사들은 그 혼란을 부추겼다.

‘거기에 더해 헌터들의 엄청난 분전까지.’

현재의 몬스터 군단은 머릿수만 많은 짐승에 불과하다.

이제 승리는 시간문제일 뿐이다.

저 수많은 괴물 중 누구도 우리를, 나를 막을 수 없었다.

아직도 모습을 드러내지 않은, 단 한 존재를 제외한다면.

‘도대체 어디에 있는 거냐.’

선지자.

모든 것이 온통 수수께끼나 다름없는 놈을 떠올리며, 나는 지상으로 떨어져 내렸다.

쾅! 서걱!

신형과 함께 내리꽂히는 백염의 창날이 또 다른 몬스터의 정수리를 쪼갰다. 정확히 반으로 갈라지며 좌우로 쓰러지는 신형 사이로 두려움에 찬 눈동자들이 보였다.

“죽어.”

나는 맹수처럼 달려들어 포식자처럼 날뛰었다.

하급 몬스터들은 피어(Fear)에 사로잡힌 것처럼 얼어붙은 채로 눈앞에 들이닥친 죽음을 바라보았고, 상위 몬스터들은 마지막 힘을 다해 발악을 펼쳤다.

이렇듯 놈들을 쓰러트리는 과정은 달랐지만, 결과는 모두 같았다.

죽음.

푹!

라이칸스로프의 미간을 꿰뚫은 창날을 비틀며 뽑았다. 흐르는 뇌수가 백염의 투명한 창날을 타고 흐른다.

쉴 새 없이 움직인 팔과 다리에서 저릿한 통증이 올라왔다.

‘빌어먹을.’

얼마나 오랫동안 싸운 걸까. 또 얼마나 많은 몬스터들을 죽인 걸까.

모르겠다. 차라리 모르는 게 낫다. 그 사실을 뇌가 인지하는 순간 육신은 더욱 피로해질 테니까.

아직까지도 모습을 드러내지 않은 선지자가 지금의 내 모습을 지켜보고 있다면, 더더욱 약해진 모습을 보일 수 없었다.

후욱. 훅.

나는 호흡을 가다듬으며 백염을 고쳐 쥐었다.

그리고 또 다른 몬스터들을 상대하기 위해 돌아선 순간. 마침내 승부의 저울추가 완전히 기울었다는 것을 깨달았다.

드득. 드드드득!

- 그어어어어!

- 꾸륵. 꾸아아악!

사막이 흔들린다. 겁에 질린 괴성과 함께 수많은 몬스터의 파도가 뒤로 물러나고 있었다.

‘도망치고 있다. 저 많은 몬스터들이.’

순간 머릿속에 떠오른 생각은 눈앞에 벌어지고 있는 현실이었다.

수적 우세?

전의를 상실하고 전력으로 도망치는 몬스터 군단의 뇌리에는 이미 그런 것 따위는 남아 있지 않았다.

눈을 깜빡이며 그 모습을 바라보던 헌터들은 지친 창검을 들었다. 벌겋게 물든 눈동자로 그 뒤를 바짝 쫓아 내달렸다.

“싹 다 죽여!”

이제 전장에 남아 있는 유일한 것은, 학살뿐이었다.
```

## Final English reading copy

```markdown
# Chapter 808

The Great Cataclysm was a massive event that changed the course of human history.

Naturally, it had been the subject of countless studies and analyses. Scholars around the world named three decisive reasons humanity had been able to win.

First: the existence of Cheon Taemin.

Second: the emergence of the Awakened, who would come to be known as Hunters.

And third, the last one:

*The intelligence and will of human beings.*

They were right.

If Cheon Taemin’s existence and the emergence of the Awakened had been unexpected salvation, human intelligence and will were what allowed us to overcome any crisis.

That was what had let humanity win—and what had caused the monsters to lose.

Decades ago.

And… right now, in this very moment.

*CRRRRACK!*

With a tremendous roar, a thousand Hunters surged forward like a wave.

The healers’ blessings rained down over the tanks, who had exhausted every ounce of their strength holding back the monsters pouring in from all sides. The towering Grand Mage dispelled the defensive magic that had enveloped the area and revealed his true power.

“Burn as bright as you like, and cut right through them.”

His voice seemed to boil with power as a massive amount of mana surged.

It was a large-scale spell that would take an ordinary mage several minutes to prepare.

But following the staff Magic Johnson swept through the air, a magic circle appeared overhead and finished forming with just a short incantation.

“Fire Wall.”

*Fwoosh—WHOOOOSH!*

Flames carrying a horrible heat raced in every direction. They burned through thick scales, melted flesh and bone, and split the monster army’s ranks apart.

—Kyaaaaaah!

Horrible cries of pain rang out as a choking stench rose all around us.

A wide-area spell that tore right through their densely packed formation.

In the midst of the chaos, one of the higher-level monsters, which seemed to have a fair amount of Intelligence, hurried to pull the broken formation back together.

Or tried to.

—Alu. Karsh…!

*CRUNCH!*

Before it could, I dropped from above and drove a punch infused with internal energy into its head, bursting its rock-hard skull.

*Ding.*

> **System**
>
> You have defeated the Lv. 101 Minotaur Warrior!
>
> You have gained a small amount of EXP!

*Slump. Thud.*

With the System notification, its stumbling body fell like a rotten log.

I spat on the corpse, adjusted my grip on White Flame, and muttered, “You piece of shit. Who asked you to ruin the moment?”

At the sight of me dropping out of the sky like a comet, the monsters around me blinked. Their eyes were as innocent as those of herbivores gathered by a stream.

But I already knew.

Those eyes only looked so gentle because they were incredibly stupid. The instincts hidden behind them were more savage and cruel than those of any living thing in the world.

—Grrk?

“Nice meeting you. Now get lost.”

With a greeting that would be both my first and last, I twisted around and swung the spearhead.

*CRRRACK!*

Flesh and bone came apart, and a haze of blood spread through the air. Dozens fell in a single strike; with the second, swung as I stepped forward, the area around me was empty.

*Squish.*

As I approached, stepping through the blood-soaked sand, the air around me gave a sharp, tingling hum.

The heat stirred up by Scorching Yang Qi was intense, but the monsters looking at me had long since frozen their eyes cold.

One Against a Thousand.

The overwhelming martial prowess and aura radiating from me.

The **Intimidation** pressing down on their bodies felt close enough to touch. Fear erased their ferocity and swallowed their instincts.

And the Hunters, who had patiently waited for this moment, didn’t let it pass.

*CRUNCH!*

“Charge! Wipe them all out!”

“Die, you bastards!”

*Clang-clang! Slice!*

With a tremendous roar, a shining wave of steel crashed into the monsters.

It had been a relatively short time, but these elites had held their ground against a force more than ten times their size without taking heavy losses.

After holding back for as long as they could against the endless tide of monsters, the Hunters seized their chance. They plunged into the formation broken apart by Magic Johnson’s wide-area spell and stabbed and slashed at everything in their path.

*Slice, thud-thud-thud!*

“God damn it! Motherfucker!”

—GRAAAAAH!

Curses and screams mingled as Force and magical power, light and darkness, clashed all around us.

And the scales of that clash were tipping toward the light by the second.

“Team Three, eyes on two o’clock! Circle around and break through!”

“Ranged unit, get ready! Fire!”

“Fire!”

*Whoosh-whoosh-whoosh—BOOM!*

A rain of arrows fell with a sharp whistle as they cut through the wind. The mages’ wide-area spells swept across the battlefield.

Each team moved like a living organism. Their tactics were disciplined, always aimed at the enemy’s openings.

The monster army had grown stronger than before as magical power became more concentrated.

But if superior physical abilities and magical power, granted at birth, were enough to win every battle, the monsters would have already conquered the world.

“Come on, you bastards.”

I shot forward, my voice cold. The moment I chose a target, my body was already moving—erasing the distance and launching into its next action.

*Slice, boom!*

I cut down the goblin shaman trying to prepare a spell, then smashed the chest of the Orc chieftain beside it.

A rain of arrows poured down over the Orcs, who were left scrambling after losing their chieftain in an instant.

*Whoosh, thud-thud-thud!*

Arrows wreathed in Force pierced their thick hides, passing through their heads and chests.

Just as a particularly huge Troll hurried to retreat at the sight of me approaching, two streaks of light curved out from behind it.

*Thud, slice!*

The first sword pierced its chest. The second cut off its head.

Their movements were perfectly coordinated, without a hint of hesitation or wasted effort.

The swordsmen who had chopped the Troll—which still writhed despite its fatal wounds—into dozens of pieces spotted me and smiled faintly.

*Xiao Shen. And Team Leader Choi.*

There was no time for the two of them and me to exchange words in the chaos of battle.

Especially when we understood each other without saying a thing.

They gave me a light nod, then charged toward another target. They were going after the higher-level monsters intelligent enough to control their respective groups.

*Good choice.*

Most people instinctively resist killing living things—especially other people.

I didn’t know if that instinct had been ingrained over the course of history or learned through civilization, but there was no doubt it existed.

Monsters were different from the start. Born to a fate of struggle, they barely even recognized their own kind.

*If we take out the monsters leading these groups, the real chaos will begin.*

No—chaos had already begun.

Four S-rank monsters, including the most powerful of them, the Manticore Lord, had fallen. On my orders, Magic Johnson and the Hunters, who had been focused solely on defense, were now plunging into the center of the monsters and cutting them apart.

The higher-level monsters leading each group, their equivalent of lower-ranking commanders, were falling all over the battlefield at the hands of A-rank Hunters led by Team Leader Choi and Xiao Shen. Yamamoto Genji was also making a conspicuous contribution.

“Hup. Gale Slash!”

The name of the technique, barked in a low voice, was pure Japanese bravado. But the power behind that single sword strike was no bluff.

*Shwaa—slice!*

With a flash of light streaking across the battlefield, dozens of monsters fell, spraying blood.

Hunters rushed into the space that had been emptied in an instant and cut down every monster in their path.

*CRUNCH! FWOOSH!*

The formation slowly collapsed, and the front line was pushed back.

But waiting for the monster army as it gave ground, step by step, were the Skeleton King and a thousand Skeletons, blocking off their rear.

“Surround them! If you have no teeth, then hold them back with your bones!”

*Clack-clack-clack!*

—GRAAAAH!

*CRUNCH!*

A massive monster several meters tall swung its mace and smashed a dozen Skeletons to pieces.

At the same time, dozens of Skeletons used the opening to latch onto it or climb up its body, sinking their rusty swords and teeth into its enormous frame.

*Thud. Crack!*

—GRAAAAAH!

The enraged roar turned into a scream of pain. Then, as the massive monster met a gruesome death, a cold blue light appeared in its eyes.

—Grr. Ah. Ah. Ah.

Reborn as an undead, the massive monster charged off, dragging its heavy body along.

The Hunters flinched at the sight, but once they spotted the Skeleton King, they went right back to fighting as if nothing had happened.

“Attack! They’re breaking!”

“Their formation’s falling apart! Don’t back down—keep pushing!”

It had been less than an hour.

But victory had already begun to swing toward humanity.

Thousands of monsters had already been wiped out. The force that had initially outnumbered us ten to one was now down to five to one—and the gap was shrinking by the second.

*CRACK! THUD!*

An Ogre Warrior, over four meters tall, collapsed without even a scream.

I leaped into the air, pushing off the shoulder of the monster as it tipped forward, its chest blown open. In the brief instant I was airborne, I took in the battlefield below.

*It’s over. If we keep pushing a little longer, we’ll win.*

The monsters no longer had any trace of the momentum they’d shown at the start, when they surrounded the Hunters and attacked without letup.

Having lost four S-rank monsters as well as the lower-ranking commanders leading their groups, the monsters were in utter disarray. The Grand Mage’s wide-area spells from the front, and the Skeleton King’s undead soldiers pressing them from behind, only made things worse.

*And the Hunters are fighting like hell, too.*

The monster army was now nothing but beasts with a lot of bodies.

Victory was only a matter of time.

Not one of those countless monsters could stop us. Could stop me.

Except for the one being that still hadn’t shown itself.

*Where the hell are you?*

Thinking of The Prophet, who was one big mystery, I dropped back toward the ground.

*BOOM! Slice!*

White Flame’s spearhead plunged down with me and split open another monster’s skull. Its body split cleanly in two and fell to either side. Between the halves, I saw eyes filled with fear.

“Die.”

I charged like a beast of prey and went on a rampage.

The lower-level monsters froze as though gripped by **Fear**, staring at the death rushing toward them. The higher-level monsters used every last bit of strength to fight back.

They fell in different ways, but the result was always the same.

Death.

*Thud!*

I twisted the spearhead that had pierced the Lycanthrope between the eyes, then pulled it free. Brains ran down White Flame’s transparent spearhead.

A dull ache crept through my arms and legs, which had been in constant motion.

*Damn it.*

How long had I been fighting? How many monsters had I killed?

I didn’t know. Better not to know. The moment my brain registered it, my body would only feel more exhausted.

If The Prophet, still nowhere in sight, was watching me now, all the more reason not to show any weakness.

*Hoo. Hah.*

I steadied my breathing and adjusted my grip on White Flame.

The moment I turned to face yet more monsters, I realized the scales of the battle had finally tipped all the way over.

*Rumble. Rrrumble!*

—GRAAAAAH!

—Krrk. GRAAAAH!

The desert shook. With terrified cries, wave after wave of monsters were retreating.

*They’re running. All those monsters.*

The thought that flashed through my mind was exactly what I was seeing.

The advantage in numbers?

The monster army, having lost its will to fight and fleeing at full speed, no longer cared about any such thing.

The Hunters stared, blinking, then raised their tired spears and swords. With bloodshot eyes, they raced after the monsters.

“Kill every last one!”

The only thing left on the battlefield now was slaughter.
```
