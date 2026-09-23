<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0807.txt",
      "sha256": "b79591b277ebe5e4d9b9e6a1dd68fc408da2954f5a247c47bbf99e911f72c0ca",
      "bytes": 13407
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f1f4cf50733f280575be375213d89335806be1998595d940695356be4097e219",
      "bytes": 1474
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1e8b8a33ae952423b359fb7c39a8c3a83fe8a43b894e38ef519681dd66dd55a7",
      "bytes": 225527
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "84be21a09ea2f4f2165746695b976cd8be8cbcc07e6fede3ad73bcfc8edbfb63",
      "bytes": 574
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b08d088bb854d874cf14b9d829212aacd492ea82ebbf8401c98f99ad170f3b7d",
      "bytes": 247557
    }
  ],
  "estimated_tokens": 8825
}
-->

# Durable State Update — Chapter 807

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 807. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 807. Profile updates may replace only one
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
  "chapter": 807,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 807,
    "continuity_sources": [807],
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
    "Jin is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "Jin commands roughly one thousand Hunters against a monster force exceeding ten thousand in the Rub’ al Khali.",
    "The monster army obeys an unseen authority; The Prophet’s location remains unknown.",
    "The Manticore Lord and Lycanthrope Champion are dead; an unidentified ally delivered the Lycanthrope Champion’s final blow.",
    "Jin is poisoned, his Fire Dragon Armor is damaged, and his special debuff has drastically reduced his stats.",
    "The Skeleton King is fighting the Death Knight Legion Commander.",
    "The battle against the monster army is ongoing. The Manticore Lord was especially strong and cunning."
  ],
  "continuity_sources": [
    806
  ],
  "open_questions": [
    "Where is The Prophet, and how is he directing the monster army?",
    "Can the defenders hold against the monster force, including its aerial monsters?",
    "Who arrived to assist Jin?",
    "Can Jin survive the poison and repair or protect his damaged Fire Dragon Armor?",
    "How will the fight between the Skeleton King and Death Knight Legion Commander end?"
  ],
  "safe_through": 806,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Use Manticore Lord for the source spelling 만티코아 로드."
  ],
  "version": 1
}
```

## Exact glossary matches

| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 초식     | **form**                                         | Numbered technique movement                           |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 마법사     | **mage**              |
| 도사      | **Daoist**                                                      |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 만티코어 | **Manticore** | A-Rank Gate monster and original raid target. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화룡신창 | **Fire Dragon Divine Spear** | Taekyung's spear technique, at the seventh stage in this chapter. |
| 골렘 | **Golem** | Magical rock-based monster classification. |
| 흑마법사 | **black wizard** | Ruler or magical classification associated with the Gate. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 마계어 | **Demon Realm language** | Language spoken by monsters from the Demon Realm. |
| 천격 | **Heavenly Strike** | A Fire Dragon Divine Spear form used by Taekyung against Hwangbo Eom. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 제시 | **Jesse** | The U.S. Secretary of State, introduced by first name. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 성우 | **Sacred Rain** | Name later given to the rain released as the Earth Mother Goddess's blessing. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 805
- **Aliases:** None
- **Role:** Yamamoto Genji is a Japanese S-rank Hunter and J1’s sole survivor.
- **Personality:** Prideful and easily offended, prone to self-aggrandizement and self-serving assumptions, and cowardly under mortal threat.
- **Voice:** Not established.
- **Relationships:** Jin Taekyung sent Yamamoto on the J1 mission and treated him after the attack, though Jin resents Yamamoto for arriving late during the Leviathan crisis.

## Korean source

```text
＃807화



초절정 고수도 불알을 걷어 차이면 쓰러지듯이, 제아무리 괴이하고 강력한 몬스터라 해도 약점은 인간과 비슷하다.

머리를 날려 버리거나, 혹은 심장을 터트리거나.

물론 어디에나 예외는 있다.

박살 난 머리마저 복구하는 트롤이 존재하고, 몸속 어딘가에 존재하는 핵을 파괴하기 전까지는 쓰러지지 않는 골렘도 있다.

언데드인 동시에 뛰어난 흑마법사인 리치는 라이프 포스 베슬(Life Force Vessel)에 영혼의 일부를 담아 보관하기도 한다.

