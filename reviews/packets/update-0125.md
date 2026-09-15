<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0125.txt",
      "sha256": "84530348447f5dc27a78bd647f085e3564c2e97c7d4a4be340435954f0a14e4e",
      "bytes": 12934
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "579d5d26d0e3efd01164fc5ebed915faf951487d21034de260577e5238e2a62b",
      "bytes": 4614
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "83c9bef552ac1eb02f2ff7f74022ad63f366ee3321e16426afd1b7464134f74c",
      "bytes": 20582
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "ea62d5f9eb0b639c4286a6b40b71b922aded20872165bbd95333c12a6f7e44d7",
      "bytes": 851
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "654a9185adefe69491b36b6bd0dce603f6d3ee51972ef058ad154f68408afb79",
      "bytes": 5199
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "6c9b6ed6ff24017bf82e0255c90b7c164b0dd828f80aaa1878246ebd17f4e72d",
      "bytes": 1511
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "34067244e778be7a4a76861e85b7bb1284ebd922e0431a8e39807b809c035236",
      "bytes": 8154
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "aa97840ed94fe2259e3183026715661fe98f80bc97c451598739eb4be3063af9",
      "bytes": 3231
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "3f26f4c64427c5c37873c7ee019702ec7b6ce021794fa95fbdfd813105cd3423",
      "bytes": 1296
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "c78f2f58fe0b0c855e9edfb56f8ead34d7084efae765d4a9b28f974e58cb2474",
      "bytes": 1356
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5dea745a2e714cf866b8b5b8934df5a17d2129e099c7ff3164432303d44df785",
      "bytes": 17837
    }
  ],
  "estimated_tokens": 20544
}
-->

# Durable State Update — Chapter 125

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 125. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 125. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 125,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 125,
    "continuity_sources": [125],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "Pung Yang is dead; Jin Taekyung killed him after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest.",
    "Taekyung fully absorbed the Blazing Flame Divine Pill and possesses forty-five years of internal energy with the Scorching Yang Qi attribute.",
    "Jin Mukyung survived his fight with Pung Yang and has recovered enough to return to the Jin Family, though he is not fully healed.",
    "Cheol Mubaek and the other wounded Mount Heng martial artists are recovering; Cheol has broken limbs and serious Internal Injuries and needs at least four months of recuperation.",
    "Lee Seowol remains Sect Leader of the Mount Heng Sword Sect and vows to preserve it for those who died defending it.",
    "The Lower District Sect sent a relief force with physicians, cooks, and laborers after the battle.",
    "Wolhwa's real name is Eun Sowol, and she is the Lower District Sect's Shanxi Branch Leader with authority over more than thirty Shanxi branches.",
    "Lee Seowol accepted Jin Wikyung's invitation to the Jin Family of Taiyuan's New Year gathering.",
    "Lee Seowol offered the Mount Heng Sword Sect's territorial rights to the Jin Family of Taiyuan as an apology.",
    "Lee Seowol proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist.",
    "Lee Seowol is seventeen years old.",
    "Jin Taekyung has decided to reject Lee Seowol's political marriage proposal because of her age and because he loves Song Song.",
    "Forty-seven mounted bandits survived the battle, but the Lower District Sect can save only about thirty with its available medicine.",
    "The Lower District Sect is spreading a rumor that the two Jin brothers defeated Pung Yang and rescued the Mount Heng Sword Sect.",
    "Cheol Mubaek is the ninth-generation successor of the Shura Annihilating Fist and gave its manual to Lee Seowol despite its inheritance traditions.",
    "Cheol Mubaek and Lee Cheonbaek first met more than thirty years ago, fought, and then became close friends.",
    "The Shura Annihilating Fist was an ancient top-ten fist technique whose lineage was believed to have ended and is no longer a current top-ten technique.",
    "Jopil is dead and left behind the Supreme Peak martial art Flame Divine Palm.",
    "Jin Taekyung possesses the Flame Divine Palm manual, a Fire Gate Clan secret technique restricted to owners of Scorching Yang Qi.",
    "The Fire King is a Supreme Peak master among the world's twenty greatest experts; his current status is unknown, and the Fire Gate Clan has a single successor."
  ],
  "continuity_sources": [
    124,
    123
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What is the origin and full long-term effect of the Temporary Strength Pill?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?",
    "Is the Fire King still alive, and if so, where is he?",
    "Was Jopil truly the nineteenth-generation successor of the Flame Divine Palm, and how did he acquire it?"
  ],
  "safe_through": 124,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 호신강기 as Body-Protecting Qi.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, 산서성 as Shanxi Province, and 총지부장 as Chief Branch Leader.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, and 천하십대권법 as the ten greatest fist techniques in the world.",
    "Render 열화문 as Fire Gate Clan, 화왕 as Fire King, 삼성 as Three Saints, 십왕 as Ten Kings, and 진무보법 as Jin Family's Manoeuvre Technique; retain the Samsung/Samseong clarification footnote."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 철 숙부 | **Uncle Cheol** | Lee Seowol's familial address for Cheol Mubaek. |
