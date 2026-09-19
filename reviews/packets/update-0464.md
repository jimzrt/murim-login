<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0464.txt",
      "sha256": "0f9220dfb91a4e73bae6f1dab1560a13af8b037b0e22f2a28d223f895d5934bf",
      "bytes": 12707
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1131f401b1398b8b070071f675ed555089019cad46ba771c09c5ea825bf3f9c0",
      "bytes": 4052
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "862df6cb65a5d58ddaca1039c8edb3289f7c6f72c9015f740ff83eb847dc35d9",
      "bytes": 150883
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f22cda277e8c2e73c34259d01befc2bfd58520c40832c672549c7d1032ee945c",
      "bytes": 553
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "a5e2ca148b0685356c8a4d3b27146d786d6095abc522e606651e792aea144538",
      "bytes": 703
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "923e9d1f3656684e7c794faaac8a93a7a41defa2795e3725f6fe7df610e1b0b7",
      "bytes": 146076
    }
  ],
  "estimated_tokens": 9281
}
-->

# Durable State Update — Chapter 464

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 464. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 464. Profile updates may replace only one
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
  "chapter": 464,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 464,
    "continuity_sources": [464],
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
    "Taekyung completed the unavoidable Peak-grade Quest The Tragedy of Dongting Lake, rescued the only two survivors found, and earned the Water Rescue Worker Title.",
    "Honglan survived the Dongting Lake disaster and is recovering; Ju Wongong remains unconscious under guard after passing the most dangerous stage of his injuries.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed with more than a thousand casualties, while the perpetrators' wider plans remain unknown.",
    "The Dongting Fisherman is a previous-generation Supreme Peak water-arts master suspected of Dark Heaven involvement and the Dongting Lake attack; the Hidden Shadow Ghost is the local name for an unseen killer of boatmen who may be connected to him.",
    "Four of five suspected Dongting Fisherman refuges were searched without results; Taekyung reached the final, deepest site and discovered an underwater cave while attempting to capture him alive.",
    "Zhuge Clan and Wudang are searching Donghu Stronghold for Dark Heaven traces; Mungyeong found no land evidence or Moving Formation remnants and entered the river to search the remaining area.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings."
  ],
  "continuity_sources": [
    463,
    462
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What is the Dongting Fisherman's exact role in Dark Heaven, is he the Hidden Shadow Ghost, and what is inside the final underwater cave?",
    "What danger did Mungyeong detect, and is it connected to Taekyung, Jeok Cheongang, or Dark Heaven?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?"
  ],
  "safe_through": 463,
  "temporary_decisions": [
    "Render 오기조원 as Five Qi Returning to Origin, 노화순청 as Furnace Fire Pure Blue, 반로환동 as Returned to Youth, and 복자 as diviner.",
    "Render 살귀 as killer demon, 은영귀 as Hidden Shadow Ghost, 일급 낭인 as First Rate wandering martial artist, 삼괴 as Three Fiends, 대마두 as great fiend, and 마군 as Demon Lord.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor; render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, 사인교 as four-person sedan chair, 홍란 as Honglan, 가기 as singing courtesan, 구족 as the nine branches of kin, 수상 구조대원 as Water Rescue Worker, and 수공 as water arts.",
    "Render 익양루 as Yiyang Tower, 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, 사천혈사 as Sichuan Blood Tragedy, and 천령폭 as Tianling Falls."
  ],
  "version": 1
}
```

## Exact glossary matches

| 하오문    | **Lower District Sect**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 칭호               | **Title**                      |
| 장비               | **Equipment**                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 야명주 | **night-shining pearls** | Pearls embedded in the cavern ceiling that provide light. |
| 화룡갑 | **Fire Dragon Armor** | Jin Taekyung's renamed bound armor, formerly the Black Dragon Armor. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 수공 | **water arts** | Water-based martial arts; the Dongting Fisherman's specialty. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 463
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 463
- **Aliases:** None
- **Role:** The Dongting Fisherman is a previous-generation Supreme Peak master whose water arts rival the Seafaring King; he is identified as Dark Heaven's tail and suspected perpetrator of the Dongting Lake attack, with hidden refuges throughout the lake.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

## Korean source

```text
＃464화