하지만 적어도 내가 아는 한, 머리가 잘리고도 살아남는 라이칸스로프는 어디에도 없었다.

설령 그것이 종족 최강의 전사인 챔피언의 칭호를 받은 S급 몬스터라 할지라도.

“제가 왔습니다! 진 사마!”

“…….”

나는 침까지 튀기며 떠들어 대는 야마모토 겐지와 목이 잘린 채 쓰러진 경험치…… 아니, 라스칸스로프 챔피언의 시신을 번갈아 보며 생각했다.

‘아니 씨팔…….’

무슨 이런 개 같은 경우가.

완벽한 레벨 업 타이밍이었는데. 이미 다 차려 놓은 밥상이었는데 그걸 웬 놈이 홀랑 가져갔다.

가슴 깊숙한 곳에서 치밀어 오르는 분노에 손발이 덜덜 떨릴 지경이다.

삐빅.



- 상태 이상, [경련]이 추가 부여됩니다!

- 상태 이상, [중독]이 더욱 심각해지고 있습니다!

- [만티코어 로드의 맹독]을 한시라도 빨리 체내에서 제거해야 합니다!



“…….”

그래. 어쩐지 손이 너무 떨리더라.

가뜩이나 안 좋은 몸 상태에 울화가 겹치니 순간 눈앞이 흐릿해진다.

계산했던 대로라면 지금쯤 레벨 업으로 멀쩡하게 회복했겠지만, 이렇게 된 이상 별수 없이 다른 방법을 쓰는 수밖에 없다.

“에? 진 사마, 혹시 불편하신 데라도?”

“넌 지금 이 꼬라지가 안 불편해 보이니, 이 씨벌놈아?”

“앗. 아아…….”

단번에 야마모토 겐지의 입을 닥치게 만든 나는 마음속으로 뇌까렸다.

‘인벤토리 오픈. 소환.’

명령어와 함께 발현되는 시스템.

슥.

덜덜 떨리는 손가락에 차가운 감촉이 닿은 순간. 앞서와는 다른 맑은 종소리가 울려 퍼졌다.

띠링. 띠링. 띠링.



- [만독지환(萬毒指環)]을 장착했습니다.

- 알 수 없는 기운이 전신을 씻어 내립니다!

- [만독지환]이 [만티코어 로드의 맹독]을 흡수했습니다!

- 상태 이상, [중독]이 해제되었습니다!

- 상태 이상, [경련]이 해제되었습니다!



연달아 울리는 종소리와 함께 시야가 또렷해지고 경련이 멎는다.

쇄골 어림으로부터 전신으로 퍼져 가던 독기(毒氣)를 빨아들인 만독지환은 특유의 검은빛으로 번뜩였다.

‘비록 레벨 업은 못 했지만…… 그나마 만독지환이라도 있어서 천만다행이야.’

승부를 빠르게 마무리 지었기에 망정이지. 만티코어 로드가 품고 있던 맹독은 그야말로 무시무시했다.

독과는 상극인 열양지기에 최상급 포션을 쓴다면 어렵지 않게 치유할 수 있었겠지만, 포션이라는 건 결국 몸 안의 기력과 생명력을 선불로 치르고 회복력을 극대화하는 물건이다.

지금처럼 남아 있는 적들이 많은 상황에서는 아무런 리스크가 없는 레벨 업이 백배는 나았다.

물론…….

“괘, 괜찮으십니까?”

저 멀리에서 슬슬 눈치나 살피다가, 후다닥 달려와 막타를 뺏어 간 어떤 놈 때문에 물 건너갔지만.

“됐다, 신경 쓰지 마.”

하지만 뭘 어쩌겠나.

이미 버스는 지나갔고, 내게는 텅 빈 정류장에서 다음 차를 기다리며 야마모토 겐지의 귀싸대기나 올려붙일 여유가 없었다.

그리고 불행 중 다행인 사실은, 스켈레톤 킹이 자신에게 주어진 일을 제시간에 맞춰 끝낼 줄 아는 훌륭한 몬스터라는 것이었다.

콰드드득!

각자의 싸움에 임하는 과정에서 상당히 멀어진 거리였지만, 2미터를 훌쩍 넘기는 거구의 데스 나이트가 갑옷째로 우그러지는 광경은 똑똑히 보고 들을 수 있었다.

