<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0806.txt",
      "sha256": "fbe0e3bc2de56d9d49d5cd6b5d5f57899c75c5fab2c98c1b18d3ac72d1fb4cde",
      "bytes": 14140
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d31bddce17275138b81582993c5734ddb4139de17fd8a2e1f437b22dbaf29b94",
      "bytes": 1504
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "49d64f850f225225ac5059ed4beae474d68243ea74bfdfa7aea76b02e0387247",
      "bytes": 225301
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "6f7baa3c2d54c99f49c05814f96c3f3a2b43db747686333a77622fa32a267101",
      "bytes": 553
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "7bb16571a4ce77fb71cae778eca591e84cac0083e713f594d23b33cd9d69bb60",
      "bytes": 666
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b08d088bb854d874cf14b9d829212aacd492ea82ebbf8401c98f99ad170f3b7d",
      "bytes": 247557
    }
  ],
  "estimated_tokens": 9122
}
-->

# Durable State Update — Chapter 806

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 806. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 806. Profile updates may replace only one
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
  "chapter": 806,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 806,
    "continuity_sources": [806],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "Jin commands roughly one thousand Hunters against a monster force exceeding ten thousand in the Rub’ al Khali.",
    "The three S-rank commanders are the Lycanthrope Champion, Death Knight Legion Commander, and Manticore Lord; the Manticore Lord is especially strong and cunning.",
    "Jin is wounded in the thigh by the Manticore Lord.",
    "The Skeleton King can maintain a thousand undead while fighting and directing them; he is taking on the Death Knight while Jin faces the Manticore Lord.",
    "The monster army obeys an unseen authority and is breaking through the defenders’ small line.",
    "The Prophet’s location is unknown; the Manticore Lord says he is everywhere and nowhere.",
    "Jin trusts Magic Johnson and the others to defend against the aerial monsters.",
    "Yamamoto has withdrawn to the front ranks beside Choi Minwoo."
  ],
  "continuity_sources": [
    804,
    805
  ],
  "open_questions": [
    "Where is The Prophet, and how is he directing the monster army?",
    "Can the defenders hold against the monster force, including its aerial monsters?",
    "What will happen in the fights against the three S-rank commanders?"
  ],
  "safe_through": 805,
  "temporary_decisions": [
    "Keep magical power distinct from mana."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 민첩               | **Agility**                    |
| 몬스터     | **monster**           |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 만티코어 | **Manticore** | A-Rank Gate monster and original raid target. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 나이트메어 | **Nightmare** | A-rank monster warhorse ridden by the Death Knight Lord. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 심해 | **deep sea** | Unexplored ocean depths where the ancient monster awakens. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 804
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 800
- **Aliases:** None
- **Role:** Leviathan was an ancient S-rank sea monster and ruler of the sea who was killed by Jin Taekyung after the deep-sea hunt, leaving a final warning that the Cataclysm was approaching.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus, its master, and withdrew into the deep sea after Asmodeus fell.

## Korean source

```text
＃806화



무림에는 오랜 세월 동안 전해져 내려오는 격언(格言)이 있다.

‘삼류 칼잡이는 길거리 왈패들에게 맞아 죽고, 절정 고수는 자신과 같은 고수와 싸우다 죽지만, 초절정 고수를 죽일 수 있는 것은 그가 가진 오만함과 방심뿐이다.’

무림인들이 생각하는 초절정 고수란 그런 존재였다.

경이과 두려움의 대상.

모두가 무림이라는 험산을 헤매고 있을 때, 드높은 봉우리 위에 우뚝 서서 그들을 굽어보는 절대자들.

그러나 이 세상에 무적(無敵)이란 단어는 통용되지 않는다.

선택받은 영역에 들어선 존재들에게도 엄연한 격차가 있는 법.

밑에서 위를 바라보는 이들은 그 사실을 알 수 없지만, 각자의 산봉우리를 차지한 존재들은 보고 느낄 수 있다.

짙은 안개 너머, 자신보다 높고 낮은 곳에 우뚝 선 또 다른 봉우리의 누군가를.

그리고 그것은 나 역시 마찬가지였다.

슈확!

비스듬히 내리그은 창날을 따라 예리한 바람이 터져 나온다.

하지만 운 나쁘게 궤적에 걸려든 몬스터들의 사지를 조각 내며 목표를 향해 쏘아진 바람은, 거대한 포효와 함께 잦아들었다.

- 캬우우우!

마력이 실린 충격파가 바람과 함께 사그라졌다.

나는 단 한 번의 울부짖음으로 창격을 상쇄시킨 괴물을 바라보았다.

‘강하다.’

사방에서 들끓는 마력에 피부가 따끔거린다. 호흡을 삼키고 뱉을 때마다 느껴지는 공기는 쓰고 쾌쾌했다.

‘만티코어 로드.’

신화 속에서 기어 나온 괴물.

심지어 그중에서도 ‘로드’라 불릴 만큼 강한 우두머리.

사박.

사자의 그것과 같은 앞발이 피에 젖은 모래를 밟은 순간, 제자리에서 사라진 놈의 신형이 공간을 갈랐다.

퍼엉!

바람만큼이나, 아니 바람보다도 빠른 속도.

어떤 의미로는 가장 최근에 쓰러트렸던 네임드 몬스터인 레비아탄보다도 훨씬 까다로운 상대다.

품고 있는 마력 자체는 레비아탄이 훨씬 높았지만, 앞서 느꼈던 강력한 힘, 그리고 지금 보이는 속도와 몸뚱어리의 크기는 대규모 학살보단 일대일에 최적화되어 있었으니까.

‘거기에 더해 라이칸스로프 챔피언까지.’

절대 방심해서는 안 되는 싸움이다.

두 S급 몬스터의 움직임을 주시하고 있던 나는 타이밍에 맞춰 땅을 박찼다. 스켈레톤 킹을 향한 전음(傳音)과 함께.

- 쪽팔리게 지지 마라.

대답은 들려오지 않았다.

그 자체로 A급 몬스터인 유령마, 나이트메어(Nightmare)를 소환한 데스 나이트 군단장이 높게 뛰어올라 스켈레톤 킹을 향해 내리꽂히는 중이었다.

콰앙!

어느덧 훌쩍 멀어진 등 뒤에서 굉음이 터져 나온다. 스켈레톤 킹의 외침이 쩌렁쩌렁하게 울려 퍼졌다.

“감히 한낱 군단장 주제에! 왕을 알현할 때에는 무릎을 꿇어라!”

저 말대로 데스 나이트 군단장이 무릎을 꿇고 충성을 맹세한다면 더할 나위 없는 결과겠지만, 현실은 그리 녹록하지 않다.

저들은 이미 다른 주인을 따르고 있고, 지금 내 눈앞에는 엄청난 마력을 머금은 꼬리와 발톱이 들이닥치고 있으니까.

쾅!

곧게 세워 공격을 받아 낸 백염의 창날이 부르르 떨린다.

그러나 앞서 있었던 한 차례의 격돌과 달리, 이번에 물러서야 하는 것은 내가 아닌 놈들이었다.

쉬잉! 서걱!

망설임 없이 내리그은 창날에 거대한 갈고리를 닮은 반인반수(半人半獸)의 발톱이 두부처럼 잘려 나간다.

‘어렵지 않은 상대다.’

단, 한 마리뿐이라면.

- 크륵?

당혹스러운 울음소리를 흘리며 뒷걸음질 치는 라이칸스로프 챔피언을 베어 가르려던 그때, 창날에 가로막혀 튕겨 나갔던 만티코어 로드의 꼬리가 뱀처럼 꿈틀거리며 내 얼굴을 노렸다.

후웅!

목덜미를 스쳐 지나가는 풍압(風壓)이 쇳덩이처럼 무겁다.

그러나 이미 한 차례 겪었던 패턴.

홀로 세 마리를 동시에 상대했다면 틀림없이 낭패를 봤겠지만, 지금 같은 상황이라면 이야기가 달라진다.

‘우선 한 놈부터.’

화륵.

손아귀에 맺힌 불길을 보고 위기를 알아차린 라이칸스로프 챔피언이 몸을 틀었지만, 타이밍이 반 박자 늦었다.

아니, 내가 빨랐다.

퍼엉!

화염신장에 직격당한 놈의 신형이 뒤로 주르륵 밀려난다.

짧은 순간 까맣게 그을린 한쪽 팔을 붙잡은 놈이 비명과도 같은 포효를 토해 냈다.

- 크아아아아!

아쉬운 일이다.

셋 중 최약체에 속하는 놈이지만, 명색이 S급 몬스터라서 그런지 원래 목표였던 가슴을 아슬아슬하게 비껴갔다.

‘일격. 앞으로 남은 일격으로 끝장낼 수 있다.’

그러나 만티코어 로드는 강한 것만큼이나 교활한 놈이었다.

내가 마무리를 하기 위해 창을 휘두르려던 그 순간, 지금껏 보인 속력을 뛰어넘어 내 등을 노렸으니까.

콰앙!

나는 벼락처럼 내리꽂힌 발톱을 막아 냈다.

엄청난 압력에 창대가 흔들리고, 사막에서도 자유롭게 움직이던 두 다리가 모래알 깊숙이 파묻혔다.

그리고 그것 역시, 놈이 계산한 상황 중 한 가지였다.

쐐애액. 퍽!

공성추(攻城鎚)보다 묵직하고 강력한 꼬리가 옆구리를 후려친다.

꼬리 끝에 담긴 가시는 화룡갑을 완전히 뚫지 못했지만, 그 위로 전해진 어마어마한 충격은 고스란히 내가 감당해야 할 몫이었다.

“흡……!”

일순간 아득해지는 시야와 동시에 가슴을 타고 치밀어 오르는 뜨거운 무언가.

울컥, 목울대를 비집고 흘러넘치려는 핏물을 삼켜 낸 나는 흐릿해진 시야 속에서도 손을 뻗었다.

‘인벤토리 오픈. 소환.’

창대에서 한 손이 떨어지자 압력이 더욱 거세진다. 그러나 나는 빛살과도 같은 속도로 인벤토리에서 꺼낸 단검을 휘둘렀다.

쉭, 서걱!

절삭음은 하나지만, 철갑 같은 꼬리를 가로지른 실선은 세 줄기다.

거대한 두 개의 앞발로 나를 짓누르려던 만티코어 로드의 눈이 크게 뜨인 것도 바로 그때였다.

푸화아아악!

희미한 실선으로부터 뒤늦게 뿜어져 나온 핏물이 분수처럼 뿜어진다.

고통으로 인해 귀까지 쩍 벌어진 만티코어 로드의 아가리에서 숱한 죽음의 악취가 풍겨왔다.

- 크허어어엉!

마치 사자와 같은 울부짖음. 불과 코앞에서 내지른 포효에 귀가 먹먹해진다.

아니, 고막이 터졌음이 틀림없다.

‘이 개새끼가.’

나는 귓가에서 흘러나오는 뜨거운 핏물을 느끼며 이를 악물었다.

그리고 짓누르는 힘이 잠시 약해진 그 틈을 타, 아직 손에 들려있던 단검을 놈의 늑골 부위에 쑤셔 박았다.

푸푹!

단검에 실린 강기(罡氣)는 열양지기로부터 비롯된 것.

용암과도 같은 열기는 단단한 가죽과 살을 가른 뒤, 뼈를 부러뜨림과 동시에 내부를 불살랐다.

치이이이익!

- 끄아아아!

- 캬우우우!

고막이 터진 탓인지, 고장 난 이어폰처럼 겹쳐 들리는 듯한 만티코어 로드의 울부짖음.

하지만 그것이 단순한 착각이 아니라는 사실을, 나는 본능적인 감각으로 깨달았다.

‘이건.’

다르다. 처음부터 잘못 들은 것이 아니다.

먼저 들려온 것이 고통에 찬 비명이라면, 두 번째 것은 분노 가득한 포효였으니까.

그리고 불길한 예감을 늘 틀리는 법이 없다.

‘라이칸스로프 챔피언.’

머릿속에 떠오른 그 이름과 함께 잠시 잊고 있던 반인반수의 괴물이 등 뒤에서 달려들었다.

슈확!

S급 몬스터라 부르기에 부족함이 없는 눈부신 속도.

금방이라도 잿가루가 되어 바스러질 것 같은 한쪽 팔을 흔들거리며 쇄도한 놈이 아직 멀쩡한 팔을 휘두르자, 갈고리처럼 휘어진 발톱이 번쩍 빛났다.

‘단검을 뽑아 휘두르기에는 이미 늦었다.’

찰나의 순간 머릿속을 스쳐 지나가는 수많은 움직임과 미래.

그 끝에 남은 선택은 하나뿐이다.

어느샌가 느리게 흘러가는 세상 속, 나는 만티코아 로드의 늑골에 박아 넣었던 단검을 놓으며 일장(一掌)을 내질렀다.

화륵, 퍼걱!

다급하게 끌어올린 공력이, 불꽃이 흩어진다.

손을 타고 전해지는 아찔한 격통 속, 나는 손바닥을 뚫고 손등으로 튀어나온 은빛 발톱을 바라보았다.

‘……씨벌.’

바로 코앞에서 멈춘 발톱을 보고 있자니 쌍욕이 절로 튀어나온다.

하지만 내게 남은 고통은 이것으로 끝이 아니었다.

우둑. 우두둑!

뼈가 어긋나는 소리와 함께 마치 자라처럼 쭉 늘어나는 목.

목숨이 오가는 위기의 순간 속, 교활한 놈답게 마지막까지 숨겨 두었던 능력을 발휘한 만티코어 로드의 목이 놈과 나 사이를 가로막던 창대를 넘어 들이닥친다.

- 크아아!

괴담 속 귀신처럼 귀 끝까지 쩍 벌어진 아가리에서는 시체 썩은내가 풍겼고, 톱날처럼 크고 날카로운 이빨을 보자 전신의 털이 곤두서는 듯한 감각이 전신을 사로잡았다.

“……!”

등골을 타고 흐르는 한기.

이대로 저 아가리가 닫히면 남은 건 죽음뿐이다.

나는 온 힘을 다해 몸을 비틀었다. 머리를 통째로 씹어 삼키려던 이빨이 머리카락을 스치며 쇄골에 틀어박혔다.

보다 정확히 말하자면, 쇄골 위를 뒤덮은 붉은 빛의 갑옷에.

콰드득!

삐빅. 삐비빅!



- [화룡갑]의 일부 부위가 파손되었습니다!

- [화룡갑]의 내구도가 대폭 하락합니다!

- 위험! 위험! 지금 같은 공격에 또다시 노출된다면 [화룡갑]이 인벤토리로 자동 수납될 수 있습니다!

- [만티코아 로드의 맹독]이 파손된 부위의 틈새로 침투했습니다!

- 상태 이상, [중독]이 부여됩니다!

- 최대한 빠른 해독이 필요합니다! 제한 시간 내에 해독하지 않을 시, 상태가 더욱 악화될 수 있습니다!



‘빌어먹을. 이건 또 무슨 소리야.’

어째 쇄골 부위가 따끔하다 싶더니만 갑자기 맹독이라니.

나는 불알 두 쪽 달고 태어난 게 전부인데, 이 새끼는 네임드급이라 그런지 가진 능력도 더럽게 많다.

“……간. 인간!”

싸우는 와중에도 이 상황을 용케 지켜봤는지, 저 멀리 등 뒤에서 스켈레톤 킹의 다급한 외침이 들려온다.

하지만 녀석의 걱정과는 달리, 나는 이대로 죽어 줄 생각이 눈곱만큼도 없다.

오히려 [중독]으로 인해 감각이 무뎌진 것이 반갑게 느껴질 정도다.

적어도 내가 지금 하려는 행동으로 인한 통증은, 이제 거의 느껴지지 않을 테니까.

“도와줘서 고맙다, 이 개새끼야.”

들릴 듯 말 듯 하게 속삭인 한 마디에 만티코아 로드의 눈이 부릅떠진 그 순간.

나는 남은 한 손이 잡고 있던 백염을 떨어트림과 동시에 놈의 목울대로 짐작되는 곳을 후려쳤다.

뻐억!

묵직한 타격음.

흡, 하고 숨을 삼킨 만티코아 로드의 눈동자에 독기가 서린다.

푸욱!

전보다 더한 힘이 실린 이빨이 화룡갑의 틈새를 벌리며 쇄골을 깊게 파고든다.

삐빅. 삐비빅. 귓가에 울려 퍼지는 경고음과는 달리 고통은 더욱 무뎌졌다. 갈고리에 걸린 생고기나 다름없던 손바닥을, 아무렇지 않게 움직일 수 있을 만큼.

콰득.

손바닥을 관통한 모습 그대로 발톱이 붙잡힌 라이칸스로프 챔피언이 이를 드러내며 웃었다.

가소롭기 그지없다는 비웃음.

그러나 그 비웃음이 사라지기까지 걸린 시간은 찰나에 불과했다.

- 크륵?

순식간에 당혹감으로 물든 얼굴. 아무리 힘을 줘도 꿈쩍하지 않는 내 모습에 눈을 깜빡이는 놈을 향해, 나는 담담하게 입을 열었다.

“내가 이 씨발럼아, 아무리 몸 상태가 안 좋아도 너 하나 못 이기겠냐.”

지금껏 올린 근력 스탯만 따져도 오우거 아빠 군번인 나다.

특수 디버프로 모든 능력치가 대폭 삭감된 지금에도, 내가 가진 신체 능력은 어지간한 S급 몬스터와 비견되거나 그 이상이었다.

근력보다는 민첩에 특화된 라이칸스로프 챔피언 정도는, 한 손으로 메다꽂을 수 있을 정도로.

“새끼…… 차렷!”

빡, 우지직!

조인트를 까인 무릎이 단번에 박살 난다.

나는 반인반수 최강의 전사가 구슬프게 울부짖는 틈을 타, 손아귀에 단단히 붙잡은 놈의 발톱을 그대로 쥐고 땅을 향해 메다꽂았다.

후웅, 쾅!

굉음과 함께 피어오르는 흙먼지. 동시에 발톱이 빠져나간 손바닥에서 핏물이 분수처럼 터져 나왔다.

하지만 내게 중요한 것은 하나다.

마침내 한 손이 비었다는 것.

‘인벤토리 오픈, 소환.’

예리한 비수가 번쩍인다. 그 위로 가파르게 솟구친 뜨거운 겁화가 만티코아 로드의 머리를 향해 날아든다.

- ……!

뒤늦게 내 계획을 깨달은 라이칸스로프 챔피언이 몸을 날렸지만, 이미 늦었다.

푸욱, 콰아아아!

가죽을 가르고 살과 뼈를 부수는 칼날. 그리고 폭발하는 화염.

띠링.

기다리던 맑은 종소리가 귓가를 울린 그때.

돌연 어디선가 휘둘려진 섬광이 내게 달려들던 라이칸스로프 챔피언의 목을 갈랐다.

서걱!

“제가 왔습니다! 진 사마!”

“…….”

이 씨벌놈이 막타를.
```

## Final English reading copy

```markdown
# Chapter 806

There’s an old saying that’s been passed down in the Murim for ages.

*A Third Rate swordsman gets beaten to death by street thugs. A Peak master dies fighting another master like himself. But the only things that can kill a Supreme Peak master are his own arrogance and carelessness.*

That was how martial artists thought of Supreme Peak masters.

Beings to be marveled at and feared.

While everyone else wandered the treacherous mountains of the Murim, they stood tall on the highest peaks, looking down at them all.

But the word *invincible* has no place in this world.

Even among those who reach the chosen realm, there are clear differences in strength.

Those looking up from below can’t see them, but the ones standing on their own peaks can see and feel it:

Someone else standing on a peak beyond the thick fog, higher or lower than their own.

And I was no different.

*Shwaa!*

A sharp gust burst from the spearhead as it slashed down at an angle.

The wind tore the limbs off the monsters unlucky enough to get caught in its path, then shot toward its target. But a massive roar swallowed it up.

—Kyaaaaa!

A shockwave imbued with magical power faded along with the wind.

I looked at the monster that had canceled out my spear strike with a single roar.

*Strong.*

Magical power boiled all around us, prickling my skin. The air tasted bitter and stale each time I breathed in and out.

*Manticore Lord.*

A monster crawled out of myth.

And a leader strong enough to be called a *Lord* even among its kind.

*Step.*

The moment its lion-like forepaw touched the blood-soaked sand, its body vanished from where it stood and tore through space.

*Boom!*

As fast as the wind—or faster.

In some ways, it was far more troublesome than Leviathan, the most recent named monster I’d taken down.

Leviathan had possessed far more magical power, but the overwhelming strength I’d sensed earlier, combined with the speed and sheer size I saw now, made this one better suited to one-on-one combat than mass slaughter.

*And there’s the Lycanthrope Champion, too.*

This was a fight where I couldn’t afford to let my guard down for even a second.

Keeping an eye on the two S-rank monsters, I kicked off the ground at just the right moment—and sent a message to the Skeleton King through Sound Transmission.

—Don’t lose and embarrass yourself.

No answer came.

The Death Knight Legion Commander summoned a Nightmare, a ghost horse that was an A-rank monster in its own right, then leapt high and came crashing down toward the Skeleton King.

*BOOM!*

A thunderous crash erupted behind me, already far off in the distance. The Skeleton King’s voice rang out across the battlefield.

“Daring to challenge me, a mere legion commander! When you stand before a king, you get on your knees!”

It would be ideal if the Death Knight Legion Commander did as he said, dropped to its knees, and swore allegiance. But reality wasn’t so accommodating.

They already served another master—and a tail and claws brimming with magical power were bearing down on me.

*BANG!*

The spearhead of White Flame, held straight up to block the attack, shuddered.

But unlike our previous clash, this time it was my opponents who had to back off.

*Whoosh! Slice!*

My spear slashed down without hesitation, cutting through the Lycanthrope Champion’s huge, hook-like claw as easily as tofu.

*Not a difficult opponent.*

If it were the only one.

—Grr?

The Lycanthrope Champion let out a startled growl and stumbled backward. I was about to cut it in two when the Manticore Lord’s tail—knocked away by my spear—writhed like a snake and lunged for my face.

*Whoom!*

The pressure of the wind brushing past my neck was as heavy as a block of iron.

But I’d already dealt with this move once.

If I’d been facing all three of them alone, I’d have been in real trouble. But in a situation like this, things were different.

*One at a time.*

*Fwoosh.*

The Lycanthrope Champion saw the flames gathering in my hand and twisted away, but it was half a beat too late.

No—I was faster.

*BOOM!*

Struck dead-on by the Flame Divine Palm, it slid backward. For a brief moment, it clutched its one arm, charred black, and let out a roar like a scream.

—GRAAAAAH!

What a shame.

It was the weakest of the three, but it was still an S-rank monster. The attack just barely missed its intended target: its chest.

*One strike. One more and I can finish it.*

But the Manticore Lord was every bit as cunning as it was strong.

Just as I swung my spear to finish the Lycanthrope off, the Manticore Lord moved faster than it had at any point so far and went for my back.

*BOOM!*

I blocked the claw that came crashing down like lightning.

The spear shaft shook under the tremendous pressure, and my legs—usually free to move even in the desert—sank deep into the sand.

That, too, was exactly what the monster had calculated.

*Shwaa! Thud!*

Its tail struck my side with more weight and force than a battering ram.

The stinger on its tip couldn’t pierce all the way through my Fire Dragon Armor, but I had to bear the full force of the tremendous impact it delivered.

“Ugh…!”

My vision went hazy. At the same time, something hot surged up through my chest.

I swallowed the blood that welled up past my throat, then reached out despite my blurred vision.

*Open Inventory. Summon.*

As one hand left the spear shaft, the pressure grew even heavier. But I swung the dagger I pulled from my Inventory at the speed of a streak of light.

*Shhk, slice!*

There was one sound of cutting, but three thin lines crossed the iron-hard tail.

The Manticore Lord’s eyes widened just as it tried to crush me with its two massive forepaws.

*FWOOSH!*

Blood belatedly sprayed from the faint lines like a fountain.

Its jaws gaped wide in pain, and the stench of countless deaths poured out.

—GRAAAAAAAH!

A roar like a lion’s. The roar it unleashed from right in front of me left my ears ringing.

No—my eardrums had to have burst.

*You son of a bitch.*

I clenched my teeth, feeling hot blood running from my ears.

Then, taking advantage of the moment when its weight on me briefly eased, I drove the dagger still in my hand into its ribs.

*Thud!*

The Force on the dagger came from Scorching Yang Qi.

Like lava, its heat sliced through tough hide and flesh, broke bone, and burned its way through the inside.

*Sssss!*

—GRAAAAH!

—Kyaaaaa!

The Manticore Lord’s roar seemed to overlap, like a pair of broken earbuds. Maybe that was because my eardrums had burst.

But my instincts told me it wasn’t just my imagination.

*This…*

It was different. I hadn’t misheard the first time.

If the first cry was a scream of pain, the second was a roar of rage.

And my ominous hunches were never wrong.

*Lycanthrope Champion.*

The name came to mind, and the half-man, half-beast monster I’d momentarily forgotten lunged at me from behind.

*Shwaa!*

It moved at a blinding speed worthy of an S-rank monster.

It charged, its one arm dangling as if it were about to crumble into ashes, then swung its still-healthy arm. Hooked claws flashed.

*Too late to pull out the dagger and swing it.*

In that instant, countless movements and possible futures flashed through my mind.

Only one choice remained at the end of them.

In a world that had somehow slowed down, I let go of the dagger stuck in the Manticore Lord’s ribs and thrust out my palm.

*Fwoosh—crack!*

The internal energy I’d hurriedly drawn up scattered like sparks.

With a dizzying pain running through my hand, I stared at the silver claw that had pierced my palm and emerged from the back of my hand.

*…Fuck.*

Looking at the claw stopped just short of my face, I couldn’t help swearing.

But that wasn’t the end of the pain I had left to suffer.

*Crack. Crunch!*

Bones shifted with a series of cracks, and a neck stretched out like a turtle’s. At the brink of death, the Manticore Lord unleashed an ability it had cunningly kept hidden until the very end. Its neck surged over the spear shaft between us and lunged at me.

—GRAAH!

Its jaws gaped all the way to its ears like a ghost from a horror story, reeking of rotting corpses. The sight of those huge, serrated teeth sent a chill through my whole body, raising every hair on end.

“……!”

A chill ran down my spine.

If those jaws closed on me, all that would be left was death.

I twisted with all my strength. The teeth that had been about to swallow my entire head brushed my hair and sank into my collarbone.

More precisely, into the red armor covering my collarbone.

*CRUNCH!*

*Beep. Beep-beep!*

> **System**
>
> Part of your **Fire Dragon Armor** has been damaged!
>
> The durability of your **Fire Dragon Armor** has dropped significantly!
>
> **Danger! Danger!** If you are exposed to another attack like that, your **Fire Dragon Armor** may be automatically returned to your Inventory!
>
> **Manticore Lord’s Venom** has entered through the gap in the damaged armor!
>
> Status abnormality **Poisoned** has been applied!
>
> Detoxify as soon as possible! If you do not detoxify within the time limit, your condition may worsen!

*Damn it. What the hell is this now?*

My collarbone had been tingling, and now suddenly I was poisoned.

I was just a guy with a pair of balls, but this bastard was a named monster. No wonder it had so many damn abilities.

“……Human!”

Even while fighting, the Skeleton King had somehow seen what happened. His urgent shout came from far behind me.

But despite his worry, I had no intention of dying here. Not even the slightest.

If anything, I was almost glad that being **Poisoned** had dulled my senses.

At least now I wouldn’t feel much pain from what I was about to do.

“Thanks for the help, you son of a bitch.”

At my barely audible whisper, the Manticore Lord’s eyes widened.

I dropped White Flame from my remaining hand and struck the spot I guessed was its throat.

*Thwack!*

A heavy impact.

The Manticore Lord sucked in a breath, and its eyes turned vicious.

*Thud!*

Its teeth drove in with even more force than before, widening the gap in my Fire Dragon Armor and sinking deep into my collarbone.

The warning beeps rang in my ears, but the pain had dulled even further. Enough that I could move my hand without a care, despite its palm being nothing more than raw flesh pierced through by a hook.

*Crack.*

The Lycanthrope Champion’s claw remained lodged in my palm. It bared its teeth in a sneer.

Pure contempt.

But the sneer lasted only an instant.

—Grr?

Its face filled with surprise in no time at all. It blinked at me, unable to budge me no matter how hard it pulled. I calmly spoke to it.

“You really think I can’t beat your ass, you little shit, just because I’m in bad shape?”

Going by the Strength stats I’d built up, I outranked even an ogre’s dad.

Even with all my stats drastically reduced by the special debuff, my physical abilities were still comparable to—or better than—those of most S-rank monsters.

The Lycanthrope Champion was specialized in Agility rather than Strength. I could slam it into the ground with one hand.

“Now, you little punk… Attention!”

*Whack! Crack!*

The knee I kicked in the joint shattered in an instant.

As the strongest of the half-man, half-beast warriors let out a mournful cry, I kept a firm grip on its claw and slammed the monster into the ground.

*Whoom—BANG!*

The earth rumbled, and a cloud of dust rose. At the same time, blood burst from the palm the claw had just torn out of.

But only one thing mattered to me.

At last, one of my hands was free.

*Open Inventory. Summon.*

A sharp dagger flashed. Above it, blazing hellfire surged and flew toward the Manticore Lord’s head.

—…!

The Lycanthrope Champion realized my plan too late and threw itself forward, but it was already too late.

*Thud—KRAAAAAASH!*

The blade cut through hide, flesh, and bone. Then the flames exploded.

*Ding.*

Just as the clear chime I’d been waiting for rang in my ears, a flash of light suddenly swept in from somewhere and cut through the Lycanthrope Champion’s neck as it charged at me.

*Slice!*

“I’m here, Jin Sama!”

“……”

This son of a bitch stole my kill.
```