동정호는 엄연한 호수지만 전체 면적만 따져도 천 리요, 가장 얕은 곳의 수심도 십여 장을 우습게 넘긴다.

특히나 지금 내가 헤엄치고 있는 곳은 그런 동정호에서도 가장 깊숙하다고 할 수 있는 지점. 수심이 훨씬 더 깊고 물살이 파도처럼 거센 것은 당연했다.

이러한 상황에서 자그마한 동혈(洞穴)을 발견할 수 있었던 것은 그야말로 천운에 가까운 일이었다.

‘저건…….’

무리를 지어 헤엄치는 수많은 물고기들 사이로, 장정 하나가 간신히 지나갈 법한 틈이 보인다.

동시에 짜릿한 무언가가 등골을 타고 흘렀다.

‘찾았다.’

강바닥 깊숙이 뿌리내린 절벽이 오랜 세월 동안 퇴적과 침식에 의해 벌어지는 것은 당연한 현상이다. 앞서 들른 네 곳의 장소에서도 몇 번이나 본 적이 있을 정도로.

하지만 이번에는 다르다.

늘 따로 놀던 이성과 본능이 한목소리로 속삭이고 있었다.

‘동정어옹의 비처.’

모든 것은 흔적을 남기는 법.

비록 아주 은밀하고도 미세한 차이였지만, 나는 지금까지 쌓인 경험과 예리한 안력을 통해 서서히 가까워지는 저 동혈의 입구에 사람의 흔적이 닿았음을 알 수 있었다.

‘입구 언저리가 매끈하다. 누군가 인위적으로 손을 댄 것이 분명해.’

바로 그 누군가의 정체는 물어보나 마나다.

전신의 감각을 극도로 끌어올린 나는 물살을 가르며 나아갔다. 천천히. 그리고 조심스럽게.

곧 생사결을 펼쳐야 하는 적에게 벌써부터 내 존재를 알리는 것은 멍청한 짓이다.

놈이 대비한다면 전세는 더욱 불리해질 테니까.

‘다행히 아직 칭호 효과의 지속 시간은 많이 남았어. 서두르지 말자.’

십 분 빨리 가려다가 오십 년 일찍 가는 사람들을 여럿 봤다.

죽느냐, 사느냐는 그 사람의 의지와 끈기에 달린 것. 나는 서두르지 않고 물의 흐름에 몸을 맡겼다.

스륵.

나를 발견한 형형색색의 물고기들이 머뭇거리는 듯싶더니, 이내 조심스럽게 내 주위를 스쳐 지나간다.

움직임이 거의 없다 보니 자신들에게 위협이 될 만한 존재라고 느끼지 못한 것이 틀림없었다.

‘좋아.’

지척에 있는 물고기가 이렇듯 착각할 정도라면 충분하다. 나는 더욱 기척을 죽이며 동혈을 향해 다가갔다.

성인 남성 하나가 간신히 들어갈 법한 크기의 입구 앞에서 작게 심호흡한 뒤 몸을 들이밀자, 숨겨져 있던 또 다른 수중 통로가 드러났다.

‘우선 느껴지는 인기척은 없고.’

입구만큼이나 좁은 통로는 생각 이상으로 깊고, 길었다.

어느 때보다 예리한 감각을 끌어올려 내부의 기척을 살핀 나는 확신이 들고 나서야 다시 이동을 시작했다.

괴상하게 생긴 물고기 몇 마리와 수중 식물을 지나쳐 얼마나 나아갔을까. 저 멀리서부터 가까워지는 희미한 빛이 있었다.

‘잠깐, 빛?’

이곳은 동정호의 물속이지만, 절벽 내부의 통로이기도 하다. 그런데 난데없이 빛이라니.

통로가 비스듬히 위를 향하고 있긴 했어도 빛이 샐 만한 구조는 절대 아니다.

‘그렇다면…….’

부드럽게 빛을 향해 유영한 나는 재차 주위를 탐색하고 나서야 통로 위로 난 작은 구멍을 향해 솟아올랐다.