놈이 내지르는 마지막 단말마도 함께.

- 그아아아아!

쏴아아악!

그것이 마지막이었다.

깊게 눌러쓴 투구 사이로 흘러나온 검은 안개가 흘러나왔고, 소멸 직전 밖으로 튀어나온 데스 나이트의 영혼을 빨아들이듯 흡수한 스켈레톤 킹은 경공을 펼쳐 다가오는 나를 보며 씩 웃었다.

“이 괴물 같은 놈.”

그리고 내 옆구리에 짐짝처럼 끼워진 야마모토 겐지를 발견하고 덧붙였다.

“저 개 같은 놈.”

동감이다. 이 새끼가 잠깐이라도 라이칸스로프 챔피언의 발을 묶었더라면 모든 것이 훨씬 수월하게 끝났을 테니까.

하지만 수천, 수만이 얽혀든 전투가 벌어지는 와중에 야마모토 겐지의 조인트를 까는 건 미친놈이나 하는 짓이다. 그럴 시간이 있다면 한 사람이라도 더 구해야 한다.

“가자.”

나는 그 짤막한 한 마디와 함께 신형을 쏘았다. 앞서 벌어진 격전을 증명하듯 삐걱대는 팔다리와 상당히 소모된 공력.

그럼에도 나는 가야 한다. 싸워야 한다.

쐐애애액, 콰앙!

강한 힘을 실어 쏘아 보낸 백염의 창날이 개미 떼처럼 우글거리는 몬스터 군단의 후미를 휩쓸었다.

먹먹한 굉음이 비명을 집어삼키고 순간 터져 나온 화염은 살아있는 괴물들의 사지를 불태운다.

‘한 번 더.’

나는 속도를 줄이지 않고 계속해서 내달렸다.

인벤토리에서 꺼내 든 또 다른 창을 역수(逆手)로 쥐고 쏘아 보냈다.

퍼엉!

강렬한 파공성이 사막을 가로지른다.

일직선에 가깝게 날아간 창에는 처음과 같은 공력이 담겨 있지 않았지만, 그 무시무시한 힘과 속도가 고스란히 실린 창날은 능히 수십의 몬스터를 관통하고도 남았다.

콰드드득!

- 크라아아아!

단지 스친 것만으로도 머리통이 수박처럼 터져 나가고, 끊어진 사지가 허공으로 솟구친다.

아무리 죽여도 줄어들 것 같지 않던 몬스터 군단이 주춤거리는 것이 느껴졌다.

퍼엉!

- 쿠륵, 끄아아!

시시각각 가까워지는 비명. 짙어지는 악취.

세 번째로 투창을 쏘아 보냈을 때는 이미 수백이 쓰러진 후였고, 허공을 박차며 솟구친 나는 옆구리에 낀 야마모토 겐지를 지면으로 내던지며 손을 뻗었다.

‘와라.’

쐐애애액! 탁!

중단전(中丹田)을 통한 부름에 응답해 날아온 백염이 손아귀에 붙잡힌다.

언제부터인가 굳이 눈으로 확인하지 않아도 알 수 있을 만큼 착 감기는 촉감.

회수와 동시에 열양지기를 불어넣자 투명한 창날이 불그스름한 홍조(紅潮)를 띠었다.

화륵.

화염. 바람. 느릿하게 움직이는 세상.

그리고…… 전장이 한눈에 내려다보이는 허공 위로 솟구친 나를 멍하니 바라보는 시선들.

솨아아아.

바람이 전신을 스친다. 멈춰 있던 시간이 조금씩 제 템포를 되찾아 움직인다.

그와 함께 부릅떠진 수많은 눈동자에서 상반된 감정이 떠오르는 것이 보였다.

누군가의 눈에는 기쁨이, 다른 누군가에게서는 서서히 현실에 스며드는 절망이 읽힌다.

인간과 몬스터. 몬스터와 인간.

서로의 대척점에 서 있는 두 종족 중 누가 환희하고 절망했을지는, 굳이 말하지 않아도 이 자리의 모두가 알고 있었다.

‘화룡신창(火龍神槍). 이 초식.’

호흡을 삼켰다.