| 철 대협 | **Great Hero Cheol** | Respectful address for Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 절정 초입 | **early Peak** | Pung Yang's specific stage within the Peak realm. |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 일류 초입 | **early First Rate** | Early stage of the First Rate realm. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 영단 흡수 | **Divine Pill Absorption** | System Quest created after Jin Taekyung takes the Blazing Flame Divine Pill. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 이름 없는 검 | **Unnamed Sword** | Oldest inventory item summoned when no item named 아무거나 can be found. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 완전 회복 | **Full Recovery** | Immediate Quest success reward that heals Taekyung's injuries. |
| 뛰어난 금창약 | **Superior Wound Medicine** | Quest reward used to treat external injuries. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 어제의 적, 오늘의 동지 | **Yesterday's Enemy, Today's Ally** | Quest completed when Taekyung delivers Wikyung's invitation. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 명성               | **Fame**                       |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 매력               | **Charm**                      |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 소생      | **I**; occasionally “this humble one” in highly formal dialogue |
| 본문      | **our sect / this sect**                                        |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 123
- **Aliases:** Tiger of Mount Heng
- **Role:** Ninth-generation successor of the Shura Annihilating Fist and Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; severely injured in battle; entrusted the manual to Lee Seowol and remains her protector
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; feared and respected by the Mount Heng Sword Sect's senior figures

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 124
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; stationed outside Jin Taekyung’s pavilion while Taekyung recovers
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 124
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 121
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 123
- **Aliases:** Blood Wolf Sword
- **Role:** Former Sect Leader of the Mount Heng Sword Sect, killed during the Red Wind Band’s assault; father of Lee Seogeun and Lee Seowol
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Deceased father of Lee Seogeun and Lee Seowol; also father of a deceased Young Sect Leader; former leader of the Mount Heng Sword Sect; longtime close friend and peer of Cheol Mubaek

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 124
- **Aliases:** None
- **Role:** Seventeen-year-old current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady; survived Pung Yang's attack with twenty-four other identified survivors; regards the Mount Heng Sword Sect as effectively destroyed but vows to preserve it for those who died defending it; offered the sect's territorial rights to the Jin Family of Taiyuan and proposed marriage to Jin Taekyung in exchange for three Peak martial arts
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge, to whom he entrusted the Shura Annihilating Fist manual; has proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 124
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

## Korean source