촤악.

“후읍.”

폐부 깊숙이 스며드는 축축한 공기.

그와 동시에 인두부(咽頭部) 어림에 생성되어 있던 투명한 아가미가 사라지는 것이 느껴졌다.

그리고 다음 순간, 물에서 빠져나와 비로소 희미한 빛의 정체를 확인한 나는 눈을 크게 떴다.

‘야명주(夜明珠).’

그곳은 동굴이었다.

저 멀리까지 뻗어 있는 길은 좁고 컴컴했으며, 간신히 허리를 펼 수 있을 만한 높이의 천장에는 크고 작은 야명주 여러 개가 일정 간격으로 점점이 박혀 있었다.

‘절벽 안에 만들어진 수중 통로와 동굴. 그리고 야명주까지…… 이 정도면 모르는 게 병신이지.’

하오문의 정보가 맞았다. 이곳은 틀림없는 동정어옹의 비처다.

마침내 놈을 찾았다는 짜릿함과 곧 벌어질 전투에 대한 긴장감으로 가슴이 쿵쿵 뛰었다.

아니, 비단 그런 감정 때문만은 아니었다.

‘저건.’

코끝을 파고드는 이질적인 냄새를 따라 고개를 돌린 나는 볼 수 있었다.

물이 고인 동굴바닥에 엎어져 있는 나무토막과 물 위에 둥둥 떠 있는 기름을.

‘횃불? 하긴, 야명주가 무한한 건 아니니까.’

동굴 천장에 박힌 야명주는 척 봐도 하급의 품질이지만, 그렇다고 해서 가격까지 하급인 것은 아니다.

동정어옹이 갑부라는 이야기는 듣지 못했으니 이 긴 동굴을 밝히기 위해서는 횃불의 역할이 필수였을 것이다.

그리고 저 반쯤 타들어 간 횃불은 내게 중요한 사실을 알려 주었다.

‘꺼진 지 얼마 되지 않았어.’

나무토막으로부터 느껴지는 미약한 온기. 기껏해야 한 두 시진 전쯤 모종의 이유로 횃불이 쓰러졌다는 걸 어렵지 않게 유추할 수 있었다.

이와 같은 상황이 가리키는 한 가지 사실 역시도.

‘동정어옹은 분명 이곳에 있다!’

결국 내가 찾고자 하는 것은 장소가 아닌 사람이다. 만일 비처를 찾았다 해도 동정어옹이 없다면 아무런 소용도 없다.

하지만 동정어옹은 횃불을 통해 자신의 존재를 알려 주었다.

내가 놈의 입장이라 했을지라도 이토록 은밀히 숨겨진 비처에 침입자가 들어올 줄은 몰랐을 것이다.

‘그게 네놈의 실수고.’

몸을 일으킨 나는 천천히 눈 앞에 펼쳐진 길을 따라 걷기 시작했다.

애병이라 할 수 있는 백염이나 화룡갑, 만독지환 등 성능 좋은 장비들이 수두룩하지만 지금은 꺼낼 때가 아니다.

오히려 빈손이라는 걸 보여 줌으로써 상대방의 방심을 끌어내고, 인벤토리를 이용한 이점을 취하는 편이 낫다.

똑, 또독.

천장에서 불규칙적으로 떨어지는 물방울 소리를 들으며, 나는 한껏 기척을 죽인 채 걷고 또 걸었다.

처음에는 일직선이었던 길이 구불구불해지고, 오르막길이나 내리막길이 나오기도 했지만 경계를 풀지는 않았다.

‘그런데…… 도대체 이 흔적들은 뭐지?’

이상함을 느끼기까지는 그리 오랜 시간이 필요하지 않았다.

내 눈썰미가 예리한 것도 있었지만, 통로의 상태가 그만큼 심상치 않은 탓이었다.

군데군데 부서지고 깨진 벽면과 불쑥 튀어나온 바위. 녹색 이끼가 가득 끼어 있는 다른 곳과 달리 새로 깨져 나간 자리는 확연하리만치 눈에 띄었다.

투두둑.

손을 대자 곧바로 떨어져 내리는 벽면의 일부분.