내가 받아들이는 세상의 시간에 발맞춰 천천히 낙하하는 신형과는 달리, 화염을 머금은 창날은 하늘을 찌를 듯 높게 들어 올렸다.

화륵.

초고온의 열기가 공간을 일그러트린 그 순간, 수많은 몬스터들에 의해 포위된 헌터들의 머리 위를 배회하던 거대한 그림자가 나를 향해 쏘아졌다.

- 삐이이잇!

귓가를 울리는 날카로운 울음소리.

동시에 보지 않아도 느껴진다. 나를 향해 쏘아지는 놈의 속도는 다른 몬스터들과는 달리 빛살처럼 빨랐고, 단 한 번의 날갯짓이 불러온 돌풍에는 막강한 마력이 담겨 있었다.

‘그리핀들의 우두머리.’

그래, 놈이 틀림없다.

하늘을 제집처럼 누비는 비행 몬스터인 만큼, 어떤 의미에서는 가장 귀찮은 상대.

하지만…….

‘상관없어.’

나는 마력의 돌풍과 함께 덮쳐오는 그리핀들을 무시한 채. 그대로 창날을 내리그었다.

천격(天格).

후우우우웅!

백염의 창날을 타고 흘러넘친 화염이 코앞까지 들이닥친 마력의 돌풍을 지우고 공간을 갈랐다.

용의 발톱처럼 날카롭고 강맹한 참격(斬格)이 빽빽하게 밀집된 몬스터 군단의 중심을 향해 쏟아졌다.

화아악!

닿기도 전에 녹아내릴 것 같은 열기와 섬광이 번뜩인다.

수백, 혹은 천에 달하는 몬스터들을 집어삼킨 겁화가 폭발했다.

꽈앙! 구구구구궁!

불의 비가 쏟아진다. 비명과 죽음이 용암처럼 흘러넘쳤다.

총탄에도 흠집 하나 나지 않는 상위 몬스터의 가죽도, 위기를 느끼고 뒤돌아 도망치려던 재빠른 하급 몬스터들도 그것을 피할 수 없었다.

죽음은 괴물들 모두에게 평등했고, 그 광경을 지켜보던 그리핀의 우두머리는 비명과도 같은 포효를 터트렸다.

- 끼아아악!

후웅, 전신을 밀어 내는 묵직한 중압감.

문득 고개를 들자, 어느새 머리 위로 날아든 그리핀의 우두머리가 나를 향해 쏘아지고 있었다.

햇빛을 가린 거대한 그림자 속에서도 막강한 마력이 실린 괴물의 부리는, 태양처럼 번쩍이고 있었다.

저 일격을 맞받아친다면?

아무리 나라고 해도 멀쩡하진 못할 거다.

조금 전 맞닥트린 두 갈래 길에서 내가 선택한 것은 놈을 상대하는 것이 아니라, 몬스터 군단의 대열을 허물어트리는 것이었으니까.

하지만.

“굳이 내가 아니어도 충분하지. 안 그래?”

- ……!

시스템을 거쳐 흘러나온 마계어에 날짐승의 동공이 세로로 길게 찢어졌다.

마지막 순간 찾아온 찰나의 머뭇거림.

그리고 바로 지금 이 순간을 기다리고 있던 이들은, 내 믿음을 배신하지 않았다.

슈확! 카아앙!

파공성과 함께 지상에서 날아든 무언가를 튕겨 낸 그리핀 우두머리가, 힘을 이기지 못하고 비틀거린다.

‘저건.’

뼈로 이루어진 골창(骨槍).

역할을 다하고 지면으로 떨어져 내리는 그 모습에 한 사람이, 아니 한 몬스터가 생각난다.

스켈레톤 킹.

지치지도 않는 주제에 나보다 한참이나 느려 터진 놈이 드디어 여기에까지 다다른 것이다.

하지만 내가 정말로 믿고 있던 사람은 따로 있었다.

우우우우웅.

사방의 공기가 부르르 몸을 떨었다. 나뿐만 아니라, 이 자리의 모두가 무거워진 전장의 공기를 느꼈다.

순식간에 잦아든 바람과 그사이 깊숙한 곳에서 솟아올라 전장을 짓누르는 거대한 마나를 느꼈다.