```text
＃125화



“은공.”

오늘의 이소월은 특히 아름다웠다. 눈처럼 새하얀 흰색 궁장에, 옥색 비녀로 틀어 올린 머리카락은 윤기가 흘렀다.

연달아 고초를 겪은 탓인지 아직 초췌해 보이긴 했지만 워낙 눈부신 미모의 소유자라 그것마저도 매력적으로 보일 정도다.

‘아니, 내가 지금 무슨 생각을 하는 거야.’

미인? 매력적? 열일곱이면 한창 교복 입고 다닐 나이 아닌가. 현실에서는 혼사가 아니라 내신을 준비해야 할 시기다.

하연이보다도 두 살이 어리니 나와는 열 살 차이. 이 정도면 조카뻘이나 다름없다.

‘그런데 확실히 나이에 맞지 않게 성숙한…… 아니다. 정신 차리자.’

이소월의 그윽한 시선을 피하면서 포권을 취했다.

“안녕하십니까.”

“문주를 뵙소.”

이소월은 평범한 소녀가 아니라 엄연히 일문(一門)을 책임진 문주다. 나와 진무경의 정중한 인사에 그녀가 화답하려던 그때였다.

“대항산검문의 문주님께서 친히 나와 주시다니. 소생 혁무진, 실로 감격했습니다!”

그래, 네가 빠지면 섭섭하지.

그녀에게 시선을 고정한 채 허리를 넙죽거리는 혁무진을 보니 한숨밖에 안 나온다.

“죄송합니다. 원체 좀 모자란 놈이라.”

“……조장.”

“보셨죠? 저랑 아무 사이도 아닌데 친한 척하는 거. 그냥 무시하시면 편합니다.”

이소월의 입가에 살짝 보조개가 패었다.

“아니에요. 저분도 본문을 위해서 싸워 주신 은인이신걸요.”

“괜찮아요. 저 녀석은 검 하나 까딱 안 했으니까 은인으로 안 치셔도 됩니다.”

“……아, 네.”

내 친절한 팩트 체크에 그녀의 웃음이 어색해진 그 순간이었다.

“은인이지, 나한테는.”

이소월의 등 뒤에서 들려온 걸걸한 목소리의 주인공은 반백의 장년인이었다. 덜컹거리는 목제 수레에 앉은 그가 눈인사를 건넨다.

“일어나지 못하는 부분은 양해 바라네. 이거 참, 나이를 먹었더니 몸이 예전 같지 않아.”

나이와 명성으로는 이 자리의 그 누구도 눈앞의 장년인을 따라갈 수 없다.

항산호 철무백의 등장에 혁무진이 잽싸게 허리를 꺾었다.

“철무백 대협을 뵙습…….”

“내 얼굴 처음 보나? 거추장스러운 인사는 넣어 둬.”

“그래도 위명이 자자하신 무림의 대선배님이신데…….”

“선배는 무슨. 그렇게 일일이 따지면 무림 살기 피곤해.”

“…….”

영감쟁이 성격 쿨한 것 보소.

뻔뻔하기로는 남부럽지 않은 혁무진이 조용히 찌그러지자 그다음은 진무경 차례였다.

“오셨습니까.”

별로 대단한 것도 없다. 짧은 한마디에 적당히 포권을 취했을 뿐이다. 그러나 진무경을 발견한 철무백의 얼굴에는 꽃이 활짝 폈다.

“어이구, 우리 진천검 아니신가. 그래, 이제 가려고?”

“그렇게 되었습니다.”

“왜, 좀 더 있다 가지 않고서. 나중에 무공에 대해 심도 깊은 이야기도 나누고 말이야. 응?”

“죄송합니다. 시간이 촉박한지라.”

“저런, 어쩔 수 없지. 하면 나중에 이 노인네 한 번 보러 와 줄 텐가?”

“강호의 대선배님께서 한 수 가르쳐 주신다니, 오히려 이 후배가 부탁드리고 싶은 일입니다.”

“으허허! 후배라, 듣기 좋네그려.”

이게 도대체 무슨 그림이지?

기껏해야 사나흘 머물렀을 뿐인데 사이좋은 조손지간을 보는 것 같다.

거기다가, 뭐? 방금은 선후배 따지면 세상 살기 피곤하다더니 말 바꾸는 것 봐라.

나는 혁무진을 향해 눈짓했다.

‘저 두 사람. 왜 저래?’

‘몰라요, 은인이라고 할 때는 언제고. 사람을 이렇게까지 차별해도 되는 겁니까?’

‘근데 솔직히 까 보면 넌 한 거 없잖아.’

‘…….’

열받은 얼굴로 입을 꾹 다무는 걸 보니 내 뜻이 충분히 전달된 모양이다.

“그래, 다음에 꼭 보자고.”

흐뭇한 할배 미소로 진무경을 바라본 철무백이 나를 향해 고개를 돌렸다.

“자넨 할 말 없나?”

순간 맹수의 눈빛이 느껴졌다고 하면 기분 탓인가?

나는 앞서 목격한 두 가지 예시 중 좋은 쪽을 따라가기로 마음먹었다.

“오셨습니까.”

“그럼 왔지, 갔나?”

“…….”

이게 아닌데?

하지만 힘들 때 웃는 것이 일류인 법. 당황하지 않고 웃음을 지어 보였다.

“몸은 괜찮으시고요?”

이번엔 철무백이 부목을 댄 사지를 흔들었다.

“괜찮아 보이나?”

“……아뇨.”

“괜찮았으면 걸어왔지. 요즘 마적 놈들은 정년도 없이 부려 먹으니 나 같은 늙은이가 버틸 재간이 있어?”

“…….”

노인네가 기억력도 좋다. 처음 만났을 때 말실수했던 걸 아직도 마음에 담아 두고 있는 모양이다.

상황을 알 리 없는 이소월은 당황한 얼굴로 빽 소리쳤다.

“숙부!”

“아이고, 늙은이 귀청 떨어지겠다.”

투덜거리던 그가 돌연 정중하게 고개를 숙였다.

“다들 고맙네.”

마지못해서 하는 인사가 아니다. 항산호 철무백. 오랜 세월 동안 오직 자신만의 길을 걸었던 노고수가 진심을 다해 말하고 있었다.

“얼마 남지 않은 늙은이의 명줄을 늘려 줘서가 아닐세. 소월이, 저 아이를 지켜 줘서 고맙네. 자네들 덕분에 항산검문이 살아남을 수 있었어.”

그가 잔잔한 눈빛으로 나와 진무경, 혁무진을 차례대로 응시했다.

“한 갑자를 넘게 살아오며 깨달은 사실이 있네. 은원(恩怨)은 무슨 수를 써서라도 갚아야 한다는 것. 내 이 자리에서 맹세하건대, 이번 일은 죽을 때까지 잊지 않겠네. 자네들이 원한다면 내 목숨을 잃는 한이 있더라도 말일세.”

이소월이 곧장 철무백의 말을 이어받았다.

“항산검문도 은인들을 기억하겠습니다. 또한 돌아가신 아버지께서 저지른 과오…… 이 자리를 빌려 사죄드립니다.”

“사죄드립니다!”

“부디 용서를!”

쩌렁쩌렁한 외침은 항산검문 무인들의 입에서 터져 나왔다.

하나같이 크고 작은 부상을 입은 그들이 아직 녹지 않은 눈밭에 무릎을 꿇은 채 우리의 대답을 기다리고 있었다.

툭.

- 네가 답해라.

진무경의 전음에 나는 바짝 마른 입술을 핥았다.

‘용서라.’

전쟁에서는 승리했지만 상처는 남았다.

명령에 따라 끊임없이 싸우고 죽어 간 무인, 심지어는 무공을 익히지 않은 여인과 아이들까지 희생됐다. 아들의 복수에 눈이 먼 이천백이 저지른 짓이었다.

항산검문과의 전쟁이 남긴 상처는 깊었고, 아물기까지는 오랜 시간이 걸릴 것이다.

‘그리고 흉터가 남겠지.’

어떤 종류의 흉터는 영원히 지워지지 않는다.

한순간에 집과 부모를 잃은 어린 남매가 그럴 것이고, 나 역시 그렇다. 고금제일인이라는 허무맹랑한 꿈을 꾼 녀석의 얼굴이 지금까지도 어른거리는 걸 보면 말이다.

그러나 지금이 봉합되어 가는 과정이라는 사실 또한 부정할 수는 없다.

‘그 상처를 준 사람들은 모두 죽었으니까.’

각자의 복수를 꿈꿨던 대장로와 이천백은 이미 최후를 맞이했다.

우리가 항산검문을 구하기 위해 며칠 밤낮을 달려왔던 이유도 그 때문이 아닐까?

진심 어린 사과와 용서가 있다면…… 흉터가 남을지라도 상처는 아물 수 있다.

바로 지금처럼.

“사죄는 받지 않겠습니다.”

고심 끝에 튀어나온 한마디다. 나는 다른 사람들의 반응을 기다리지 않고 말을 이었다.

“제가 누군가에게 사죄받고, 용서할 만한 자격이 있는 사람은 못 되거든요.”

이 자리의 누구도 그럴 만한 자격이 안 된다. 저들이 사죄해야 할 사람들은 태원진가에 있다.

내 말을 알아들었는지 이소월과 철무백이 고개를 끄덕였다.

“돌아오는 원단(元旦)에 뵐게요.”

“태원이라. 삼십 년 만의 외유가 되겠군.”

항산검문은 결코 환영받지 못하는 손님이다. 특히 형편없이 쪼그라든 현재로서는 온갖 수모와 굴욕을 당할 수도 있다.

하지만 이 또한 저들이 모두 감내해야 할 문제. 내가 할 수 있는 일도, 끼어들 이유도 없다.

- 잘했다.

진무경의 짤막한 전음을 들으며 마지막 인사를 건넸다.

“그럼 이만.”

마차를 향해 돌아서려던 그 순간이었다.

“은공.”

“네?”

“그거 아세요? 원단까지 보름도 남지 않았다는 거.”

이소월의 시냇물 같은 목소리가 졸졸졸 이어졌다.

“지난번에 듣지 못한 대답, 기대할게요.”

당황해서 입만 벙긋거리는 나를 진무경이 잡아끌었다.

등 뒤로 들려오는 철무백의 심기 불편한 듯한 기침 소리를 마지막으로, 마차가 힘차게 출발했다.



* * *



태원진가로 돌아가는 길은 빠르고 순탄했다. 마부의 숙련된 솜씨도 한몫했지만 조급한 마음이 사라지니 모든 게 그렇게 느껴졌다.

“후우.”

막 운기조식을 끝마친 진무경이 문득 중얼거렸다.

“생각해 보니 절정 무공은 구경도 못 했군.”

항산검문에 가면 절정 무공을 볼 수 있다는 진위경의 꾐에 빠져 동행하게 된 그다. 나는 점잖게 대꾸했다.

“괜찮아. 풍양 덕분에 북망산 구경은 했잖아.”

“그따위 말을 위로라고 하는 거냐?”

“아니, 놀린 건데.”

진무경의 손에서 뼈 어긋나는 소리가 들렸다.

“많이 컸군.”

“부상 다 회복하면 비무 한 판 하실?”

“지금 당장이라도…… 끙.”

자리를 박차고 일어나려던 진무경이 눈살을 찌푸렸다.

아무리 회복이 빠르다 한들 이제 고작 나흘이다. 그가 입은 부상이 완쾌되기에는 턱도 없이 짧은 시간.

자리에 무너지듯 주저앉은 녀석이 나를 노려보았다.

“운 좋은 줄 알아라.”

“운 좋은 건 모르겠고, 명줄 하나는 기똥차게 굵지.”

매번 죽을 고비를 맞이하는데도 사는 걸 보면 날 때부터 명줄 하나는 튼튼한 모양이다. 아니면 천운(天運)을 타고났거나.

“어쨌건 잘했다.”

“응?”

“이잉?”

뜬금없는 칭찬 스티커에 나와 혁무진이 동시에 눈을 동그랗게 떴다. 정작 당사자는 뭐 잘못됐냐는 얼굴이다.

“왜 그러지? 못 들을 말이라도 들은 표정들인데.”

“귀신이 따로 없네.”

“앗, 혹시 이미 풍양한테 죽고 원귀가 되어서 여기 계시는 거 아닐까요?”

제법 그럴듯한 가설이었지만 진무경 앞에서는 자나 깨나 입조심해야 한다.

나는 먼지 나게 두들겨 맞는 혁무진을 바라보며 품 안을 더듬었다.

‘인벤토리 오픈. 소환.’

다음 순간, 동그랗고 단단한 뭔가가 손끝에 닿았다.

풍양이 남기고 간. 아니, 풍양에게서 빼앗은 유일한 물건이다.

‘아이템 확인.’

띠링.



아이템창



[잠력단]

종류 : 영단

등급 : ???

제한 : [절정 무인] 이상

설명 : [알 수 없는 누군가]가 제조한 단환. 약 한 시진 동안 복용자의 잠재된 힘을 대폭 끌어 올리는 대신, 그에 대한 대가가 뒤따른다. 최악의 경우가 아니고서는 복용하지 말 것.

효과 : 전투 관련 능력치 +100

[공력] +15년

[호신강기] 사용 가능





제한 시간이 짧은 걸 감안해도 무지막지한 효과. 풍양이 그렇게 자신만만하던 이유가 충분히 이해가 된다.

후유증이 얼마나 심각한지는 모르겠지만 당장 목숨이 위태롭다면 두 개가 아니라 스무 개도 먹어야지, 뭘.

하지만 정작 마음에 걸리는 부분은 따로 있었다.

‘알 수 없는 누군가가 제조한 단환이라.’

아이템 등급도 물음표에, 정확한 후유증은 나와 있지 않으며 심지어 제조자는 베일에 싸여 있다.

도대체 어떤 놈이 이런 괴상한 물건을 만들어 냈을까?

‘이거, 구린내가 진동을 하는데.’

잠력단을 손안에서 굴리며 생각에 잠겨 있던 그때였다.

저 멀리서 아련하게 들려오는 누군가의 외침.

- 무경아아! 태경아아아!!

열정적으로 혁무진의 이마를 후려치던 진무경이 멈칫했다.

“환청인가?”

응, 아냐.
```