‘이건 작정하고 힘을 가하지 않는 이상 불가능한 일인데.’

이 동굴 전체는 적게 잡아도 수백 년간 축적된 단단한 암석들로 이루어져 있다.

그런 만큼 상당한 공력을 실어 타격을 가해야 하는데…… 동정어옹이 자신의 소중한 보금자리를 스스로 부술 만한 이유가 있을까?

‘혹시 이곳에서 전투가……. 아니, 아니야. 이건 분명히 한 사람의 흔적이다.’

무공의 정체와 뿌리를 읽어 낼 만한 안목은 한참 부족하지만, 곳곳에 남긴 흔적을 통해 상황을 유추하는 것은 초절정의 경지에 도달한 내게 있어 그리 어려운 일이 아니다.

잠시 미간을 좁힌 채 골똘히 생각에 잠겨 있던 나는 고개를 내저었다.

‘우선 동정어옹에 집중해야 해. 섣부른 방심도, 과한 긴장도 금물이야.’

그렇게 끊임없이 마음속으로 되뇌며 걸음을 옮기던 그 순간이었다.

철벅, 촤악!

“……!”

갑자기 들려온 소리에 찬물을 뒤집어쓴 사람처럼 정신이 번쩍 들었다.

전신으로부터 활짝 열린 감각이 소리를 분석하고, 이내 새로운 정보를 뇌 쪽으로 흘려보냈다.

‘오십여 장 앞. 생각보다 가깝다.’

거기에 더해 소리가 유독 깊고 크게 울린다. 지금 내가 걸어가고 있는 이 좁은 동굴 통로가 아닌, 더욱 넓은 공간이 있다는 뜻이다.

스윽.

한 걸음. 그리고 또 다시 한 걸음.

발끝에 모든 신경을 기울여 축축한 동굴 바닥을 밟았다.

미리 열양지기를 이용해 흠뻑 젖어 있던 물기를 말려서 천만다행이다. 몸에서 떨어진 물기가 바닥에 떨어져 소리를 냈다면 놈에게 정체를 들키고 말았을 것이다.

‘반드시 이 동굴에서 끝내야 해. 수중에서 싸운다면 훨씬 힘들어진다.’

상대는 천하에서 손에 꼽히는 수공(水功)의 초절정 고수다.

내 무위에 자신이 없는 것은 아니지만, 동정어옹과 수중에서 싸우게 된다면 시스템이 알려 준 20%의 위력 감소를 고스란히 떠안아야 한다.

하지만 이곳은 단단한 지면이 있는 엄연한 육지이고, 그러니 디버프 역시 당연히 없었다.

‘이 기회를 놓칠 수는 없지.’

그사이에도 오십여 장의 거리는 빠르게 좁혀졌다.

첩, 추와악.

계속해서 들려오는 알 수 없는 소리는 거리와 방향을 실시간으로 알려 주는 훌륭한 이정표였고, 나는 꺾어지는 동굴의 통로에서 전신의 근육을 이완시켰다.

이미 준비는 끝났다. 어떻게 움직여서 어떤 식으로 끝장낼지 수십여 가지의 이미지가 눈앞을 스친다.

만약 동정어옹이 버거운 상대라면 온 힘을 다해 죽일 것이고, 그렇지 않다면 사로잡아 더 큰 몸통을 끌어내야 한다.

‘단숨에, 벼락처럼 끝낸다.’

짧은 호흡과 동시에, 나는 단전 깊숙이 잠들어 있던 화룡을 깨웠다.

계속해서 운기를 통해 채워 넣은 삼 갑자의 열양지기가 전신의 사지 백해로 흘러들었다.

수백 개의 혈도와 기경팔맥(奇經八脈)에 뜨거운 열기를 불어넣고, 모든 신체 능력을 극대화시켰다.

그리고…….

팟!

단 한 걸음이면 족했다.

비스듬히 꺾여 있는 벽면을 부드럽게 밟으며 나는 쏘아졌다.

동굴의 중심부로 추정되는 반경 삼십여 장의 공간. 등을 돌린 채 쭈그려 앉은 백발의 노인을 향해.