- 삐잇?

우두머리를 비롯한 백여 마리의 그리핀들이 당혹스러운 눈빛으로 서로를 바라보았다.

놈들은 더 이상 날갯짓을 하고 있지 않았다.

아니, 누군가에 의해 허공에 묶여 버렸다.

“솟구치고, 내리꽂혀라.”

평소의 유쾌함은 단 한 줌도 찾아볼 수 없는, 삭막하고도 가라앉은 목소리가 이어졌다.

“리버스 그래비티(Reverse Gravity)”

그리고 그 순간.

후우우우웅!

범위 안의 중력이 제멋대로 날뛰었다.

자로 잰 것처럼 정확하게 남아 있는 비행 몬스터들을 붙잡은 마나가 놈들을 지상으로 처박았다.

- 삐이이잇!

그리핀 우두머리의 울음소리를 들으며, 나는 문득 그런 생각이 들었다.

수백 미터 상공에서, 그것도 무려 일백에 달하는 거대한 그리핀 무리가 빛살처럼 지상으로 처박히는 광경을 뭐라고 불러야 할까.

절경? 아니면…….

‘마법?’

적어도 한 가지는 확실하다.

전투의 마지막을 장식하는 이 끝내주는 광경을 연출한 대마도사는, 확실히 전 세계 최고의 워 메이지(War Mage)라 불릴 자격이 있다는 것.

쿠구궁! 콰드드득!

끝없이 번져 가는 불길과 혼란. 유성우처럼 쏟아진 그리핀들의 거대한 몸뚱어리에 짓눌려 죽어 가는 무수한 괴물들.

완전히 중심이 와해되어 몬스터 군단을 바라보던 나는 공력을 실어 외쳤다.

“포메이션! 전환!”

이 전투는, 이미 승리했다.

“저 개새끼들, 싹 다 죽여 버려.”

와아아아아아!

하늘과 땅을 떨어 울리는 거대한 함성과 함께. 아직 예리함을 잃지 않은 일천의 창칼이 물결처럼 나아갔다.
```

## Final English reading copy

```markdown
# Chapter 807

Even a Supreme Peak master will go down if he gets kicked in the balls. No matter how strange or powerful a monster is, its weaknesses are much like a human’s.

Blow its head off, or burst its heart.

Of course, there are exceptions to everything.

There are Trolls that can put even a shattered head back together, and Golems that won’t fall until you destroy the core somewhere inside their bodies.

A Lich, both undead and a skilled black wizard, might store part of its soul in a Life Force Vessel.

But as far as I knew, there wasn’t a single Lycanthrope anywhere that could survive having its head cut off.

Not even one that was an S-rank monster and had earned the title of Champion as the strongest warrior of its kind.

“I’ve arrived! Jin Sama!”

“……”

I looked back and forth between Yamamoto Genji, who was chattering so loudly he was spitting, and the headless body of the EXP… No, the Lycanthrope Champion.

*No, fuck…*

What kind of bullshit was this?

It had been the perfect time to level up. The meal was already laid out in front of me, and some bastard had swooped in and gobbled it all up.

I was so furious, it felt like my hands and feet might start shaking.

*Beep.*

> **System**
>
> Status abnormality **Convulsions** has been applied!
>
> Status abnormality **Poisoned** is worsening!
>
> **Manticore Lord’s Venom** must be removed from your body as soon as possible!

“……”

Right. No wonder my hands were shaking so much.

With my condition already this bad, the anger made my vision blur for a moment.

If things had gone as I’d calculated, I’d have leveled up by now and recovered completely. But since it had come to this, I had no choice but to use another method.

“Um? Jin Sama, are you feeling unwell?”

“Does this look like I’m feeling fine, you fucking idiot?”

“Ah. Oh…”

I shut Yamamoto Genji up with a single remark, then muttered to myself.

*Open Inventory. Summon.*

The System manifested in response to the command.

*Shk.*

The moment my trembling fingers touched something cold, a clear chime unlike the earlier ones rang out.

*Ding. Ding. Ding.*

> **System**
>
> Equipped **Myriad-Poison Ring**.
>
> An unknown energy washes over your entire body!
>
> The **Myriad-Poison Ring** has absorbed **Manticore Lord’s Venom**!
>
> Status abnormality **Poisoned** has been removed!
>
> Status abnormality **Convulsions** has been removed!