## Final English reading copy

```markdown
# Chapter 125

“Benefactor.”

Lee Seowol was especially beautiful today. She wore a snow-white formal robe, and her hair, twisted up with a jade hairpin, gleamed.

She still looked haggard from everything she had been through, but her beauty was so dazzling that even her exhaustion seemed charming.

*No. What am I thinking?*

Beautiful? Charming? At seventeen, she was at the age when she should be wearing a school uniform and preparing for her grades, not marriage.

She was two years younger than Hayeon, which put ten years between us. With an age gap like that, she might as well have been my niece.

*Still, she certainly seems mature for her age… No. Get a grip.*

Avoiding Lee Seowol’s deep gaze, I clasped my hands in a formal salute.

“Greetings.”

“I greet the Sect Leader.”

Lee Seowol was no ordinary girl. She was the Sect Leader responsible for an entire sect. Just as she was about to return Jin Mukyung’s and my polite greetings—

“Imagine the Sect Leader of the great Mount Heng Sword Sect coming out to greet us in person. I, Hyuk Mujin, am deeply honored!”

Of course. It wouldn’t be complete without you.

Hyuk Mujin kept his gaze fixed on her while repeatedly bowing at the waist. All I could do was sigh.

“I apologize. He’s a little short in the head.”

“...Captain.”

“You saw that, right? He’s pretending to be close to you even though you two have nothing to do with each other. You’ll be better off ignoring him.”

A faint dimple appeared beside Lee Seowol’s mouth.

“Not at all. He’s also a Benefactor who fought for our sect.”

“It’s fine. He didn’t lift a finger, so you don’t have to count him as a Benefactor.”

“...Oh. I see.”

Her smile had just turned awkward when a rough voice came from behind her.

“He’s a Benefactor to me.”

The speaker was a middle-aged man with half-gray hair. Sitting in a clattering wooden cart, he gave us a nod.

“Please excuse me for being unable to stand. Well, growing old has made me less sturdy than I used to be.”

No one here could match the middle-aged man before us in either age or fame.

At the appearance of Cheol Mubaek, the Tiger of Mount Heng, Hyuk Mujin quickly bent at the waist.

“I greet Great Hero Cheol Mubaek—”

“Is this the first time you’ve seen my face? Skip the troublesome formalities.”

“But you’re a great senior of the Murim, renowned throughout the martial world...”

“Senior, my foot. If you worry about things like that one by one, life in the Murim gets tiring.”

“...”

The old man had quite the laid-back personality.

Even Hyuk Mujin, who was shameless enough to rival anyone, quietly shrank back. That left Jin Mukyung.

“You’ve arrived.”

Nothing special. He simply clasped his hands in a brief salute. Yet Cheol Mubaek’s face lit up the instant he saw him.

“Well, look at that. Isn’t this our Heaven Shaking Sword? So, you’re leaving now?”

“It seems so.”

“Why don’t you stay a little longer? We could have a serious discussion about martial arts later. Hmm?”

“I’m sorry, but I’m pressed for time.”

“Oh, what a shame. It can’t be helped, then. How about coming to see this old man sometime?”

“If a great senior of the martial world is willing to teach me, then I’m the one who should be asking for such an opportunity.”

“Ha-ha-ha! Senior, huh? That sounds nice.”

What was I looking at?

They had only spent three or four days together, but they looked like a close grandfather and grandson.

And what about that? Hadn’t he just said that life became tiring if you worried about seniority and junior status? Look at him changing his tune.

I shot Hyuk Mujin a glance.

*What’s with those two?*

*No idea. He called me a Benefactor before. Is it really okay to treat people this differently?*

*But if you’re being honest, you didn’t actually do anything.*

*...*

He clamped his mouth shut with an irritated expression. My meaning seemed to have gotten through.

“All right. Make sure you come next time.”

Cheol Mubaek looked at Jin Mukyung with a satisfied grandfatherly smile before turning toward me.

“What about you? Don’t you have anything to say?”

For a moment, I could have sworn I felt the gaze of a predator.

I decided to follow the better of the two examples I had just witnessed.

“You’ve arrived.”

“Of course I have. Did I go somewhere?”

“...”

That wasn’t it.

But smiling in hard times was the mark of a First Rate man. I put on a smile without panicking.

“Are you feeling all right?”

This time, Cheol Mubaek shook his splinted limbs.

“Do I look all right?”

“...No.”

“If I were all right, I would have walked here. These days, those mounted-bandit bastards work people without even a retirement age. What chance does an old man like me have?”

“...”

The old man had quite a memory. He still seemed to be holding on to the mistake I had made when we first met.

Lee Seowol, who knew nothing about the situation, shouted in embarrassment.

“Uncle!”

“Good grief, my old ears are going to fall off.”

After grumbling, he suddenly bowed his head politely.

“Thank you, everyone.”

This wasn’t a reluctant gesture. Cheol Mubaek, the Tiger of Mount Heng, was an old master who had walked his own path for many years. He was speaking from the bottom of his heart.

“It’s not because you extended the life of an old man with little time left. Seowol—thank you for protecting that child. Thanks to all of you, the Mount Heng Sword Sect survived.”

He gazed calmly at me, Jin Mukyung, and Hyuk Mujin in turn.

“I’ve learned something after living for more than a jiazi.[^1] Gratitude and grudges must be repaid, no matter what it takes. I swear here and now that I will never forget what happened, not until the day I die. If you wish it, I’ll repay you even if it costs me my life.”

Lee Seowol immediately took up his words.

“The Mount Heng Sword Sect will remember our Benefactors. I would also like to apologize here for the wrongdoing committed by my late father...”

“We apologize!”

“Please forgive us!”

The thunderous cries burst from the mouths of the Mount Heng martial artists.

All of them bore injuries, both major and minor. Kneeling in the snow that had not yet melted, they waited for our answer.

A tap.

*You answer.*

At Jin Mukyung’s Sound Transmission, I licked my dry lips.

*Forgiveness.*

We had won the war, but wounds remained.

Martial artists had fought and died without end on the orders of their superiors. Even women and children who had never learned martial arts had been sacrificed. It was all the work of Lee Cheonbaek, who had been blinded by his desire to avenge his son.

The wounds left by the war with the Mount Heng Sword Sect ran deep, and it would take a long time for them to heal.

*And scars will remain.*

Some scars could never be erased.

The young siblings who had lost their home and parents in an instant would carry such scars. So would I. Even now, I could still see the face of the man who had dreamed of becoming the greatest under heaven.

But I couldn’t deny that the wounds were beginning to close.

*The people who caused them are all dead.*

The Head Elder and Lee Cheonbaek, each of whom had dreamed of revenge, had already met their ends.

Wasn’t that why we had raced here day and night to save the Mount Heng Sword Sect?

With a sincere apology and forgiveness... wounds could heal, even if scars remained.

Just as they were now.

“I won’t accept your apology.”

The words came out only after considerable thought. Without waiting for anyone else to react, I continued.

“I’m not someone with the right to receive an apology from you or to forgive you.”

No one here had that right. The people they needed to apologize to were in the Jin Family of Taiyuan.

Apparently understanding what I meant, Lee Seowol and Cheol Mubaek both nodded.

“I’ll see you on New Year’s Day.”

“Taiyuan. It will be my first time venturing out in thirty years.”

The Mount Heng Sword Sect was hardly a welcome guest. Especially in its current, pitifully diminished state, it might have to endure all kinds of humiliation and disgrace.

But that was something they would have to bear themselves. There was nothing I could do, nor any reason for me to interfere.

*Well done.*

With Jin Mukyung’s brief Sound Transmission in my ear, I offered one last farewell.

“Then, we’ll be going.”

I had just turned toward the carriage when Lee Seowol called out.

“Benefactor.”

“Yes?”

“Did you know that there are fewer than fifteen days left until New Year’s Day?”

Her voice flowed like a little stream.

“I’m looking forward to hearing the answer I didn’t get last time.”

I could only open and close my mouth in confusion. Jin Mukyung grabbed me and pulled me away.

The carriage set off at full speed, with the sound of Cheol Mubaek’s distinctly displeased cough following us from behind.

* * *

The journey back to the Jin Family of Taiyuan was quick and smooth. The coachman’s skill played a part, but with the impatience in my heart gone, everything seemed easier.

“Phew.”

Jin Mukyung had just finished circulating his qi when he suddenly muttered,

“Now that I think about it, I didn’t even get to see a Peak martial art.”

He had joined the journey after being lured by Jin Wikyung’s claim that he could see Peak martial arts if he went to Mount Heng. I answered him calmly.

“It’s fine. Thanks to Pung Yang, you got to see Mount Beimang.”

“You call that consolation?”

“No. I was teasing you.”

The sound of bones cracking came from Jin Mukyung’s hand.

“You’ve grown a lot.”

“Would you like to spar once your injuries have fully healed?”

“I could do it right now... Urgh.”

Jin Mukyung tried to spring to his feet, then immediately frowned.

No matter how quickly he recovered, it had only been four days. That was nowhere near enough time for his injuries to heal completely.

He collapsed back into his seat and glared at me.

“You should consider yourself lucky.”

“I don’t know about lucky, but my lifeline sure is damn tough.”

The fact that I kept surviving despite facing the brink of death every time suggested that I had been born with an unusually sturdy lifeline. Either that, or I had been blessed with heaven’s fortune.

“Anyway, you did well.”

“Huh?”

“Eeeh?”

Hyuk Mujin and I both widened our eyes at the unexpected praise sticker. The person who had given it looked at us as if he couldn’t understand what was wrong.

“Why are you looking at me like that? You look as if you’ve heard something you weren’t supposed to.”

“You’re like a ghost.”

“Wait, could it be that you already died to Pung Yang and became a vengeful spirit, and you’re here with us?”

It was a fairly plausible theory, but around Jin Mukyung, you had to watch your mouth at all times.

I felt around inside my clothes while watching Hyuk Mujin get beaten until dust flew.

*Inventory open. Summon.*

The next moment, my fingertips touched something round and hard.

It was the only thing Pung Yang had left behind.

Or rather, the only thing I had taken from Pung Yang.

*Check item.*

*Ding.*



> **System**
>
> **Item Window**
>
> **Temporary Strength Pill**
>
> **Type:** Elixir  
> **Grade:** ???  
> **Restriction:** Peak martial artist or higher  
> **Description:** A pill manufactured by an unknown person. It greatly raises the user’s latent power for about one shichen, but a price must be paid in return. Do not take it except in the worst-case scenario.  
> **Effect:** Combat-related stats +100  
>
> **Internal energy:** +15 years  
>
> **Body-Protecting Qi:** Available

Even with the short time limit, the effect was absurd. It was easy to understand why Pung Yang had been so confident.

I had no idea how severe the aftereffects were, but if my life were in danger, I’d eat twenty of them, not two. Obviously.

But the part that bothered me was something else.

*An elixir manufactured by an unknown person.*

The Item’s Grade was marked with question marks, its exact aftereffects were not listed, and even its maker was shrouded in mystery.

What kind of bastard had created such a bizarre thing?

*This thing reeks of something shady.*

I was turning the Temporary Strength Pill over in my hand and lost in thought when a distant cry reached us.

“Mukyuuung! Taekyuuung!”

Jin Mukyung, who had been enthusiastically hammering Hyuk Mujin on the forehead, suddenly stopped.

“Was that a hallucination?”

Yeah, no.

[^1]: A jiazi is a traditional sixty-year cycle.
```