‘동정어옹!’

소리 없는 부르짖음이 내 안에서 울려 퍼진다.

저 작고 초라한 뒷모습을 한 늙은이가 수많은 사람을 해쳤다는 것이 믿기지 않았고, 잠시 묻어 두었던 분노가 차가운 불꽃이 되어 솟구쳤다.

‘인벤토리 오픈, 소환!’

느려진 세상 속, 동정어옹을 향해 쇄도하는 내 전신에 시스템이라는 미지의 힘이 덧입혀졌다.

스륵, 턱.

벌거벗고 있던 상체를 감싸는 붉은 갑옷, 화룡갑(火龍鉀).

이어 오직 나만이 볼 수 있는 빛무리가 손가락을 스침과 동시에 만독지환(萬毒指環)이라는 신물의 형태로 변화하고, 투명한 창날을 지닌 창 한 자루가 손아귀에 잡힌다.

그리고 다음 순간, 삼 갑자에 달하는 열양지기가 그 모든 것들에 스며들었다.

쏴아아아악!

축축한 공기가, 바닥에 고여 있던 강물이, 머리 위로 떨어져 내리던 물방울이 사라졌다. 아니, 증발했다.

백염(白炎)의 투명한 창날 위로 들불처럼 일어난 청백색의 강기는 막아서는 모든 것들을 태우며 나아갔다.

그 뜨겁고도 파괴적인 기운의 집약체가 향하는 곳에, 한 사람이 있었다.

‘죽어라.’

화살은 쏘아졌고 잠시 둥지에 앉아 쉬고 있던 새는 피할 수 없을 것이다.

내게는 동정어옹이 바로 그 새나 다름없었다.

자신의 둥지가 안전하다고 믿었던 새.

뒤늦게 깨달았다 해도 이미 쏘아진 화살을 막을 수는 없다.

새가 황급히 날개를 펼친다 한들, 죽거나 다치는 결과는 피할 수 없을 것이다.

바로 지금, 아주 느릿하게 신형을 돌리는 동정어옹처럼.

‘이미 늦었어.’

하지만 다음 순간, 나는 깨달았다.

섣부른 확신은 금물이었음을.

쾅!

어디선가 날아온 새하얀 빛줄기가, 백염의 창날을 후려쳤다.
```

## Final English reading copy

```markdown
# Chapter 464

Dongting Lake was unquestionably a lake, but its total area alone stretched for a thousand *li*, and even its shallowest points easily exceeded a dozen *zhang* in depth.

The place I was swimming through now was one of the deepest parts of Dongting Lake. Naturally, the water was much deeper here, and the current raged like waves.

Finding a small underwater cave under these circumstances was practically an act of heaven’s grace.

*That’s…*

Amid countless fish swimming in schools, I spotted a gap barely wide enough for a full-grown man to squeeze through.

At the same time, a thrill ran down my spine.

*I found it.*

Cliffs rooted deep in a riverbed naturally split apart over the years through sedimentation and erosion. I had seen it several times at the four places we had already visited.

But this time was different.

My reason and instinct, which usually went their separate ways, were whispering the same thing.

*The Dongting Fisherman’s secret refuge.*

Everything left traces.

Though the difference was extremely subtle and well hidden, my accumulated experience and keen eyes told me that human hands had touched the entrance of the cave slowly drawing closer.

*The edges of the entrance are smooth. Someone definitely worked on them.*

There was no need to ask who that someone was.

I heightened every one of my senses to their limit and cut through the current.

Slowly. Carefully.

It would be stupid to announce my presence to an enemy with whom I would soon be locked in a life-and-death duel.

If he prepared himself, the situation would become even more unfavorable.

*Fortunately, there’s still plenty of time left on the Title’s effect. No need to rush.*

I had seen plenty of people hurry to arrive ten minutes earlier, only to arrive fifty years early.

Whether a person lived or died depended on their will and perseverance. I did not hurry. I let the current carry me along.

*Swish.*

The brilliantly colored fish that noticed me seemed to hesitate, then cautiously brushed past me.

Since I was barely moving, they must not have sensed me as something that posed a threat.