As the chimes rang one after another, my vision cleared and the convulsions stopped.

The Myriad-Poison Ring had drawn in the poison spreading from around my collarbone throughout my body. It gleamed with its usual black light.

*I may not have leveled up, but at least I had the Myriad-Poison Ring. Thank God for that.*

It was a good thing I’d ended the fight quickly. The venom the Manticore Lord had carried was truly terrifying.

With Scorching Yang Qi, which was the natural enemy of poison, and a top-grade potion, I could have been cured without much difficulty. But a potion ultimately worked by paying in advance with the body’s energy and vitality to maximize its recovery.

In a situation like this, with so many enemies left, leveling up—with none of the risk—would have been a hundred times better.

Of course…

“A-are you all right?”

Some bastard had been hanging back, watching for an opening, then rushed in and stole the last hit from me.

“Forget it. Don’t worry about it.”

But what could I do?

The bus had already left, and I didn’t have time to stand at an empty bus stop waiting for the next one and slap Yamamoto Genji across the face.

The one bit of good news amid all the bad was that the Skeleton King was the kind of excellent monster who knew how to finish his assigned job on time.

*Crack-crunch!*

We’d gotten quite far apart while fighting our respective opponents, but I could clearly see—and hear—the Death Knight, well over two meters tall, crumple along with his armor.

His final scream came with it.

—GRAAAAAAH!

*Fwoosh!*

That was the end.

Black mist poured out from beneath the helmet pulled low over his face. The Skeleton King seemed to absorb the Death Knight’s soul as it spilled out just before Erasure. Then he grinned at me as I approached using lightfoot.

“You monster.”

Then he spotted Yamamoto Genji tucked under my arm like a piece of luggage and added, “That fucking bastard.”

I agreed. If that little shit had even slowed the Lycanthrope Champion down for a moment, everything would’ve ended much more smoothly.

But kicking Yamamoto Genji in the joints in the middle of a battle involving thousands—tens of thousands—of fighters would be something only a lunatic would do. If I had time for that, I needed to use it to save one more person.

“Let’s go.”

With that brief word, I shot forward. My limbs creaked, proof of the fierce battle that had just taken place, and my internal energy was considerably depleted.

Even so, I had to go. I had to fight.

*Shweee—BOOM!*

The spearhead of White Flame, sent flying with tremendous force, swept through the rear of the monster army swarming like ants.

A muffled boom swallowed the screams, and the flames that erupted in an instant burned the limbs off the living monsters.

*One more time.*

I kept running without slowing down.

I pulled another spear from my Inventory, gripped it in a reverse hold, and hurled it.

*Boom!*

A thunderous crack split across the desert.

The spear didn’t carry the same internal energy as the first one, but its spearhead still held all that terrible force and speed—enough to pierce dozens of monsters with ease.

*Crack-crunch!*

—GRAAAH!

Even a glancing blow burst their heads like watermelons, sending severed limbs flying into the air.

I could feel the monster army, which had seemed like it would never grow smaller no matter how many I killed, falter.

*Boom!*

—Grrk, gaaah!

The screams drew closer by the moment. The stench grew stronger.

By the time I hurled my spear for the third time, hundreds had already fallen. I kicked off the air and soared upward, then flung Yamamoto Genji from under my arm toward the ground and reached out.

*Come.*

White Flame came flying in response to the call through my Middle Dantian and landed in my hand with a snap.

Somehow, its familiar grip had become so natural that I could recognize it without even looking.

As soon as I reclaimed it, I poured in Scorching Yang Qi. The transparent spearhead took on a reddish glow.

*Fwoosh.*

Flames. Wind. A world moving slowly.

And… the eyes staring blankly at me as I soared through the air, with the entire battlefield laid out below.

*Whoosh.*

The wind brushed across my body. Time, which had stopped, gradually returned to its usual pace.

I saw conflicting emotions surface in countless eyes that had opened wide.

There was joy in some. In others, despair was slowly sinking into reality.

Humans and monsters. Monsters and humans.

Which of the two opposing species was rejoicing and which was despairing? No one here needed to say it.

