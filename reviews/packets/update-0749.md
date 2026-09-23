<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0749.txt",
      "sha256": "d138722f3118cc9b5a136f62e29baf784c680da3c303a1bd0b7e1544e2fb3c4c",
      "bytes": 12553
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2d2f47a94c3f08deff0050e619d5d2578269cf7ec224c2ffb9a29ccdff8f85ff",
      "bytes": 2536
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4080a6ede1a1a5aa7a903939e21bd7b1b4a7ae1cfb8fe93132893e637532b77a",
      "bytes": 216382
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "2d488cc3a3f658cc38704daa444b3d05c5056c45962ab786fa6b9823a69efba6",
      "bytes": 553
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "3cc04beb5a02db4f50774dc38d028154b48d50404405355ab268bb3abb688b79",
      "bytes": 699
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "8fe908fd061e845f300bb49db5dc3fbf3788af15abac6132e4666622641f5372",
      "bytes": 620
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f5d8289bb9fb9f75b963eaa0e347a7b4e2b1134ead2f3a64f4f28c27aa4697c2",
      "bytes": 229305
    }
  ],
  "estimated_tokens": 8912
}
-->

# Durable State Update — Chapter 749

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 749. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 749. Profile updates may replace only one
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
  "chapter": 749,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 749,
    "continuity_sources": [749],
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
    "The Prophet commands the revived Hasasin and has announced a second series of terrorist attacks after the earlier attacks called Allah's Judgment.",
    "The Prophet can create a transparent concealment barrier that cannot be detected by science or Magic.",
    "The Prophet possesses at least ten unrefined S-rank Magic Gems that retain their original power.",
    "The retired Grand Mage Siegfried Wassmann was found dead in his sealed hideout after his life force was apparently drained by unknown magic.",
    "Michael Silbert remains the strongest suspect in Siegfried's death and has now personally entered the Japanese battlefield while pursuing his ambition to become the undisputed best.",
    "Jin has accepted the Supreme Peak Quest Unknown Death, whose mission is to discover the truth behind Siegfried's death.",
    "Michael and Huginn continue manipulating events and media coverage to isolate Jin and punish countries and Guilds that support him.",
    "Magic Johnson is investigating stolen research materials from Siegfried's laboratory but has not yet produced results.",
    "Huginn has completed an undisclosed operation whose consequences remain pending.",
    "Leviathan, the ancient S-rank sea monster once commanded by Asmodeus, has awakened and is devastating Japan while seeking a pure Magic Gem.",
    "Japan has requested Korean emergency assistance, with five Ares Guild and Peace Guild teams and the Korean Air Force heading toward Tokyo.",
    "A blue-white burst of light-flames has struck Leviathan, but its source and effect are unknown."
  ],
  "continuity_sources": [
    748
  ],
  "open_questions": [
    "Who killed Siegfried Wassmann, by what magic, and why?",
    "How did Michael Silbert learn about A Area and Cheon Taemin's condition, and did he order Siegfried's death?",
    "What is The Prophet's identity, and how are the Prophet's terrorist campaign and Leviathan's reappearance connected?",
    "What is Huginn's undisclosed operation, and can its consequences actually bring Jin down?",
    "Who or what caused Leviathan's awakening, and who unleashed the blue-white light-flames that struck it?"
  ],
  "safe_through": 748,
  "temporary_decisions": [
    "Render 선지자 as The Prophet.",
    "Render 레비아탄 as Leviathan and 스사노오 as Susanoo.",
    "Render 마력 as magical power, distinct from mana.",
    "Render 마정 as Magic Gem.",
    "Render 마계어 as Demon Realm language and 광염 as light-flames."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 신법     | **movement technique**                           |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 칭호               | **Title**                      |
| 민첩               | **Agility**                    |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 브레스 | **Breath** | Dragonkin power used by the Wyverns. |
| 탈진 | **Exhaustion** | System status effect caused by exhausting all internal energy while severely injured. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 똥개 | **Ddong Gae** | Taekyung's mocking misremembering of Hwang Gae's name. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 마정 | **Magic Gem** | Monster power source; Leviathan seeks an untouched one. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 748
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 697
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 748
- **Aliases:** None
- **Role:** Leviathan is an ancient S-rank sea monster and ruler of the sea that has awakened from a long deep-sea sleep and is devastating Japan.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus, its master, and withdrew into the deep sea after Asmodeus fell.

## Korean source

```text
＃749화



레비아탄은 바다의 재앙인 동시에 왕이다.

이는 마계에서도, 지구에서도 변함없는 사실이었다.

바다는 레비아탄이 태어난 고향이자 무패(無敗)의 전장이었고, 탄생과 함께 부여받은 이 광대한 영토 안에서 왕의 감시를 속일 수 있는 것은 아무것도 없었다.

그래, 분명 그랬을 터였다.

화아아아악!

찰나의 순간.

먹잇감을 앞에 두고 탐욕에 물들어 있던 괴물의 움직임이 멈췄다. 동시에 오랜 굶주림으로 마비되어 있던 레비아탄의 감각이 깨어났다.

‘이건.’

도대체 언제부터였을까.

깨달음과 함께 느려진 세상 속에서 레비아탄은 똑똑히 보고 느낄 수 있었다.

벼락처럼 빠르고, 태양과도 같은 열기를 품고 있는 강대한 기운을.

푸른 수면을 집어삼키며 내리꽂히는 그 화염이 바로 자신을 향하고 있음을.

촤악!

더 이상 망설일 여유 따위는 없었다.

먹이를 삼키기 위해 벌렸던 거대한 아가리가 수중에서 급히 선회했다.

곧이어 어느새 코앞까지 들이닥친 화염을, 레비아탄은 마력을 머금은 수백 개의 이빨로 씹어 부수었다.

아니, 그럴 수 있으리라 믿어 의심치 않았다.

콰득!

화염과 이빨이 닿은 그 순간, 머리를 뒤흔들 만큼 강렬한 충격이 찾아오기 전까지는.

콰드드드득!

- ……!

뭐라고?

레비아탄의 거대한 눈동자가 고통과 충격으로 부릅떠졌다.

대격변 당시 수십 척의 항공모함을 침몰시킨 자신의 이빨이, 그토록 날카롭고 파괴적인 무기가 단 일격을 견디지 못해 박살 난 것이다.

‘도대체, 도대체 어떻게?’

레비아탄이 해결되지 않는 의문으로 덜컥 굳어 버린 그때.

충돌의 여파로 일어난 무수한 기포(氣泡)가 흩어지며 이 모든 의문을 불러일으킨 원인이 모습을 드러냈다.

창.

그것은 한 자루의 창이었다.

고오오옹.

물과 파도 속에서도 꺼지지 않는 화염을 두른 은빛 창은 파르르 몸을 떨고 있었다.

마치 살아 있는 생물이라도 되는 듯이. 자신을 쥔 주인의 손길이 마음에 드는 듯이.

그리고 그 창의 주인에게는, 레비아탄이 수없이 죽여 왔던 어느 종족의 피가 흐르고 있었다.

- 어떻게 인간 따위가……!

숨길 수 없는 경악이 담긴 신화 속 괴수의 부르짖음에, 작고 하찮은 인간은 입술을 달싹이는 것으로 답을 대신했다.

일섬(一殲).

아득한 섬광이, 바다를 물들였다.



* * *



주위에서 흔히들 말한다. 원래 인생은 한 방이라고.

동의한다. 한 방을 노리다가, 바로 그 한 방에 인생을 날려 먹을 수 있다는 점에서 특히.

구구구궁!

하늘이, 아니 바다가 갈라지는 듯한 굉음.

동시에 터져 나온 거대한 충격파가 모든 힘을 소진한 몸뚱어리를 날려 보낸다.

회오리치는 급류(急流)에 휘말린 나는, 아득해진 시야 속에서 쉴 새 없이 울려 퍼지는 경고음을 들을 수 있었다.

삐빅. 삐비빅!



- 당신은 모든 공력과 기력을 소진했습니다!

- 당신의 신체가 [일섬]의 반동을 견디지 못합니다!

- 상태 이상, [공력 소진]이 부여됩니다!

- 상태 이상, [탈진]이 부여됩니다!

- 상태 이상, [빈혈]이 부여됩니다!

- 상태 이상, [근육 파열]이 부여됩니다!

- 상태 이상, [내상]이 부여됩니다!

- 경고! 경고! 모든 행동에는 대가가 따른다는 것을 명심하십시오!

- 과도한 힘의 남용은 스스로에게 칼날이 되어 돌아올 수 있습니다.

- 특수 디버프, [망가진 신체]가 부여됩니다!

- 회복 전까지 모든 전투 관련 능력치가 50씩 하락합니다! 회복 과정과 결과에 따라 일부 능력치를 영구 상실할 수 있습니다!

- [근력]이 일시적으로 50 하락합니다!

- [민첩]이…….

.

.

.

하이 리스크(High Risk), 하이 리턴(High Return).

그 말 그대로다.

내가 강해지는 것에 비례하여 일섬의 위력 역시 기하급수적으로 상승했다.

무림에서는 천무지체(天武肢體)로 오해받을 정도로 완벽에 가까운 이 육체조차 더는 감당하지 못할 만큼.

‘빌어먹을.’

어지럽다. 숨이 가쁘다.

이미 지친 수준을 넘어 망가져 버린 육체는 비명을 내지르고, 사막처럼 메마른 단전은 내게 그만 멈춰 줄 것을 호소한다.

손가락 하나 까딱할 수 없을 정도로 치명적인 여파.

하지만 이런 상황조차 예상하지 못했다면, 대뜸 일섬부터 날리는 미친 짓은 처음부터 시도도 하지 않았다.

‘인벤토리 오픈. 소환.’

생각과 동시에 시스템에 적용된 명령어가 작동한다.

흐릿한 시야 속에서 불쑥 나타난 실루엣과 함께, 누군가의 퉁명스러운 목소리가 머릿속에서 울려 퍼졌다.

- 꼴이 말이 아니군. 네놈에게 딱 어울리는 모습이야.

저 싸가지 없는 말투가 이렇게 반갑게 느껴질 줄이야.

고통스러운 와중에도 히죽 웃는 나를 보며 혀를 찬 스켈레톤 킹이, 작은 크리스털 병을 입에 쑤셔 박았다.

오직 이 세상에서만 사용할 수 있는 해결책.

최상급 포션이라 불리는 바로 그 보물을.

꿀꺽.

그리고 힘겹게 목울대를 넘긴 순간, 청량한 기운이 신체 구석구석으로 퍼져나갔다.

띠링.



- [최상급 포션]을 사용하셨습니다!

- 모든 상태 이상이 해제되었습니다!



텅 비었던 단전이 가득 차오른다. 끊어졌던 근육이 이어지고, 흐릿하던 시야는 맑고 또렷해졌다.

레벨 업에 버금가는 엄청난 치유력.

그러나 뒤이어 들려온 경고음은 나조차도 예상치 못했던 것이었다.

삐빅!



- 특수 디버프, [망가진 신체]가 효력을 거부합니다!

- 해당 디버프는 인위적인 방법으로 제거할 수 없습니다!

- [망가진 신체]의 디버프 효과가 유지됩니다!



‘……이게 무슨.’

처음 겪는 상황에 잠시 당황했지만, 저 경고음의 의미를 곱씹어볼 여유 따위는 없었다.

아직 이 전투는 끝나지 않았으니까.

그어어어어어어!

수중에서도 똑똑히 들을 수 있는 포효.

바다 깊숙이 가라앉은 무수한 잔해와 시신들로도 가리지 못한 레비아탄의 거대한 동체는 고통으로 몸부림치고 있었다.

콰과과광!

상당한 거리였지만 레비아탄의 상태는 한눈에 보기에도 끔찍했다.

과거 한 입으로 항공모함을 토막 냈다던 아가리가 한쪽 눈과 함께 절반이나 뜯겨 나갔고, 가죽과 뼈가 사라진 옆구리에서 쏟아지는 녹색 핏물은 반경 수백 미터를 잠식한 상황.

그러나 그것만으로도 놈에게는 천운이었다.

만약 마지막 순간 놈이 본능적으로 고개를 틀지 않았다면, 그리고 이곳이 수중이 아니라 육지였다면 이미 진작 최후를 맞이했을 테니까.

‘일격으로 끝냈어야 했는데.’

아쉬웠지만 어쩔 수 없었다.

상대는 바다의 재앙이라 불리는 레비아탄.

똥개도 앞마당에서는 한 수 접고 들어간다는데, 바다에서 태어나 지배자로 군림해온 놈을 물속에서 상대하는 것은 아크 리치 때보다 몇 배나 까다로웠다.

하지만…….

‘죽인다. 반드시.’

촤아아악!

나와 스켈레톤 킹은 동시에 쏘아졌다. 거센 물살이 앞을 가로막았지만 아무런 장애물도 되지 못했다.

나는 투명한 물갈퀴가 달린 손으로 창대를 굳게 말아쥐었다.

몇 달 전, 동정호에서의 퀘스트를 완료하고 얻은 [수상 구조대원]의 칭호 효과.

한번 발동 시 24시간 동안만 유지 가능한데다 내가 익힌 [열양지기]의 상성으로 인해 모든 위력이 20퍼센트나 감소 되는 막대한 패널티가 있지만, 그 모든 걸 감수할 만큼 효과는 확실했다.

쐐애애액!

마치 육지에서 경신법을 펼친 것과 같은 속도.

고통으로 울부짖던 레비아탄이 빠르게 가까워지는 우리를 발견하고 포효했다.

- 그아아아아!

놈이 반쯤 뜯겨 나간 아가리를 한껏 벌린 그 순간.

콰륵, 콰르르륵!

물살의 흐름이 바뀌었다. 바람 한 점 없는 수중임에도 불구하고 주위의 모든 것이 토네이도에 휩쓸린 것처럼 놈의 아가리를 향해 빨려 들어갔다.

그야말로 재해(災害)와도 같은 한 장면.

하지만 나는 멈추지 않았다. 오히려 근처의 잔해를 밟고 박차듯 속도를 높였다.

신화 속 괴물을 향해. 그곳에서 꿈틀거리는 강대한 마력을 향해.

그리고 다음 순간.

고오옹.

레비아탄을 중심으로 몰려들던 물살과 잔해가, 거대한 파동과 함께 터져 나왔다.

콰아아아아아!

과거 존재했다던 드래곤의 브레스(Breath)가 이런 느낌이었을까.

엄청난 마력을 머금은 물의 파동은 막아서는 모든 것을 지우며 쏘아졌다.

- 간악한 인간이여!

등 뒤에서 들려오는 스켈레톤 킹의 다급한 외침.

하지만 나는 녀석의 부름에 대답하지 않았다.

대신 충만하게 차오른 하단전의 공력을 끌어올려 백염의 창날에 꺼지지 않는 화염을 심었다.

치이이익!

사방으로 퍼져나가는 뜨거운 열기.

휘몰아치던 급류와 압력이 녹아내리듯 사라진다. 바다가 품고 있던 냉기 대신 용암과도 같은 기운이 주위를 지배했다.

적어도 지금 이 순간. 이 공간은 나만의 것이었다.

다른 무엇도 침범할 수 없는.

‘벤다.’

머릿속을 지배한 그 일념(一念)과 함께, 나는 창날을 내리그었다.

뱀처럼 뻗어 나간 청백색의 화염이 코앞까지 들이닥친 거대한 파동을 후려쳤다.

아니, 베었다.

서걱!

정확히 반으로 쪼개진 파동이 양옆으로 흩어진 그 순간. 나는 볼 수 있었다.

경악으로 부릅뜬 레비아탄의 눈동자를.

그리고 저 멀리에서 오싹한 기운을 흩뿌리는 무언가를 향해, 믿을 수 없는 속도로 헤엄쳐 가는 거대한 동체를.

‘마정석!’

이제야 알 것 같았다. 장장 수십여 년간 자취를 감추었던 괴물이 왜 갑작스럽게 모습을 드러낸 것인지. 무엇이 놈을 이 열도까지 이끌었는지.

- 막아!

스켈레톤 킹이 비명 같은 외침과 함께 손을 뻗었다.

나무가 자라듯 솟구친 뼈마디가 내 발끝을 힘차게 밀어 냈다.

퍼엉!

먹먹한 파공음과 함께 쏘아지는 신형. 거센 물살을 가르며 놈을 향해 다가가던 그때.

그아아아. 콰지직!

악어를 닮은 아가리가 커다란 잔해를 집어삼켰다.

한때 화물선이었던 철골과 무너진 건물의 콘크리트 더미. 그리고 그에 비하면 한없이 작지만, 그 무엇보다 위험한 기운을 간직한 어떤 것도 함께.

으적.

모든 것을 한입에 씹어 삼킨 레비아탄이 고개를 돌렸다.

두려움과 비웃음이 뒤섞인 눈동자로 가까워지는 날 응시하던 놈은, 지금껏 본 적 없는 엄청난 속도로 헤엄쳐 나아갔다.

나나 스켈레톤 킹을 향해서가 아닌, 자신이 왔던 넓은 바다를 향해.

- 기운을 흡수하기까지는 시간이 걸린다! 그 전에 놈을 죽여!

나는 스켈레톤의 외침을 들으며 백염을 역수(逆手)로 쥐었다.

놈과 나 사이의 거리는 고작 백여 미터.

그러나 [수상 구조대원]의 칭호 효과가 아무리 뛰어나도, 레비아탄의 속도를 따라잡을 수는 없다.

‘한 번. 단 한 번만.’

남은 공력을 모조리 끌어모아 창날에 실었다.

‘이번에는…… 반드시 끝낸다.’

온 정신을 집중했다. 물의 흐름을 느끼고, 호흡을 가라앉혔다. 모든 신경과 근육이 올올이 살아나 손끝과 어깨를 향해 실리는 듯한 기분.

꾸구구국.

그리고 전신의 핏줄이 도드라진 그 순간.

팽팽하게 당겨진 활시위를 놓는 것처럼, 나는 한 자루의 창을 온 힘을 다해 쏘아 보냈다.

콰아아아아아!

깊은 수심을 가로지르는 한 줄기의 화염.

그러나 그 끝에, 괴수의 비명은 없었다.
```

## Final English reading copy

```markdown
# Chapter 749

Leviathan was both the calamity and the king of the sea.

That was true in the Demon Realm and on Earth alike.

The sea was Leviathan’s birthplace and undefeated battlefield, and within this vast territory granted to it at birth, there was nothing that could escape the king’s watch.

Yes, that was certainly how it should have been.

*Fwoooooosh!*

In the blink of an eye, the monster’s movement stopped with its prey before it, greed filling its thoughts. At the same time, Leviathan’s senses, numbed by its long starvation, awakened.

*What is this?*

When had it begun?

As realization dawned and the world slowed around it, Leviathan could see and feel everything clearly.

A mighty force, swift as lightning and carrying the heat of the sun.

The flames plunging down and swallowing the blue surface were headed straight for it.

*Splaaash!*

There was no time left to hesitate.

The enormous maw it had opened to swallow its prey turned sharply underwater.

A moment later, Leviathan crushed the flames with hundreds of teeth imbued with magical power.

No—it had believed, without the slightest doubt, that it could.

*Krrrk!*

That was what it believed until the instant the flames and its teeth collided, bringing a violent impact that shook its head.

*Krrrrrrk!*

—…!

What?

Leviathan’s enormous eyes widened in pain and shock.

The teeth that had sunk dozens of aircraft carriers during the Great Cataclysm—teeth so sharp and destructive that they were weapons in their own right—had been shattered in a single strike.

*How? How is this possible?*

Leviathan froze, caught in an unanswered question.

Then the countless bubbles stirred up by the collision scattered, revealing the cause of all its confusion.

A spear.

*Gooooong.*

The silver spear was wrapped in flames that refused to go out even amid the water and waves, and it trembled faintly.

As though it were a living creature.

As though it liked the touch of the hand holding it.

And flowing through the owner of that spear was the blood of a species Leviathan had killed countless times.

—How can a mere human…!

At the cry of the mythical beast, filled with undisguised astonishment, the small and insignificant human answered by merely moving his lips.

One Annihilation.

A distant flash of light dyed the sea.

* * *

People often say that life comes down to one big shot.

I agree—especially because when you go for that one shot, it can be the very shot that costs you your life.

*Rrrrrumble!*

A thunderous roar, as if the sky—or rather, the sea—were splitting apart.

At the same time, a tremendous shock wave sent my body flying after I had expended every ounce of strength.

Swept up in a whirling current, I could hear warning sounds ringing out endlessly through my fading vision.

*Beep. Beep-beep!*

> **System**
>
> - You have exhausted all your internal energy and stamina!
>
> - Your body cannot withstand the recoil of **One Annihilation**!
>
> - Status abnormality, **Internal Energy Depletion**, has been applied!
>
> - Status abnormality, **Exhaustion**, has been applied!
>
> - Status abnormality, **Anemia**, has been applied!
>
> - Status abnormality, **Muscle Tear**, has been applied!
>
> - Status abnormality, **Internal Injury**, has been applied!
>
> - Warning! Warning! Remember that every action comes with a price!
>
> - Excessive abuse of power may return as a blade turned against you.
>
> - Special debuff, **Broken Body**, has been applied!
>
> - All combat-related attributes decrease by 50 until recovery! Depending on the recovery process and its results, you may permanently lose some attributes!
>
> - **Strength** temporarily decreases by 50!
>
> - **Agility**…

.

.

.

High risk, high return.

That was exactly what it meant.

As I grew stronger, the power of One Annihilation had risen exponentially as well.

It had risen to the point that even this nearly perfect body—which people in Murim might mistake for a Heavenly Martial Physique—could no longer withstand it.

*Damn it.*

I was dizzy. My breathing was ragged.

My body had gone beyond exhaustion and fallen into ruin, screaming in agony, while my dantian, dry as a desert, begged me to stop.

The aftermath was severe enough that I could not even move a finger.

But if I had not anticipated a situation like this, I would never have attempted something as insane as firing One Annihilation in the first place.

*Open Inventory. Summon.*

The command entered into the System activated the instant I thought it.

Along with a silhouette that abruptly appeared in my blurred vision, someone’s curt voice rang out inside my head.

—You look awful. It’s a perfect look for you, you bastard.

I never thought that rude tone would sound so welcome.

Seeing me grin despite the pain, the Skeleton King clicked his tongue and shoved a small crystal bottle into my mouth.

A solution that could be used only in this world.

The treasure known as a Top-Grade Potion.

*Gulp.*

The instant I finally forced it down my throat, a refreshing energy spread through every corner of my body.

*Ding!*

> **System**
>
> - You have used **Top-Grade Potion**!
>
> - All status abnormalities have been removed!

My empty dantian filled to the brim. My torn muscles knitted back together, and my hazy vision became clear and sharp.

Its healing power was comparable to a Level Up.

But the warning that followed was something even I had not expected.

*Beep!*

> **System**
>
> - The special debuff, **Broken Body**, rejects the effect!
>
> - This debuff cannot be removed by artificial means!
>
> - The effects of **Broken Body** remain active!

*…What the hell?*

I was briefly flustered by the situation I had never experienced before, but I had no time to dwell on what the warning meant.

The battle was not over yet.

*Grrrrrrrrrrr!*

A roar that could be heard clearly even underwater.

Leviathan’s enormous body, impossible to hide even among the countless wrecks and corpses sunk deep beneath the sea, writhed in pain.

*KABOOOOOM!*

Though it was some distance away, Leviathan’s condition was horrifying at a glance.

The maw said to have once torn an aircraft carrier to pieces with a single bite had been ripped halfway off, along with one eye. Green blood poured from its flank, where the hide and bones had vanished, spreading across a radius of several hundred meters.

But even that was incredibly fortunate for the monster.

If it had not instinctively turned its head at the last moment—and if this had been land instead of underwater—it would have met its end long ago.

*I should have finished it with one strike.*

It was regrettable, but there was nothing I could do.

My opponent was Leviathan, the calamity of the sea.

They say even a stray dog gets the home-field advantage in its own yard, and fighting a creature born in the sea and ruling over it was several times more difficult underwater than fighting the Arch Lich.

But…

*I’ll kill it. I have to.*

*Splaaaaash!*

The Skeleton King and I shot forward at the same time. The powerful current blocking our path was no obstacle at all.

I wrapped my hand, fitted with transparent webbing, tightly around the spear shaft.

This was the effect of the **Water Rescue Worker** Title I had obtained after completing the Quest at Dongting Lake a few months ago.

Once activated, it lasted for only twenty-four hours. Worse, because it clashed with the **Scorching Yang Qi** I had learned, all my power was reduced by a full twenty percent.

Even so, the effect was worth every drawback.

*Fwoooooosh!*

I moved as quickly as though I were using a movement technique on land.

Leviathan, howling in pain, spotted us closing in and roared.

—GRAAAAAAAH!

The instant it opened its half-torn maw as wide as it could—

*Krrrk. Krrrrrk!*

The flow of the water changed.

Even though there was not a breath of wind underwater, everything around us was sucked toward Leviathan’s maw as if caught in a tornado.

It was a scene worthy of a disaster.

But I did not stop. Instead, I stepped on a nearby piece of wreckage and kicked off it, accelerating even further.

Toward the mythical monster.

Toward the powerful magical power writhing within it.

And then—

*Gooooong.*

The water and wreckage gathering around Leviathan burst outward in a massive wave.

*KRAAAAAAAASH!*

*Was this what the Breath of the dragons said to have once existed felt like?*

The wave of water, filled with tremendous magical power, shot forward, erasing everything in its path.

—You treacherous human!

The Skeleton King’s desperate shout came from behind me.

But I did not answer him.

Instead, I drew up the internal energy filling my lower dantian and embedded an undying flame into the blade of White Flame.

*Sssssss!*

Scorching heat spread in every direction.

The raging current and pressure melted away as though they had never existed. In place of the chill held by the sea, an energy like molten lava dominated the surroundings.

At least for this moment, this space belonged to me alone.

Nothing else could intrude.

*Cut.*

With that single thought dominating my mind, I brought down the spearhead.

Blue-white flames, stretching forward like a snake, lashed at the enormous wave that had reached the space directly before me.

No.

They cut it.

*Shhk!*

The wave split precisely in half and scattered to either side.

In that instant, I saw Leviathan’s eyes widen in shock.

And I saw its enormous body swimming away at an unbelievable speed toward something in the distance, something scattering a chilling energy.

*The Magic Gem!*

I finally understood.

Why the monster that had disappeared for decades had suddenly revealed itself.

What had drawn it to this archipelago.

—Stop it!

The Skeleton King thrust out a hand with a scream.

Bones rose upward like a growing tree and forcefully pushed against the tips of my feet.

*Bang!*

My body shot forward with a dull boom, and I advanced toward Leviathan, cutting through the powerful current.

*GRAAAAAH! KRRRUNCH!*

Its crocodile-like maw swallowed a massive piece of wreckage.

Steel beams that had once been a cargo ship.

A pile of concrete from a collapsed building.

And along with them, something infinitely smaller by comparison, yet carrying an energy more dangerous than anything else.

*Crunch.*

Leviathan chewed and swallowed everything in a single bite before turning its head.

It watched me draw closer with eyes that held both fear and mockery, then swam away at a speed I had never seen before.

Not toward me or the Skeleton King, but toward the vast sea from which it had come.

—It’ll take time for it to absorb the energy! Kill it before then!

Hearing the Skeleton King’s shout, I gripped White Flame in reverse.

The distance between Leviathan and me was barely a hundred meters.

But no matter how powerful the effect of the **Water Rescue Worker** Title was, I could not catch up to Leviathan’s speed.

*Once. Just once.*

I gathered every bit of internal energy I had left and poured it into the spearhead.

*This time… I’ll finish it. I have to.*

I focused all my attention.

I felt the flow of the water and calmed my breathing. Every nerve and muscle throughout my body seemed to awaken one by one, gathering toward my fingertips and shoulder.

*Krrrrrk.*

Then, at the instant the veins across my entire body stood out—

Like releasing a tightly drawn bowstring, I hurled the spear forward with every ounce of strength I possessed.

*KRAAAAAAAASH!*

A single line of flame streaked across the deep water.

But there was no monster’s scream at the end of it.
```