*Good.*

If a fish this close could be fooled so easily, it was enough. I suppressed my presence even further and approached the cave.

I took a small breath in front of the entrance, which was just large enough for one adult man to squeeze through, then pushed my body inside.

Another underwater passage hidden beyond it came into view.

*No presence so far.*

The passage, no wider than the entrance, was deeper and longer than I had expected.

I sharpened my senses more than ever and searched the passage for any human presence. Only after I was certain there was none did I begin moving again.

I passed several strange-looking fish and aquatic plants. How far had I gone?

A faint light was approaching from far ahead.

*Wait. Light?*

This was underwater in Dongting Lake, but it was also a passage inside a cliff. How could there suddenly be light?

The passage did angle upward, but its structure left no way for light to leak in.

*Then…*

I swam gently toward the light, searched my surroundings once more, and finally shot upward toward a small hole in the ceiling of the passage.

*Splash!*

I sucked in a breath.

Damp air seeped deep into my lungs.

At the same time, I felt the transparent gills that had formed around my throat disappear.

The next moment, I emerged from the water and finally saw the source of the faint light. My eyes widened.

*Night-shining pearls.*

It was a cave.

The path stretched into the distance, narrow and dark. Large and small night-shining pearls were embedded at regular intervals across the ceiling, which was only high enough for me to barely straighten my back.

*A submerged passage and a cave carved inside a cliff. Night-shining pearls, too… At this point, you’d have to be an idiot not to know.*

The Lower District Sect’s information had been correct. This was unquestionably the Dongting Fisherman’s secret refuge.

My heart pounded with the thrill of finally finding him and the tension of the battle that would soon begin.

No. It was not just those emotions.

*That.*

I turned my head, following a strange smell that worked its way into my nose, and saw them.

A piece of wood lying facedown on the waterlogged floor of the cave, and oil floating on the surface of the water.

*A torch? Well, it’s not like he has an unlimited supply of night-shining pearls.*

The night-shining pearls embedded in the ceiling were obviously low quality, but that did not mean they were cheap.

I had never heard that the Dongting Fisherman was a tycoon, so torches must have been essential for lighting this long cave.

And that half-burned torch told me something important.

*It hasn’t been out for long.*

A faint warmth remained in the piece of wood. It was not difficult to infer that the torch had fallen for some reason only one or two *shichen* ago.

There was also one fact this situation pointed to.

*The Dongting Fisherman is definitely here!*

In the end, the person I wanted to find was not a place but a man. Even if I found his secret refuge, it would be useless if the Dongting Fisherman was not there.

But through the torch, the Dongting Fisherman had revealed his presence.

Even if I were in his position, I would never have expected an intruder to enter a secret refuge hidden this well.

*That’s your mistake.*

I rose to my feet and began walking slowly along the path stretching out before me.

I had plenty of high-performance equipment, including White Flame, which could be called my favored weapon, Fire Dragon Armor, and the Myriad-Poison Ring. But now was not the time to bring them out.

It would be better to make my opponent lower his guard by showing him that my hands were empty, then take advantage of the benefits my Inventory offered.

*Drip. Drip-drop.*

Listening to the irregular sound of water dripping from the ceiling, I walked on and on with my presence suppressed as much as possible.

The path, straight at first, began to twist. Inclines and declines appeared as well, but I never let down my guard.

*But… What are these traces?*

It did not take long for me to sense that something was strange.

My sharp eye was part of it, but the state of the passage was that abnormal.

Sections of the walls had been smashed and broken here and there, with rocks jutting out abruptly. Unlike the other places, which were covered in green moss, the freshly broken sections stood out unmistakably.

*Thud-thud.*

When I touched it, part of the wall immediately crumbled and fell away.

*This would be impossible without applying force deliberately.*

The entire cave consisted of solid rock that had accumulated over at least several hundred years.

To damage it, someone would have to strike with a considerable amount of internal energy. But was there any reason for the Dongting Fisherman to destroy his precious refuge himself?

*Could there have been a battle here…? No. No, this is definitely the trace of a single person.*