*Fire Dragon Divine Spear. This form.*

I drew in a breath.

My body descended slowly, keeping pace with time as I perceived it, while the flame-filled spearhead rose high, as if to pierce the sky.

*Fwoosh.*

At that moment, when the space around me warped under the extreme heat, a massive shadow that had been circling over the Hunters surrounded by monsters shot toward me.

—Screee!

A piercing cry rang in my ears.

At the same time, I could sense it without looking. Unlike the other monsters, it was flying toward me like a streak of light. The gale raised by a single flap of its wings carried immense magical power.

*The leader of the Griffins.*

Yeah. It had to be.

As a flying monster that ranged through the sky as if it owned it, it was one of the most troublesome opponents in its own way.

But…

*I don’t care.*

Ignoring the Griffin leader rushing at me with its gale of magical power, I brought the spearhead down.

Heavenly Strike.

*Whoooooom!*

Flames poured over the spearhead of White Flame, wiping out the gale of magical power rushing toward me and cleaving through space.

A fierce, razor-sharp slash, like a dragon’s claw, rained down toward the center of the densely packed monster army.

*Fwoosh!*

The heat and flash were so intense they seemed capable of melting everything before they even touched it.

Hellfire engulfed hundreds—maybe a thousand—monsters and exploded.

*BOOM! Rumble-rumble!*

A rain of fire poured down. Screams and death flowed like lava.

Neither the hides of the upper-level monsters—unmarked even by bullets—nor the quick-footed lower-level ones who sensed danger and tried to flee could escape it.

Death was equal for all the monsters, and the leader of the Griffins watching the scene let out a roar like a scream.

—Kyaaaah!

*Whoom.* A heavy pressure pushed against my whole body.

I raised my head. The leader of the Griffins, already overhead, was shooting toward me.

Even within its massive shadow, which blocked the sunlight, the monster’s beak shone like the sun, packed with immense magical power.

What if I met that attack head-on?

Even I wouldn’t come away unscathed.

At the fork in the road I’d faced a moment ago, I’d chosen not to fight it, but to break up the monster army’s formation.

But—

“I don’t have to be the one to do it. Right?”

—…!

The eyes of the flying beast narrowed into vertical slits at the Demon Realm language that came through the System.

A brief hesitation in its final moment.

And the ones waiting for that very moment didn’t betray my faith in them.

*Shwoop! Clang!*

The leader of the Griffins deflected something that flew up from the ground with a sharp crack, then staggered, unable to withstand the force.

*That’s…*

A bone spear.

As I watched it fall to the ground after serving its purpose, I thought of one person—or rather, one monster.

The Skeleton King.

That bastard, who never got tired and was much slower than me, had finally made it all the way here.

But the person I’d truly been counting on was someone else.

*Rumble.*

The air all around us shuddered. Everyone here, not just me, felt the battlefield’s atmosphere grow heavy.

I felt the wind die down in an instant, and the enormous mana rising from somewhere deep below press down on the battlefield.

—Screep?

The leader and more than a hundred Griffins looked at one another in confusion.

They were no longer flapping their wings.

No—they’d been bound in midair by someone.

“Rise, then crash back down.”

The voice that followed was stripped of every trace of his usual cheer. It was bleak and subdued.

“Reverse Gravity.”

And then—

*Whoooooom!*

Gravity within the area went wild.

Mana seized the remaining flying monsters with precision and slammed them into the ground.

—Screee!

Listening to the leader of the Griffins cry out, I found myself wondering what to call the sight of a massive flock of nearly a hundred Griffins plummeting toward the ground like streaks of light from hundreds of meters in the air.

A spectacular sight? Or…

*Magic?*

At least one thing was certain.

The Grand Mage who had staged this spectacular scene to close out the battle certainly deserved to be called the world’s greatest War Mage.

*Rumble! Crack-crunch!*

The flames spread without end. Chaos took hold. Countless monsters were crushed beneath the Griffins’ huge bodies as they rained down like a meteor shower.

Watching the monster army, its center completely broken, I shouted as I poured internal energy into my voice.

“Formation! Change!”

This battle was already won.

“Kill every last one of those bastards!”

A massive roar shook heaven and earth. The thousand spears and blades, still sharp, surged forward like a wave.
```