I was still far from having the insight to discern the nature and roots of martial arts, but having reached the Supreme Peak realm, I had little trouble inferring what had happened from the traces left throughout the passage.

I furrowed my brow and thought deeply for a moment before shaking my head.

*I need to focus on the Dongting Fisherman first. Careless complacency and excessive tension are both forbidden.*

I kept repeating that to myself as I continued walking.

Then it happened.

*Splash! Whoosh!*

“……!”

The sudden sound snapped me to attention like a person doused with cold water.

The senses spread wide across my entire body analyzed the sound, then sent new information flowing toward my brain.

*Fifty-odd zhang ahead. Closer than I expected.*

On top of that, the sound echoed unusually deeply and loudly. That meant there was a larger space ahead, not merely this narrow cave passage I was walking through.

*Swish.*

One step. Then another.

I focused every nerve in my toes as they touched the damp cave floor.

It was a blessing that I had used my Scorching Yang Qi beforehand to dry the water that had soaked me through. If water dripping from my body had struck the floor and made a sound, the Dongting Fisherman would have discovered me.

*I have to finish this in the cave. Fighting underwater would make things much harder.*

My opponent was a Supreme Peak master of water arts, one of the best in the world.

I had confidence in my own martial prowess, but if I fought the Dongting Fisherman underwater, I would have to bear the full twenty percent reduction in power the System had warned me about.

But this was solid ground—firm land—and that meant there was no debuff.

*I can’t let this opportunity slip away.*

The fifty-odd zhang between us rapidly narrowed.

*Tap. Whoooosh.*

The incomprehensible sound continued to reach me, serving as an excellent landmark that revealed the distance and direction in real time. As I came to a bend in the cave passage, I relaxed every muscle in my body.

I was ready.

Dozens of images flashed before my eyes, showing how I would move and how I would finish him.

If the Dongting Fisherman proved too formidable, I would kill him with everything I had. If not, I would capture him and use him to draw out the bigger player behind him.

*I’ll end it in one stroke, like a bolt of lightning.*

With a short breath, I awakened the fire dragon sleeping deep within my dantian.

The three *jiazi* of Scorching Yang Qi I had continually replenished through circulation flowed into every limb and bone of my body.

I infused hundreds of acupoints and the Eight Extraordinary Meridians with searing heat, maximizing every physical ability.

And then…

*Pop!*

One step was enough.

I gently stepped onto the slanted wall and shot forward.

A space roughly thirty *zhang* in radius, presumably the center of the cave.

Toward a white-haired old man crouching with his back turned to me.

*The Dongting Fisherman!*

A silent cry rang out within me.

It was hard to believe that this small, shabby old man had harmed so many people. The anger I had buried for a while surged up as a cold flame.

*Inventory open. Summon!*

As the world slowed, the unknown power of the System covered my entire body as I charged toward the Dongting Fisherman.

*Swish. Clack.*

Red armor wrapped around my bare upper body: Fire Dragon Armor.

Then, as a cluster of light visible only to me brushed against my fingers, it transformed into the divine treasure known as the Myriad-Poison Ring. At the same time, a spear with a transparent blade appeared in my hand.

The next moment, three *jiazi* of Scorching Yang Qi seeped into all of it.

*Whoooooosh!*

The damp air vanished. The river water pooled on the floor vanished. Even the droplets falling from above vanished.

No—they evaporated.

Blue-white Force rose from White Flame’s transparent spearhead like a wildfire, burning through everything in its path.

There was one person in the direction toward which that hot and destructive concentration of energy was headed.

*Die.*

The arrow had been fired, and the bird that had been resting in its nest would not be able to escape.

To me, the Dongting Fisherman was no different from that bird.

A bird that had believed its nest was safe.

Even if it realized the truth too late, it could not stop an arrow that had already been fired.

Even if the bird hurriedly spread its wings, it could not avoid being killed or injured.

Just like the Dongting Fisherman, who was turning his body very slowly right now.

*It’s already too late.*

But the next moment, I realized something.

I should never have been so quick to assume.

*Boom!*

A snow-white streak of light flew in from somewhere and struck White Flame’s spearhead.
```
